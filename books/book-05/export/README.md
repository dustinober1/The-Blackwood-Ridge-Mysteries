# The Planted Page — Proof and Export

**Current status:** Final proof, metadata verification, repository-standard export generation, and export validation are complete. Package and publication remain pending.

## Authoritative source

The eight files under `../manuscript/` are the controlling story prose. The export process reads those files directly, removes only source YAML and source headings, and compares the reader text in every generated format back to the chapter sources.

## Stable source and report files

- `assemble-manuscript.py` — creates `manuscript-combined.md` without retyping chapter prose.
- `finalize-package.py` — validates source metadata and accepted source blobs, builds formats, renders the DOCX, runs EPUB validation, compares source-to-export text, and writes reports.
- `run-export.py` — applies the scoped correction for Book 4’s empty-string replacement-character sentinel while preserving every other inherited validation.
- `build.sh` — build entry point.
- `manuscript-combined.md` — validated combined reader-facing source.
- `manuscript-combined.txt` — validated plain-text review source.
- `manuscript-combined.html` — validated standalone HTML review source.
- `word-count-report.md` — generated counts and hashes.
- `export-readiness.md` — generated proof/export status record.
- `validation-report.md` — generated results for 207 checks.

## Reproducible generated artifacts

The workflow generates these under ignored directories and uploads them as review artifacts:

- `dist/The-Planted-Page.docx`
- `dist/The-Planted-Page.epub`
- `dist/export-manifest.json`
- `qa/` DOCX render pages, PDF, and contact sheets

The validated DOCX rendered to 68 pages and four contact sheets. EPUBCheck reported 0 fatals, 0 errors, 0 warnings, and 0 infos. All eight chapter bodies matched the controlling sources in Markdown, TXT, HTML, DOCX, and EPUB.

## Scope boundary

This is an export-stage pipeline only. It does not create or modify a cover, listing copy, retailer metadata form, upload ZIP, advertising asset, release package, retailer submission, or publication record. Package and publication remain pending, and this book is not marked upload ready or published.
