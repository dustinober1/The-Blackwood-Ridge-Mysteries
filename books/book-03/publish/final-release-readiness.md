# Book 3 Final Release Readiness — The Challenger

**Date:** 2026-07-12  
**Repository:** `dustinober1/The-Blackwood-Ridge-Mysteries`  
**Release state:** **UPLOAD READY — NOT YET PUBLISHED**

## Outcome

*The Challenger* now has a reproducible and mechanically validated ebook release package. The package contains:

- a reflowable EPUB 3 with embedded cover, navigation, bibliographic metadata, series metadata, and reader back matter;
- a separate 1,600 × 2,560 px RGB JPEG cover for retailer upload;
- final retailer listing copy, seven keyword phrases, category recommendations, and pricing guidance;
- an author-facing KDP upload sheet;
- SHA-256 hashes and a machine-readable validation manifest;
- a human-readable validation report;
- a ZIP containing the upload and reference files.

Generated binaries live under the ignored `books/book-03/export/dist/` and `books/book-03/package/dist/` directories during a local build. GitHub Actions publishes the validated files as the `book-03-release-package` workflow artifact.

## Story preservation

The authoritative reader-facing story source remains:

`books/book-03/export/manuscript-combined.md`

No chapter manuscript source was edited during release finalization. The retail assembler fails closed unless it finds:

- all eight expected chapters in order;
- the locked final sentence, `She did not need the bell to ring before she began.`;
- the established title, author, and series metadata;
- exactly one legacy edition line to normalize for the July 2026 release package.

The culprit, clue ladder, chronology, confession, arrest, emotional resolution, and final story beat are unchanged.

## Reader-facing production additions

The generated retail manuscript adds, after the locked story ending:

1. a review request;
2. the series list through Book 4;
3. an author bio.

The first-edition line is normalized from `June 2026` to `July 2026` only in the generated retail manuscript. The authoritative story source is not rewritten for that production-only change.

## Validation result

The release pipeline passed against the authoritative Book 3 manuscript.

| Check | Result |
|---|---|
| Story word count | 24,212 |
| Retail package word count | 24,486 |
| Chapter count | 8 |
| Cover | JPEG, RGB, 1,600 × 2,560 px, 72 dpi |
| EPUB version | EPUB 3 |
| EPUBCheck | 0 fatals, 0 errors, 0 warnings, 0 infos |
| Navigation | Eight chapters plus review, series, and author sections present and ordered |
| Embedded cover | Matches the separate upload cover byte-for-byte |
| Placeholder scan | No `TODO`, `TBD`, `Document X`, `Book 1 reading`, template token, or internal planning label |
| Locked ending | Present exactly once |

### Deterministic release hashes

- EPUB: `a8f7d99bbec7ed9664dbc0f7fd9251b917dda26695f42e7159534933db14a1f8`
- Cover JPEG: `e39da2e0a6102373888302b8d9cd8270d6fa1ebecff1757d00bed007770683e7`
- Retail Markdown: `4ba88471787e6719995b81535ec10e900844e3b0540e2ed221adb395bc09352d`

## Visual QA

The EPUB was rendered section by section for visual inspection. The initial build exposed a duplicate automatic Pandoc title page in front of the manuscript's own title page. The build was corrected with `--epub-title-page=false` and rebuilt.

The corrected EPUB structure is:

1. cover;
2. manuscript title/copyright section;
3. contents;
4. Chapters 1–8;
5. thank-you/review request;
6. series list;
7. author bio.

The final cover was checked at full size and thumbnail scale for title hierarchy, series identification, author legibility, contrast, edge safety, and continuity with the established deep-plum, gold, archival-paper, and brass-glass series language.

## Retail listing package

The upload-ready listing at `books/book-03/publish/listing.md` includes:

- primary and short descriptions;
- tagline and hook options;
- content advisory;
- seven keyword phrases;
- three category recommendations;
- a $2.99 launch-price recommendation;
- completed production checks and remaining platform actions.

The title remains *The Challenger*. Because the phrase is broad, the retailer listing should always include the complete series and author metadata. This readiness record is not a legal title-clearance opinion.

## Remaining author-controlled retailer actions

The repository cannot truthfully mark publication complete until these actions occur on the retailer platform:

1. choose the release or preorder date;
2. confirm territorial rights;
3. choose DRM treatment;
4. choose whether to continue KDP Select / Kindle Unlimited enrollment;
5. upload the EPUB and separate JPEG cover;
6. enter the description, keywords, categories, price, and series relationship;
7. answer the platform's content-disclosure questions from the actual production history;
8. inspect the title in the KDP online previewer or Kindle Previewer;
9. submit the book;
10. confirm retailer acceptance and a live detail page.

Until those steps are complete:

- `books/book-03/progress.yaml` correctly retains `publish: pending`;
- the root series tracker may describe Book 3 as `upload_ready`;
- no repository file should claim the title is live, distributed, or published.
