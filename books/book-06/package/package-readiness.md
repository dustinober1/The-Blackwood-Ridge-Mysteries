---
status: complete
technical_exports: complete
metadata_and_listing: complete
release_tooling: complete
cover: approved
release_snapshot: created
publish: pending
---

# Package Readiness — The Pattern

## Completed package work

- Accepted final-proof/export state retained without chapter-manuscript edits.
- Spoiler-safe retailer metadata, HTML/plain-text descriptions, back-cover copy, series copy, biography, keywords, categories, advisory, taglines, and social copy prepared.
- Retailer upload worksheet and author-decision checklist prepared without inventing ISBN, price, date, rights, DRM, exclusivity, print, barcode, or audiobook fields.
- Fail-closed package validator and release builder prepared using the Book 5 convention.
- Canonical ebook cover supplied at `books/book-06/cover.jpeg` (JPEG, RGB, 1,600 × 2,560 px) and explicitly approved by Dustin Ober on 2026-07-26; approval recorded with matching SHA-256 in `books/book-06/package/cover-approval.json`.
- Exact final line, provenance limit, chapter order, accepted counts, and 293/293 proof/export result are preserved as package controls.

## Release build result

PR #45 (`agent/book-06-package-assembly`) added the package layer and approved cover. PR #46 (`agent/book-06-release-build`) ran the `book-06-release-package` CI workflow and merged to `main`; its final commit (`bcc1ebd`, cherry-picked onto `main` as `f122ec6` after a push-race with the concurrent `book-06-proof-export.yml` workflow) added the permanent release snapshot:

- EPUBCheck: 0 fatals / 0 errors / 0 warnings / 0 infos.
- Deterministic rebuild verified (identical hashes on a second build).
- Permanent release snapshot committed at `books/book-06/release/` (EPUB, cover, upload ZIP, manifest, listing/retailer copy, KDP upload sheet).
- Full record: `books/book-06/release/release-validation.md` and `release-manifest.json`.

Two structural issues surfaced and were fixed along the way:

- `export/release-package.py` needed the same pandoc-version-drift fixes discovered on Book 5 (nav-in-spine duplicate title heading; NCX `dtb:uid` not synced to the fixed OPF UUID) — carried over directly since this script was adapted from Book 5's.
- `.github/workflows/book-06-release-package.yml`'s `build-and-validate` job required `fetch-depth: 0` so Book 6's export scope validator (`finalize-package.py`, added by PR #41) could resolve `git merge-base` against `main`. That validator also fails closed on any diff touching a package/cover/listing/publication/release/retailer asset, so the package-assembly PR (#45) and the release-build PR (#46) had to be split — the release build could only run once the package files were already on `main`.

## Current accurate state

- Final proof: complete.
- Export: complete and validated.
- Package preparation, including cover approval and release build: complete.
- Package: complete.
- Publication: pending; not uploaded or published.
- Root Book 6 status: `upload_ready`.

The next production action is the author retailer-controlled decisions (price, rights, DRM, exclusivity, release timing) in `books/book-06/package/author-decision-checklist.md`, followed by retailer upload.
