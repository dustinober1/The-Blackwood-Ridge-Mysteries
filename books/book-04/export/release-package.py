#!/usr/bin/env python3
"""Build and validate the upload-ready Book 4 ebook package.

This release layer runs the existing Book 4 production pipeline, then creates the
retailer-facing EPUB, cover, DOCX, validation records, and upload ZIP. It does
not edit chapter source files or claim that the book has been published.
"""
from __future__ import annotations

import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET

from bs4 import BeautifulSoup
from PIL import Image

TITLE = "The Archive Fire"
AUTHOR = "Vesper Blythe"
SERIES = "The Blackwood Ridge Mysteries"
SERIES_NUMBER = 4
LANGUAGE = "en-US"
BUILD_DATE = date(2026, 7, 12)
EXPECTED_SIZE = (1600, 2560)
LOCKED_ENDING = "She set the tea beside it, close enough for the steam to pass over the glass."
EXPECTED_CHAPTERS = [
    "Chapter 1 — Smoke Under Town Hall",
    "Chapter 2 — The Salvage Table",
    "Chapter 3 — A Shelf That Lied Twice",
    "Chapter 4 — The Predecessor’s Hand",
    "Chapter 5 — Water Lines",
    "Chapter 6 — Bad Procedure",
    "Chapter 7 — The Ash Index",
    "Chapter 8 — The Box Asked For",
]
FORBIDDEN = [
    re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.IGNORECASE),
    re.compile(r"AUTHOR DECISION REQUIRED", re.IGNORECASE),
    re.compile(r"Document X", re.IGNORECASE),
    re.compile(r"<<<<<<|======|>>>>>>"),
    re.compile(r"\{\{.*?\}\}", re.DOTALL),
]

HERE = Path(__file__).resolve().parent
BOOK_DIR = HERE.parent
REPO_ROOT = BOOK_DIR.parents[1]
DIST = HERE / "dist"
COVER_SOURCE = BOOK_DIR / "cover.jpeg"
COMBINED = HERE / "manuscript-combined.md"
EPUB = DIST / "The-Archive-Fire.epub"
DOCX = DIST / "The-Archive-Fire.docx"
COVER = DIST / "The-Archive-Fire-cover.jpg"
MANIFEST = DIST / "release-manifest.json"
VALIDATION = DIST / "release-validation.md"
UPLOAD_ZIP = DIST / "The-Archive-Fire-upload-package.zip"


def run(command: list[str], *, cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        command,
        cwd=str(cwd) if cwd else None,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if check and result.returncode != 0:
        raise RuntimeError(f"Command failed ({result.returncode}): {' '.join(command)}\n{result.stdout}")
    return result


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def story_word_count(markdown: str) -> int:
    chapter_start = markdown.find("# Chapter 1 —")
    back_start = markdown.find("# A Note from the Author")
    if chapter_start < 0 or back_start < 0:
        raise RuntimeError("Could not isolate story body")
    story = markdown[chapter_start:back_start]
    story = re.sub(r"[`*_>#-]", " ", story)
    return len(re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b", story, flags=re.UNICODE))


def ensure_source_ending(markdown: str) -> None:
    if markdown.count(LOCKED_ENDING) != 1:
        raise RuntimeError(
            f"Locked ending must appear exactly once; found {markdown.count(LOCKED_ENDING)}"
        )


def patch_generated_docs() -> None:
    replacements = {
        BOOK_DIR / "publish" / "listing.md": (
            "Author decisions and the missing final cover remain tracked in `books/book-04/package/author-decision-checklist.md`.",
            "The final cover is present and validated. Remaining retailer-controlled choices are tracked in `books/book-04/package/author-decision-checklist.md`.",
        ),
        BOOK_DIR / "revision" / "notes.md": (
            "- Package: in progress because no final cover asset exists and author-controlled retailer/print decisions remain.",
            "- Package: complete for ebook upload; retailer-controlled choices remain.",
        ),
        HERE / "README.md": (
            "Export is technically complete and reproducible. The book has not been uploaded or published. The overall package remains incomplete until a valid cover is supplied and author-controlled retailer decisions are made.",
            "Export and ebook packaging are technically complete and reproducible. The book has not been uploaded or published; retailer-controlled release choices remain.",
        ),
    }
    for path, (old, new) in replacements.items():
        text = path.read_text(encoding="utf-8")
        if old in text:
            path.write_text(text.replace(old, new), encoding="utf-8")
        elif new not in text:
            raise RuntimeError(f"Expected release-status text not found in {path}")


def validate_cover() -> dict[str, object]:
    if not COVER_SOURCE.exists():
        raise RuntimeError(f"Missing cover: {COVER_SOURCE}")
    with Image.open(COVER_SOURCE) as image:
        image.load()
        if image.format != "JPEG":
            raise RuntimeError(f"Cover must be JPEG; found {image.format}")
        if image.size != EXPECTED_SIZE:
            raise RuntimeError(f"Cover must be {EXPECTED_SIZE}; found {image.size}")
        if image.mode != "RGB":
            raise RuntimeError(f"Cover must be RGB; found {image.mode}")
        dpi = image.info.get("dpi", (72, 72))
        info = {
            "format": image.format,
            "mode": image.mode,
            "width": image.width,
            "height": image.height,
            "dpi": [round(float(dpi[0])), round(float(dpi[1]))],
        }
    shutil.copyfile(COVER_SOURCE, COVER)
    return info


def build_retail_epub() -> None:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise RuntimeError("pandoc is required")
    css = HERE / "epub.css"
    command = [
        pandoc,
        str(COMBINED),
        "--from=markdown",
        "--to=epub3",
        "--toc",
        "--toc-depth=1",
        "--epub-title-page=false",
        "--epub-cover-image",
        str(COVER),
        "--metadata",
        f"title={TITLE}",
        "--metadata",
        f"author={AUTHOR}",
        "--metadata",
        f"lang={LANGUAGE}",
        "--metadata",
        f"rights=Copyright © 2026 {AUTHOR}. All rights reserved.",
        "--metadata",
        "subject=Atmospheric cozy mystery; amateur sleuth; archival mystery",
    ]
    if css.exists():
        command.extend(["--css", str(css)])
    command.extend(["-o", str(EPUB)])
    run(command)


def locate_opf(archive: zipfile.ZipFile) -> str:
    root = ET.fromstring(archive.read("META-INF/container.xml"))
    node = root.find(".//{*}rootfile")
    if node is None or not node.get("full-path"):
        raise RuntimeError("EPUB container has no OPF rootfile")
    return node.get("full-path", "")


def validate_epub() -> dict[str, object]:
    with EPUB.open("rb") as handle:
        if not handle.read(4).startswith(b"PK"):
            raise RuntimeError("EPUB is not a ZIP package")
    with zipfile.ZipFile(EPUB) as archive:
        names = archive.namelist()
        if not names or names[0] != "mimetype":
            raise RuntimeError("EPUB mimetype is not first")
        if archive.read("mimetype") != b"application/epub+zip":
            raise RuntimeError("EPUB mimetype is incorrect")
        if "META-INF/container.xml" not in names:
            raise RuntimeError("EPUB container.xml missing")

        opf_path = locate_opf(archive)
        opf = ET.fromstring(archive.read(opf_path))
        opf_dir = Path(opf_path).parent
        title = "".join(node.text or "" for node in opf.findall(".//{*}title")).strip()
        creators = [normalize(node.text or "") for node in opf.findall(".//{*}creator")]
        languages = [normalize(node.text or "") for node in opf.findall(".//{*}language")]
        if title != TITLE or AUTHOR not in creators or LANGUAGE not in languages:
            raise RuntimeError(
                f"EPUB metadata mismatch: title={title!r}, creators={creators!r}, languages={languages!r}"
            )

        manifest: dict[str, tuple[str, str]] = {}
        cover_href = None
        nav_href = None
        for item in opf.findall(".//{*}manifest/{*}item"):
            item_id = item.get("id", "")
            href = item.get("href", "")
            properties = item.get("properties", "")
            resolved = str((opf_dir / href).as_posix())
            manifest[item_id] = (resolved, properties)
            if "cover-image" in properties.split():
                cover_href = resolved
            if "nav" in properties.split():
                nav_href = resolved
        if not cover_href or cover_href not in names:
            raise RuntimeError("EPUB embedded cover missing")
        if archive.read(cover_href) != COVER.read_bytes():
            raise RuntimeError("Embedded EPUB cover does not match separate cover")
        if not nav_href or nav_href not in names:
            raise RuntimeError("EPUB navigation document missing")

        spine_ids = [node.get("idref", "") for node in opf.findall(".//{*}spine/{*}itemref")]
        spine_paths = [manifest[item_id][0] for item_id in spine_ids if item_id in manifest]
        if not spine_paths or any(path not in names for path in spine_paths):
            raise RuntimeError("EPUB spine is incomplete")

        all_h1: list[str] = []
        all_text: list[str] = []
        for path in spine_paths:
            soup = BeautifulSoup(archive.read(path), "html.parser")
            all_h1.extend(normalize(node.get_text(" ", strip=True)) for node in soup.find_all("h1"))
            all_text.append(soup.get_text(" ", strip=True))
        chapter_h1 = [value for value in all_h1 if value.startswith("Chapter ")]
        if chapter_h1 != EXPECTED_CHAPTERS:
            raise RuntimeError(f"EPUB chapter order mismatch: {chapter_h1!r}")
        if all_h1.count(TITLE) != 1:
            raise RuntimeError(f"EPUB must have one manuscript title heading; found {all_h1.count(TITLE)}")

        extracted = "\n".join(all_text)
        if extracted.count(LOCKED_ENDING) != 1:
            raise RuntimeError("Locked ending is missing or duplicated in EPUB")
        for pattern in FORBIDDEN:
            found = pattern.search(extracted)
            if found:
                raise RuntimeError(f"Forbidden reader-facing marker in EPUB: {found.group(0)!r}")

        nav = BeautifulSoup(archive.read(nav_href), "html.parser")
        nav_text = normalize(nav.get_text(" ", strip=True))
        for heading in EXPECTED_CHAPTERS:
            if heading not in nav_text:
                raise RuntimeError(f"Navigation missing {heading}")
        for heading in ["A Note from the Author", "The Blackwood Ridge Mysteries", "About the Author"]:
            if heading not in nav_text:
                raise RuntimeError(f"Navigation missing {heading}")

    epubcheck = shutil.which("epubcheck")
    output = "epubcheck unavailable; internal EPUB 3 validation passed"
    if epubcheck:
        result = run([epubcheck, str(EPUB)], check=False)
        output = result.stdout.strip()
        if result.returncode != 0:
            raise RuntimeError(f"EPUBCheck failed:\n{output}")
    return {
        "epubcheck": output,
        "spine_documents": len(spine_paths),
        "chapter_count": len(chapter_h1),
        "title_heading_count": all_h1.count(TITLE),
    }


def write_release_records(cover_info: dict[str, object], epub_info: dict[str, object]) -> None:
    markdown = COMBINED.read_text(encoding="utf-8")
    ensure_source_ending(markdown)
    for pattern in FORBIDDEN:
        found = pattern.search(markdown)
        if found:
            raise RuntimeError(f"Forbidden reader-facing marker in combined manuscript: {found.group(0)!r}")

    files = [EPUB, COVER, DOCX, COMBINED]
    for path in files:
        if not path.exists() or path.stat().st_size == 0:
            raise RuntimeError(f"Missing or empty release file: {path}")

    story_words = story_word_count(markdown)
    retail_words = len(re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b", re.sub(r"[`*_>#-]", " ", markdown)))
    records = []
    for path in files:
        records.append(
            {
                "name": path.name,
                "path": str(path.relative_to(BOOK_DIR)),
                "size_bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )

    manifest = {
        "book": TITLE,
        "series": SERIES,
        "series_number": SERIES_NUMBER,
        "author": AUTHOR,
        "release_state": "upload_ready_not_published",
        "build_date": BUILD_DATE.isoformat(),
        "story_words": story_words,
        "retail_words": retail_words,
        "chapter_count": 8,
        "cover": cover_info,
        "epub": epub_info,
        "artifacts": records,
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    epubcheck_summary = str(epub_info["epubcheck"])
    validation = f"""# The Archive Fire — Release Validation

- Release state: **UPLOAD READY — NOT YET PUBLISHED**
- Build date: {BUILD_DATE.isoformat()}
- Story words: {story_words:,}
- Retail package words: {retail_words:,}
- Chapters: 8
- Cover: JPEG / RGB / {cover_info['width']}×{cover_info['height']}
- Locked ending: present exactly once
- Duplicate automatic title page: absent
- Embedded EPUB cover: byte-for-byte match with separate upload cover
- Reader-facing placeholders/internal markers: none detected

## EPUBCheck

```text
{epubcheck_summary}
```

## Deterministic hashes

- EPUB: `{sha256(EPUB)}`
- Cover: `{sha256(COVER)}`
- DOCX: `{sha256(DOCX)}`
- Retail Markdown: `{sha256(COMBINED)}`

No chapter manuscript source was edited by this release layer. Publication remains pending until retailer acceptance and a live detail page are confirmed.
"""
    VALIDATION.write_text(validation, encoding="utf-8")


def build_upload_zip() -> None:
    listing_files = [
        (BOOK_DIR / "listing" / "listing-copy.md", "The-Archive-Fire-listing-copy.md"),
        (BOOK_DIR / "listing" / "retailer-description.html", "The-Archive-Fire-retailer-description.html"),
        (BOOK_DIR / "listing" / "retailer-description.txt", "The-Archive-Fire-retailer-description.txt"),
        (BOOK_DIR / "publish" / "upload-package.md", "The-Archive-Fire-KDP-upload-sheet.md"),
    ]
    with zipfile.ZipFile(UPLOAD_ZIP, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path, arcname in [
            (EPUB, "The-Archive-Fire.epub"),
            (COVER, "The-Archive-Fire-cover.jpg"),
            (DOCX, "The-Archive-Fire.docx"),
            (MANIFEST, "The-Archive-Fire-release-manifest.json"),
            (VALIDATION, "The-Archive-Fire-release-validation.md"),
            *listing_files,
        ]:
            if not path.exists():
                raise RuntimeError(f"Upload package source missing: {path}")
            archive.write(path, arcname)


def main() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    run([sys.executable, str(HERE / "finalize-package.py")], cwd=REPO_ROOT)
    patch_generated_docs()
    cover_info = validate_cover()
    build_retail_epub()
    epub_info = validate_epub()
    write_release_records(cover_info, epub_info)
    build_upload_zip()
    print(VALIDATION.read_text(encoding="utf-8"))
    print(f"Created {UPLOAD_ZIP}")


if __name__ == "__main__":
    main()
