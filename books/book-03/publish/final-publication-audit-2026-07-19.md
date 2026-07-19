# Book 3 Final Publication Audit — The Challenger

**Audit date:** 2026-07-19  
**Starting `main` commit:** `2fb6277c1c536dd57fb2d360ffc781b39d16925a`  
**Audit branch:** `agent/book-03-final-publication-package-20260719`  
**Author:** Vesper Blythe  
**Series:** The Blackwood Ridge Mysteries, Book 3

## Scope

This audit is limited to Book 3 and the root series tracker. No Book 1, Book 2, or Book 4–8 manuscript or publication asset was changed.

## Files inspected

- `progress.yaml`
- `.github/workflows/book-03-release-package.yml`
- `books/book-03/progress.yaml`
- `books/book-03/outline.md`
- `books/book-03/content-notes.md`
- `books/book-03/revision/book-03-polish-pass.md`
- `books/book-03/manuscript/ch-01.md`
- `books/book-03/manuscript/ch-02.md`
- `books/book-03/manuscript/ch-03.md`
- `books/book-03/manuscript/ch-04.md`
- `books/book-03/manuscript/ch-05.md`
- `books/book-03/manuscript/ch-06.md`
- `books/book-03/manuscript/ch-07.md`
- `books/book-03/manuscript/ch-08.md`
- `books/book-03/export/manuscript-combined.md`
- `books/book-03/export/build.sh`
- `books/book-03/export/validate-release.py`
- `books/book-03/export/export-readiness.md`
- `books/book-03/package/packaging.md`
- `books/book-03/package/package-readiness.md`
- `books/book-03/publish/listing.md`
- `books/book-03/publish/upload-package.md`
- `books/book-03/publish/publish-readiness.md`
- `books/book-03/publish/final-release-readiness.md`

## Verified manuscript controls

- Eight chapters are recorded in order:
  1. The Visitor Who Came Looking
  2. After the Lecture
  3. The Door Opens
  4. The Second Hand
  5. The Gap
  6. The Keeper
  7. Still Hands
  8. The Man Who Buried It
- The canonical reader-facing source is `books/book-03/export/manuscript-combined.md`.
- The established locked ending is `She did not need the bell to ring before she began.`
- Recorded story word count: **24,212**.
- Recorded retail-package word count: **24,486**.
- Title, author, series name, and series number are consistently recorded as `The Challenger`, `Vesper Blythe`, `The Blackwood Ridge Mysteries`, and Book 3.
- The existing validation logic fails closed on missing or reordered chapters, duplicate or missing locked ending, prohibited placeholders, missing back matter, invalid EPUB package structure, missing navigation, invalid cover, or a mismatched embedded cover.

## Recorded export and cover evidence

The most recent committed readiness record reports:

- EPUB 3;
- EPUBCheck: 0 fatals, 0 errors, 0 warnings, 0 infos;
- cover: JPEG, RGB, 1,600 × 2,560 px;
- embedded EPUB cover matching the separate upload cover byte-for-byte;
- correct navigation and spine order;
- no placeholder or hidden-control leakage;
- SHA-256:
  - EPUB: `a8f7d99bbec7ed9664dbc0f7fd9251b917dda26695f42e7159534933db14a1f8`
  - cover: `e39da2e0a6102373888302b8d9cd8270d6fa1ebecff1757d00bed007770683e7`
  - retail Markdown: `4ba88471787e6719995b81535ec10e900844e3b0540e2ed221adb395bc09352d`

These hashes are historical evidence from the prior release build. Generated binaries are intentionally ignored by Git and supplied through the GitHub Actions artifact.

## Metadata and listing review

The canonical listing provides a spoiler-safe primary description, short description, seven keyword phrases, three category recommendations, content advisory, and a clearly labeled $2.99 pricing recommendation. The upload sheet now explicitly records:

- no approved subtitle;
- no invented publication date;
- no invented ISBN;
- territorial-rights confirmation required;
- DRM as an author decision, with consistency to Books 1 and 2 recommended;
- the correct canonical listing path: `books/book-03/publish/listing.md`.

## Defect fixed

The prior upload sheet pointed to nonexistent `Book-3-listing-copy.md`. It now points to the canonical `books/book-03/publish/listing.md` and separates recommendations from retailer-controlled decisions.

## Fail-closed release gate

| Gate | Result |
|---|---|
| Approved manuscript | PASS — recorded canonical manuscript and locked ending |
| Complete chapter set and order | PASS — eight chapters recorded and validated by release script |
| Correct title/author/series metadata | PASS |
| Complete listing copy | PASS |
| Seven keyword fields | PASS |
| Categories and price recommendation | PASS |
| Correct series reading order and cross-sell | PASS in committed package records |
| No placeholders or hidden controls | PASS in recorded validation |
| Approved cover specification | PASS in recorded validation |
| Validated EPUB | PASS in recorded prior validation |
| Canonical filenames defined | PASS |
| Current reviewed-commit workflow artifact available | **NOT VERIFIED** — no workflow run is attached to starting commit `2fb6277c1c536dd57fb2d360ffc781b39d16925a` |
| Current artifact checksums reproduced from reviewed commit | **NOT VERIFIED** |
| Uncommitted required asset | Generated binaries are not committed by design; current workflow artifact is required |

## Verdict

**NOT UPLOAD READY**

The manuscript, metadata, cover specification, build system, and prior validation evidence are publication-ready. The fail-closed gate remains closed because a fresh release workflow artifact tied to the reviewed branch commit has not yet been generated and its checksums have not been compared with the recorded canonical values.

## Next precise action

Run `.github/workflows/book-03-release-package.yml` on `agent/book-03-final-publication-package-20260719`, download the `book-03-release-package` artifact, confirm `validation.json` reports `PASS`, verify EPUBCheck has zero errors and warnings, and confirm the artifact contains the exact canonical filenames before changing this verdict to `UPLOAD READY`.
