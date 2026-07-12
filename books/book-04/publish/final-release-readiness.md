# Book 4 Final Release Readiness — The Archive Fire

**Date:** 2026-07-12  
**Repository:** `dustinober1/The-Blackwood-Ridge-Mysteries`  
**Release state:** **UPLOAD READY — NOT YET PUBLISHED**

## Outcome

*The Archive Fire* has a reproducible, mechanically validated ebook publication package built from the authoritative Book 4 manuscript and the author-approved repository cover.

The release artifact contains:

- a reflowable EPUB 3 with embedded cover, navigation, bibliographic metadata, stable identifier, and series metadata;
- a separate 1,600 × 2,560 px RGB JPEG cover for retailer upload;
- a DOCX review copy;
- final listing copy and HTML/plain-text retailer descriptions;
- a KDP upload sheet containing title, author, series, keyword, category, pricing, and final-platform guidance;
- a machine-readable manifest and human-readable validation report;
- one ZIP containing all nine upload/reference files.

Generated binaries live under the ignored `books/book-04/export/dist/` directory during a build. GitHub Actions publishes the validated files as the `book-04-release-package` artifact.

## Story preservation

The authoritative reader-facing source remains:

`books/book-04/export/manuscript-combined.md`

No chapter manuscript source was edited during release finalization. The release gate requires:

- all eight expected chapters in order;
- the locked final sentence, `For one breath, it was enough to know that when she did, she would not be reading alone.`;
- the established title, author, and series metadata;
- no TODO, TBD, conflict marker, template token, or internal planning label in reader-facing content.

The plot, clues, false-suspect functions, chronology, solution, arrest basis, consultant arrangement, supplemental Crowe record, Ruth Mallory’s duplicate system, brass cat charm, floorboard ending, and final magnifying-glass image are unchanged.

## Final validation

| Check | Result |
|---|---|
| Manuscript body words (chapter prose) | 34,960 |
| Combined reader-facing words | 35,249 |
| Chapter count | 8 |
| DOCX render proof | 97 pages; every page rendered |
| DOCX visual contact sheets | 5 |
| Cover | JPEG, RGB, 1,600 × 2,560 px, 72 dpi |
| EPUB | EPUB 3, reflowable |
| EPUBCheck | 0 fatals, 0 errors, 0 warnings, 0 infos |
| Reader title page | Exactly one; navigation title excluded from page count |
| Embedded cover | Byte-for-byte match with separate upload cover |
| Locked ending | Present exactly once |
| Placeholder/internal-marker scan | Clean |

## Stable upload/source hashes

The EPUB and cover hashes were reproduced unchanged in consecutive validated builds.

- EPUB: `4e05722551fbcbb582b1e8f1a48116b6f34db43a33e9fef9f51b6b85b6d9459c`
- Cover JPEG: `5cb56980999a2d864bcf26e3025cb625c34beab44dcc88eef7ae7c7c4af25d3a`
- Reader-facing Markdown: `0a52ac312edc290c32700fa769552ca7c815539bcd7ad62321e4786d0bd60089`

The exact DOCX hash is retained in each generated release manifest because office-package metadata can vary between otherwise equivalent builds.

## Retailer package

The upload ZIP contains:

1. `The-Archive-Fire.epub`
2. `The-Archive-Fire-cover.jpg`
3. `The-Archive-Fire.docx`
4. `The-Archive-Fire-release-manifest.json`
5. `The-Archive-Fire-release-validation.md`
6. `The-Archive-Fire-listing-copy.md`
7. `The-Archive-Fire-retailer-description.html`
8. `The-Archive-Fire-retailer-description.txt`
9. `The-Archive-Fire-KDP-upload-sheet.md`

## Remaining author-controlled retailer actions

The repository cannot truthfully mark publication complete until the author:

1. chooses the release or preorder date;
2. confirms territorial publication rights;
3. chooses DRM treatment;
4. chooses whether to continue KDP Select / Kindle Unlimited or another exclusivity program;
5. confirms the final list price, recommended at `$2.99` for series consistency;
6. uploads the EPUB and separate cover;
7. enters the supplied description, keywords, categories, price, and series relationship;
8. answers the platform’s content-disclosure questions from the actual production history;
9. inspects the title in the retailer previewer or Kindle Previewer;
10. submits the book and confirms a live detail page.

Until then:

- `books/book-04/progress.yaml` correctly retains `publish: pending`;
- the root series tracker may describe Book 4 as `upload_ready`;
- no repository file should claim the title has been uploaded, accepted, distributed, or published.
