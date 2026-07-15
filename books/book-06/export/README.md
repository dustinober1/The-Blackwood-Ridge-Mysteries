# The Pattern — Controlled Export

**Current status:** Controlled proofreading is complete. This directory assembles and validates the repository-standard reader-facing exports. Package, cover, listing, upload, and publication remain pending.

## Authoritative source

The eight files under `../manuscript/` are the controlling proofread story prose. The export process reads those files directly, verifies the accepted Git blobs and counts, removes only YAML production front matter and source headings, and compares every chapter in every generated format back to the source body.

## Stable source and report files

- `assemble-manuscript.py` — assembles the reader-facing Markdown without retyping chapter prose.
- `finalize-package.py` — verifies the PR #31 source baseline, generates front/back matter and formats, validates source identity, renders DOCX, runs EPUBCheck, enforces scope, and writes reports.
- `run-export.py` — applies the inherited Book 4 DOCX sentinel correction and normalizes DOCX/EPUB container metadata for byte-stable rebuilds.
- `build.sh` — build entry point.
- `manuscript-combined.md` — canonical validated combined reader-facing source.
- `manuscript-combined.txt` — canonical plain-text review source.
- `manuscript-combined.html` — canonical standalone HTML review source.
- `word-count-report.md` — generated counts and hashes.
- `export-readiness.md` — generated controlled export status record.
- `validation-report.md` — generated validation ledger.
- `../export-report.md` — complete controlled export assembly record.

Run the complete controlled build with `python books/book-06/export/run-export.py`.

## Reproducible generated artifacts

The workflow generates these under ignored directories and uploads them as review artifacts:

- `dist/The-Pattern.docx`
- `dist/The-Pattern.epub`
- `dist/export-manifest.json`
- `qa/` DOCX render pages, PDF, and contact sheets

## Scope boundary

This is an export-stage pipeline only. It does not create or modify a cover, package, listing copy, retailer metadata form, upload ZIP, advertising asset, release package, retailer submission, or publication record. Book 6 remains not upload ready and not published.
