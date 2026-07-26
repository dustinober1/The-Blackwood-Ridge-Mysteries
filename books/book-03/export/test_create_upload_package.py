#!/usr/bin/env python3
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parent))

from create_upload_package import PACKAGE_FILES, create_upload_package


class CreateUploadPackageTests(unittest.TestCase):
    def test_archive_contains_exact_release_inventory_in_order(self) -> None:
        with TemporaryDirectory() as directory:
            dist = Path(directory)
            for name in PACKAGE_FILES:
                (dist / name).write_bytes(name.encode("utf-8"))

            output = create_upload_package(dist)

            with zipfile.ZipFile(output) as archive:
                self.assertEqual(archive.namelist(), PACKAGE_FILES)

    def test_nested_upload_cover_is_byte_identical_to_standalone_cover(self) -> None:
        with TemporaryDirectory() as directory:
            dist = Path(directory)
            approved_cover_bytes = b"approved-cover-bytes"
            for name in PACKAGE_FILES:
                data = approved_cover_bytes if name == "The-Challenger-cover.jpg" else name.encode("utf-8")
                (dist / name).write_bytes(data)

            output = create_upload_package(dist)

            with zipfile.ZipFile(output) as archive:
                self.assertEqual(
                    archive.read("The-Challenger-cover.jpg"),
                    (dist / "The-Challenger-cover.jpg").read_bytes(),
                )

    def test_missing_cover_fails_package_creation(self) -> None:
        with TemporaryDirectory() as directory:
            dist = Path(directory)
            for name in PACKAGE_FILES:
                if name != "The-Challenger-cover.jpg":
                    (dist / name).write_bytes(name.encode("utf-8"))

            with self.assertRaisesRegex(FileNotFoundError, "The-Challenger-cover.jpg"):
                create_upload_package(dist)


if __name__ == "__main__":
    unittest.main(verbosity=2)
