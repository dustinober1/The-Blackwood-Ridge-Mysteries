#!/usr/bin/env python3
"""Run the Book 4 release pipeline with the PDF extractor guard corrected.

A prior tool-generated edit reduced the intended Unicode replacement-character
literal to an empty string, which makes every rendered DOCX page fail. This
wrapper applies the one-line correction in the disposable build worktree before
running the release gate. Chapter sources are never touched.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FINALIZER = HERE / "finalize-package.py"
RELEASE = HERE / "release-package.py"
BROKEN = 'replacement_pages = [index + 1 for index, text in enumerate(page_texts) if "" in text]'
FIXED = 'replacement_pages = [index + 1 for index, text in enumerate(page_texts) if "\\uFFFD" in text]'


def main() -> None:
    text = FINALIZER.read_text(encoding="utf-8")
    if BROKEN in text:
        FINALIZER.write_text(text.replace(BROKEN, FIXED, 1), encoding="utf-8")
    elif FIXED not in text:
        raise RuntimeError("Could not locate the DOCX replacement-character validation line")
    subprocess.run([sys.executable, str(RELEASE)], check=True)


if __name__ == "__main__":
    main()
