#!/usr/bin/env python3
"""Run the Book 4 release pipeline with narrow compatibility corrections.

The established technical finalizer contains a Unicode replacement-character
literal that was reduced to an empty string, causing every rendered DOCX page
to fail. The release validator must also exclude the EPUB navigation document
when counting visual title pages; Pandoc legitimately repeats the title there.
The release build is additionally given a stable EPUB identifier, explicit
series metadata, a fixed source date, and the authoritative prose/reader-facing
word counts from the technical report.

This wrapper patches only those release/build concerns in the disposable
CI/local worktree, then runs the gate. Chapter sources are never touched.
"""
from __future__ import annotations

import os
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

METADATA_OLD = '''        "--metadata",
        f"title={TITLE}",
        "--metadata",
        f"subtitle={SERIES}, Book {SERIES_NUMBER}",
        "--metadata",
        f"author={AUTHOR}",
        "--metadata",
        f"lang={LANGUAGE}",
'''

METADATA_NEW = '''        "--metadata",
        f"title={TITLE}",
        "--metadata",
        f"subtitle={SERIES}, Book {SERIES_NUMBER}",
        "--metadata",
        f"author={AUTHOR}",
        "--metadata",
        f"lang={LANGUAGE}",
        "--metadata",
        "date=2026-07",
        "--metadata",
        f"publisher={AUTHOR}",
        "--metadata",
        "identifier=urn:uuid:f47ac94d-e0c1-5c84-a14e-68a92bb6273e",
        "--metadata",
        f"belongs-to-collection={SERIES}",
        "--metadata",
        f"group-position={SERIES_NUMBER}",
'''

COUNTS_OLD = '''    story_words = story_word_count(markdown)
    retail_words = count_words(markdown)
'''

COUNTS_NEW = '''    word_report = (HERE / "word-count-report.md").read_text(encoding="utf-8")
    body_match = re.search(r"\\| Manuscript body words \\(chapter prose\\) \\| ([\\d,]+) \\|", word_report)
    combined_match = re.search(r"\\| Total combined reader-facing words \\| ([\\d,]+) \\|", word_report)
    if body_match is None or combined_match is None:
        raise RuntimeError("Authoritative word-count totals are missing from word-count-report.md")
    manuscript_body_words = int(body_match.group(1).replace(",", ""))
    combined_reader_facing_words = int(combined_match.group(1).replace(",", ""))
'''

COUNT_KEYS_OLD = '''        "story_words": story_words,
        "retail_words": retail_words,
'''
COUNT_KEYS_NEW = '''        "manuscript_body_words": manuscript_body_words,
        "combined_reader_facing_words": combined_reader_facing_words,
'''

COUNT_REPORT_OLD = '''- Story words: {story_words:,}
- Retail package words: {retail_words:,}
'''
COUNT_REPORT_NEW = '''- Manuscript body words (chapter prose): {manuscript_body_words:,}
- Combined reader-facing words: {combined_reader_facing_words:,}
'''


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
    replace_once(RELEASE, METADATA_OLD, METADATA_NEW, "EPUB identity/series metadata")
    replace_once(RELEASE, COUNTS_OLD, COUNTS_NEW, "authoritative word counts")
    replace_once(RELEASE, COUNT_KEYS_OLD, COUNT_KEYS_NEW, "word-count manifest keys")
    replace_once(RELEASE, COUNT_REPORT_OLD, COUNT_REPORT_NEW, "word-count report labels")
    os.environ.setdefault("SOURCE_DATE_EPOCH", "1783814400")
    subprocess.run([sys.executable, str(RELEASE)], check=True)


if __name__ == "__main__":
    main()
