#!/usr/bin/env python3
"""Validate the author-approved Book 3 cover and every release copy of it."""
from __future__ import annotations

import argparse
from io import BytesIO
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys
import zipfile
from xml.etree import ElementTree as ET

from PIL import Image, UnidentifiedImageError


BOOK_TITLE = "The Challenger"
AUTHOR = "Vesper Blythe"
SERIES = "The Blackwood Ridge Mysteries"
SERIES_NUMBER = 3
APPROVED_TEXT = [
    "THE BLACKWOOD RIDGE MYSTERIES · BOOK 3",
    "THE CHALLENGER",
    "VESPER BLYTHE",
]
REQUIRED_FIELDS = {
    "book",
    "author",
    "series",
    "series_number",
    "approval_status",
    "approved_asset_path",
    "source_asset_path",
    "approved_sha256",
    "approved_size_bytes",
    "approved_format",
    "approved_mode",
    "approved_width",
    "approved_height",
    "approved_text",
    "approval_note",
}


class CoverProvenanceError(ValueError):
    """Raised when the approved-cover chain is incomplete or inconsistent."""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
    except OSError as exc:
        raise CoverProvenanceError(f"approved cover is unreadable: {path}: {exc}") from exc
    return digest.hexdigest()


def local_name(tag: str) -> str:
    return tag.split("}", 1)[-1]


def load_authority(path: Path) -> dict[str, object]:
    if not path.is_file():
        raise CoverProvenanceError(f"approved-cover authority record is missing: {path}")
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise CoverProvenanceError(f"approved-cover authority record is unreadable: {path}: {exc}") from exc
    if not isinstance(record, dict):
        raise CoverProvenanceError("approved-cover authority record must be a JSON object")
    missing = sorted(REQUIRED_FIELDS - set(record))
    if missing:
        raise CoverProvenanceError(f"approved-cover authority record is missing fields: {', '.join(missing)}")
    expected_identity = {
        "book": BOOK_TITLE,
        "author": AUTHOR,
        "series": SERIES,
        "series_number": SERIES_NUMBER,
        "approval_status": "APPROVED",
        "approved_format": "JPEG",
        "approved_mode": "RGB",
        "approved_width": 1600,
        "approved_height": 2560,
        "approved_text": APPROVED_TEXT,
    }
    for field, expected in expected_identity.items():
        if record.get(field) != expected:
            raise CoverProvenanceError(
                f"approved-cover authority field {field!r} must be {expected!r}, got {record.get(field)!r}"
            )
    approved_hash = record.get("approved_sha256")
    if not isinstance(approved_hash, str) or len(approved_hash) != 64:
        raise CoverProvenanceError("approved_sha256 must be a 64-character SHA-256 value")
    if not isinstance(record.get("approved_size_bytes"), int) or record["approved_size_bytes"] <= 0:
        raise CoverProvenanceError("approved_size_bytes must be a positive integer")
    return record


def repository_root(authority_path: Path) -> Path:
    resolved = authority_path.resolve()
    try:
        return resolved.parents[4]
    except IndexError as exc:
        raise CoverProvenanceError(f"cannot infer repository root from authority path: {authority_path}") from exc


def resolve_record_path(repo_root: Path, raw_path: object, field: str) -> Path:
    if not isinstance(raw_path, str) or not raw_path:
        raise CoverProvenanceError(f"{field} must be a non-empty repository-relative path")
    candidate = (repo_root / raw_path).resolve()
    try:
        candidate.relative_to(repo_root.resolve())
    except ValueError as exc:
        raise CoverProvenanceError(f"{field} escapes the repository root: {raw_path}") from exc
    return candidate


def inspect_image(path: Path) -> dict[str, object]:
    try:
        with Image.open(path) as image:
            image.load()
            return {
                "format": image.format,
                "mode": image.mode,
                "width": image.width,
                "height": image.height,
            }
    except (OSError, UnidentifiedImageError) as exc:
        raise CoverProvenanceError(f"cover image is unreadable or corrupt: {path}: {exc}") from exc


def validate_recorded_asset(
    path: Path,
    record: dict[str, object],
    *,
    prefix: str,
) -> dict[str, object]:
    if not path.is_file():
        raise CoverProvenanceError(f"{prefix} asset is missing: {path}")
    actual_hash = sha256(path)
    expected_hash = record.get(f"{prefix}_sha256")
    if expected_hash is not None and actual_hash != expected_hash:
        raise CoverProvenanceError(
            f"{prefix} cover checksum mismatch: expected {expected_hash}, got {actual_hash}"
        )
    actual_size = path.stat().st_size
    expected_size = record.get(f"{prefix}_size_bytes")
    if expected_size is not None and actual_size != expected_size:
        raise CoverProvenanceError(
            f"{prefix} cover byte size mismatch: expected {expected_size}, got {actual_size}"
        )
    image = inspect_image(path)
    for field in ("format", "mode", "width", "height"):
        expected = record.get(f"{prefix}_{field}")
        if expected is not None and image[field] != expected:
            raise CoverProvenanceError(
                f"{prefix} cover {field} mismatch: expected {expected!r}, got {image[field]!r}"
            )
    return {"path": str(path), "sha256": actual_hash, "size_bytes": actual_size, **image}


def validate_approved_asset(authority_path: Path) -> dict[str, object]:
    record = load_authority(authority_path)
    repo_root = repository_root(authority_path)
    approved_path = resolve_record_path(repo_root, record["approved_asset_path"], "approved_asset_path")
    source_path = resolve_record_path(repo_root, record["source_asset_path"], "source_asset_path")
    approved = validate_recorded_asset(approved_path, record, prefix="approved")
    source = validate_recorded_asset(source_path, record, prefix="source")
    return {
        "record": record,
        "repository_root": str(repo_root),
        "authority_path": str(authority_path),
        "approved": approved,
        "source": source,
    }


def extract_epub_cover(epub_path: Path) -> tuple[str, bytes]:
    if not epub_path.is_file():
        raise CoverProvenanceError(f"EPUB is missing: {epub_path}")
    try:
        with zipfile.ZipFile(epub_path) as archive:
            names = set(archive.namelist())
            container_path = "META-INF/container.xml"
            if container_path not in names:
                raise CoverProvenanceError("EPUB container.xml is missing")
            container = ET.fromstring(archive.read(container_path))
            rootfile = next((item for item in container.iter() if local_name(item.tag) == "rootfile"), None)
            if rootfile is None or not rootfile.attrib.get("full-path"):
                raise CoverProvenanceError("EPUB rootfile is not declared")
            opf_path = rootfile.attrib["full-path"]
            if opf_path not in names:
                raise CoverProvenanceError(f"EPUB package document is missing: {opf_path}")
            opf = ET.fromstring(archive.read(opf_path))
            manifest = next((item for item in opf if local_name(item.tag) == "manifest"), None)
            if manifest is None:
                raise CoverProvenanceError("EPUB manifest is missing")
            cover_item = None
            for item in manifest:
                if local_name(item.tag) != "item":
                    continue
                if "cover-image" in set(item.attrib.get("properties", "").split()):
                    cover_item = item
                    break
            if cover_item is None or not cover_item.attrib.get("href"):
                raise CoverProvenanceError("EPUB does not declare a cover-image resource")
            embedded_path = str(PurePosixPath(opf_path).parent / cover_item.attrib["href"])
            if embedded_path not in names:
                raise CoverProvenanceError(f"EPUB embedded cover is missing: {embedded_path}")
            data = archive.read(embedded_path)
    except zipfile.BadZipFile as exc:
        raise CoverProvenanceError(f"EPUB is not a readable ZIP archive: {epub_path}") from exc
    except ET.ParseError as exc:
        raise CoverProvenanceError(f"EPUB cover metadata XML is invalid: {exc}") from exc
    try:
        with Image.open(BytesIO(data)) as image:
            image.load()
    except (OSError, UnidentifiedImageError) as exc:
        raise CoverProvenanceError(f"EPUB embedded cover is unreadable or corrupt: {exc}") from exc
    return embedded_path, data


def validate_release_covers(
    authority_path: Path,
    *,
    standalone_path: Path | None = None,
    epub_path: Path | None = None,
) -> dict[str, object]:
    result = validate_approved_asset(authority_path)
    approved_hash = str(result["approved"]["sha256"])
    if standalone_path is not None:
        if not standalone_path.is_file():
            raise CoverProvenanceError(f"standalone release cover is missing: {standalone_path}")
        standalone_hash = sha256(standalone_path)
        if standalone_hash != approved_hash:
            raise CoverProvenanceError(
                f"standalone release cover does not match the approved cover checksum: "
                f"expected {approved_hash}, got {standalone_hash}"
            )
        result["standalone"] = {
            "path": str(standalone_path),
            "sha256": standalone_hash,
            "size_bytes": standalone_path.stat().st_size,
        }
    if epub_path is not None:
        embedded_path, embedded_bytes = extract_epub_cover(epub_path)
        embedded_hash = sha256_bytes(embedded_bytes)
        if embedded_hash != approved_hash:
            raise CoverProvenanceError(
                f"embedded EPUB cover does not match the approved cover checksum: "
                f"expected {approved_hash}, got {embedded_hash}"
            )
        if standalone_path is not None and embedded_hash != str(result["standalone"]["sha256"]):
            raise CoverProvenanceError("embedded EPUB cover does not match the standalone release cover")
        result["embedded"] = {
            "path": embedded_path,
            "sha256": embedded_hash,
            "size_bytes": len(embedded_bytes),
        }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--authority", type=Path, required=True)
    parser.add_argument("--standalone", type=Path)
    parser.add_argument("--epub", type=Path)
    args = parser.parse_args()
    try:
        result = validate_release_covers(
            args.authority,
            standalone_path=args.standalone,
            epub_path=args.epub,
        )
    except CoverProvenanceError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    summary = {
        "status": "PASS",
        "authority_path": result["authority_path"],
        "approved": result["approved"],
        "source": result["source"],
    }
    if "standalone" in result:
        summary["standalone"] = result["standalone"]
    if "embedded" in result:
        summary["embedded"] = result["embedded"]
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
