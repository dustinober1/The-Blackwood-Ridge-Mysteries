#!/usr/bin/env python3
"""Fail-closed validation for The Challenger's KDP-ready ebook package."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree as ET

from PIL import Image

BOOK_TITLE = "The Challenger"
AUTHOR = "Vesper Blythe"
SERIES = "The Blackwood Ridge Mysteries"
SERIES_NUMBER = "3"
LANGUAGE_PREFIX = "en"
STORY_END = "She did not need the bell to ring before she began."
CHAPTERS = [
    "The Visitor Who Came Looking",
    "After the Lecture",
    "The Door Opens",
    "The Second Hand",
    "The Gap",
    "The Keeper",
    "Still Hands",
    "The Man Who Buried It",
]
BACK_MATTER = ["Thank You for Reading", SERIES, "About the Author"]
WORD_RE = re.compile(r"[A-Za-z0-9]+(?:[’'-][A-Za-z0-9]+)*")
BLOCKER_RE = re.compile(r"(?i)(?:\bTODO\b|\bTBD\b|Document X|Book 1 reading|<placeholder>|\{\{)")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def artifact(path: Path) -> dict[str, object]:
    return {"path": str(path), "size_bytes": path.stat().st_size, "sha256": sha256(path)}


def local_name(tag: str) -> str:
    return tag.split("}", 1)[-1]


def text_content(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def validate_markdown(path: Path, errors: list[str], stats: dict[str, object]) -> None:
    text = path.read_text(encoding="utf-8")
    if "First edition: July 2026" not in text:
        errors.append("retail manuscript edition line is not July 2026")
    if BLOCKER_RE.search(text):
        errors.append("retail manuscript contains a placeholder or internal planning label")
    expected = [f"# Chapter {i} — {title}" for i, title in enumerate(CHAPTERS, 1)]
    positions = [text.find(value) for value in expected]
    if any(position < 0 for position in positions) or positions != sorted(positions):
        errors.append("retail manuscript chapter headings are missing or out of order")
    if text.count(STORY_END) != 1:
        errors.append("locked story ending is missing or duplicated")
    ending_position = text.find(STORY_END)
    for heading in ("# Thank You for Reading", f"# {SERIES}", "# About the Author"):
        if text.count(heading) != 1 or text.find(heading) < ending_position:
            errors.append(f"back matter heading is missing, duplicated, or misplaced: {heading}")
    chapter_start = text.find(expected[0]) if expected else -1
    story_end = ending_position + len(STORY_END)
    story_text = text[chapter_start:story_end] if chapter_start >= 0 and ending_position >= 0 else ""
    stats["story_word_count"] = len(WORD_RE.findall(story_text))
    stats["retail_word_count"] = len(WORD_RE.findall(text))
    stats["chapter_count"] = sum(text.count(f"# Chapter {i} — ") for i in range(1, 9))


def validate_cover(path: Path, errors: list[str], stats: dict[str, object]) -> None:
    with Image.open(path) as image:
        stats["cover_format"] = image.format
        stats["cover_mode"] = image.mode
        stats["cover_dimensions"] = list(image.size)
        stats["cover_dpi"] = list(image.info.get("dpi", (0, 0)))
        if image.format != "JPEG":
            errors.append(f"cover format must be JPEG, got {image.format}")
        if image.mode != "RGB":
            errors.append(f"cover mode must be RGB, got {image.mode}")
        if image.size != (1600, 2560):
            errors.append(f"cover dimensions must be 1600x2560, got {image.size}")
    if path.stat().st_size >= 50 * 1024 * 1024:
        errors.append("cover file exceeds KDP's 50 MB maximum")


def validate_epub(path: Path, cover_path: Path, errors: list[str], stats: dict[str, object]) -> None:
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        if not names or names[0] != "mimetype":
            errors.append("EPUB mimetype entry is not first")
        elif zf.read("mimetype") != b"application/epub+zip":
            errors.append("EPUB mimetype value is invalid")
        if "META-INF/container.xml" not in names:
            errors.append("EPUB container.xml is missing")
            return

        for name in [n for n in names if n.lower().endswith((".xml", ".opf", ".xhtml", ".ncx"))]:
            try:
                ET.fromstring(zf.read(name))
            except Exception as exc:
                errors.append(f"invalid XML in {name}: {exc}")

        container = ET.fromstring(zf.read("META-INF/container.xml"))
        rootfile = next((e for e in container.iter() if local_name(e.tag) == "rootfile"), None)
        if rootfile is None or not rootfile.attrib.get("full-path"):
            errors.append("EPUB rootfile is not declared")
            return
        opf_path = rootfile.attrib["full-path"]
        if opf_path not in names:
            errors.append(f"EPUB package document is missing: {opf_path}")
            return
        opf = ET.fromstring(zf.read(opf_path))
        opf_dir = PurePosixPath(opf_path).parent

        metadata = next((e for e in opf if local_name(e.tag) == "metadata"), None)
        manifest = next((e for e in opf if local_name(e.tag) == "manifest"), None)
        spine = next((e for e in opf if local_name(e.tag) == "spine"), None)
        if metadata is None or manifest is None or spine is None:
            errors.append("EPUB package metadata, manifest, or spine is missing")
            return

        values: dict[str, list[str]] = {}
        for element in metadata:
            values.setdefault(local_name(element.tag), []).append(text_content(element))
        if BOOK_TITLE not in values.get("title", []):
            errors.append("EPUB title metadata is invalid")
        if AUTHOR not in values.get("creator", []):
            errors.append("EPUB creator metadata is invalid")
        if not any(value.lower().startswith(LANGUAGE_PREFIX) for value in values.get("language", [])):
            errors.append("EPUB language metadata is invalid")

        metas = [e for e in metadata if local_name(e.tag) == "meta"]
        meta_pairs = {(e.attrib.get("property", ""), text_content(e)) for e in metas}
        if ("belongs-to-collection", SERIES) not in meta_pairs:
            errors.append("EPUB series collection metadata is missing")
        if ("group-position", SERIES_NUMBER) not in meta_pairs:
            errors.append("EPUB series position metadata is missing")

        manifest_items = [e for e in manifest if local_name(e.tag) == "item"]
        id_to_path: dict[str, PurePosixPath] = {}
        cover_item: ET.Element | None = None
        nav_item: ET.Element | None = None
        for item in manifest_items:
            href = item.attrib.get("href", "")
            full = opf_dir / href
            id_to_path[item.attrib.get("id", "")] = full
            if str(full) not in names:
                errors.append(f"EPUB manifest resource is missing: {full}")
            properties = set(item.attrib.get("properties", "").split())
            if "cover-image" in properties:
                cover_item = item
            if "nav" in properties:
                nav_item = item
        if cover_item is None:
            errors.append("EPUB does not declare a cover-image resource")
        else:
            embedded_path = opf_dir / cover_item.attrib.get("href", "")
            if str(embedded_path) in names:
                from io import BytesIO
                with Image.open(BytesIO(zf.read(str(embedded_path)))) as embedded:
                    if embedded.size != (1600, 2560):
                        errors.append(f"embedded EPUB cover has wrong dimensions: {embedded.size}")
                    if embedded.mode != "RGB":
                        errors.append(f"embedded EPUB cover is not RGB: {embedded.mode}")
                if hashlib.sha256(zf.read(str(embedded_path))).hexdigest() != sha256(cover_path):
                    errors.append("embedded EPUB cover does not match the upload cover")
        if nav_item is None:
            errors.append("EPUB navigation document is missing")
        else:
            nav_path = str(opf_dir / nav_item.attrib.get("href", ""))
            if nav_path in names:
                nav_text = text_content(ET.fromstring(zf.read(nav_path)))
                expected_nav = CHAPTERS + BACK_MATTER
                positions = [nav_text.find(value) for value in expected_nav]
                if any(position < 0 for position in positions) or positions != sorted(positions):
                    errors.append("EPUB navigation is missing required sections or has them out of order")

        spine_ids = [e.attrib.get("idref", "") for e in spine if local_name(e.tag) == "itemref"]
        if not spine_ids or any(item_id not in id_to_path for item_id in spine_ids):
            errors.append("EPUB spine contains unresolved resources")

        visible = []
        for name in names:
            if name.lower().endswith((".xhtml", ".html", ".htm")):
                try:
                    visible.append(text_content(ET.fromstring(zf.read(name))))
                except Exception:
                    pass
        visible_text = "\n".join(visible)
        if STORY_END not in visible_text:
            errors.append("EPUB is missing the locked story ending")
        if BLOCKER_RE.search(visible_text):
            errors.append("EPUB contains a placeholder or internal planning label")
        for required in CHAPTERS + BACK_MATTER:
            if required not in visible_text:
                errors.append(f"EPUB visible text is missing: {required}")

    checker = shutil.which("epubcheck")
    if checker:
        completed = subprocess.run(
            [checker, str(path)], text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False
        )
        stats["epubcheck"] = completed.stdout[-4000:]
        if completed.returncode != 0:
            errors.append("epubcheck reported errors")
    else:
        stats["epubcheck"] = "not installed; internal EPUB 3 validation completed"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--retail-md", type=Path, required=True)
    parser.add_argument("--epub", type=Path, required=True)
    parser.add_argument("--cover", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()

    errors: list[str] = []
    stats: dict[str, object] = {}
    for path in (args.retail_md, args.epub, args.cover):
        if not path.is_file():
            errors.append(f"required artifact is missing: {path}")
    if not errors:
        validate_markdown(args.retail_md, errors, stats)
        validate_cover(args.cover, errors, stats)
        validate_epub(args.epub, args.cover, errors, stats)

    result = {
        "book": BOOK_TITLE,
        "author": AUTHOR,
        "series": SERIES,
        "series_number": 3,
        "build_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "source_commit": os.environ.get("GITHUB_SHA", "local"),
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "stats": stats,
        "artifacts": [artifact(path) for path in (args.retail_md, args.epub, args.cover) if path.is_file()],
    }
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    md = [
        "# Book 3 Release Validation — The Challenger",
        "",
        f"- **Status:** {result['status']}",
        f"- **Source commit:** `{result['source_commit']}`",
        f"- **Story words:** {stats.get('story_word_count', 'n/a')}",
        f"- **Retail package words:** {stats.get('retail_word_count', 'n/a')}",
        f"- **Chapters:** {stats.get('chapter_count', 'n/a')}",
        f"- **Cover:** {stats.get('cover_format', 'n/a')} / {stats.get('cover_mode', 'n/a')} / {stats.get('cover_dimensions', 'n/a')}",
        "",
        "## Artifact hashes",
        "",
    ]
    for item in result["artifacts"]:
        md.append(f"- `{item['path']}` — {item['size_bytes']} bytes — SHA-256 `{item['sha256']}`")
    md.extend(["", "## Errors", ""])
    md.extend([f"- {error}" for error in errors] or ["- None."])
    args.markdown.write_text("\n".join(md) + "\n", encoding="utf-8")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Validated {BOOK_TITLE}: {stats.get('story_word_count')} story words")


if __name__ == "__main__":
    main()
