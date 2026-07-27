#!/usr/bin/env python3
"""Regression tests for controlled-export record authority normalization."""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("sanitize-export-records.py")


def load_module():
    spec = importlib.util.spec_from_file_location("book6_sanitize_export_records", MODULE_PATH)
    if not spec or not spec.loader:
        raise RuntimeError(f"Unable to import {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SanitizeExportRecordsTests(unittest.TestCase):
    def fixture(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        export = root / "books/book-06/export"
        export.mkdir(parents=True)
        (export / "export-readiness.md").write_text(
            "**Controlled proofreading complete. Repository-standard export assembly complete and validated. Package, cover, listing, upload, and publication remain pending.**\n\n"
            "No cover, listing copy, retailer form, upload ZIP, advertising asset, release package, retailer submission, publication record, or release-status change is included. The next stage after merge is **Book 6 controlled package assembly/readiness**.\n",
            encoding="utf-8",
        )
        (export / "validation-report.md").write_text(
            "# Validation\n\nPackage, cover, listing, upload, and publication remain pending.\n",
            encoding="utf-8",
        )
        (root / "books/book-06/export-report.md").write_text(
            "- Exact Book 5 status: package in progress; publication pending; approved canonical ebook cover remains the blocker; Book 5 is not upload ready.\n"
            "- Book 7 Chapter 1 exists and is formally accepted at 3,100 manuscript-prose words; it is outside Book 6 export authority, and no Book 7 chapter manuscript changed in this validation scope.\n"
            "- Exact Book 6 status: controlled revision, line edit, final prose polish, proofreading, and export assembly complete; package, cover, listing, upload, and publication pending; Book 6 is not upload ready.\n\n"
            "## Intentionally not created\n\n"
            "No blocker remains within controlled export assembly. Package, cover, listing, upload, and publication work remain deliberately deferred. After this export pull request is reviewed and merged, the recommended next stage is **Book 6 controlled package assembly/readiness**.\n",
            encoding="utf-8",
        )
        (export / "build.log").write_text(
            "Validated The Pattern: 25,646 manuscript-prose words\n"
            "Checks: 293/293 passed\n"
            "Package: pending\nCover: pending\nListing: pending\nUpload: pending\nPublication: pending\n",
            encoding="utf-8",
        )
        dist = export / "dist"
        dist.mkdir()
        (dist / "export-manifest.json").write_text(
            json.dumps(
                {
                    "status": "export_validated_package_pending",
                    "package_status": "pending",
                    "cover_status": "pending",
                    "listing_status": "pending",
                    "upload_status": "pending",
                    "publication_status": "pending",
                    "upload_ready": False,
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        return temp, root

    def test_sanitizes_all_lifecycle_claims(self) -> None:
        _, root = self.fixture()
        module = load_module()
        module.sanitize(root)
        combined = "\n".join(
            path.read_text(encoding="utf-8")
            for path in (
                root / "books/book-06/export/export-readiness.md",
                root / "books/book-06/export/validation-report.md",
                root / "books/book-06/export-report.md",
                root / "books/book-06/export/build.log",
            )
        )
        self.assertNotIn("Package, cover, listing, upload, and publication remain pending", combined)
        self.assertNotIn("Book 7 Chapter 1 exists", combined)
        self.assertNotIn("Book 6 controlled package assembly/readiness", combined)
        self.assertIn("outside this controlled-export record's authority", combined)
        manifest = json.loads((root / "books/book-06/export/dist/export-manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["status"], "export_identity_validated")
        self.assertEqual(manifest["package_status"], "not_evaluated")
        self.assertIsNone(manifest["upload_ready"])
        self.assertEqual(manifest["lifecycle_status_authority"], "governing repository lifecycle records")

    def test_is_idempotent(self) -> None:
        _, root = self.fixture()
        module = load_module()
        module.sanitize(root)
        before = {
            path: path.read_bytes()
            for path in (root / "books/book-06").rglob("*")
            if path.is_file()
        }
        module.sanitize(root)
        after = {path: path.read_bytes() for path in before}
        self.assertEqual(before, after)

    def test_missing_expected_record_fails_closed(self) -> None:
        _, root = self.fixture()
        (root / "books/book-06/export/export-readiness.md").write_text("unexpected\n", encoding="utf-8")
        module = load_module()
        with self.assertRaises(RuntimeError):
            module.sanitize(root)


if __name__ == "__main__":
    unittest.main()
