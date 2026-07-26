#!/usr/bin/env python3
"""Fail-closed validation for The Challenger's retailer-ready ebook package."""
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

from cover_provenance import CoverProvenanceError, validate_release_covers


BOOK_TITLE = "The Challenger"
AUTHOR = "Vesper Blythe"
SERIES = "The Blackwood Ridge Mysteries"
SERIES_NUMBER = "3"
LANGUAGE_PREFIX = "en"
STORY_END = "She did not need the bell to ring before she began."
EXPECTED_STORY_WORDS = 24_212
EXPECTED_RETAIL_WORDS = 24_486
EXPECTED_CHAPTERS = 8
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
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


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
    story_words = len(WORD_RE.findall(story_text))
    retail_words = len(WORD_RE.findall(text))
    chapter_count = sum(text.count(f"# Chapter {i} — ") for i in range(1, EXPECTED_CHAPTERS + 1))
    stats["story_word_count"] = story_words
    stats["retail_word_count"] = retail_words
    stats["chapter_count"] = chapter_count
    stats["locked_ending_occurrences"] = text.count(STORY_END)
    if story_words != EXPECTED_STORY_WORDS:
        errors.append(f"story word count must be {EXPECTED_STORY_WORDS}, got {story_words}")
    if retail_words != EXPECTED_RETAIL_WORDS:
        errors.append(f"retail word count must be {EXPECTED_RETAIL_WORDS}, got {retail_words}")
    if chapter_count != EXPECTED_CHAPTERS:
        errors.append(f"chapter count must be {EXPECTED_CHAPTERS}, got {chapter_count}")


def validate_cover(path: Path, errors: list[str], stats: dict[str, object]) -> None:
    with Image.open(path) as image:
        image.load()
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
        errors.append("cover file exceeds the 50 MB retailer maximum")


def epubcheck_counts(output: str) -> dict[str, int]:
    return {
        "fatal_count": len(re.findall(r"(?im)^\s*FATAL\(", output)),
        "error_count": len(re.findall(r"(?im)^\s*ERROR\(", output)),
        "warning_count": len(re.findall(r"(?im)^\s*WARNING\(", output)),
        "info_count": len(re.findall(r"(?im)^\s*INFO\(", output)),
    }


def run_epubcheck(path: Path, errors: list[str], stats: dict[str, object]) -> None:
    checker = shutil.which("epubcheck")
    if not checker:
        stats["epubcheck"] = {
            "version": "not installed",
            "exit_status": None,
            "fatal_count": None,
            "error_count": None,
            "warning_count": None,
            "info_count": None,
            "output": "",
        }
        errors.append("epubcheck is required but not installed")
        return
    version_run = subprocess.run(
        [checker, "--version"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    version_lines = [line.strip() for line in version_run.stdout.splitlines() if line.strip()]
    completed = subprocess.run(
        [checker, str(path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    counts = epubcheck_counts(completed.stdout)
    stats["epubcheck"] = {
        "version": version_lines[0] if version_lines else "unknown",
        "exit_status": completed.returncode,
        **counts,
        "output": completed.stdout[-4000:],
    }
    if completed.returncode != 0 or any(counts[key] for key in ("fatal_count", "error_count", "warning_count")):
        errors.append(
            "epubcheck must report exit status 0 with zero fatals, errors, and warnings"
        )


def validate_epub(path: Path, cover_path: Path, errors: list[str], stats: dict[str, object]) -> None:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if not names or names[0] != "mimetype":
            errors.append("EPUB mimetype entry is not first")
        elif archive.read("mimetype") != b"application/epub+zip":
            errors.append("EPUB mimetype value is invalid")
        if "META-INF/container.xml" not in names:
            errors.append("EPUB container.xml is missing")
            return

        for name in [item for item in names if item.lower().endswith((".xml", ".opf", ".xhtml", ".ncx"))]:
            try:
                ET.fromstring(archive.read(name))
            except Exception as exc:
                errors.append(f"invalid XML in {name}: {exc}")

        container = ET.fromstring(archive.read("META-INF/container.xml"))
        rootfile = next((item for item in container.iter() if local_name(item.tag) == "rootfile"), None)
        if rootfile is None or not rootfile.attrib.get("full-path"):
            errors.append("EPUB rootfile is not declared")
            return
        opf_path = rootfile.attrib["full-path"]
        if opf_path not in names:
            errors.append(f"EPUB package document is missing: {opf_path}")
            return
        opf = ET.fromstring(archive.read(opf_path))
        opf_dir = PurePosixPath(opf_path).parent

        metadata = next((item for item in opf if local_name(item.tag) == "metadata"), None)
        manifest = next((item for item in opf if local_name(item.tag) == "manifest"), None)
        spine = next((item for item in opf if local_name(item.tag) == "spine"), None)
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

        metas = [item for item in metadata if local_name(item.tag) == "meta"]
        meta_pairs = {(item.attrib.get("property", ""), text_content(item)) for item in metas}
        if ("belongs-to-collection", SERIES) not in meta_pairs:
            errors.append("EPUB series collection metadata is missing")
        if ("group-position", SERIES_NUMBER) not in meta_pairs:
            errors.append("EPUB series position metadata is missing")

        manifest_items = [item for item in manifest if local_name(item.tag) == "item"]
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

                embedded_bytes = archive.read(str(embedded_path))
                with Image.open(BytesIO(embedded_bytes)) as embedded:
                    embedded.load()
                    if embedded.size != (1600, 2560):
                        errors.append(f"embedded EPUB cover has wrong dimensions: {embedded.size}")
                    if embedded.mode != "RGB":
                        errors.append(f"embedded EPUB cover is not RGB: {embedded.mode}")
                if hashlib.sha256(embedded_bytes).hexdigest() != sha256(cover_path):
                    errors.append("embedded EPUB cover does not match the upload cover")
        if nav_item is None:
            errors.append("EPUB navigation document is missing")
        else:
            nav_path = str(opf_dir / nav_item.attrib.get("href", ""))
            if nav_path in names:
                nav_text = text_content(ET.fromstring(archive.read(nav_path)))
                expected_nav = CHAPTERS + BACK_MATTER
                positions = [nav_text.find(value) for value in expected_nav]
                if any(position < 0 for position in positions) or positions != sorted(positions):
                    errors.append("EPUB navigation is missing required sections or has them out of order")

        spine_ids = [item.attrib.get("idref", "") for item in spine if local_name(item.tag) == "itemref"]
        if not spine_ids or any(item_id not in id_to_path for item_id in spine_ids):
            errors.append("EPUB spine contains unresolved resources")

        visible = []
        for name in names:
            if name.lower().endswith((".xhtml", ".html", ".htm")):
                try:
                    visible.append(text_content(ET.fromstring(archive.read(name))))
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

    run_epubcheck(path, errors, stats)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--retail-md", type=Path, required=True)
    parser.add_argument("--epub", type=Path, required=True)
    parser.add_argument("--cover", type=Path, required=True)
    parser.add_argument("--approved-record", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()

    errors: list[str] = []
    stats: dict[str, object] = {}
    for path in (args.retail_md, args.epub, args.cover, args.approved_record):
        if not path.is_file():
            errors.append(f"required artifact or authority record is missing: {path}")

    if not errors:
        try:
            provenance = validate_release_covers(
                args.approved_record,
                standalone_path=args.cover,
                epub_path=args.epub,
            )
            record = provenance["record"]
            stats["cover_provenance"] = {
                "approval_status": record["approval_status"],
                "authority_path": str(args.approved_record),
                "approved_asset_path": record["approved_asset_path"],
                "source_asset_path": record["source_asset_path"],
                "approved_sha256": provenance["approved"]["sha256"],
                "approved_size_bytes": provenance["approved"]["size_bytes"],
                "standalone_sha256": provenance["standalone"]["sha256"],
                "embedded_path": provenance["embedded"]["path"],
                "embedded_sha256": provenance["embedded"]["sha256"],
                "approved_text": record["approved_text"],
            }
        except CoverProvenanceError as exc:
            errors.append(f"cover provenance validation failed: {exc}")

    if not errors:
        validate_markdown(args.retail_md, errors, stats)
        validate_cover(args.cover, errors, stats)
        validate_epub(args.epub, args.cover, errors, stats)

    source_commit = (
        os.environ.get("BOOK03_SOURCE_COMMIT")
        or os.environ.get("GITHUB_SHA")
        or "local"
    )
    result = {
        "book": BOOK_TITLE,
        "author": AUTHOR,
        "series": SERIES,
        "series_number": 3,
        "build_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "source_commit": source_commit,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "cover_provenance": stats.get("cover_provenance", {}),
        "stats": stats,
        "artifacts": [artifact(path) for path in (args.retail_md, args.epub, args.cover) if path.is_file()],
    }
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    provenance_stats = stats.get("cover_provenance", {})
    epubcheck_stats = stats.get("epubcheck", {})
    markdown = [
        "# Book 3 Release Validation — The Challenger",
        "",
        f"- **Status:** {result['status']}",
        f"- **Source commit:** `{result['source_commit']}`",
        f"- **Story words:** {stats.get('story_word_count', 'n/a')}",
        f"- **Retail package words:** {stats.get('retail_word_count', 'n/a')}",
        f"- **Chapters:** {stats.get('chapter_count', 'n/a')}",
        f"- **Cover:** {stats.get('cover_format', 'n/a')} / {stats.get('cover_mode', 'n/a')} / {stats.get('cover_dimensions', 'n/a')}",
        f"- **Approved cover SHA-256:** `{provenance_stats.get('approved_sha256', 'n/a')}`",
        f"- **EPUBCheck:** {epubcheck_stats.get('version', 'n/a')} / exit {epubcheck_stats.get('exit_status', 'n/a')} / {epubcheck_stats.get('fatal_count', 'n/a')} fatals / {epubcheck_stats.get('error_count', 'n/a')} errors / {epubcheck_stats.get('warning_count', 'n/a')} warnings",
        "",
        "## Approved cover provenance",
        "",
        f"- Status: `{provenance_stats.get('approval_status', 'n/a')}`",
        f"- Authority: `{provenance_stats.get('authority_path', 'n/a')}`",
        f"- Approved asset: `{provenance_stats.get('approved_asset_path', 'n/a')}`",
        f"- Source asset: `{provenance_stats.get('source_asset_path', 'n/a')}`",
        f"- Standalone SHA-256: `{provenance_stats.get('standalone_sha256', 'n/a')}`",
        f"- Embedded cover: `{provenance_stats.get('embedded_path', 'n/a')}`",
        f"- Embedded SHA-256: `{provenance_stats.get('embedded_sha256', 'n/a')}`",
        "",
        "## Artifact hashes",
        "",
    ]
    for item in result["artifacts"]:
        markdown.append(f"- `{item['path']}` — {item['size_bytes']} bytes — SHA-256 `{item['sha256']}`")
    markdown.extend(["", "## Errors", ""])
    markdown.extend([f"- {error}" for error in errors] or ["- None."])
    args.markdown.write_text("\n".join(markdown) + "\n", encoding="utf-8")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Validated {BOOK_TITLE}: {stats.get('story_word_count')} story words")


if __name__ == "__main__":
    main()
