#!/usr/bin/env python3
"""Assemble the reader-facing Book 6 Markdown manuscript without changing prose."""
from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
BOOK_DIR = HERE.parent
CHAPTERS = [
    (1, "The Box at Closing", "ch-01.md"),
    (2, "A Fall That Did Not Fit", "ch-02.md"),
    (3, "The Surveyor’s Missing Line", "ch-03.md"),
    (4, "Marks Made Later", "ch-04.md"),
    (5, "The Road Through Bellweather", "ch-05.md"),
    (6, "What the Ledger Withheld", "ch-06.md"),
    (7, "The Weight of the Map", "ch-07.md"),
    (8, "The Pattern", "ch-08.md"),
]
FRONT = ["title-page.md", "copyright.md", "contents.md"]
BACK = ["author-note.md", "series.md", "about-the-author.md"]


def normalize_apostrophes(value: str) -> str:
    return value.replace("’", "'").replace("‘", "'")


def chapter_body(path: Path, number: int, expected_title: str) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML front matter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{path}: unterminated YAML front matter")
    lines = text[end + 5:].lstrip("\n").splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError(f"{path}: missing source heading")
    actual_title = lines[0][2:].strip()
    if normalize_apostrophes(actual_title) != normalize_apostrophes(f"Chapter {number} — {expected_title}"):
        raise ValueError(f"{path}: title mismatch {actual_title!r}")
    body = "\n".join(lines[1:]).strip()
    if not body:
        raise ValueError(f"{path}: empty body")
    return body


def main() -> None:
    parts = [(BOOK_DIR / "front-matter" / name).read_text(encoding="utf-8").strip() for name in FRONT]
    for number, title, filename in CHAPTERS:
        body = chapter_body(BOOK_DIR / "manuscript" / filename, number, title)
        parts.append(f"# Chapter {number} — {title}\n\n{body}")
    parts.extend((BOOK_DIR / "back-matter" / name).read_text(encoding="utf-8").strip() for name in BACK)
    output = HERE / "manuscript-combined.md"
    output.write_text("\n\n---\n\n".join(parts).rstrip() + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
