#!/usr/bin/env python3
"""Assemble Book 3's retail manuscript without modifying story prose."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

TITLE = "The Challenger"
AUTHOR = "Vesper Blythe"
SERIES_LINE = "The Blackwood Ridge Mysteries, Book 3"
EDITION_OLD = "First edition: June 2026"
EDITION_NEW = "First edition: July 2026"
STORY_END = "She did not need the bell to ring before she began."
CHAPTERS = [
    "The Visitor Who Came Looking",
    "After the Lecture",
    "The Door Opens",
    "The Second Hand",
    "The Gap",
    "The Keeper",
    "Still Hands",
    "The Man Who Buried It",
]


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def main() -> None:
    here = Path(__file__).resolve().parent
    book = here.parent
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=here / "manuscript-combined.md")
    parser.add_argument("--output", type=Path, default=here / "dist" / "manuscript-retail.md")
    args = parser.parse_args()

    source = args.source.read_text(encoding="utf-8")
    if source.count(EDITION_OLD) != 1:
        fail(f"expected exactly one legacy edition line {EDITION_OLD!r}")
    if TITLE not in source or AUTHOR not in source or SERIES_LINE not in source:
        fail("title-page metadata is incomplete")
    if not source.rstrip().endswith(STORY_END):
        fail("authoritative manuscript does not end at the locked story ending")

    expected = [f"# Chapter {n} — {title}" for n, title in enumerate(CHAPTERS, 1)]
    positions = [source.find(value) for value in expected]
    if any(position < 0 for position in positions) or positions != sorted(positions):
        fail("chapter headings are missing or out of order")

    # Preserve the source story byte-for-byte except for the stale edition month and
    # export-only page-break markup. The story's final sentence is checked above.
    retail = source.replace(EDITION_OLD, EDITION_NEW, 1)
    retail = re.sub(r"(?m)^\\newpage\s*$", '<div class="pagebreak"></div>', retail)

    back_matter_paths = [
        book / "back-matter" / "review-request.md",
        book / "back-matter" / "series.md",
        book / "back-matter" / "about-author.md",
    ]
    parts = [retail.rstrip()]
    for path in back_matter_paths:
        if not path.is_file():
            fail(f"missing back matter: {path}")
        text = path.read_text(encoding="utf-8").strip()
        text = re.sub(r"(?m)^\\newpage\s*$", '<div class="pagebreak"></div>', text)
        parts.append(text)

    assembled = "\n\n".join(parts).rstrip() + "\n"
    for heading in ("# Thank You for Reading", "# The Blackwood Ridge Mysteries", "# About the Author"):
        if assembled.count(heading) != 1:
            fail(f"retail back matter heading invalid: {heading}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(assembled, encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
