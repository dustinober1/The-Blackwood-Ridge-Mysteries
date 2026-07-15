# Book 6 Controlled Export Assembly Report

## Repository and dependency

- Repository: `dustinober1/The-Blackwood-Ridge-Mysteries`
- Default branch: `main`
- PR #31: `Proofread Book 6` — merged into `main`
- PR #31 source branch: `agent/book-06-controlled-proofreading`
- PR #31 source head: `15ffd86577f2914729f25c0932a97ff2a830be1f`
- PR #31 base: `105634b1dbf41a9c15ab6d2ea3df7d9945c8b264`
- PR #31 merge commit: `d23d2e745ea0a5fda414321b6c82eda427459a87`
- Starting post-PR-#31 `main` HEAD: `d23d2e745ea0a5fda414321b6c82eda427459a87`
- Export branch: `agent/book-06-controlled-export-assembly`
- Export PR: #32 — `Assemble Book 6 export`

## Complete source list

### Controlling manuscript

- `books/book-06/manuscript/ch-01.md`
- `books/book-06/manuscript/ch-02.md`
- `books/book-06/manuscript/ch-03.md`
- `books/book-06/manuscript/ch-04.md`
- `books/book-06/manuscript/ch-05.md`
- `books/book-06/manuscript/ch-06.md`
- `books/book-06/manuscript/ch-07.md`
- `books/book-06/manuscript/ch-08.md`

### Controlling edit and lifecycle records

- `books/book-06/proofreading-report.md`
- `books/book-06/final-prose-polish-report.md`
- `books/book-06/line-edit-report.md`
- `books/book-06/revision-plan.md`
- `books/book-06/README.md`
- `books/book-06/content-notes.md`
- `books/book-06/outline.md`
- `books/book-06/progress.yaml`
- `books/book-06/manuscript/README.md`

### Book 6 bible and continuity controls

- `books/book-06/bible/mystery-solution.md`
- `books/book-06/bible/suspect-matrix.md`
- `books/book-06/bible/clue-ladder.md`
- `books/book-06/bible/story-memory.md`
- `books/book-06/bible/timeline.md`
- `books/book-06/bible/continuity-locks.md`
- `books/book-06/bible/character-arcs.md`
- `books/book-06/bible/carry-forward.md`
- `books/book-06/bible/book-05-to-06-handoff.md`
- `series-outline.md`

### Export convention references

- `books/book-05/export/README.md`
- `books/book-05/export/.gitignore`
- `books/book-05/export/assemble-manuscript.py`
- `books/book-05/export/finalize-package.py`
- `books/book-05/export/run-export.py`
- `books/book-05/export/build.sh`
- `.github/workflows/book-05-proof-export.yml`
- Book 5 combined Markdown/TXT/HTML and export reports
- `books/book-04/export/finalize-package.py`, inherited only as the repository’s shared conversion and validation implementation

## Verified sources

| Ch. | Title | Controlled words | Markdown-aware words | Proofread blob | Breaks | Locked final line |
|---:|---|---:|---:|---|---:|---|
| 1 | The Box at Closing | 3,266 | 3,262 | `c9a12f2305b08b1cf81ea88c1ef49e94e7a453c6` | 4 | `The ladder had not rolled.` |
| 2 | A Fall That Did Not Fit | 3,135 | 3,136 | `6404737d8d0610908608f7d8ab45c02cd75158fd` | 4 | `One had been cleaned.` |
| 3 | The Surveyor’s Missing Line | 3,130 | 3,122 | `59575d837b6c51d22d57ff4033e6a09bc218a409` | 5 | `Sheet 47 had described a public right-of-way through Bellweather river land.` |
| 4 | Marks Made Later | 3,150 | 3,142 | `401d46dad388ddb6ca7df6041c464465a19a48c5` | 5 | `South line retrieval.` |
| 5 | The Road Through Bellweather | 3,100 | 3,104 | `81fad0335b3781712b38d4d3139d92ffe94b3476` | 6 | `The road through Bellweather did not contain the missing thirty-nine minutes.` |
| 6 | What the Ledger Withheld | 3,279 | 3,281 | `6b43203b07287771b99ef87240955ec31206e996` | 5 | `It was enough to ask where Dana had put the rest.` |
| 7 | The Weight of the Map | 3,105 | 3,095 | `9ffbb201458d822bafcdf24ffe3b28df283b635a` | 5 | `The route field remained blank.` |
| 8 | The Pattern | 3,481 | 3,471 | `be9f1a5531c3a6d61430483b76ed01472d0a03e4` | 5 | `Who knew which page she would open next?` |

The eight exact repository chapter blobs were reconstructed only for isolated execution, verified byte-for-byte, and used to generate the artifacts. No uploaded or stale manuscript copy controlled the build.

## Export conventions discovered

Book 5 establishes `books/book-N/export/` as the controlled export directory; committed combined Markdown, TXT, and HTML; generated front and back matter; reproducible DOCX/EPUB, manifest, PDF render, page images, and contact sheets as ignored validation artifacts; Pandoc conversion; LibreOffice render validation; EPUBCheck; checksum records; and explicit exclusion of package, cover, listing, upload, and publication work.

## Source-to-output mapping

- Source YAML front matter → omitted from reader-facing files.
- Source full chapter heading → reader-facing Heading 1 / EPUB navigation entry.
- Source `***` → preserved canonical Markdown break and established conversion in other formats.
- Chapter paragraphs, sentences, words, punctuation, quotation marks, apostrophes, italics, code-formatted documentary text, order, and ending → source-identical after normalized conversion.
- Front matter → title page, copyright, and contents using approved repository truth and Book 5 convention.
- Back matter → author note, Books 1–6 series list, and existing author bio convention.

## Counts

- Controlled manuscript-prose count: **25,646**
- Markdown-aware manuscript-body count: **25,613**
- Front/back matter: **257**
- Chapter headings: **48**
- Combined reader-facing count: **25,918**
- Reconciliation: **25,613 + 257 + 48 = 25,918**

## Artifact manifest

| Format | File | Classification | Bytes | SHA-256 |
|---|---|---|---:|---|
| Markdown | `manuscript-combined.md` | canonical reader-facing export | 167,821 | `46a4a608c86f98fc7a90de31ceea89d313298a8b2db5d9744c53fe697ae381a0` |
| TXT | `manuscript-combined.txt` | canonical reader-facing export | 171,225 | `82f8ee17eb9757abca5dd83ca5b5cd2c4424333bab56bcfcaf22765e94bf11b1` |
| HTML | `manuscript-combined.html` | canonical reader-facing export | 181,943 | `f0235f54163f83ad9c13346a1255f552948e0742676696fb7b4722b23a629463` |
| DOCX | `The-Pattern.docx` | reproducible reader-facing review artifact | 90,956 | `adb45d52f4d41bfa9a86f901e3542772a408964a47f0b89849cfd213037fac94` |
| EPUB | `The-Pattern.epub` | reproducible reader-facing review artifact | 79,206 | `66aa8e30c513fdbf2c5fc28abbf5b774b6dfa42d6d1b7168f5c4d1ae0ff2b420` |
| PDF | `The-Pattern.pdf` | validation artifact | 518,205 | `20de09c88e756cfdeaf5fcbce6fe747fd2bb806050f013021cbdc1dfe3152476` |

The five reader-facing formats, manifest, PDF render, 71 page images, and four contact sheets were created in the isolated controlled build. The branch contains the complete reproducible pipeline, approved matter, and reports. Because connector-authored commits did not dispatch Actions and the connector cannot transfer local binary artifacts, the stable combined Markdown/TXT/HTML and ignored binary/QA outputs await the configured workflow run rather than being falsely reported as branch-integrated.

## Validation

- 234/234 local checks passed.
- All 40 chapter-format identity comparisons passed.
- All 40 cross-format final-line checks passed.
- All 39 canonical scene breaks were preserved.
- No missing, duplicate, or truncated chapter content was detected.
- No YAML, mission lock, bible text, hidden Eli truth, production status, report text, or other internal control leaked.
- DOCX opened, parsed, and rendered to 71 pages; 71 page PNGs and four contact sheets were produced and visually reviewed.
- EPUB opened and passed package/XML/metadata/spine/navigation/source-text checks.
- **EPUBCheck remains pending** because the executable is unavailable in the active runtime and connector-authored commits did not dispatch the newly added workflow. No pass is claimed.

## Story and procedural preservation

- POV and voice remain single third-person limited through Callie Thorne.
- Dana Wren remains Miriam Vale’s murderer.
- Map weight six remains the cumulative weapon; no single class result is independently dispositive.
- Dana does not confess; questioning stops after counsel invocation.
- Murder proof remains independent of curator identity.
- Halbrook’s October 8 accidental death remains separate from later concealment and the October 3/6/8/9–12 chronology remains intact.
- Tara’s authenticated alibi and separate privacy/custody consequences remain intact.
- Graphite, binder, polymer, composition, grade, brand, owner, buyer, writer, pencil, and instrument limits remain non-identifying.
- The three routing marks remain distinct from Miriam’s triangle.
- Callie remains a bounded consultant; Cross retains warrants, interviews, evidence, legal conclusions, and arrest authority; Bell and lawful custodians retain custody.
- Exact Mercer provenance wording remains unchanged.
- Mae’s practical/emotional role remains within established limits.
- Eli remains unidentified, non-suspicious, outside the original evidence and official case authority, and absent from hidden-truth leakage.

## Files created

- `.github/workflows/book-06-proof-export.yml`
- `books/book-06/front-matter/title-page.md`
- `books/book-06/front-matter/copyright.md`
- `books/book-06/front-matter/contents.md`
- `books/book-06/back-matter/author-note.md`
- `books/book-06/back-matter/series.md`
- `books/book-06/back-matter/about-the-author.md`
- `books/book-06/export/.gitignore`
- `books/book-06/export/README.md`
- `books/book-06/export/assemble-manuscript.py`
- `books/book-06/export/finalize-package.py`
- `books/book-06/export/run-export.py`
- `books/book-06/export/build.sh`
- `books/book-06/export/word-count-report.md`
- `books/book-06/export/export-readiness.md`
- `books/book-06/export/validation-report.md`
- `books/book-06/export-report.md`

## Files modified

- `books/book-06/README.md`
- `books/book-06/manuscript/README.md`
- `series-outline.md`

## Controls inspected and intentionally unchanged

- all eight proofread manuscript chapter files;
- `books/book-06/proofreading-report.md`;
- `books/book-06/final-prose-polish-report.md`;
- `books/book-06/line-edit-report.md`;
- `books/book-06/revision-plan.md`;
- `books/book-06/content-notes.md`;
- `books/book-06/outline.md`;
- `books/book-06/progress.yaml`, whose `export_complete: false` remains accurate pending the repository gate;
- all eight chapter mission locks;
- all nine present Book 6 bible files;
- Book 5 files and lifecycle controls;
- Book 7 planning; no prose exists.

## Artifacts intentionally not created

- cover or cover approval files;
- listing copy or retailer descriptions;
- retailer metadata forms, identifiers, prices, or ISBN claims;
- upload ZIPs or retailer/platform bundles;
- advertising assets;
- release packages;
- distribution, submission, upload, or publication records;
- Book 7 prose.

## Scope and neighboring books

- Book 5 changed: none.
- Exact Book 5 status: package in progress, approved canonical ebook cover pending, publication pending, not upload ready.
- Book 7 manuscript directory: absent; no Book 7 prose exists or was created.
- No package, cover, listing, upload, distribution, or publication asset was created or modified.

## Current Book 6 status and blocker

Book 6 has proofread-source export artifacts assembled and independently validated, but controlled export completion is **not yet recorded** because EPUBCheck/CI remains pending. Book 6 is not upload ready. Package, cover, listing, upload, and publication remain pending.

After EPUBCheck/CI passes, the stable generated exports and manifest should be committed by the configured workflow, the lifecycle controls should be synchronized to export complete, and PR #32 should remain open for review. After its eventual merge, the recommended next stage is **Book 6 controlled package assembly/readiness**.
