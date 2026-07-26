#!/usr/bin/env python3
"""Build and validate the Book 5 retailer package.

This release layer is deliberately fail-closed. It refuses to build or create a
release snapshot until an approved canonical cover exists at
``books/book-05/cover.jpeg`` and every package-readiness check passes. It never
uploads, submits, distributes, or publishes the book.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import uuid
import zipfile
from datetime import date
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

from bs4 import BeautifulSoup
from PIL import Image

TITLE = "The Planted Page"
AUTHOR = "Vesper Blythe"
SERIES = "The Blackwood Ridge Mysteries"
SERIES_NUMBER = 5
LANGUAGE = "en-US"
RIGHTS = "Copyright © 2026 Vesper Blythe. All rights reserved."
BUILD_DATE = date(2026, 7, 14)
FIXED_ZIP_TIME = (2026, 7, 14, 0, 0, 0)
FIXED_EPUB_UUID = str(
    uuid.uuid5(uuid.NAMESPACE_URL, "urn:blackwood-ridge:book-5:the-planted-page:vesper-blythe:release")
)
MANUSCRIPT_WORDS = 25174
COMBINED_WORDS = 25501
LOCKED_ENDING = "She closed the file."
PROVENANCE = "Found in returned Mercer volume by M. Hartwell; prior loose-paper location not established."
EXPECTED_COVER_SIZE = (1600, 2560)
EXPECTED_CHAPTERS = [
    "Chapter 1 — The Hand at the Door",
    "Chapter 2 — A Note in His Hand",
    "Chapter 3 — The Comparison Room",
    "Chapter 4 — The Same Letter Twice",
    "Chapter 5 — What the Trust Passed",
    "Chapter 6 — The Hand That Waited",
    "Chapter 7 — The Page Under Pressure",
    "Chapter 8 — The Current Hand",
]
FORBIDDEN = [
    re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.IGNORECASE),
    re.compile(r"AUTHOR DECISION REQUIRED", re.IGNORECASE),
    re.compile(r"<<<<<<|======|>>>>>>"),
    re.compile(r"eli-hidden-chronology|internal_series_spoilers|internal_continuity_control", re.IGNORECASE),
]

HERE = Path(__file__).resolve().parent
BOOK_DIR = HERE.parent
REPO_ROOT = BOOK_DIR.parents[1]
DIST = HERE / "dist"
COVER_SOURCE = BOOK_DIR / "cover.jpeg"
COMBINED = HERE / "manuscript-combined.md"
RETAIL_MD = DIST / "manuscript-retail.md"
EPUB = DIST / "The-Planted-Page.epub"
DOCX = DIST / "The-Planted-Page.docx"
COVER = DIST / "The-Planted-Page-cover.jpg"
MANIFEST = DIST / "release-manifest.json"
VALIDATION = DIST / "release-validation.md"
UPLOAD_ZIP = DIST / "The-Planted-Page-upload-package.zip"


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


def load_readiness_module(repo_root: Path):
    path = repo_root / "books/book-05/package/validate-readiness.py"
    spec = importlib.util.spec_from_file_location("book5_package_readiness", path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot import readiness validator: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_release_ready(repo_root: Path = REPO_ROOT) -> dict[str, Any]:
    canonical_cover = repo_root / "books/book-05/cover.jpeg"
    if not canonical_cover.exists():
        raise RuntimeError("Missing approved ebook cover at books/book-05/cover.jpeg")
    module = load_readiness_module(repo_root)
    result = module.validate(repo_root)
    if result["status"] != "ready_for_release_build":
        raise RuntimeError("Book 5 release preflight failed:\n- " + "\n- ".join(result["blockers"]))
    return result


def validate_reader_text(label: str, text: str) -> None:
    if text.count(LOCKED_ENDING) != 1:
        raise RuntimeError(f"{label}: locked ending count is {text.count(LOCKED_ENDING)}, expected 1")
    if text.count(PROVENANCE) != 1:
        raise RuntimeError(f"{label}: provenance count is {text.count(PROVENANCE)}, expected 1")
    for pattern in FORBIDDEN:
        match = pattern.search(text)
        if match:
            raise RuntimeError(f"{label}: forbidden reader-facing marker {match.group(0)!r}")


def validate_cover() -> dict[str, Any]:
    with Image.open(COVER_SOURCE) as image:
        image.load()
        if image.format != "JPEG":
            raise RuntimeError(f"Cover must be JPEG; found {image.format}")
        if image.mode != "RGB":
            raise RuntimeError(f"Cover must be RGB; found {image.mode}")
        if image.size != EXPECTED_COVER_SIZE:
            raise RuntimeError(f"Cover must be {EXPECTED_COVER_SIZE}; found {image.size}")
        if COVER_SOURCE.stat().st_size >= 50 * 1024 * 1024:
            raise RuntimeError("Cover must be under 50 MB")
        info = {
            "format": image.format,
            "mode": image.mode,
            "width": image.width,
            "height": image.height,
            "size_bytes": COVER_SOURCE.stat().st_size,
            "sha256": sha256(COVER_SOURCE),
        }
    shutil.copyfile(COVER_SOURCE, COVER)
    return info


def assemble_epub_source() -> None:
    source = COMBINED.read_text(encoding="utf-8")
    title_block = f"# {TITLE}\n\n**{AUTHOR}**\n\n*{SERIES} — Book {SERIES_NUMBER}*\n\n---\n\n"
    if not source.startswith(title_block):
        raise RuntimeError("Combined manuscript title block does not match the locked Book 5 format")
    retail = source[len(title_block):]
    validate_reader_text("Retail EPUB Markdown", retail)
    RETAIL_MD.write_text(retail, encoding="utf-8")


def rewrite_epub(path: Path, transform) -> None:
    temporary = path.with_suffix(path.suffix + ".rewrite")
    with zipfile.ZipFile(path, "r") as source, zipfile.ZipFile(temporary, "w") as target:
        entries = sorted(source.infolist(), key=lambda item: (item.filename != "mimetype", item.filename))
        for original in entries:
            data = source.read(original.filename)
            data = transform(original.filename, data)
            info = zipfile.ZipInfo(original.filename, FIXED_ZIP_TIME)
            info.create_system = 3
            info.external_attr = original.external_attr or (0o100644 << 16)
            info.compress_type = zipfile.ZIP_STORED if original.filename == "mimetype" else zipfile.ZIP_DEFLATED
            target.writestr(info, data, compress_type=info.compress_type, compresslevel=9)
    temporary.replace(path)


def locate_opf(archive: zipfile.ZipFile) -> str:
    root = ET.fromstring(archive.read("META-INF/container.xml"))
    rootfile = root.find(".//{*}rootfile")
    if rootfile is None or not rootfile.get("full-path"):
        raise RuntimeError("EPUB container has no OPF rootfile")
    return rootfile.get("full-path", "")


def locate_ncx(archive: zipfile.ZipFile, opf_path: str) -> str | None:
    opf_dir = Path(opf_path).parent
    opf = ET.fromstring(archive.read(opf_path))
    for item in opf.findall(".//{*}manifest/{*}item"):
        if item.get("media-type") == "application/x-dtbncx+xml":
            return str((opf_dir / item.get("href", "")).as_posix())
    return None


def add_series_metadata_and_normalize() -> None:
    with zipfile.ZipFile(EPUB) as archive:
        opf_path = locate_opf(archive)
        ncx_path = locate_ncx(archive, opf_path)

    def transform(name: str, data: bytes) -> bytes:
        if name not in (opf_path, ncx_path):
            return data
        text = data.decode("utf-8")
        # The NCX carries its own dtb:uid independent of the OPF identifier; both must
        # be pinned to the same fixed UUID so EPUBCheck's NCX-001 identifier-match rule
        # passes and rebuilds stay byte-stable.
        text = re.sub(r"urn:uuid:[0-9a-fA-F-]+", f"urn:uuid:{FIXED_EPUB_UUID}", text)
        text = re.sub(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", "2026-07-14T00:00:00Z", text)
        if name == opf_path and "belongs-to-collection" not in text:
            series_meta = (
                f'<meta property="belongs-to-collection" id="collection">{SERIES}</meta>\n'
                '<meta refines="#collection" property="collection-type">series</meta>\n'
                f'<meta refines="#collection" property="group-position">{SERIES_NUMBER}</meta>\n'
            )
            text = text.replace("</metadata>", series_meta + "</metadata>")
        return text.encode("utf-8")

    rewrite_epub(EPUB, transform)


def build_retail_epub() -> None:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise RuntimeError("pandoc is required")
    assemble_epub_source()
    command = [
        pandoc,
        str(RETAIL_MD),
        "--from=markdown",
        "--to=epub3",
        "--toc",
        "--toc-depth=1",
        "--epub-cover-image",
        str(COVER),
        "--metadata",
        f"title={TITLE}",
        "--metadata",
        f"subtitle={SERIES}, Book {SERIES_NUMBER}",
        "--metadata",
        f"author={AUTHOR}",
        "--metadata",
        f"lang={LANGUAGE}",
        "--metadata",
        f"rights={RIGHTS}",
        "--metadata",
        "subject=Atmospheric cozy mystery; amateur sleuth; handwriting mystery",
        "-o",
        str(EPUB),
    ]
    css = HERE / "epub.css"
    if css.exists():
        command[command.index("-o"):command.index("-o")] = ["--css", str(css)]
    run(command)
    add_series_metadata_and_normalize()


def validate_epub() -> dict[str, Any]:
    with zipfile.ZipFile(EPUB) as archive:
        names = archive.namelist()
        if not names or names[0] != "mimetype":
            raise RuntimeError("EPUB mimetype must be first")
        if archive.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            raise RuntimeError("EPUB mimetype must be uncompressed")
        if archive.read("mimetype") != b"application/epub+zip":
            raise RuntimeError("EPUB mimetype is incorrect")
        opf_path = locate_opf(archive)
        opf = ET.fromstring(archive.read(opf_path))
        opf_dir = Path(opf_path).parent
        title = normalize("".join(node.text or "" for node in opf.findall(".//{*}title")))
        creators = [normalize(node.text or "") for node in opf.findall(".//{*}creator")]
        languages = [normalize(node.text or "") for node in opf.findall(".//{*}language")]
        rights = [normalize(node.text or "") for node in opf.findall(".//{*}rights")]
        if title != TITLE or AUTHOR not in creators or LANGUAGE not in languages or RIGHTS not in rights:
            raise RuntimeError("EPUB bibliographic metadata mismatch")
        collection_values = [normalize(node.text or "") for node in opf.findall(".//{*}meta") if node.get("property") == "belongs-to-collection"]
        group_positions = [normalize(node.text or "") for node in opf.findall(".//{*}meta") if node.get("property") == "group-position"]
        if SERIES not in collection_values or str(SERIES_NUMBER) not in group_positions:
            raise RuntimeError("EPUB series metadata is missing or incorrect")

        manifest: dict[str, tuple[str, str]] = {}
        cover_href = nav_href = None
        for item in opf.findall(".//{*}manifest/{*}item"):
            item_id = item.get("id", "")
            resolved = str((opf_dir / item.get("href", "")).as_posix())
            properties = item.get("properties", "")
            manifest[item_id] = (resolved, properties)
            if "cover-image" in properties.split():
                cover_href = resolved
            if "nav" in properties.split():
                nav_href = resolved
        if not cover_href or archive.read(cover_href) != COVER.read_bytes():
            raise RuntimeError("Embedded cover does not match the separate upload cover")
        if not nav_href or nav_href not in names:
            raise RuntimeError("EPUB navigation document is missing")
        spine_ids = [node.get("idref", "") for node in opf.findall(".//{*}spine/{*}itemref")]
        spine_paths = [manifest[item_id][0] for item_id in spine_ids if item_id in manifest]
        if not spine_paths or any(path not in names for path in spine_paths):
            raise RuntimeError("EPUB spine is incomplete")

        all_h1: list[str] = []
        extracted_parts: list[str] = []
        for path in spine_paths:
            if path == nav_href:
                # Pandoc includes the nav document in the spine and auto-titles it with
                # the book title; its headings/content are validated separately below.
                continue
            soup = BeautifulSoup(archive.read(path), "html.parser")
            all_h1.extend(normalize(node.get_text(" ", strip=True)) for node in soup.find_all("h1"))
            extracted_parts.append(soup.get_text(" ", strip=True))
        chapter_h1 = [value for value in all_h1 if value.startswith("Chapter ")]
        if chapter_h1 != EXPECTED_CHAPTERS:
            raise RuntimeError(f"EPUB chapter sequence mismatch: {chapter_h1!r}")
        if all_h1.count(TITLE) != 1:
            raise RuntimeError(f"EPUB title heading count is {all_h1.count(TITLE)}, expected 1")
        extracted = "\n".join(extracted_parts)
        validate_reader_text("EPUB", extracted)
        nav_text = normalize(BeautifulSoup(archive.read(nav_href), "html.parser").get_text(" ", strip=True))
        for heading in [*EXPECTED_CHAPTERS, "A Note from the Author", SERIES, "About the Author"]:
            if heading not in nav_text:
                raise RuntimeError(f"EPUB navigation missing {heading}")

    epubcheck = shutil.which("epubcheck")
    if not epubcheck:
        raise RuntimeError("epubcheck is required for final package validation")
    result = run([epubcheck, str(EPUB)], check=False)
    if result.returncode != 0:
        raise RuntimeError(f"EPUBCheck failed:\n{result.stdout}")
    output = result.stdout.strip()
    if "0 errors" not in output and "No errors or warnings detected" not in output:
        raise RuntimeError(f"Unexpected EPUBCheck result:\n{output}")
    return {
        "epubcheck": output,
        "chapter_count": len(chapter_h1),
        "spine_documents": len(spine_paths),
        "title_heading_count": all_h1.count(TITLE),
    }


def validate_support_files() -> None:
    html_path = BOOK_DIR / "listing/retailer-description.html"
    html = html_path.read_text(encoding="utf-8")
    if len(html) > 4000:
        raise RuntimeError(f"Retailer HTML is {len(html)} characters; limit is 4,000")
    soup = BeautifulSoup(html, "html.parser")
    allowed = {"p", "b", "em", "i", "u", "br", "h4", "h5", "h6", "ol", "ul", "li"}
    unsupported = sorted({tag.name for tag in soup.find_all()} - allowed)
    if unsupported:
        raise RuntimeError(f"Unsupported retailer HTML tags: {unsupported}")
    for path in [
        BOOK_DIR / "listing/listing-copy.md",
        BOOK_DIR / "listing/retailer-description.txt",
        BOOK_DIR / "publish/upload-package.md",
        BOOK_DIR / "publication/metadata.md",
    ]:
        if not path.exists() or not path.read_text(encoding="utf-8").strip():
            raise RuntimeError(f"Missing or empty support file: {path}")


def write_release_records(cover_info: dict[str, Any], epub_info: dict[str, Any]) -> None:
    validate_support_files()
    combined_text = COMBINED.read_text(encoding="utf-8")
    validate_reader_text("Combined Markdown", combined_text)
    files = [EPUB, COVER, DOCX, COMBINED]
    for path in files:
        if not path.exists() or path.stat().st_size == 0:
            raise RuntimeError(f"Missing or empty release file: {path}")
    artifacts = [
        {
            "name": path.name,
            "path": str(path.relative_to(BOOK_DIR)),
            "size_bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in files
    ]
    payload = {
        "book": TITLE,
        "series": SERIES,
        "series_number": SERIES_NUMBER,
        "author": AUTHOR,
        "release_state": "upload_ready_not_published",
        "validated": BUILD_DATE.isoformat(),
        "manuscript_body_words": MANUSCRIPT_WORDS,
        "combined_reader_facing_words": COMBINED_WORDS,
        "chapter_count": 8,
        "cover": cover_info,
        "epub": epub_info,
        "artifacts": artifacts,
    }
    MANIFEST.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    report = f"""# The Planted Page — Release Validation

- Release state: **UPLOAD READY — NOT YET PUBLISHED**
- Build date: {BUILD_DATE.isoformat()}
- Manuscript body words: {MANUSCRIPT_WORDS:,}
- Combined reader-facing words: {COMBINED_WORDS:,}
- Chapters: 8
- Cover: JPEG / RGB / {cover_info['width']}×{cover_info['height']}
- Locked ending: present exactly once
- Exact provenance: present exactly once
- Title pages: exactly one
- Embedded EPUB cover: byte-for-byte match with separate upload cover
- Reader-facing placeholders/internal markers: none detected
- Series metadata: {SERIES}, position {SERIES_NUMBER}

## EPUBCheck

```text
{epub_info['epubcheck']}
```

## Deterministic hashes

- EPUB: `{sha256(EPUB)}`
- Cover: `{sha256(COVER)}`
- DOCX: `{sha256(DOCX)}`
- Reader-facing Markdown: `{sha256(COMBINED)}`

No chapter manuscript source was edited by this release layer. Publication remains pending until retailer acceptance and a live detail page are confirmed.
"""
    VALIDATION.write_text(report, encoding="utf-8")


def build_upload_zip() -> None:
    sources = [
        (EPUB, "The-Planted-Page.epub"),
        (COVER, "The-Planted-Page-cover.jpg"),
        (DOCX, "The-Planted-Page.docx"),
        (MANIFEST, "The-Planted-Page-release-manifest.json"),
        (VALIDATION, "The-Planted-Page-release-validation.md"),
        (BOOK_DIR / "listing/listing-copy.md", "The-Planted-Page-listing-copy.md"),
        (BOOK_DIR / "listing/retailer-description.html", "The-Planted-Page-retailer-description.html"),
        (BOOK_DIR / "listing/retailer-description.txt", "The-Planted-Page-retailer-description.txt"),
        (BOOK_DIR / "publish/upload-package.md", "The-Planted-Page-KDP-upload-sheet.md"),
    ]
    with zipfile.ZipFile(UPLOAD_ZIP, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path, arcname in sources:
            if not path.exists():
                raise RuntimeError(f"Upload package source missing: {path}")
            info = zipfile.ZipInfo(arcname, FIXED_ZIP_TIME)
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def main() -> None:
    require_release_ready(REPO_ROOT)
    DIST.mkdir(parents=True, exist_ok=True)
    run([sys.executable, str(HERE / "run-export.py")], cwd=REPO_ROOT)
    cover_info = validate_cover()
    build_retail_epub()
    epub_info = validate_epub()
    write_release_records(cover_info, epub_info)
    build_upload_zip()
    print(VALIDATION.read_text(encoding="utf-8"))
    print(f"Created {UPLOAD_ZIP}")


if __name__ == "__main__":
    main()
