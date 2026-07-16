# Book 6 Controlled Export Validation

## Result

- **Previously recorded full local export checks:** 234/234 passed
- **Previously recorded post-normalization checks:** 23/23 passed
- **Repair reproduction focused checks:** 65/65 passed
- **Source blobs:** 8/8 exact
- **Controlled manuscript words:** 25,646
- **Combined reader-facing words:** 25,918
- **Reader-facing formats compared:** Markdown, TXT, HTML, DOCX, EPUB
- **Source-to-output chapter identity:** 40/40 chapter-format comparisons passed
- **Locked final-line checks:** 40/40 passed across formats
- **Canonical Markdown scene-break checks:** 8/8 passed; 39/39 breaks preserved
- **DOCX:** opened, parsed, styled, rendered to 71 pages, no blank pages, no replacement glyphs, eight intentional chapter starts, 71 page images, four visually reviewed contact sheets
- **EPUB:** ZIP/package, mimetype, container, OPF, title, author, language, spine, navigation, links, and chapter text passed
- **EPUBCheck:** W3C EPUBCheck 5.1.0; 0 fatals, 0 errors, 0 warnings, 0 infos; exit status 0
- **Forbidden/internal-control leakage:** none detected
- **Repository CI:** pending; original job `87412089696` and rerun job `87450211413` both failed before any step executed and exposed no downloadable log or artifacts

## Commands executed

```text
python local_reproduce.py
pandoc manuscript-combined.md -f markdown -t plain --wrap=none -o manuscript-combined.txt
pandoc manuscript-combined.md -f markdown -t html5 --standalone -M pagetitle="The Pattern" -M author="Vesper Blythe" -M lang=en-US -o manuscript-combined.html
pandoc manuscript-combined.md -f markdown -t docx --reference-doc reference.docx -o dist/The-Pattern.docx
pandoc dist/epub-source.md -f markdown -t epub3 --toc --toc-depth=1 -M title="The Pattern" -M author="Vesper Blythe" -M lang=en-US -o dist/The-Pattern.epub
libreoffice --headless --convert-to pdf --outdir qa/docx-render dist/The-Pattern.docx
pdftoppm -png -r 72 qa/docx-render/The-Pattern.pdf qa/docx-pages/page
java -jar /tmp/epubvenv/lib/python3.13/site-packages/epubcheck/epubcheck.jar books/book-06/export/dist/The-Pattern.epub
```

EPUBCheck output:

```text
Validating using EPUB version 3.3 rules.
No errors or warnings detected.
Messages: 0 fatals / 0 errors / 0 warnings / 0 infos

EPUBCheck completed
EXIT_STATUS=0
```

## Deterministic checksum comparison

| Artifact | Repair build SHA-256 | PR #32 recorded SHA-256 | Result |
|---|---|---|---|
| Markdown | `46a4a608c86f98fc7a90de31ceea89d313298a8b2db5d9744c53fe697ae381a0` | same | exact |
| TXT | `82f8ee17eb9757abca5dd83ca5b5cd2c4424333bab56bcfcaf22765e94bf11b1` | same | exact |
| HTML | `f0235f54163f83ad9c13346a1255f552948e0742676696fb7b4722b23a629463` | same | exact after evidenced author-metadata repair |
| DOCX | `adb45d52f4d41bfa9a86f901e3542772a408964a47f0b89849cfd213037fac94` | same | exact |
| EPUB | `66aa8e30c513fdbf2c5fc28abbf5b774b6dfa42d6d1b7168f5c4d1ae0ff2b420` | same | exact |
| PDF render | `8e681aba4789913418f339c3e72d3c543f4c272987fbb9d092eefcdc4d8b4e96` | `457da9c58920921a890a53e1db954617a3ce0a6adf00f51f0f1061262369eeb6` | justified build-specific difference; 518,205 bytes and 71 pages remained stable |

## Visual review

All four contact sheets were inspected. No clipping, overlap, missing glyph, accidental blank page, broken chapter heading, lost scene break, malformed footer, or back-matter layout defect was observed.

## Gate disposition

The deterministic export and real EPUBCheck pass locally. The stable combined files were generated and checksum-verified, but the repository Actions job has still not reached its first workflow step. Therefore the repository CI gate, stable generated-output integration, and `export_complete: true` lifecycle transition remain pending. No cause beyond the observed pre-step Actions failure is asserted.
