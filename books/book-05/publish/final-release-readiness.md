# Book 5 Final Release Readiness — The Planted Page

**Date:** 2026-07-14  
**Repository:** `dustinober1/The-Blackwood-Ridge-Mysteries`  
**Release state:** **BLOCKED — APPROVED COVER REQUIRED — NOT PUBLISHED**

## Completed state

- Manuscript body: 25,174 words across eight accepted chapters.
- Combined reader-facing export: 25,501 words.
- Proof/export validation: 207/207 checks passed.
- DOCX proof: 68 pages; four contact sheets.
- Export EPUBCheck: 0 fatals, 0 errors, 0 warnings, 0 infos.
- Stable Markdown, TXT, HTML, DOCX, and export EPUB hashes already recorded in `books/book-05/export/word-count-report.md`.
- Retailer metadata, listing copy, descriptions, keywords, categories, advisory, and upload worksheet prepared.
- Fail-closed final release tooling, regression tests, and workflow prepared.

## Exact blocker

No approved canonical cover exists at `books/book-05/cover.jpeg`, and `books/book-05/package/cover-approval.json` correctly remains `pending`.

Therefore no final cover-embedded EPUB, upload cover, upload ZIP, release manifest, release hash set, or permanent release snapshot has been generated. The book must remain `in_progress`; package remains `in_progress`; publication remains `pending`.

## Locked story controls

- Final line: `She closed the file.` — accepted export validation confirms it appears exactly once.
- Provenance statement: `Found in returned Mercer volume by M. Hartwell; prior loose-paper location not established.` — accepted export validation confirms it appears exactly once and remains non-dispositive.
- Eight chapter titles and order remain unchanged.
- No protected later-series continuity is present in public metadata or listing copy.

## Required next action

Supply and explicitly approve a JPEG, RGB, 1,600 × 2,560 px, under-50-MB ebook cover at `books/book-05/cover.jpeg`. Record the approving name, approval date, canonical path, and exact cover SHA-256 in `books/book-05/package/cover-approval.json`. Then run the release workflow, inspect the thumbnail and rendered package, confirm byte-identical cover embedding, require EPUBCheck zero errors/warnings, create the deterministic release snapshot, and only then consider changing Book 5 to `upload_ready`.
