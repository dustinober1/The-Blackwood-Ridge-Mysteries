# The Planted Page — Proof and Export

**Current status:** Final proof and metadata verification are complete. Repository-standard export tooling is prepared; generated outputs must pass the Book 5 proof/export workflow before export is marked complete.

## Authoritative source

The eight files under `../manuscript/` are the controlling story prose. The export process reads those files directly, removes only source YAML and source headings, and compares the reader text in every generated format back to the chapter sources.

## Stable source and report files

- `assemble-manuscript.py` — creates `manuscript-combined.md` without retyping chapter prose.
- `finalize-package.py` — validates source metadata and counts, builds formats, renders the DOCX, runs EPUB validation, compares source-to-export text, and writes reports.
- `build.sh` — build entry point.
- `manuscript-combined.md` — generated combined reader-facing source.
- `manuscript-combined.txt` — generated plain-text review source.
- `manuscript-combined.html` — generated standalone HTML review source.
- `word-count-report.md` — generated counts and hashes.
- `export-readiness.md` — generated proof/export status record.
- `validation-report.md` — generated check results.

## Reproducible generated artifacts

The workflow generates these under ignored directories and uploads them as review artifacts:

- `dist/The-Planted-Page.docx`
- `dist/The-Planted-Page.epub`
- `dist/export-manifest.json`
- `qa/` DOCX render pages, PDF, and contact sheets

## Scope boundary

This is an export-stage pipeline only. It does not create or modify a cover, listing copy, retailer metadata form, upload ZIP, advertising asset, release package, retailer submission, or publication record. Package and publication remain pending.
