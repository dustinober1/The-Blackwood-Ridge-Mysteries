# Book 3 Publish Readiness — The Challenger

2026-06-30 (final publish-readiness / upload-prep verification pass)

Base head checked: `578e361af13d83d6606512f5b4a3014d7a6890af`

Initial comparison result: `main` was identical to the provided base head before this pass.

Scope confirmed: `dustinober1/The-Blackwood-Ridge-Mysteries`, default branch `main`.

No upload, publication, retail submission, or live package generation was performed.

## Files read

Required Book 3 files:

- `books/book-03/progress.yaml`
- `books/book-03/export/manuscript-combined.md`
- `books/book-03/export/build.sh`
- `books/book-03/export/export-readiness.md`
- `books/book-03/package/packaging.md`
- `books/book-03/package/package-readiness.md`
- `books/book-03/publish/listing.md`

Additional Book 3 verification file:

- `books/book-03/content-notes.md`

Book 1 / Book 2 package and publish convention references:

- `books/book-01/package/packaging.md`
- `books/book-01/publish/listing.md`
- `books/book-02/package/packaging.md`
- `books/book-02/publish/listing.md`

Repo convention search performed:

- Searched for standalone manual-upload / KDP-upload checklist patterns. Existing convention keeps upload tasks in `publish/listing.md` launch checklists and readiness reports rather than separate upload-checklist files.

## Files changed

- `books/book-03/publish/publish-readiness.md` — created this final upload-prep verification report.

No manuscript prose, export source, build script, package guidance, listing metadata, cover material, or progress-stage state was changed.

## Publish / upload metadata verified

| Field | Verified value | Source |
|-------|----------------|--------|
| Title | `The Challenger` | Export manuscript, build script, listing |
| Author | `Vesper Blythe` | Export manuscript, build script, listing |
| Series | `The Blackwood Ridge Mysteries` | Export manuscript, listing |
| Series number | `Book 3` | Export manuscript, listing, package guidance |
| Primary lead | `Callie Thorne` | Listing / manuscript alignment |
| Genre | Cozy mystery / amateur sleuth | Listing / package guidance |
| Tone lane | Atmospheric bookish cozy, archival mystery, restrained emotional stakes | Listing / package guidance |
| Publish state | `pending` | `progress.yaml` |

Verified `books/book-03/progress.yaml` still records:

```yaml
  export: complete
  package: complete
  publish: pending
```

The publish stage was not advanced.

## EPUB / build-script readiness

Verified `books/book-03/export/build.sh`:

- runs from the export directory with `cd "$(dirname "$0")"`;
- requires `pandoc` and exits clearly if it is not installed;
- builds from `manuscript-combined.md`;
- uses Markdown input and EPUB3 output;
- includes a table of contents with depth 1;
- sets EPUB metadata title to `The Challenger`;
- sets EPUB metadata author to `Vesper Blythe`;
- sets language metadata to `en`;
- outputs `the-challenger.epub`.

Verified `books/book-03/export/manuscript-combined.md`:

- begins with `# The Challenger`;
- includes `**Vesper Blythe**` on the title page;
- includes `*The Blackwood Ridge Mysteries, Book 3*`;
- includes a copyright / fiction disclaimer page;
- includes a contents page with the expected eight chapters;
- follows the Book 1 / Book 2 combined-manuscript convention described in `export-readiness.md`;
- contains the Book 3 case setup, murder, investigation, confession, and restrained closure needed for a complete standalone novella.

No EPUB was generated in this pass. The expected manual build command remains:

```bash
cd books/book-03/export
./build.sh
```

Expected output after local build:

```text
the-challenger.epub
```

## Cover / package readiness

Verified `books/book-03/package/packaging.md` is consistent with Book 1 and Book 2 package conventions:

- status remains `draft`;
- format is ebook;
- target dimensions are `1600x2560 px (1:1.6)`;
- `series_book: 3` is present;
- package guidance inherits the Book 2 / established series template;
- cover direction is atmospheric archival cozy, not police procedural, thriller, horror, or true crime;
- recommended Concept A, **The Red and Blue Overlay**, matches the manuscript's stylometry / second-hand / archival evidence device;
- the brass magnifying glass is preserved as the series visual anchor;
- color, typography, series-label, author-name, and template instructions preserve continuity with Books 1 and 2;
- notes clearly state that no upload or publication action is performed by the package file.

Remaining cover task is manual: generate/finalize the cover image, add typography outside the image generator, and verify it against the package checklist before KDP upload.

## Listing readiness

Verified `books/book-03/publish/listing.md` against the manuscript, content notes, package guidance, and Books 1 / 2 listing convention.

### Blurb / short blurb

The primary blurb and mobile short variant are consistent with the manuscript and series tone:

- Dr. Vivian Larter arrives with a fair academic challenge to Callie's Wren attribution;
- the Book 3 hook centers on stylometry, the second hand, missing comparative samples, missing folios, the County Historical Society, and the reading-room murder;
- the case is framed as an atmospheric bookish cozy / amateur-sleuth investigation rather than a graphic thriller;
- Cross and Eli are referenced in ways that match their supporting roles without overpromising romance, police-procedural focus, or sidekick antics;
- the series line states that each novella resolves its own case while deepening the series arc.

### Keywords

The seven keyword stubs are consistent with the Book 1 / Book 2 strategy:

1. `cozy mystery bookshop`
2. `small town amateur sleuth mystery`
3. `literary cozy mystery atmospheric`
4. `cozy mystery novella series`
5. `archival mystery missing documents`
6. `handwriting clue mystery`
7. `academic murder mystery amateur sleuth`

The first four preserve series cross-discovery; the final three rotate toward Book 3's archival / handwriting-attribution device.

### Categories

The category guidance is consistent with Books 1 and 2:

1. Mystery, Thriller & Suspense > Cozy
2. Mystery, Thriller & Suspense > Women Sleuths
3. Mystery, Thriller & Suspense > Mystery > Amateur Sleuth

The listing correctly warns that dashboard category paths should be verified manually at upload time because platform category nodes can change.

### Pricing

Pricing guidance recommends `$2.99`, matching Books 1 and 2 and preserving the established novella-series strategy. No price change is recommended during this pass.

### Content warnings

The listing's content warnings are consistent with `books/book-03/content-notes.md`:

- off-page blunt-force murder of Dr. Vivian Larter;
- restrained on-page crime-scene/body aftermath;
- implied blood scent;
- grief, insomnia, professional self-doubt, and moral self-comparison;
- archival tampering, family shame, long-term concealment, and institutional betrayal;
- suspicion and arrest of a trusted institutional figure;
- no sexual content, no profanity, and no graphic violence.

## Issues found / fixed

### Fixed

- Created this final publish-readiness report because `books/book-03/publish/publish-readiness.md` did not exist before this pass.

### No blocking issues found

No blocking mismatch was found in:

- title metadata;
- author metadata;
- series name;
- series number;
- export source path;
- EPUB output filename;
- package guidance;
- draft listing metadata;
- pricing strategy;
- content warnings;
- `progress.yaml` publish state.

### Not changed intentionally

- Did not edit manuscript prose.
- Did not edit `books/book-03/export/manuscript-combined.md`.
- Did not edit `books/book-03/export/build.sh`.
- Did not edit `books/book-03/package/packaging.md`.
- Did not edit `books/book-03/publish/listing.md`.
- Did not create `the-challenger.epub`.
- Did not create a final cover JPEG/TIFF.
- Did not create a live retail package.
- Did not upload or publish anything.
- Did not mark `publish: complete`.

## Manual KDP / upload checklist

Use this checklist only after the author is ready to perform the manual upload outside the repo.

### Pre-upload local QA

- [ ] Generate / finalize the Book 3 cover from `books/book-03/package/packaging.md`, preferably Concept A: The Red and Blue Overlay.
- [ ] Add all cover typography manually using the locked Book 1 / Book 2 series template.
- [ ] Confirm cover text exactly reads:
  - `The Blackwood Ridge Mysteries · Book 3` or the established matching series-label format;
  - `The Challenger`;
  - `Vesper Blythe`.
- [ ] Confirm final cover dimensions and file type match the established ebook-cover guidance.
- [ ] Run `books/book-03/export/build.sh` locally if a fresh EPUB is needed.
- [ ] Open the generated `the-challenger.epub` in an EPUB viewer and spot-check:
  - title page;
  - author line;
  - series line;
  - contents / navigation;
  - chapter breaks;
  - italics;
  - final chapter ending;
  - no accidental YAML/front-matter leakage.

### KDP entry

- [ ] Enter title: `The Challenger`.
- [ ] Enter author: `Vesper Blythe`.
- [ ] Link to series: `The Blackwood Ridge Mysteries`.
- [ ] Set series number: `Book 3`.
- [ ] Upload EPUB: `books/book-03/export/the-challenger.epub`.
- [ ] Upload final cover image.
- [ ] Paste the primary blurb from `books/book-03/publish/listing.md`.
- [ ] Enter the seven keyword stubs from `books/book-03/publish/listing.md`.
- [ ] Select the listed categories or their current dashboard equivalents.
- [ ] Set price to `$2.99` unless a deliberate series-promotion change is made.
- [ ] Enroll in KDP Select / Kindle Unlimited if continuing the Books 1 / 2 strategy.
- [ ] Add optional content-warning note if KDP provides a suitable field.
- [ ] Set publication date.
- [ ] Preview in the KDP online previewer before submitting.

### Do not do in repo until after publication is actually live

- [ ] Do not mark `publish: complete`.
- [ ] Do not add a live retailer URL.
- [ ] Do not record publication as complete.
- [ ] Do not create post-publication notes until the upload has actually been submitted / approved.

## Status after this pass

- Concept: complete.
- Bible: complete.
- Outline: complete.
- Draft: complete.
- Revise: complete.
- Polish: complete.
- Export: complete.
- Package: complete.
- Publish: pending.

Book 3 is ready for manual KDP/upload preparation in repo terms: manuscript export source, build script, package guidance, and draft listing metadata are aligned. The remaining work is manual platform action and final cover/EPUB QA outside this pass.

## Commit notes from this pass

- Publish-readiness report created: commit SHA to be recorded from this file-creation commit.
