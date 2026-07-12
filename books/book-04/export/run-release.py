#!/usr/bin/env python3
"""Run the Book 4 release pipeline with two narrow validator corrections.

The established technical finalizer contains a Unicode replacement-character
literal that was reduced to an empty string, causing every rendered DOCX page
to fail. The release validator must also exclude the EPUB navigation document
when counting visual title pages; Pandoc legitimately repeats the title there.

This wrapper patches only those validators in the disposable CI/local build
worktree, then runs the release gate. Chapter sources are never touched.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FINALIZER = HERE / "finalize-package.py"
RELEASE = HERE / "release-package.py"

DOCX_BROKEN = 'replacement_pages = [index + 1 for index, text in enumerate(page_texts) if "" in text]'
DOCX_FIXED = 'replacement_pages = [index + 1 for index, text in enumerate(page_texts) if "\\uFFFD" in text]'

EPUB_OLD = '''        all_h1: list[str] = []
        extracted_parts: list[str] = []
        for path in spine_paths:
            soup = BeautifulSoup(archive.read(path), "html.parser")
            all_h1.extend(normalize(node.get_text(" ", strip=True)) for node in soup.find_all("h1"))
            extracted_parts.append(soup.get_text(" ", strip=True))
        chapter_h1 = [value for value in all_h1 if value.startswith("Chapter ")]
        if chapter_h1 != EXPECTED_CHAPTERS:
            raise RuntimeError(f"EPUB chapter sequence mismatch: {chapter_h1!r}")
        if all_h1.count(TITLE) != 1:
            raise RuntimeError(f"EPUB title heading count is {all_h1.count(TITLE)}, expected 1")
'''

EPUB_NEW = '''        all_h1: list[str] = []
        reader_title_locations: list[tuple[int, str]] = []
        extracted_parts: list[str] = []
        for spine_index, path in enumerate(spine_paths):
            soup = BeautifulSoup(archive.read(path), "html.parser")
            headings = [normalize(node.get_text(" ", strip=True)) for node in soup.find_all("h1")]
            all_h1.extend(headings)
            # The nav document repeats the bibliographic title by design; it is
            # not a rendered reader title page and must not be counted as one.
            if TITLE in headings and path != nav_href:
                reader_title_locations.append((spine_index, path))
            extracted_parts.append(soup.get_text(" ", strip=True))
        chapter_h1 = [value for value in all_h1 if value.startswith("Chapter ")]
        if chapter_h1 != EXPECTED_CHAPTERS:
            raise RuntimeError(f"EPUB chapter sequence mismatch: {chapter_h1!r}")
        if len(reader_title_locations) != 1:
            raise RuntimeError(
                f"EPUB reader title-page mismatch: {reader_title_locations!r}; expected exactly one non-navigation title page"
            )
'''

FIELD_OLD = '"title_heading_count": all_h1.count(TITLE),'
FIELD_NEW = '"reader_title_documents": [{"spine_index": index, "path": path} for index, path in reader_title_locations],'

REPORT_OLD = '- Title pages: exactly one'
REPORT_NEW = '- Reader title page: exactly one; navigation title excluded'


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old in text:
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
    elif new not in text:
        raise RuntimeError(f"Could not locate {label} correction in {path}")


def main() -> None:
    replace_once(FINALIZER, DOCX_BROKEN, DOCX_FIXED, "DOCX replacement-character")
    replace_once(RELEASE, EPUB_OLD, EPUB_NEW, "EPUB reader title-page structure")
    replace_once(RELEASE, FIELD_OLD, FIELD_NEW, "EPUB title manifest field")
    replace_once(RELEASE, REPORT_OLD, REPORT_NEW, "release report title wording")
    subprocess.run([sys.executable, str(RELEASE)], check=True)


if __name__ == "__main__":
    main()
