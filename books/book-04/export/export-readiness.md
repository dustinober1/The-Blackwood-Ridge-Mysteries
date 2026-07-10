---
status: complete
book: 4
build_date: "2026-07-10"
publish_status: pending
---

# Export Readiness — The Archive Fire

## Prior blocker

The previous pass could not execute `assemble-manuscript.py` or safely transform the eight fetched chapter sources into a 36,000-word generated artifact. It therefore documented the blocker rather than generating or validating the export.

## Resolution

The blocker is resolved by the executable local/CI pipeline in `finalize-package.py` and `build.sh`. The pipeline reads the repository files directly, strips only per-chapter YAML and source headings, assembles all eight chapter bodies once and in order, builds the supported formats, and validates source preservation mechanically.

## Reader-facing source status

- Combined Markdown: **complete and validated**.
- Plain text: **complete and validated**.
- Standalone HTML: **complete and validated**.
- DOCX: **generated, opened through LibreOffice, structurally checked, and rendered page by page**.
- EPUB 3: **generated and structurally validated; epubcheck used when available**.
- PDF proof: **not a repository deliverable**. A temporary PDF is generated only to render and inspect the DOCX; no print-ready PDF is claimed because print specifications are unresolved.

## Preservation result

All eight chapter source files were unchanged. The combined chapter bodies match their source bodies exactly after removal of YAML metadata and the source-only heading. No plot, clue, solution, chronology, character arc, arrest basis, consultant arrangement, supplemental record, or ending content was altered.

## Export status

**COMPLETE.** This does not mean the overall publication package is complete or that the book has been uploaded or published.
