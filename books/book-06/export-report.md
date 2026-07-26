# Book 6 Controlled Export Assembly Report

## Dependency and repository baseline

- Repository: `dustinober1/The-Blackwood-Ridge-Mysteries`
- Default branch: `main`
- PR #31: `Proofread Book 6` — merged
- PR #31 source branch: `agent/book-06-controlled-proofreading`
- PR #31 source head: `15ffd86577f2914729f25c0932a97ff2a830be1f`
- PR #31 base: `105634b1dbf41a9c15ab6d2ea3df7d9945c8b264`
- PR #31 merge commit and historical Book 6 source baseline: `d23d2e745ea0a5fda414321b6c82eda427459a87`
- Current validation change-scope merge base: `3f83c731ab54bbd8f2aaf9386b92eea0a18d08f4`
- Historical export branch: `agent/book-06-controlled-export-assembly`

## Verified source manuscript

| Ch. | Title | Words | Git blob | Source SHA-256 | Body SHA-256 | Scene breaks | Final line |
|---:|---|---:|---|---|---|---:|---|
| 1 | The Box at Closing | 3,266 | `c9a12f2305b08b1cf81ea88c1ef49e94e7a453c6` | `6d7af9f360c3bc240854c16b96ca7e2d18309734258a07b0f5e6a7ebeb0f2db7` | `6107ec6397fd77a3eaf3c479b71a30ba38289893418c6ec4063c0fbacf431f70` | 4 | `The ladder had not rolled.` |
| 2 | A Fall That Did Not Fit | 3,135 | `6404737d8d0610908608f7d8ab45c02cd75158fd` | `e0e16d3b3aa900891971d84814d42f8b7ba7a3a1fb02a57e206a55bf2033696d` | `3de8014394f846ed5c1e3491030ef4630c1c62f3196778f969542921f9ca0242` | 4 | `One had been cleaned.` |
| 3 | The Surveyor’s Missing Line | 3,130 | `59575d837b6c51d22d57ff4033e6a09bc218a409` | `0b838ad947dae46b1eef6f68212bb777236e4c3a6657127b7740344327c84ba6` | `8f2c295ed1b0bd38bd98417de38de493b9c1da1c5b2e023555e65bc2ba39fdc4` | 5 | `Sheet 47 had described a public right-of-way through Bellweather river land.` |
| 4 | Marks Made Later | 3,150 | `401d46dad388ddb6ca7df6041c464465a19a48c5` | `44f748cbfcb36b3521eaaa4cc94a64bfbc95a8a28aba643f2a5551a6629dc75c` | `db12bdf780733c20d5d78988d4a6dec7ccdc54b48cd0428d8f0c1722685b510c` | 5 | ``South line retrieval.`` |
| 5 | The Road Through Bellweather | 3,100 | `81fad0335b3781712b38d4d3139d92ffe94b3476` | `cff63950d03b58397d025ad376824d55eeb4a56f4c6940ef875b893ef7fe43d5` | `3f645d5e78dc337fb6e926fbfc494c498300c0e193dfa4fd47865a5fcda0f720` | 6 | `The road through Bellweather did not contain the missing thirty-nine minutes.` |
| 6 | What the Ledger Withheld | 3,279 | `6b43203b07287771b99ef87240955ec31206e996` | `b518c0a1a0ca3e40480b518e28318079f820c4f1c62a7d18500e610e3a2e7b5d` | `007ff17d55e7f0b472ad545329a7cdf65285ef9e3061546029b1bedb60ea1584` | 5 | `It was enough to ask where Dana had put the rest.` |
| 7 | The Weight of the Map | 3,105 | `9ffbb201458d822bafcdf24ffe3b28df283b635a` | `40dc88aa15cd003c637da88360d57322b94a6e8d24e610affc77675080d4bb8a` | `d76355650bf4d1396b718b49abea6710fa77e0340236ce86624594249e4221be` | 5 | `The route field remained blank.` |
| 8 | The Pattern | 3,481 | `be9f1a5531c3a6d61430483b76ed01472d0a03e4` | `f0f88da8dbfbec9d757706ea669f35733f306ed5c3b6d5833eb05045c2d255ce` | `e04723ba1497dcbe7089978a618e22b9fa837d2602b4bd5ef1dc60ea49a1f0b8` | 5 | `Who knew which page she would open next?` |

- Manuscript-prose total: **25,646**
- Chapter order: **1–8**
- Exact Mercer wording preserved: `Found in returned Mercer volume by M. Hartwell; prior loose-paper location not established.`
- POV: single third-person limited through Callie Thorne

## Export conventions discovered

Book 5 establishes `books/book-N/export/` as the controlled export directory; committed combined Markdown, TXT, HTML, readiness/count/validation reports; generated front and back matter; reproducible ignored DOCX/EPUB/manifest/QA outputs; Pandoc conversion; DOCX render validation; EPUBCheck; source-to-format identity comparison; deterministic ZIP timestamps and EPUB identifiers; and explicit exclusion of package, cover, listing, upload, and publication work.

### Book 5 references inspected

- `books/book-05/export/README.md`
- `books/book-05/export/.gitignore`
- `books/book-05/export/assemble-manuscript.py`
- `books/book-05/export/finalize-package.py`
- `books/book-05/export/run-export.py`
- `books/book-05/export/build.sh`
- `.github/workflows/book-05-proof-export.yml`
- `books/book-05/export/manuscript-combined.md`
- `books/book-05/export/manuscript-combined.txt`
- `books/book-05/export/manuscript-combined.html`
- `books/book-05/export/word-count-report.md`
- `books/book-05/export/export-readiness.md`
- `books/book-05/export/validation-report.md`

## Export manifest

| Artifact | Classification | Bytes | SHA-256 |
|---|---|---:|---|
| `manuscript-combined.md` | canonical reader-facing export | 167,821 | `46a4a608c86f98fc7a90de31ceea89d313298a8b2db5d9744c53fe697ae381a0` |
| `manuscript-combined.txt` | canonical reader-facing export | 171,225 | `82f8ee17eb9757abca5dd83ca5b5cd2c4424333bab56bcfcaf22765e94bf11b1` |
| `manuscript-combined.html` | canonical reader-facing export | 181,884 | `b43cd32af3652ecc7b9d2cc9686ce69c2f1d4af8c3e1bde26a7a6bb8d8e76e8a` |
| `The-Pattern.docx` | reproducible review artifact | 90,932 | `cf637051d1880b3a7b5997e7ab49f850ca4d374bbdefdfbad602f2972f51bd2a` |
| `The-Pattern.epub` | reproducible review artifact | 79,223 | `3dc88fa9a2658d2e806d5f21714876ed69ba171b9220b3fb2b7895d1b8d2ad09` |

### Source-to-output mapping

- YAML production front matter: removed from all reader-facing outputs.
- Source chapter headings: mapped to `Chapter N — Title` reader headings.
- Source `***` scene breaks: preserved in canonical Markdown and converted through the established Pandoc pipeline.
- Paragraphs, sentences, words, punctuation, quotation marks, apostrophes, italics, documentary formatting, chapter order, and chapter-final lines: preserved by exact normalized source-to-output comparison.
- Front matter: title page, copyright page, and contents generated from repository-approved title, author, series, book number, and inherited Book 5 convention.
- Back matter: author note, series list through Book 6, and existing author bio convention.

## Counts

- Manuscript prose: **25,646**
- Front/back matter: **257**
- Chapter headings: **48**
- Combined reader-facing count: **25,918**

## Validation and artifact-open results

- Validator command: `python books/book-06/export/run-export.py`
- Checks passed: **293/293**
- Markdown: parsed and source-identical chapter by chapter.
- TXT: opened and source-identical chapter by chapter.
- HTML: parsed as standalone HTML and source-identical chapter by chapter.
- DOCX: opened, structurally checked, rendered to **71 pages**, and reviewed through **4 contact sheets**.
- EPUB: opened, navigation/metadata checked, source-identical chapter by chapter, and EPUBCheck passed.
- Duplicate/missing/truncated content: none detected.
- Hidden control, mission-lock, bible, spoiler, status, or Eli-truth leakage: none detected.
- Complete scope diff at validation time:
- `.github/workflows/book-06-proof-export.yml`
- `books/book-06/export-report.md`
- `books/book-06/export/export-readiness.md`
- `books/book-06/export/finalize-package.py`
- `books/book-06/export/manuscript-combined.html`
- `books/book-06/export/manuscript-combined.md`
- `books/book-06/export/manuscript-combined.txt`
- `books/book-06/export/test_finalize_package_scope.py`
- `books/book-06/export/validation-report.md`
- `books/book-06/export/word-count-report.md`

## Locked story and procedural preservation

- Dana Wren remains Miriam Vale’s murderer.
- Map weight six remains the cumulative weapon.
- Dana does not confess; questioning still stops after counsel invocation.
- Murder proof remains independent of curator identity; murderer-versus-curator separation remains intact.
- Halbrook’s October 8 accidental death remains separate from later concealment and the October 3/6/8/9–12 sequence remains intact.
- Tara’s authenticated alibi and separate misconduct/custody consequences remain intact.
- Graphite, binder, polymer, composition, grade, brand, owner, buyer, writer, pencil, and instrument limits remain non-identifying.
- The three modern routing marks remain separate from Miriam’s triangle.
- Callie remains a bounded consultant; Cross retains legal/procedural authority; Bell and lawful custodians retain custody.
- Mae’s established role and limits remain intact.
- Eli remains unidentified, non-suspicious, and outside original evidence, warrants, searches, laboratories, recovery, remains, and suspect access.

## Lifecycle and neighboring-book status

- Controls updated: `books/book-06/README.md`, `books/book-06/manuscript/README.md`, `books/book-06/progress.yaml`, `books/book-06/outline.md`, and `series-outline.md`.
- Completed revision, line-edit, final-prose-polish, and proofreading records were inspected and intentionally not rewritten.
- Book 5 files changed: **none**.
- Exact Book 5 status: package in progress; publication pending; approved canonical ebook cover remains the blocker; Book 5 is not upload ready.
- Book 7 Chapter 1 exists and is formally accepted at 3,100 manuscript-prose words; it is outside Book 6 export authority, and no Book 7 chapter manuscript changed in this validation scope.
- Exact Book 6 status: controlled revision, line edit, final prose polish, proofreading, and export assembly complete; package, cover, listing, upload, and publication pending; Book 6 is not upload ready.

## Intentionally not created

- cover files or cover approvals
- listing copy or retailer descriptions
- retailer metadata forms or identifiers
- upload ZIPs or platform bundles
- advertising assets
- release packages
- publication or distribution records
- any Book 7 manuscript prose by the Book 6 export workflow

## Blockers and next stage

No blocker remains within controlled export assembly. Package, cover, listing, upload, and publication work remain deliberately deferred. After this export pull request is reviewed and merged, the recommended next stage is **Book 6 controlled package assembly/readiness**.
