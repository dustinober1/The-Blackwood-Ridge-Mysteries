#!/usr/bin/env python3
"""Build the Book 1 audiobook narration manuscript PDF.

Reads the canonical chapters in ../manuscript/, highlights every paragraph
listed in HIGHLIGHTS with a yellow band, appends the front matter from
narrator-notes.typ, and renders with typst.

Round-3 workflow: fix the prose in ../manuscript/, add the new paragraphs'
opening text to HIGHLIGHTS, update the revision box in narrator-notes.typ,
bump the OUTPUT name/date, then rerun this script.
"""

import re
import subprocess
import sys

from pathlib import Path

HERE = Path(__file__).resolve().parent
MANUSCRIPT_DIR = HERE.parent / "manuscript"
CHAPTERS = [MANUSCRIPT_DIR / f"ch-{i:02d}.md" for i in range(1, 9)]
NOTES_TYP = HERE / "narrator-notes.typ"
INTERMEDIATE_TYP = HERE / "manuscript.typ"
OUTPUT_PDF = HERE / "The-Annotated-Murder-Audiobook-Narration-Manuscript-2026-10.pdf"

NUM_WORD = {1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT"}

# Paragraphs to highlight: exact opening text of the paragraph as it appears
# in the chapter file. Each prefix must match exactly one paragraph.
HIGHLIGHTS = [
    ("ch-02", "The shop opened at ten,"),
    ("ch-02", "She sold almost nothing."),
    ("ch-02", '"No." Mae smiled,'),
    ("ch-02", "On the word *threads*,"),
    ("ch-02", '"His notes, though.'),
    ("ch-07", "Not the bell. The knock."),
]

BODY_PREAMBLE = """\
// Body pages: running header + centered page number, continuing the
// front-matter page counter (story starts on page 3, as in the July copy).
#set page(paper: "us-letter",
  margin: (x: 1.05in, top: 1.1in, bottom: 0.95in),
  numbering: "1",
  number-align: center,
  header: align(center, text(size: 8.5pt, style: "italic", tracking: 0.09em)[THE ANNOTATED MURDER | VESPER BLYTHE]))
#set text(font: ("Georgia", "Libertinus Serif"), size: 11pt, lang: "en", hyphenate: true)
#set par(leading: 0.62em, spacing: 1.0em, justify: true)
#set block(above: 1.0em, below: 1.0em)

#let hl(body) = block(width: 100%, fill: rgb("#fff3a0"), inset: (x: 9pt, y: 7pt), radius: 3pt, breakable: true, body)
"""

ESCAPE_CHARS = set("\\#$*_[]@~`")


def escape_typst(text: str) -> str:
    out = []
    for ch in text:
        if ch in ESCAPE_CHARS:
            out.append("\\" + ch)
        else:
            out.append(ch)
    return "".join(out)


def paragraph_to_typst(raw: str) -> str:
    # The manuscript uses *...* for emphasis only; typst uses _..._.
    # Escape typst markup specials in every segment.
    if raw.count("*") % 2:
        raise ValueError(f"unbalanced * emphasis markers in paragraph: {raw[:60]!r}")
    segments = raw.split("*")
    parts = []
    for i, segment in enumerate(segments):
        piece = escape_typst(segment)
        parts.append(f"_{piece}_" if i % 2 else piece)
    return "".join(parts)


def strip_front_matter(text: str) -> tuple[dict, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    meta: dict[str, str] = {}
    if match:
        for line in match.group(1).splitlines():
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip().strip('"')
        text = text[match.end():]
    return meta, text


def split_paragraphs(body: str) -> list[str]:
    paragraphs: list[str] = []
    buffer: list[str] = []
    for line in body.splitlines():
        if line.strip():
            buffer.append(line.strip())
        elif buffer:
            paragraphs.append(" ".join(buffer))
            buffer = []
    if buffer:
        paragraphs.append(" ".join(buffer))
    return paragraphs


def build_body() -> str:
    highlight_keys = set(HIGHLIGHTS)
    seen: set[tuple[str, str]] = set()
    parts = [BODY_PREAMBLE]

    for n, path in enumerate(CHAPTERS, start=1):
        meta, body = strip_front_matter(path.read_text())
        title = meta.get("title", "").upper()
        heading = f"CHAPTER {NUM_WORD[n]}: {title}"
        parts.append("#pagebreak()\n")
        parts.append(
            f'#align(center, text(size: 16.5pt, weight: "bold", tracking: 0.02em)[{escape_typst(heading)}])\n'
        )
        parts.append("#v(1.1em)\n\n")

        for paragraph in split_paragraphs(body):
            prefix_key = next(
                (h for h in HIGHLIGHTS if h[0] == path.stem and paragraph.startswith(h[1])),
                None,
            )
            typst_paragraph = paragraph_to_typst(paragraph)
            if prefix_key:
                seen.add(prefix_key)
                parts.append(f"#hl[{typst_paragraph}]\n\n")
            else:
                parts.append(f"{typst_paragraph}\n\n")

        parts.append("\n")

    missing = [h for h in HIGHLIGHTS if h not in seen]
    if missing:
        raise SystemExit(f"ERROR: highlight prefixes matched no paragraph: {missing}")

    parts.append("#v(2.2em)\n")
    parts.append('#align(center, text(weight: "bold")[END OF MANUSCRIPT])\n')
    return "".join(parts)


def main() -> None:
    typst_source = NOTES_TYP.read_text() + "\n" + build_body()
    INTERMEDIATE_TYP.write_text(typst_source)

    result = subprocess.run(
        [
            "typst", "compile",
            "--font-path", "/System/Library/Fonts",
            "--font-path", "/System/Library/Fonts/Supplemental",
            str(INTERMEDIATE_TYP), str(OUTPUT_PDF),
        ],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        raise SystemExit("ERROR: typst compile failed")

    print(f"highlighted paragraphs: {len(HIGHLIGHTS)} (all matched)")
    print(f"wrote {OUTPUT_PDF}")


if __name__ == "__main__":
    main()
