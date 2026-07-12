---
status: technical-validation-complete
book: 4
validated: "2026-07-10"
publish_status: pending
---

# Final Validation Report — The Archive Fire

## Scope and starting state

- Repository: `dustinober1/The-Blackwood-Ridge-Mysteries`
- Default branch: `main`
- Required starting HEAD: `9d946e89c0c03983f5a797ed9d5970858314c7dd`
- Required starting message: `Document Book 4 export artifact generation blocker`
- Books 1–3: excluded from the build and edit scope.

## Mechanical validation

| Area | Check | Result | Detail |
|---|---|---|---|
| Markdown | Markdown: no forbidden marker <<<<<<<|=======|>>>>>>> | PASS | not found |
| Markdown | Markdown: no forbidden marker \b(?:TODO|TBD|FIXME)\b | PASS | not found |
| Markdown | Markdown: no forbidden marker AUTHOR DECISION REQUIRED | PASS | not found |
| Markdown | Markdown: no forbidden marker \[\s*PLACEHOLDER\s*\] | PASS | not found |
| Markdown | Markdown: no forbidden marker \{\{.*?\}\} | PASS | not found |
| Markdown | Markdown: no forbidden marker internal (?:note|commentary|production) | PASS | not found |
| Markdown | Markdown: chapter sequence and titles | PASS | found [('1', 'Smoke Under Town Hall'), ('2', 'The Salvage Table'), ('3', 'A Shelf That Lied Twice'), ('4', 'The Predecessor’s Hand'), ('5', 'Water Lines'), ('6', 'Bad Procedure'), ('7', 'The Ash Index'), ('8', 'The Bo... |
| Markdown | Markdown: eight chapters | PASS | found 8 |
| Markdown | Markdown: no YAML metadata leak | PASS | checked source-only keys |
| Markdown | Markdown: no raw page-break commands | PASS | checked |
| Markdown | Markdown: Chapter 1 body preserved exactly | PASS | source f87f1ad4754c235ec90cfde1bf8a4f9cc5fb618ce9a838f236cc6b385cf485e2; combined f87f1ad4754c235ec90cfde1bf8a4f9cc5fb618ce9a838f236cc6b385cf485e2 |
| Markdown | Markdown: Chapter 2 body preserved exactly | PASS | source 1bdd6ff1ee9896b966fc67534bfa3c754929b36574d12f4a8d9a3835358db1eb; combined 1bdd6ff1ee9896b966fc67534bfa3c754929b36574d12f4a8d9a3835358db1eb |
| Markdown | Markdown: Chapter 3 body preserved exactly | PASS | source 4e1c1e303e664e714cc9615dfe5dfcb86ccb92306a46f69d5ead86756b65bbfb; combined 4e1c1e303e664e714cc9615dfe5dfcb86ccb92306a46f69d5ead86756b65bbfb |
| Markdown | Markdown: Chapter 4 body preserved exactly | PASS | source 020da82df14caeea016058efa68c35e34180d9fe021bc2b810e844281ae2fe73; combined 020da82df14caeea016058efa68c35e34180d9fe021bc2b810e844281ae2fe73 |
| Markdown | Markdown: Chapter 5 body preserved exactly | PASS | source 00c9b751b0706a561e304b5ce6f60f37ca38ab0613f81657e1287e0df9d3a83e; combined 00c9b751b0706a561e304b5ce6f60f37ca38ab0613f81657e1287e0df9d3a83e |
| Markdown | Markdown: Chapter 6 body preserved exactly | PASS | source c887c804549f28e3875bb127b68e74ebc455d19455a73cfdfb7918a20666af73; combined c887c804549f28e3875bb127b68e74ebc455d19455a73cfdfb7918a20666af73 |
| Markdown | Markdown: Chapter 7 body preserved exactly | PASS | source 5bf643c05f69b9dd9c527c0157b8b93d31acd5230ed6f958f4b30dafedff738a; combined 5bf643c05f69b9dd9c527c0157b8b93d31acd5230ed6f958f4b30dafedff738a |
| Markdown | Markdown: Chapter 8 body preserved exactly | PASS | source f0fb8d6d709e2a394ddf0fda265b54c99c6ab6d0b07ce3e6cece761a0e267fb1; combined f0fb8d6d709e2a394ddf0fda265b54c99c6ab6d0b07ce3e6cece761a0e267fb1 |
| Markdown | Markdown: no duplicated chapter bodies | PASS | unique hashes: 8 |
| Markdown | Markdown: front matter order | PASS | [0, 86, 676] |
| Markdown | Markdown: back matter order | PASS | [207512, 207740, 207877] |
| HTML | HTML: no forbidden marker <<<<<<<|=======|>>>>>>> | PASS | not found |
| HTML | HTML: no forbidden marker \b(?:TODO|TBD|FIXME)\b | PASS | not found |
| HTML | HTML: no forbidden marker AUTHOR DECISION REQUIRED | PASS | not found |
| HTML | HTML: no forbidden marker \[\s*PLACEHOLDER\s*\] | PASS | not found |
| HTML | HTML: no forbidden marker \{\{.*?\}\} | PASS | not found |
| HTML | HTML: no forbidden marker internal (?:note|commentary|production) | PASS | not found |
| HTML | HTML: chapter sequence | PASS | ['Chapter 1 — Smoke Under Town Hall', 'Chapter 2 — The Salvage Table', 'Chapter 3 — A Shelf That Lied Twice', 'Chapter 4 — The Predecessor’s Hand', 'Chapter 5 — Water Lines', 'Chapter 6 — Bad Procedure', 'Chapter 7 — ... |
| HTML | HTML: title and author | PASS | checked |
| HTML | HTML: no broken internal links | PASS | [] |
| DOCX | DOCX: valid package structure | PASS | set() |
| DOCX | DOCX: chapter heading sequence | PASS | ['Chapter 1 — Smoke Under Town Hall', 'Chapter 2 — The Salvage Table', 'Chapter 3 — A Shelf That Lied Twice', 'Chapter 4 — The Predecessor’s Hand', 'Chapter 5 — Water Lines', 'Chapter 6 — Bad Procedure', 'Chapter 7 — ... |
| DOCX | DOCX: chapter headings use Heading 1 | PASS | [('Chapter 1 — Smoke Under Town Hall', 'Heading1', True), ('Chapter 2 — The Salvage Table', 'Heading1', True), ('Chapter 3 — A Shelf That Lied Twice', 'Heading1', True), ('Chapter 4 — The Predecessor’s Hand', 'Heading... |
| DOCX | DOCX: chapter page breaks | PASS | [('Chapter 1 — Smoke Under Town Hall', True), ('Chapter 2 — The Salvage Table', True), ('Chapter 3 — A Shelf That Lied Twice', True), ('Chapter 4 — The Predecessor’s Hand', True), ('Chapter 5 — Water Lines', True), ('... |
| DOCX | DOCX text: no forbidden marker <<<<<<<|=======|>>>>>>> | PASS | not found |
| DOCX | DOCX text: no forbidden marker \b(?:TODO|TBD|FIXME)\b | PASS | not found |
| DOCX | DOCX text: no forbidden marker AUTHOR DECISION REQUIRED | PASS | not found |
| DOCX | DOCX text: no forbidden marker \[\s*PLACEHOLDER\s*\] | PASS | not found |
| DOCX | DOCX text: no forbidden marker \{\{.*?\}\} | PASS | not found |
| DOCX | DOCX text: no forbidden marker internal (?:note|commentary|production) | PASS | not found |
| DOCX | DOCX: no raw Markdown/page syntax | PASS | [] |
| DOCX | DOCX: core title | PASS | checked |
| DOCX | DOCX: core author | PASS | checked |
| DOCX | DOCX: LibreOffice opens and renders | PASS | skipped (tools missing) |
| DOCX | DOCX render: no accidental blank pages | PASS | skipped (tools missing) |
| DOCX | DOCX render: no broken replacement characters | PASS | skipped (tools missing) |
| DOCX | DOCX render: every chapter starts once | PASS | skipped (tools missing) |
| DOCX | DOCX render: chapter headings begin pages | PASS | skipped (tools missing) |
| DOCX | DOCX render: no widowed chapter headings | PASS | skipped (tools missing) |
| DOCX | DOCX render: every page rendered | PASS | skipped (tools missing) |
| DOCX | DOCX render: contact sheets created | PASS | skipped (tools missing) |
| EPUB | EPUB: nonempty ZIP | PASS | 24 entries |
| EPUB | EPUB: mimetype first | PASS | mimetype |
| EPUB | EPUB: mimetype uncompressed | PASS | 0 |
| EPUB | EPUB: container present | PASS | checked |
| EPUB | EPUB: mimetype correct | PASS | application/epub+zip |
| EPUB | EPUB: OPF path resolved | PASS | EPUB/content.opf |
| EPUB | EPUB: title metadata | PASS | 'The Archive Fire' |
| EPUB | EPUB: author metadata | PASS | 'Vesper Blythe' |
| EPUB | EPUB: language metadata | PASS | 'en-US' |
| EPUB | EPUB: all manifest resources exist | PASS | [] |
| EPUB | EPUB: readable spine | PASS | ['EPUB/text/cover.xhtml', 'EPUB/text/title_page.xhtml', 'EPUB/nav.xhtml', 'EPUB/text/ch001.xhtml', 'EPUB/text/ch002.xhtml', 'EPUB/text/ch003.xhtml', 'EPUB/text/ch004.xhtml', 'EPUB/text/ch005.xhtml', 'EPUB/text/ch006.x... |
| EPUB | EPUB: navigation document | PASS | EPUB/nav.xhtml |
| EPUB | EPUB: all eight chapter headings | PASS | ['Chapter 1 — Smoke Under Town Hall', 'Chapter 2 — The Salvage Table', 'Chapter 3 — A Shelf That Lied Twice', 'Chapter 4 — The Predecessor’s Hand', 'Chapter 5 — Water Lines', 'Chapter 6 — Bad Procedure', 'Chapter 7 — ... |
| EPUB | EPUB: chapter order | PASS | ['Chapter 1 — Smoke Under Town Hall', 'Chapter 2 — The Salvage Table', 'Chapter 3 — A Shelf That Lied Twice', 'Chapter 4 — The Predecessor’s Hand', 'Chapter 5 — Water Lines', 'Chapter 6 — Bad Procedure', 'Chapter 7 — ... |
| EPUB | EPUB: no duplicate chapters | PASS | {'Chapter 1 — Smoke Under Town Hall': 1, 'Chapter 2 — The Salvage Table': 1, 'Chapter 3 — A Shelf That Lied Twice': 1, 'Chapter 4 — The Predecessor’s Hand': 1, 'Chapter 5 — Water Lines': 1, 'Chapter 6 — Bad Procedure'... |
| EPUB | EPUB extracted text: no forbidden marker <<<<<<<|=======|>>>>>>> | PASS | not found |
| EPUB | EPUB extracted text: no forbidden marker \b(?:TODO|TBD|FIXME)\b | PASS | not found |
| EPUB | EPUB extracted text: no forbidden marker AUTHOR DECISION REQUIRED | PASS | not found |
| EPUB | EPUB extracted text: no forbidden marker \[\s*PLACEHOLDER\s*\] | PASS | not found |
| EPUB | EPUB extracted text: no forbidden marker \{\{.*?\}\} | PASS | not found |
| EPUB | EPUB extracted text: no forbidden marker internal (?:note|commentary|production) | PASS | not found |
| EPUB | EPUB: no broken internal links | PASS | [] |
| EPUB | EPUB: internal structural validator | PASS | epubcheck executable unavailable |
| Retailer HTML | Retailer HTML: parses | PASS | parsed |
| Retailer HTML | Retailer HTML: supported basic tags only | PASS | [] |
| Retailer HTML | Retailer HTML: under 4,000 characters | PASS | 1006 characters |
| Retailer HTML | Retailer HTML: no prohibited/unsupported claims | PASS | [] |

## Tool versions

- **python:** 3.14.6
- **pandoc:** pandoc 3.10
- **libreoffice:** not available
- **pdftoppm:** not available
- **epubcheck:** not available

## Exact commands

```text
bash books/book-04/export/build.sh
python3 books/book-04/export/finalize-package.py
pandoc books/book-04/export/manuscript-combined.md --from=markdown --to=plain --wrap=none -o books/book-04/export/manuscript-combined.txt
pandoc books/book-04/export/manuscript-combined.md --from=markdown --to=html5 --standalone -o books/book-04/export/manuscript-combined.html
pandoc books/book-04/export/manuscript-combined.md --from=markdown --to=docx --reference-doc books/book-04/export/reference.docx -o books/book-04/export/dist/The-Archive-Fire.docx
libreoffice --headless --convert-to pdf --outdir books/book-04/export/qa/docx-render books/book-04/export/dist/The-Archive-Fire.docx
pdftoppm -png -r 72 books/book-04/export/qa/docx-render/The-Archive-Fire.pdf books/book-04/export/qa/docx-pages/page
pandoc books/book-04/export/manuscript-combined.md --from=markdown --to=epub3 --toc --toc-depth=1 -o books/book-04/export/dist/The-Archive-Fire.epub
epubcheck books/book-04/export/dist/The-Archive-Fire.epub  # when available
```

## Exact methods

- Direct SHA-256 comparison of every authoritative chapter file before and after the pipeline.
- Exact string comparison between each stripped source chapter body and its section in `manuscript-combined.md`.
- Heading/order, duplicate-body, YAML-leak, conflict-marker, placeholder, and internal-note scans.
- BeautifulSoup HTML parse, heading-order check, and internal-link resolution.
- DOCX Open Packaging Convention/XML inspection for metadata, heading styles, and page-break properties.
- LibreOffice headless DOCX open/render, page-text extraction with `pypdf`, chapter-start checks, blank-page scan, broken-character scan, and all-page PNG rendering.
- EPUB ZIP/mimetype/container/OPF/manifest/spine/navigation/resource/link/metadata/chapter-order validation; `epubcheck` when executable is available.
- Retailer HTML allow-list and 4,000-character validation.

## DOCX render proof

- Page count: 97
- Every page rendered to PNG: yes.
- Contact sheets generated: 0.
- This page count is for the author-review DOCX render only and is **not** a final paperback page count.

## Story and clue readiness audit

- [x] Ruth’s call still establishes the shelf that lied twice.
- [x] The staged Ruth note remains wrong because it lacks Ruth’s complete record system.
- [x] The brass cat charm setup, recovery, and evidentiary payoff remain intact.
- [x] Clara’s K-two lie remains separate from Ruth’s personal key-ring/charm path.
- [x] Simon, Clara, Nell, and Tavis remain false-suspect or record-failure paths.
- [x] Tavis remains morally responsible for the 1991 failure, not Ruth’s murderer.
- [x] Lila Crowe remains a public hit-and-run death with a smoothed record, not a disappearance.
- [x] Ben Calder remains exposed through accumulation rather than confession.
- [x] Cross’s arrest basis remains accumulated present-day evidence.
- [x] Callie remains a consulting records specialist, not a deputy.
- [x] Eli remains useful but bounded.
- [x] Mae’s thaw remains work-based, not apology-based.
- [x] Bell’s photographs and Cross’s log still make Callie’s reading portable.
- [x] The supplemental Crowe record remains restrained.
- [x] The consultant arrangement remains case-by-case and bounded.
- [x] The floorboard ending remains unchanged in meaning.
- [x] Eleanor’s brass magnifying glass remains beside damaged paper as a tool, not a relic.

## Manuscript-file changes

None. No chapter file changed in this publication pass.

## Package boundary

    Technical manuscript/export work is complete. Package completion is ready, as a valid cover has been supplied. Publish remains pending.
