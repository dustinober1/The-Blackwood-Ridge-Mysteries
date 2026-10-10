# Book 1 — Audiobook Narration Manuscript

Production copies of *The Annotated Murder* for narrator Annette Callaghan,
who records from PDF and re-records only changed passages.

## Contents

- `narrator-notes.typ` — title page + narrator notes (pronunciations, Latin
  guide, performance guidance) plus the boxed revision note listing what
  changed and which paragraphs are highlighted.
- `build-manuscript.py` — builds the PDF: reads the canonical chapters in
  `../manuscript/`, wraps every paragraph listed in `HIGHLIGHTS` in a yellow
  band, appends front matter, renders via typst.
- `The-Annotated-Murder-Audiobook-Narration-Manuscript-2026-10.pdf` — the
  October 2026 revision copy (round 2). Highlighted paragraphs are the only
  text that differs from the July 2026 copy.
- `manuscript.typ` — generated intermediate (gitignored).

## Rebuilding

```bash
python3 build-manuscript.py
```

Requires `typst` (0.13+) on PATH. The script fails loudly if any `HIGHLIGHTS`
prefix no longer matches a paragraph, so stale entries can't silently drop.

## Round history

- **July 2026 (round 1)** — narrator-flagged continuity fixes in ch-01, ch-05,
  ch-06, ch-07 (commits `a2b7efd`, `07f68b0`, `0d2cca4`, `884319c`). July PDF
  was exported by hand from iA Writer; no build source existed in the repo,
  which is why this folder and build script were added.
- **October 2026 (round 2)** — four fixes from Annette's second pass:
  1. ch-02: drive home → walk home (Callie has no car).
  2. ch-02: "She sold nothing" → "She sold almost nothing".
  3. ch-02: "certain threads" exchange resequenced so the hands-still beat
     lands on the word *threads*.
  4. ch-07: Callie puts on her coat before answering Mae's knock.

## Round 3 (when more narrator notes arrive)

1. Fix the prose in `../manuscript/ch-*.md` (that is the canonical source).
2. Add each changed paragraph's exact opening text to `HIGHLIGHTS` in
   `build-manuscript.py`.
3. Update the revision box in `narrator-notes.typ` (and the title-page date if
   issuing a fresh production copy).
4. Rename `OUTPUT_PDF` to the new date and rerun the script.
