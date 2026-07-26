#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
import zipfile

from PIL import Image


EXPORT_DIR = Path(__file__).resolve().parent
BOOK_DIR = EXPORT_DIR.parent
REPO_ROOT = BOOK_DIR.parents[1]
VALIDATOR = EXPORT_DIR / "cover_provenance.py"
APPROVED_DIR = BOOK_DIR / "package" / "approved"
APPROVED_COVER = APPROVED_DIR / "The-Challenger-cover.jpg"
AUTHORITY = APPROVED_DIR / "approved-cover.json"
BUILD_SCRIPT = EXPORT_DIR / "build.sh"
WORKFLOW = REPO_ROOT / ".github" / "workflows" / "book-03-release-package.yml"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def make_image(path: Path, *, color: tuple[int, int, int], fmt: str, size: tuple[int, int]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", size, color).save(path, fmt)


def write_epub(path: Path, cover_bytes: bytes) -> None:
    container = """<?xml version="1.0"?>
<container xmlns="urn:oasis:names:tc:opendocument:xmlns:container" version="1.0">
  <rootfiles><rootfile full-path="EPUB/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>
"""
    opf = """<?xml version="1.0"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>Test</dc:title></metadata>
  <manifest><item id="cover" href="media/cover.jpg" media-type="image/jpeg" properties="cover-image"/></manifest>
  <spine/>
</package>
"""
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("META-INF/container.xml", container)
        archive.writestr("EPUB/content.opf", opf)
        archive.writestr("EPUB/media/cover.jpg", cover_bytes)


class Fixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.approved_dir = root / "books" / "book-03" / "package" / "approved"
        self.approved = self.approved_dir / "The-Challenger-cover.jpg"
        self.source = self.approved_dir / "The-Challenger-cover-source.png"
        self.authority = self.approved_dir / "approved-cover.json"
        make_image(self.approved, color=(30, 20, 40), fmt="JPEG", size=(1600, 2560))
        make_image(self.source, color=(30, 20, 40), fmt="PNG", size=(992, 1586))
        self.write_authority()

    def write_authority(self) -> None:
        record = {
            "book": "The Challenger",
            "author": "Vesper Blythe",
            "series": "The Blackwood Ridge Mysteries",
            "series_number": 3,
            "approval_status": "APPROVED",
            "approved_asset_path": "books/book-03/package/approved/The-Challenger-cover.jpg",
            "source_asset_path": "books/book-03/package/approved/The-Challenger-cover-source.png",
            "approved_sha256": sha256(self.approved),
            "approved_size_bytes": self.approved.stat().st_size,
            "approved_format": "JPEG",
            "approved_mode": "RGB",
            "approved_width": 1600,
            "approved_height": 2560,
            "approved_text": [
                "THE BLACKWOOD RIDGE MYSTERIES · BOOK 3",
                "THE CHALLENGER",
                "VESPER BLYTHE",
            ],
            "approval_note": "Test authority record.",
            "source_sha256": sha256(self.source),
            "source_size_bytes": self.source.stat().st_size,
            "source_format": "PNG",
            "source_mode": "RGB",
            "source_width": 992,
            "source_height": 1586,
        }
        self.authority.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")


def run_validator(authority: Path, *, standalone: Path | None = None, epub: Path | None = None) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, str(VALIDATOR), "--authority", str(authority)]
    if standalone is not None:
        command.extend(["--standalone", str(standalone)])
    if epub is not None:
        command.extend(["--epub", str(epub)])
    return subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


class CoverProvenanceRegressionTests(unittest.TestCase):
    def test_checked_in_authority_matches_author_approved_jpeg(self) -> None:
        self.assertTrue(AUTHORITY.is_file(), "approved-cover.json must lock the author-approved JPEG")
        completed = run_validator(AUTHORITY)
        self.assertEqual(completed.returncode, 0, completed.stderr)

    def test_missing_approved_cover_fails_closed(self) -> None:
        with TemporaryDirectory() as directory:
            fixture = Fixture(Path(directory))
            fixture.approved.unlink()
            completed = run_validator(fixture.authority)
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("missing", completed.stderr.lower())

    def test_modified_approved_cover_fails_locked_checksum(self) -> None:
        with TemporaryDirectory() as directory:
            fixture = Fixture(Path(directory))
            fixture.approved.write_bytes(fixture.approved.read_bytes() + b"modified")
            completed = run_validator(fixture.authority)
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("checksum", completed.stderr.lower())

    def test_generated_substitute_with_correct_dimensions_cannot_pass(self) -> None:
        with TemporaryDirectory() as directory:
            fixture = Fixture(Path(directory))
            make_image(fixture.approved, color=(90, 10, 10), fmt="JPEG", size=(1600, 2560))
            completed = run_validator(fixture.authority)
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("checksum", completed.stderr.lower())

    def test_standalone_and_embedded_covers_must_match_approved_bytes(self) -> None:
        with TemporaryDirectory() as directory:
            fixture = Fixture(Path(directory))
            standalone = Path(directory) / "The-Challenger-cover.jpg"
            shutil.copyfile(fixture.approved, standalone)
            substitute = Path(directory) / "substitute.jpg"
            make_image(substitute, color=(5, 80, 20), fmt="JPEG", size=(1600, 2560))
            epub = Path(directory) / "book.epub"
            write_epub(epub, substitute.read_bytes())
            completed = run_validator(fixture.authority, standalone=standalone, epub=epub)
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("embedded epub cover does not match", completed.stderr.lower())

    def test_valid_standalone_and_embedded_covers_pass(self) -> None:
        with TemporaryDirectory() as directory:
            fixture = Fixture(Path(directory))
            standalone = Path(directory) / "The-Challenger-cover.jpg"
            shutil.copyfile(fixture.approved, standalone)
            epub = Path(directory) / "book.epub"
            write_epub(epub, fixture.approved.read_bytes())
            completed = run_validator(fixture.authority, standalone=standalone, epub=epub)
            self.assertEqual(completed.returncode, 0, completed.stderr)

    def test_active_release_path_uses_approved_asset_and_not_generator(self) -> None:
        build = BUILD_SCRIPT.read_text(encoding="utf-8")
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("package/approved/The-Challenger-cover.jpg", build)
        self.assertIn("approved-cover.json", build)
        self.assertNotIn("generate-cover.py", build)
        self.assertNotIn("generate-cover.py", workflow)

    def test_authority_records_only_the_approved_cover_text(self) -> None:
        record = json.loads(AUTHORITY.read_text(encoding="utf-8"))
        self.assertEqual(
            record["approved_text"],
            [
                "THE BLACKWOOD RIDGE MYSTERIES · BOOK 3",
                "THE CHALLENGER",
                "VESPER BLYTHE",
            ],
        )
        self.assertEqual(record["approval_status"], "APPROVED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
