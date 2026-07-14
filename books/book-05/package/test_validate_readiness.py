#!/usr/bin/env python3
"""Regression tests for the Book 5 package-readiness gate."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
MODULE_PATH = HERE / "validate-readiness.py"


def load_module():
    spec = importlib.util.spec_from_file_location("book5_package_readiness", MODULE_PATH)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot import {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def seed_repo(root: Path) -> None:
    book = root / "books/book-05"
    (book / "listing").mkdir(parents=True)
    (book / "export").mkdir(parents=True)
    (book / "listing/retailer-description.html").write_text(
        "<p><b>Everyone recognizes the handwriting.</b></p><p>Callie investigates.</p>\n",
        encoding="utf-8",
    )
    (book / "listing/listing-copy.md").write_text(
        "\n".join(
            [
                "# Listing",
                "1. `handwriting forgery mystery`",
                "2. `small town Virginia mystery`",
                "3. `antiquarian bookshop sleuth`",
                "4. `clean mystery novella`",
                "5. `female records consultant`",
                "6. `family inheritance mystery`",
                "7. `winter atmospheric mystery`",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    (book / "export/word-count-report.md").write_text(
        "Manuscript-prose total: **25,174**\nCombined reader-facing total: **25,501**\n",
        encoding="utf-8",
    )
    (book / "export/validation-report.md").write_text(
        "Checks passed: **207/207**\nMessages: 0 fatals / 0 errors / 0 warnings / 0 infos\n",
        encoding="utf-8",
    )
    chapters = [
        "The Hand at the Door",
        "A Note in His Hand",
        "The Comparison Room",
        "The Same Letter Twice",
        "What the Trust Passed",
        "The Hand That Waited",
        "The Page Under Pressure",
        "The Current Hand",
    ]
    manuscript = "\n\n".join(
        f"# Chapter {number} — {title}\n\nBody {number}."
        for number, title in enumerate(chapters, 1)
    )
    manuscript += (
        "\n\nFound in returned Mercer volume by M. Hartwell; prior loose-paper location not established."
        "\n\nShe closed the file.\n"
    )
    (book / "export/manuscript-combined.md").write_text(manuscript, encoding="utf-8")


class PackageReadinessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_missing_cover_is_only_blocker(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            seed_repo(root)
            result = self.module.validate(root)
            self.assertEqual(
                result["blockers"],
                ["Missing approved ebook cover at books/book-05/cover.jpeg"],
            )
            self.assertEqual(result["checks_passed"], result["checks_total"] - 1)

    def test_valid_cover_clears_cover_gate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            seed_repo(root)
            cover = root / "books/book-05/cover.jpeg"
            Image.new("RGB", (1600, 2560)).save(cover, format="JPEG", quality=95)
            result = self.module.validate(root)
            self.assertEqual(result["status"], "ready_for_release_build")
            self.assertEqual(result["blockers"], [])

    def test_duplicate_locked_ending_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            seed_repo(root)
            path = root / "books/book-05/export/manuscript-combined.md"
            path.write_text(path.read_text(encoding="utf-8") + "She closed the file.\n", encoding="utf-8")
            result = self.module.validate(root)
            self.assertTrue(any("locked final line exactly once" in blocker for blocker in result["blockers"]))

    def test_unsupported_description_tag_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            seed_repo(root)
            path = root / "books/book-05/listing/retailer-description.html"
            path.write_text("<div>Unsupported</div>\n", encoding="utf-8")
            result = self.module.validate(root)
            self.assertTrue(any("unsupported HTML tag" in blocker for blocker in result["blockers"]))


if __name__ == "__main__":
    unittest.main()
