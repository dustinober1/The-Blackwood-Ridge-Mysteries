# Book 4 Export Readiness — The Archive Fire

2026-07-03 export artifact generation blocker pass

Starting HEAD verified: `c12536358fc187b208080c67e7fa94d0a2ed2ce3`

Commit message verified at start: `Prepare Book 4 export package`

Initial comparison result: `main` was identical to the provided starting HEAD before this pass.

Scope confirmed: `dustinober1/The-Blackwood-Ridge-Mysteries`, default branch `main`, with write permission visible.

## Status

Export remains **in progress**, not complete.

The combined reader-facing manuscript artifact is still expected at:

- `books/book-04/export/manuscript-combined.md`

The artifact was **not** committed in this pass because it could not be generated safely through the available connector path.

Package remains pending. Publish remains pending.

No EPUB, retail package, upload package, cover asset, or publication event was created in this pass.

## Files read

Book 4 source/status files:

- `books/book-04/progress.yaml`
- `books/book-04/export/assemble-manuscript.py`
- `books/book-04/export/build.sh`
- `books/book-04/export/export-readiness.md`
- `books/book-04/package/package-readiness.md`
- `books/book-04/outline.md`

Book 4 manuscript files:

- `books/book-04/manuscript/ch-01.md`
- `books/book-04/manuscript/ch-02.md`
- `books/book-04/manuscript/ch-03.md`
- `books/book-04/manuscript/ch-04.md`
- `books/book-04/manuscript/ch-05.md`
- `books/book-04/manuscript/ch-06.md`
- `books/book-04/manuscript/ch-07.md`
- `books/book-04/manuscript/ch-08.md`

Book 3 convention references inspected:

- `books/book-03/export/manuscript-combined.md`
- `books/book-03/export/build.sh`
- `books/book-03/export/export-readiness.md`
- `books/book-03/progress.yaml`

## Files changed

- `books/book-04/export/export-readiness.md` — updated with this blocker report.

No manuscript chapter source file was edited.

No Book 1, Book 2, or Book 3 file was edited.

## Blocker

`books/book-04/export/assemble-manuscript.py` exists and contains the correct exact-source assembly logic for creating:

- `books/book-04/export/manuscript-combined.md`

However, the available GitHub connector in this pass can read and write repository blobs but cannot execute repository scripts. It also does not provide a safe direct resource-to-blob transform that would pipe the fetched chapter sources through the committed assembler logic and commit the generated artifact without manually reconstructing the full 36,026-word manuscript inside a connector write call.

Because the export artifact must preserve source chapter prose exactly after stripping YAML front matter and source headings, manually reconstructing the entire reader-facing manuscript in a write payload was judged unsafe. A partial or manually drifted artifact would be worse than leaving the export accurately marked in progress.

## Current expected safe generation command

From a normal repository checkout, run either:

```bash
python3 books/book-04/export/assemble-manuscript.py
```

or:

```bash
cd books/book-04/export
./build.sh
```

The first command should generate only the combined Markdown manuscript. The second command should generate the combined Markdown manuscript and then attempt EPUB generation through pandoc if pandoc is installed.

## Expected generated artifact requirements

The generated `books/book-04/export/manuscript-combined.md` should include:

- title page;
- author line;
- series line;
- copyright / fiction disclaimer page;
- contents page;
- export-safe `\newpage` page breaks;
- chapters assembled from the eight Book 4 source chapter files in order;
- per-chapter YAML front matter stripped;
- source chapter headings stripped;
- normalized reader-facing chapter headings added as `# Chapter N — Title`;
- no reader-facing upload, package, or publication instructions embedded in the manuscript.

## Chapter order validated for future generation

1. Chapter 1 — Smoke Under Town Hall
2. Chapter 2 — The Salvage Table
3. Chapter 3 — A Shelf That Lied Twice
4. Chapter 4 — The Predecessor's Hand
5. Chapter 5 — Water Lines
6. Chapter 6 — Bad Procedure
7. Chapter 7 — The Ash Index
8. Chapter 8 — The Box Asked For

## Word count

Current source chapter metadata total: **36,026 words**.

Breakdown:

- Chapter 1: 4,341
- Chapter 2: 4,715
- Chapter 3: 4,890
- Chapter 4: 4,596
- Chapter 5: 3,965
- Chapter 6: 4,539
- Chapter 7: 4,392
- Chapter 8: 4,588

## Validation completed before stopping

- Confirmed `main` matched starting HEAD `c12536358fc187b208080c67e7fa94d0a2ed2ce3` before editing.
- Confirmed `books/book-04/export/manuscript-combined.md` was absent before this pass.
- Read all eight manuscript source files.
- Confirmed chapter order and titles against the Book 4 outline and assembler.
- Confirmed the committed assembler is the correct source of truth for safe exact-source generation.
- Confirmed no manuscript source files were edited.
- Confirmed no Book 1, Book 2, or Book 3 files were edited.
- Confirmed no EPUB was created.
- Confirmed no final retail package was created.
- Confirmed no cover asset was generated.
- Confirmed no publication or upload action was performed.
- Confirmed package remains pending.
- Confirmed publish remains pending.

## Story and continuity preservation

No story/prose revision was performed in this pass. The source manuscript files were not edited.

The following locked story elements remain preserved in the source manuscript files:

- Ruth's call sets up the shelf that lied twice.
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
- Floorboard ending remains intact in meaning.
- Eleanor's brass magnifying glass remains beside damaged paper as a tool, not a relic.
- Callie does not read alone.

## Not completed in this pass

- `books/book-04/export/manuscript-combined.md` was not generated or committed.
- Export was not marked complete.
- `books/book-04/progress.yaml` was not advanced.
- `books/book-04/package/package-readiness.md` was not advanced.
- No EPUB was generated.
- No final retail package was created.
- No cover asset was generated.
- No publication or upload action was performed.
- Package finalization was not performed.

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

Book 4 still needs the combined manuscript artifact generated from a real repository checkout before export can safely be marked complete.
