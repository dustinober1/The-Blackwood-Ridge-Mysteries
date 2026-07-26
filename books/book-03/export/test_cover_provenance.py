#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import unittest

from PIL import Image


EXPORT_DIR = Path(__file__).resolve().parent
BOOK_DIR = EXPORT_DIR.parent
APPROVED_COVER = BOOK_DIR / "package" / "approved" / "The-Challenger-cover.jpg"
AUTHORITY = BOOK_DIR / "package" / "approved" / "approved-cover.json"
BUILD_SCRIPT = EXPORT_DIR / "build.sh"


class CoverProvenanceRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with Image.open(APPROVED_COVER) as image:
            diagnostics = {
                "sha256": hashlib.sha256(APPROVED_COVER.read_bytes()).hexdigest(),
                "size_bytes": APPROVED_COVER.stat().st_size,
                "format": image.format,
                "mode": image.mode,
                "width": image.width,
                "height": image.height,
                "dpi": list(image.info.get("dpi", (0, 0))),
            }
        print("APPROVED_COVER_DIAGNOSTICS=" + json.dumps(diagnostics, sort_keys=True))

    def test_authority_record_exists(self) -> None:
        self.assertTrue(AUTHORITY.is_file(), "approved-cover.json must lock the author-approved JPEG")

    def test_build_uses_approved_cover_and_never_invokes_generator(self) -> None:
        build = BUILD_SCRIPT.read_text(encoding="utf-8")
        self.assertIn("package/approved/The-Challenger-cover.jpg", build)
        self.assertNotIn("generate-cover.py", build)


if __name__ == "__main__":
    unittest.main(verbosity=2)
