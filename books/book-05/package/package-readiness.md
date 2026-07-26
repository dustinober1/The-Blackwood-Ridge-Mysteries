---
status: complete
technical_exports: complete
metadata_and_listing: complete
release_tooling: complete
cover: approved
release_snapshot: created
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

## Release build result

PR #44 (`agent/book-05-release-build`) ran the `book-05-release-package` CI workflow and merged to `main` at commit `c0e2174`. The controlled release build produced and validated the retailer EPUB, DOCX, cover, and upload ZIP:

- EPUBCheck: 0 fatals / 0 errors / 0 warnings / 0 infos.
- Deterministic rebuild verified (identical hashes on a second build).
- Permanent release snapshot committed at `books/book-05/release/` (EPUB, cover, upload ZIP, manifest, listing/retailer copy, KDP upload sheet).
- Full record: `books/book-05/release/release-validation.md` and `release-manifest.json`.

Two build-script bugs surfaced by current `pandoc`/`epubcheck` versions were fixed along the way (`books/book-05/export/release-package.py`): the EPUB nav document being counted as a duplicate title heading, and the NCX `dtb:uid` not being synced to the fixed OPF UUID.

## Current accurate state

- Final proof: complete.
- Export: complete and validated.
- Package preparation, including cover approval and release build: complete.
- Package: complete.
- Publication: pending; not uploaded or published.
- Root Book 5 status: `upload_ready`.

The next production action is the author retailer-controlled decisions (price, rights, DRM, exclusivity, release timing) in `books/book-05/package/author-decision-checklist.md`, followed by retailer upload.
