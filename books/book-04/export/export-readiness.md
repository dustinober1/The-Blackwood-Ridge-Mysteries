# Book 4 Export Readiness — The Archive Fire

2026-07-04 export-prep validation pass

Base head checked: `ec8a778ad5527c558b1eb3a403a4da0946b8cb91`

Initial comparison result: `main` was identical to the provided base head before export-prep changes.

Scope confirmed: `dustinober1/The-Blackwood-Ridge-Mysteries`, default branch `main`, with write permission visible.

## Status

Export is **in progress**, not complete.

This pass prepared exact-source assembly tooling and completed manuscript/package-readiness validation, but did not mark export complete because the combined manuscript file was not safely committed as a generated artifact in this connector pass. The export stage should be marked complete only after `books/book-04/export/assemble-manuscript.py` is run and `books/book-04/export/manuscript-combined.md` is committed or otherwise verified from the generated output.

Package remains pending. Publish remains pending.

## Files read

Book 4 source/status files:

- `books/book-04/progress.yaml`
- `books/book-04/outline.md`
- `books/book-04/revision-plan.md`
- `books/book-04/bible/story-memory.md`
- `books/book-04/bible/carry-forward.md`

Book 4 manuscript files:

- `books/book-04/manuscript/ch-01.md`
- `books/book-04/manuscript/ch-02.md`
- `books/book-04/manuscript/ch-03.md`
- `books/book-04/manuscript/ch-04.md`
- `books/book-04/manuscript/ch-05.md`
- `books/book-04/manuscript/ch-06.md`
- `books/book-04/manuscript/ch-07.md`
- `books/book-04/manuscript/ch-08.md`

Existing Book 4 production files inspected:

- `books/book-04/export/export-readiness.md`
- `books/book-04/package/packaging.md`
- `books/book-04/publish/listing.md`

Book 1-3 convention references inspected:

- `books/book-03/export/manuscript-combined.md`
- `books/book-03/export/build.sh`
- `books/book-03/export/export-readiness.md`
- `books/book-03/package/package-readiness.md`
- `books/book-03/progress.yaml`
- Book 1 and Book 2 package/listing/export references as needed through repo search.

## Files changed

- `books/book-04/progress.yaml` — revised and polish marked complete; export marked `in_progress`; package and publish left pending.
- `books/book-04/export/assemble-manuscript.py` — created exact-source Markdown assembly script.
- `books/book-04/export/build.sh` — created Book 4 EPUB build script that first assembles the combined manuscript.
- `books/book-04/export/export-readiness.md` — replaced placeholder status with this validation report.
- `books/book-04/package/package-readiness.md` — created package-readiness validation report without marking package complete.

No manuscript chapter file was edited.

No Book 1, Book 2, or Book 3 file was edited.

## Assembly tool behavior

`books/book-04/export/assemble-manuscript.py` is designed to generate:

- `books/book-04/export/manuscript-combined.md`

The generated manuscript should:

- use the Book 3 export convention for title page, author line, series line, copyright/disclaimer page, contents, page breaks, and normalized chapter headings;
- read the eight Book 4 source chapters in order;
- strip each chapter file YAML front matter;
- strip each chapter file source heading;
- add normalized reader-facing headings of the form `# Chapter N — Title`;
- preserve the chapter prose from the manuscript source files exactly after front-matter/heading stripping;
- add no commentary, upload instructions, or package notes to the reader-facing manuscript.

`books/book-04/export/build.sh` runs the assembly script first, then builds `the-archive-fire.epub` with pandoc if pandoc is installed.

## Chapter order validated

1. Chapter 1 — Smoke Under Town Hall
2. Chapter 2 — The Salvage Table
3. Chapter 3 — A Shelf That Lied Twice
4. Chapter 4 — The Predecessor's Hand
5. Chapter 5 — Water Lines
6. Chapter 6 — Bad Procedure
7. Chapter 7 — The Ash Index
8. Chapter 8 — The Box Asked For

## Word count

Current chapter metadata total: **36,026 words**.

Breakdown:

- Chapter 1: 4,341
- Chapter 2: 4,715
- Chapter 3: 4,890
- Chapter 4: 4,596
- Chapter 5: 3,965
- Chapter 6: 4,539
- Chapter 7: 4,392
- Chapter 8: 4,588

## Export validation performed

- All eight chapter source files were read.
- Chapter order and titles were checked against the outline and manuscript files.
- No merge conflict markers were found during manuscript review.
- No unresolved placeholder text was found during manuscript review.
- Individual chapter YAML front matter exists only in source chapters and should be stripped by the assembly tool.
- No manuscript prose was revised in this pass.
- No package/upload/publication file was created that claims live publication.

## Mystery/package-readiness validation

- Ruth's call still sets up the shelf that lied twice.
- The fake Ruth note remains staged and wrong because it lacks Ruth's record system.
- Brass cat charm setup, recovery, and payoff remain intact.
- Clara's K-two lie remains separate from Ruth's key-ring/charm path.
- Simon, Clara, Nell, and Tavis remain false-suspect / record-failure paths.
- Tavis remains morally responsible for the old 1991 failure, not Ruth's murderer.
- Lila Crowe remains a public hit-and-run death with a smoothed record, not a disappearance.
- Ben Calder remains exposed through accumulation, not confession.
- Cross's arrest basis remains accumulated present-day evidence.
- Callie remains a consulting records specialist, not a deputy.
- Eli remains useful but bounded.
- Mae's thaw remains work-based, not apology-based.
- Bell's photographs and Cross's log still make Callie's reading portable.
- Supplemental Crowe record remains restrained.
- Consultant arrangement remains case-by-case and bounded.
- Floorboard ending remains unchanged in meaning.
- Eleanor's brass magnifying glass remains beside damaged paper as a tool, not a relic.

## Not completed in this pass

- `books/book-04/export/manuscript-combined.md` still needs to be generated by running `python3 books/book-04/export/assemble-manuscript.py` from the repository root or `./build.sh` from `books/book-04/export/`.
- No EPUB was generated.
- No final retail package was created.
- No cover asset was generated.
- No publication or upload action was performed.

## Status after this pass

- Concept: complete.
- Bible: complete.
- Outline: complete.
- Draft: complete.
- Revise: complete.
- Polish: complete.
- Export: in progress.
- Package: pending.
- Publish: pending.
