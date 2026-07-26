#!/usr/bin/env python3
"""Regression tests for the Book 6 package-readiness gate."""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
MODULE_PATH = HERE / "validate-readiness.py"


def load_module():
    spec = importlib.util.spec_from_file_location("book6_package_readiness", MODULE_PATH)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot import {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def seed_repo(root: Path) -> None:
    book = root / "books/book-06"
    (book / "listing").mkdir(parents=True)
    (book / "export").mkdir(parents=True)
    (book / "package").mkdir(parents=True)
    (book / "listing/retailer-description.html").write_text(
        "<p><b>The maps were real.</b></p><p>Callie investigates.</p>\n",
        encoding="utf-8",
    )
    (book / "listing/listing-copy.md").write_text(
        "\n".join(
            [
                "# Listing",
                "1. `historical records mystery`",
                "2. `small town Virginia mystery`",
                "3. `antiquarian bookshop sleuth`",
                "4. `clean mystery novella`",
                "5. `female amateur sleuth`",
                "6. `cold case mystery`",
                "7. `atmospheric small town mystery`",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    (book / "export/word-count-report.md").write_text(
        "Manuscript-prose total: **25,646**\nCombined reader-facing total: **25,918**\n",
        encoding="utf-8",
    )
    (book / "export/validation-report.md").write_text(
        "Checks passed: **293/293**\nMessages: 0 fatals / 0 errors / 0 warnings / 0 infos\n",
        encoding="utf-8",
    )
    chapters = [
        "The Box at Closing",
        "A Fall That Did Not Fit",
        "The Surveyor’s Missing Line",
        "Marks Made Later",
        "The Road Through Bellweather",
        "What the Ledger Withheld",
        "The Weight of the Map",
        "The Pattern",
    ]
    manuscript = "\n\n".join(
        f"# Chapter {number} — {title}\n\nBody {number}."
        for number, title in enumerate(chapters, 1)
    )
    manuscript += (
        "\n\nFound in returned Mercer volume by M. Hartwell; prior loose-paper location not established."
        "\n\nWho knew which page she would open next?\n"
    )
    (book / "export/manuscript-combined.md").write_text(manuscript, encoding="utf-8")
    (book / "package/cover-approval.json").write_text(
        json.dumps(
            {
                "cover_path": "books/book-06/cover.jpeg",
                "status": "pending",
                "approved_by": None,
                "approved_on": None,
                "sha256": None,
            }
        )
        + "\n",
        encoding="utf-8",
    )


def approve_cover(module, root: Path, cover: Path) -> None:
    approval = root / "books/book-06/package/cover-approval.json"
    approval.write_text(
        json.dumps(
            {
                "cover_path": "books/book-06/cover.jpeg",
                "status": "approved",
                "approved_by": "Vesper Blythe",
                "approved_on": "2026-07-26",
                "sha256": module.sha256(cover),
            }
        )
        + "\n",
        encoding="utf-8",
    )


class PackageReadinessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_missing_cover_is_only_blocker(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            seed_repo(root)
            result = self.module.validate(root)
            self.assertEqual(len(result["blockers"]), 1)
            self.assertIn("Missing or unapproved ebook cover", result["blockers"][0])
            self.assertEqual(result["checks_passed"], result["checks_total"] - 1)

    def test_valid_but_unapproved_cover_remains_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            seed_repo(root)
            cover = root / "books/book-06/cover.jpeg"
            Image.new("RGB", (1600, 2560)).save(cover, format="JPEG", quality=95)
            result = self.module.validate(root)
            self.assertEqual(result["status"], "blocked")
            self.assertIn("Missing or unapproved ebook cover", result["blockers"][0])

    def test_valid_approved_cover_clears_cover_gate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            seed_repo(root)
            cover = root / "books/book-06/cover.jpeg"
            Image.new("RGB", (1600, 2560)).save(cover, format="JPEG", quality=95)
            approve_cover(self.module, root, cover)
            result = self.module.validate(root)
            self.assertEqual(result["status"], "ready_for_release_build")
            self.assertEqual(result["blockers"], [])

    def test_duplicate_locked_ending_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            seed_repo(root)
            path = root / "books/book-06/export/manuscript-combined.md"
            path.write_text(
                path.read_text(encoding="utf-8") + "Who knew which page she would open next?\n",
                encoding="utf-8",
            )
            result = self.module.validate(root)
            self.assertTrue(any("locked final line exactly once" in blocker for blocker in result["blockers"]))

    def test_unsupported_description_tag_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            seed_repo(root)
            path = root / "books/book-06/listing/retailer-description.html"
            path.write_text("<div>Unsupported</div>\n", encoding="utf-8")
            result = self.module.validate(root)
            self.assertTrue(any("unsupported HTML tag" in blocker for blocker in result["blockers"]))


if __name__ == "__main__":
    unittest.main()
