#!/usr/bin/env python3
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parent))

from create_upload_package import create_upload_package


class CreateUploadPackageTests(unittest.TestCase):
    def test_archive_contains_every_release_verification_input(self) -> None:
        expected = [
            "The-Challenger.epub",
            "The-Challenger-cover.jpg",
            "manuscript-retail.md",
            "Book-3-listing-copy.md",
            "README-FIRST.md",
            "validation.json",
            "release-validation.md",
        ]
        with TemporaryDirectory() as directory:
            dist = Path(directory)
            for name in expected:
                (dist / name).write_text(name, encoding="utf-8")

            output = create_upload_package(dist)

            with zipfile.ZipFile(output) as archive:
                self.assertEqual(archive.namelist(), expected)


if __name__ == "__main__":
    unittest.main()
