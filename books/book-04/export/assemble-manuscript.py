#!/usr/bin/env python3
"""Assemble the reader-facing Book 4 Markdown manuscript without changing prose."""
from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOOK_DIR = HERE.parent
CHAPTERS = [
    (1, 'Smoke Under Town Hall', 'ch-01.md'),
    (2, 'The Salvage Table', 'ch-02.md'),
    (3, 'A Shelf That Lied Twice', 'ch-03.md'),
    (4, 'The Predecessor’s Hand', 'ch-04.md'),
    (5, 'Water Lines', 'ch-05.md'),
    (6, 'Bad Procedure', 'ch-06.md'),
    (7, 'The Ash Index', 'ch-07.md'),
    (8, 'The Box Asked For', 'ch-08.md'),
]
FRONT = ['title-page.md', 'copyright.md', 'contents.md']
BACK = ['author-note.md', 'series.md', 'about-the-author.md']


def normalize_apostrophes(value: str) -> str:
    return value.replace("’", "'").replace("‘", "'")


def chapter_body(path: Path, number: int, expected_title: str) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML front matter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{path}: unterminated YAML front matter")
    remainder = text[end + 5:].lstrip("\n")
    lines = remainder.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError(f"{path}: missing source heading")
    actual = lines[0][2:].strip()
    if normalize_apostrophes(actual) != normalize_apostrophes(expected_title):
        raise ValueError(f"{path}: title mismatch {actual!r}")
    body = "\n".join(lines[1:]).strip()
    if not body:
        raise ValueError(f"{path}: empty body")
    return body


def main() -> None:
    parts = []
    for name in FRONT:
        parts.append((BOOK_DIR / "front-matter" / name).read_text(encoding="utf-8").strip())
    for number, title, filename in CHAPTERS:
        body = chapter_body(BOOK_DIR / "manuscript" / filename, number, title)
        parts.append(f"# Chapter {number} — {title}\n\n{body}")
    for name in BACK:
        parts.append((BOOK_DIR / "back-matter" / name).read_text(encoding="utf-8").strip())
    output = HERE / "manuscript-combined.md"
    output.write_text("\n\n---\n\n".join(parts).rstrip() + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
