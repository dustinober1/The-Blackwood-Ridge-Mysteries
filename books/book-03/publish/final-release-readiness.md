# Book 3 Final Release Readiness — The Challenger

**Correction date:** 2026-07-25  
**Repository:** `dustinober1/The-Blackwood-Ridge-Mysteries`  
**Release state:** **UPLOAD READY — NOT YET PUBLISHED**

## Superseded release evidence

The earlier successful release workflow embedded and packaged a programmatically generated cover substitute. The old cover SHA-256 was:

`e39da2e0a6102373888302b8d9cd8270d6fa1ebecff1757d00bed007770683e7`

That artifact was mechanically valid but did not establish author approval. It also contained additional cover text not included in the later author-approved asset. The old cover hash and all retailer-upload packages containing it are explicitly superseded.

## Governing approved cover

| Field | Approved value |
|---|---|
| Asset | `books/book-03/package/approved/The-Challenger-cover.jpg` |
| Authority | `books/book-03/package/approved/approved-cover.json` |
| Format / mode | JPEG / RGB |
| Dimensions | 1,600 × 2,560 px |
| Size | 2,105,356 bytes |
| SHA-256 | `e96585dacae4e7aacb4aaabbec939c9efeac61560216f86fd99feae480ffdbaf` |

The cover contains only:

- `THE BLACKWOOD RIDGE MYSTERIES · BOOK 3`
- `THE CHALLENGER`
- `VESPER BLYTHE`

## Corrected release pipeline

The active build validates the authority record and copies the approved JPEG directly. It does not generate a replacement cover. The former generator has been removed.

The release validator records and compares:

- approved source SHA-256;
- standalone release-cover SHA-256;
- nested upload-cover bytes;
- EPUB-embedded cover path and SHA-256;
- exact title, author, series, and approved text;
- image format, mode, dimensions, and byte size.

## Replacement workflow evidence

- Workflow: `Book 3 release package`
- Run ID: `30183982603`
- Run URL: `https://github.com/dustinober1/The-Blackwood-Ridge-Mysteries/actions/runs/30183982603`
- Event: pull request
- Requested branch: `agent/book-03-approved-cover-release-repair-20260725`
- Recorded source commit: `00840da785c553b1b0658cec406cef1ac7ba27df`
- Job: `build-and-validate` — success
- Artifact: `book-03-release-package`
- Artifact ID: `8626458510`
- Artifact size: 8,662,940 bytes
- Artifact digest: `sha256:a8e8d3bb6705b1072ebe90f6980f11c30b430145ade650668fb972c0ac9ae95e`
- Expiration: 2026-08-25 UTC

All workflow steps succeeded: checkout, Python setup, dependency installation, regression tests, release build/validation, validation-report display, artifact upload, and post-job cleanup.

## Replacement artifact inventory

Outer artifact, exactly:

1. `The-Challenger.epub`
2. `The-Challenger-cover.jpg`
3. `The-Challenger-upload-package.zip`
4. `manuscript-retail.md`
5. `validation.json`
6. `release-validation.md`

Nested upload ZIP, exactly:

1. `The-Challenger.epub`
2. `The-Challenger-cover.jpg`
3. `manuscript-retail.md`
4. `Book-3-listing-copy.md`
5. `README-FIRST.md`
6. `validation.json`
7. `release-validation.md`

Every duplicated file is byte-identical between the outer artifact and nested upload ZIP.

## Mechanical verification

| Check | Result |
|---|---|
| `validation.json` | PASS; no errors |
| Story words | 24,212 |
| Retail-package words | 24,486 |
| Chapters | 8 |
| Locked ending | Present exactly once |
| Cover | JPEG, RGB, 1,600 × 2,560 px |
| Cover identity | Approved = standalone = nested = EPUB embedded |
| EPUBCheck | v4.2.6; 0 fatals, 0 errors, 0 warnings, 0 infos; exit 0 |
| EPUB metadata | Correct title, author, language, series, and series position |
| EPUB manifest | 18 resources; none missing |
| EPUB spine | 15 ordered items; no unresolved resource |
| Manuscript prose | No source manuscript file changed by the corrective pull request |

## Fresh replacement hashes

- EPUB: `186ca0e550504545928c90605b258d283e736d06ae367ac5c9d0cc60d1dee072`
- Approved/standalone/nested/embedded cover: `e96585dacae4e7aacb4aaabbec939c9efeac61560216f86fd99feae480ffdbaf`
- Retail Markdown: `4ba88471787e6719995b81535ec10e900844e3b0540e2ed221adb395bc09352d`
- Upload ZIP: `356c15235781bfba10432bcfb086e7030ae922dacab6b734683230c6021eb5f9`
- `validation.json`: `c2f06eb05a094d09bb24c3373f9cda9beefd98971df6aae7550e23bbf2b7e6e0`
- `release-validation.md`: `14ab9b7cc40065265c39beb023472e118181c02da81315f5a0a4a94f6229c57f`

## Visual verification

At full size and approximately 150-pixel thumbnail width, the approved cover has readable series, title, and author hierarchy; no subtitle/tagline; no cropped or malformed typography; no edge clipping or visible corruption; and visible red/blue annotations, brass magnifying glass, pale marble bookend, archival papers/books, and warm reading lamp.

## Verdict

**UPLOAD READY**

This verdict means the replacement artifact is technically ready for author review and retailer preview. It does not mean uploaded, submitted, retailer accepted, live, distributed, or published.

`publish: pending` remains required.
