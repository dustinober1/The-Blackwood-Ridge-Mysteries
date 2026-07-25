#!/usr/bin/env python3
"""Create the complete Book 3 upload and verification bundle."""
from __future__ import annotations

from pathlib import Path
import zipfile


PACKAGE_FILES = [
    "The-Challenger.epub",
    "The-Challenger-cover.jpg",
    "manuscript-retail.md",
    "Book-3-listing-copy.md",
    "README-FIRST.md",
    "validation.json",
    "release-validation.md",
]


def create_upload_package(dist: Path) -> Path:
    missing = [name for name in PACKAGE_FILES if not (dist / name).is_file()]
    if missing:
        raise FileNotFoundError(f"missing release files: {', '.join(missing)}")

    output = dist / "The-Challenger-upload-package.zip"
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in PACKAGE_FILES:
            archive.write(dist / name, arcname=name)
    return output


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("dist", type=Path)
    args = parser.parse_args()
    print(create_upload_package(args.dist))
