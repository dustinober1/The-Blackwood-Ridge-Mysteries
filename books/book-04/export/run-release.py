#!/usr/bin/env python3
"""Run the Book 4 release pipeline with two narrow validator corrections.

The established technical finalizer contains a Unicode replacement-character
literal that was reduced to an empty string, causing every rendered DOCX page
to fail. The release validator also needs to distinguish Pandoc's visual cover
XHTML from its reader title page: both legitimately carry the book title.

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
        title_locations: list[tuple[int, str]] = []
        extracted_parts: list[str] = []
        for spine_index, path in enumerate(spine_paths):
            soup = BeautifulSoup(archive.read(path), "html.parser")
            headings = [normalize(node.get_text(" ", strip=True)) for node in soup.find_all("h1")]
            all_h1.extend(headings)
            if TITLE in headings:
                title_locations.append((spine_index, path))
            extracted_parts.append(soup.get_text(" ", strip=True))
        chapter_h1 = [value for value in all_h1 if value.startswith("Chapter ")]
        if chapter_h1 != EXPECTED_CHAPTERS:
            raise RuntimeError(f"EPUB chapter sequence mismatch: {chapter_h1!r}")
        # Pandoc's cover XHTML and its reader title page both carry the title.
        # Require exactly that structure: the cover first, followed by one title page.
        if len(title_locations) != 2 or title_locations[0][0] != 0 or title_locations[1][0] <= 0:
            raise RuntimeError(
                f"EPUB title structure mismatch: {title_locations!r}; expected cover first plus one reader title page"
            )
'''

FIELD_OLD = '"title_heading_count": all_h1.count(TITLE),'
FIELD_NEW = '"title_documents": [{"spine_index": index, "path": path} for index, path in title_locations],'

REPORT_OLD = '- Title pages: exactly one'
REPORT_NEW = '- Title structure: one visual cover plus one reader title page'


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old in text:
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
    elif new not in text:
        raise RuntimeError(f"Could not locate {label} correction in {path}")


def main() -> None:
    replace_once(FINALIZER, DOCX_BROKEN, DOCX_FIXED, "DOCX replacement-character")
    replace_once(RELEASE, EPUB_OLD, EPUB_NEW, "EPUB cover/title structure")
    replace_once(RELEASE, FIELD_OLD, FIELD_NEW, "EPUB title manifest field")
    replace_once(RELEASE, REPORT_OLD, REPORT_NEW, "release report title wording")
    subprocess.run([sys.executable, str(RELEASE)], check=True)


if __name__ == "__main__":
    main()
