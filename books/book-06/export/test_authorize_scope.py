#!/usr/bin/env python3
"""Regression tests for Book 6 workflow authority classification."""
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

POLICY = Path(__file__).with_name("authorize-scope.py")
spec = importlib.util.spec_from_file_location("book6_authorize_scope", POLICY)
if not spec or not spec.loader:
    raise RuntimeError(f"Cannot import {POLICY}")
policy = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = policy
spec.loader.exec_module(policy)


class AuthorityTests(unittest.TestCase):
    def test_unchanged_existing_book7_prose_uses_normal_validation(self):
        self.assertEqual(
            policy.classify_scope(["books/book-06/export/finalize-package.py"]),
            "book6_validation",
        )

    def test_pr42_authorized_drafting_shape_passes(self):
        self.assertEqual(
            policy.classify_scope([
                "books/book-07/control/chapter-02-mission-lock.md",
                "books/book-07/manuscript/ch-02.md",
                "books/book-07/README.md",
                "books/book-07/progress.yaml",
                "books/book-07/manuscript/README.md",
                "series-outline.md",
            ]),
            "authorized_book7_drafting",
        )

    def test_book6_export_mixed_with_book7_manuscript_fails(self):
        with self.assertRaises(RuntimeError):
            policy.classify_scope([
                "books/book-06/export/finalize-package.py",
                "books/book-07/manuscript/ch-05.md",
            ])

    def test_book6_manuscript_mixed_with_book7_manuscript_fails(self):
        with self.assertRaises(RuntimeError):
            policy.classify_scope([
                "books/book-06/manuscript/ch-01.md",
                "books/book-07/manuscript/ch-05.md",
            ])

    def test_book5_book8_cover_and_release_paths_fail(self):
        prohibited = [
            "books/book-05/README.md",
            "books/book-08/outline.md",
            "books/book-03/package/approved/The-Challenger-cover.jpg",
            "books/book-07/package/metadata.md",
            ".github/workflows/book-03-release-package.yml",
        ]
        for path in prohibited:
            with self.subTest(path=path), self.assertRaises(RuntimeError):
                policy.classify_scope([
                    "books/book-07/manuscript/ch-05.md", path
                ])

    def test_unrecognized_mixed_path_fails_closed(self):
        with self.assertRaises(RuntimeError):
            policy.classify_scope([
                "books/book-07/manuscript/ch-05.md",
                "notes/free-form.txt",
            ])

    def test_missing_explicit_base_fails_closed(self):
        import os
        old = os.environ.get("BOOK6_SCOPE_BASE_REF")
        os.environ["BOOK6_SCOPE_BASE_REF"] = "missing-base"
        try:
            with self.assertRaises(RuntimeError):
                policy.resolve_scope_base()
        finally:
            if old is None:
                os.environ.pop("BOOK6_SCOPE_BASE_REF", None)
            else:
                os.environ["BOOK6_SCOPE_BASE_REF"] = old


if __name__ == "__main__":
    unittest.main()
