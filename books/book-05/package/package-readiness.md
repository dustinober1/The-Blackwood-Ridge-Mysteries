---
status: in_progress
technical_exports: complete
metadata_and_listing: complete
release_tooling: complete
cover: approved
release_snapshot: not_created
publish: pending
---

# Package Readiness — The Planted Page

## Completed package work

- Accepted final-proof/export state retained without chapter-manuscript edits.
- Spoiler-safe retailer metadata, HTML/plain-text descriptions, back-cover copy, series copy, biography, keywords, categories, advisory, taglines, and social copy prepared.
- Retailer upload worksheet and author-decision checklist prepared without inventing ISBN, price, date, rights, DRM, exclusivity, print, barcode, or audiobook fields.
- Fail-closed package validator and release builder prepared using the Book 4 convention.
- Canonical ebook cover supplied at `books/book-05/cover.jpeg` (JPEG, RGB, 1,600 × 2,560 px) and explicitly approved by Dustin Ober on 2026-07-26; approval recorded with matching SHA-256 in `books/book-05/package/cover-approval.json`.
- Exact final line, provenance limit, chapter order, accepted counts, and 207/207 proof/export result are preserved as package controls.

## Validated readiness

`validate-readiness.py` now reports **13/13 checks passed, status: ready_for_release_build**, with no blockers. This confirms the approved cover and all other package controls; it does not itself create a release snapshot or mark the book upload ready, uploaded, accepted, distributed, or published.

## Remaining steps to package completion

The following still require a dedicated release-build task and are not authorized by this readiness confirmation alone:

- a cover-embedded final EPUB;
- a separate upload cover;
- a deterministic retailer upload ZIP;
- a final release manifest or release hash set;
- a permanent `books/book-05/release/` snapshot;
- `package: complete` or root `upload_ready` status.

## Current accurate state

- Final proof: complete.
- Export: complete and validated.
- Package preparation, including cover approval: complete.
- Package: in progress; readiness validated, release build/snapshot not yet run.
- Publication: pending; not uploaded or published.
- Root Book 5 status: `in_progress`.

The cover is no longer a blocker. The next production action is the Book 5 release build/snapshot task, followed by author retailer-controlled decisions (price, rights, DRM, exclusivity, release timing) before upload.
