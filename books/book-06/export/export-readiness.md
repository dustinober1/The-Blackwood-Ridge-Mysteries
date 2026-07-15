# Book 6 Controlled Export Readiness

## Current status

**The deterministic Book 6 export has been reproduced locally from the eight immutable repository chapter blobs and passed a real W3C EPUBCheck 5.1.0 validation. The one evidenced export-code defect—missing author metadata in standalone HTML—has been repaired. The repository Actions job still fails before step execution, so the repository CI gate and stable generated-output integration remain pending.**

Book 6 is not upload ready and is not published. `export_complete: false` remains correct.

## Completed and verified in the repair pass

- PR #32 source head `7740fcf4daa1888e0d4f40172d65785718ee5957` and merge commit `0f863d07bc6bef26d3804f5907775705c1012fa4` were verified.
- All eight chapter Git blobs match the locked proofreading baseline exactly.
- The controlled manuscript remains 25,646 words; the assembled reader-facing count is 25,918.
- All eight chapter titles, all eight locked final lines, and all 39 scene breaks are preserved.
- Markdown, TXT, HTML, DOCX, and EPUB chapter text remained source-identical with no missing, duplicate, truncated, or reordered prose.
- YAML, internal controls, and hidden Eli truth did not leak.
- DOCX opened and rendered to 71 pages; all 71 page images and four contact sheets passed visual review.
- EPUB package structure, metadata, manifest, spine, navigation, source text, and mimetype passed.
- W3C EPUBCheck 5.1.0 reported 0 fatals, 0 errors, 0 warnings, and 0 infos; exit status 0.
- Markdown, TXT, HTML, DOCX, and EPUB checksums reproduce the values recorded in PR #32.
- The validation PDF remains build-specific; page count, extracted text, layout, and byte size remained stable while its checksum changed with LibreOffice metadata.

## Evidenced code repair

`books/book-06/export/run-export.py` now restores the approved standalone-HTML author metadata before checksums and reports are written. Without that metadata, the merged script produced SHA-256 `0c86fd0310011d7007ddc7ff15d04eb91b4bcdbd23af59b18c8f2750a5089bb2`; with the repair it reproduces the PR #32 checksum `f0235f54163f83ad9c13346a1255f552948e0742676696fb7b4722b23a629463`.

## Remaining repository gate

GitHub Actions run `29432890902` originally created job `87412089696`, which failed with zero recorded steps, no downloadable log, and no artifacts. A repair-session failed-job rerun created job `87450211413`; it again failed with zero recorded steps, no downloadable log, and no artifacts. GitHub exposes no supported root cause, so none is asserted.

The stable combined Markdown, TXT, and HTML files were freshly generated and checksum-verified locally but remain pending repository integration until the repair branch can accept those generated files or a workflow run reaches its commit step. The DOCX, EPUB, manifest, PDF render, page images, and contact sheets remain ignored review artifacts under repository convention.

## Production boundary

No package, cover, listing copy, retailer metadata form, upload bundle, advertising asset, distribution action, or publication record was created. The immediate next production action is to resolve or outlast the external pre-step Actions blocker, integrate the stable combined exports, pass the repository workflow, review this repair PR, and merge it. **Book 6 controlled package assembly/readiness begins only after that merge.**
