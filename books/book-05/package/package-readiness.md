---
status: in_progress
technical_exports: complete
metadata_and_listing: complete
release_tooling: complete
cover: blocked_missing_or_unapproved
release_snapshot: not_created
publish: pending
---

# Package Readiness — The Planted Page

## Completed non-cover package work

- Accepted final-proof/export state retained without chapter-manuscript edits.
- Spoiler-safe retailer metadata, HTML/plain-text descriptions, back-cover copy, series copy, biography, keywords, categories, advisory, taglines, and social copy prepared.
- Retailer upload worksheet and author-decision checklist prepared without inventing ISBN, price, date, rights, DRM, exclusivity, print, barcode, or audiobook fields.
- Fail-closed package validator and release builder prepared using the Book 4 convention.
- Release workflow prepared to validate the blocked state on pull requests and to build/commit a permanent release snapshot only after a technically valid approved cover exists.
- Exact final line, provenance limit, chapter order, accepted counts, and 207/207 proof/export result are preserved as package controls.

## Blocking asset

**Required approved ebook cover missing or unapproved.** The canonical asset must be supplied at:

`books/book-05/cover.jpeg`

Required repository gate: JPEG, RGB, exactly 1,600 × 2,560 px, under 50 MB, correct title/author/series/Book 5 text, thumbnail-legible, crop-safe, series-consistent, and explicitly approved.

## Consequences of the blocker

Until the cover is supplied and approved, the workflow must not create or retain:

- a cover-embedded final EPUB;
- a separate upload cover;
- a deterministic retailer upload ZIP;
- a final release manifest or release hash set;
- a permanent `books/book-05/release/` snapshot;
- `package: complete` or root `upload_ready` status.

## Current accurate state

- Final proof: complete.
- Export: complete and validated.
- Non-cover package preparation: complete.
- Package: in progress; blocked by approved cover.
- Publication: pending; not uploaded or published.
- Root Book 5 status: `in_progress`.

Provided the metadata/tooling checks remain green, the missing or unapproved cover is the only package blocker.
