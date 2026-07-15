# Book 6 Controlled Export Validation

## Result

- **Local checks:** 234/234 passed
- **Source blobs:** 8/8 exact
- **Controlled manuscript words:** 25,646
- **Reader-facing formats compared:** Markdown, TXT, HTML, DOCX, EPUB
- **Source-to-output chapter identity:** 40/40 chapter-format comparisons passed
- **Locked final-line checks:** 40/40 passed across formats
- **Canonical Markdown scene-break checks:** 8/8 passed; 39/39 breaks preserved
- **DOCX:** opened, parsed, styled, rendered, 71 pages, no blank pages, no replacement glyphs, eight intentional chapter starts, four visual contact sheets
- **EPUB:** ZIP/package, mimetype, container, OPF, title, author, language, spine, navigation, and chapter text passed
- **Forbidden/internal-control leakage:** none detected
- **EPUBCheck:** pending; executable unavailable and the new workflow could not be dispatched through connector-authored commits

## Commands executed

```text
python /mnt/data/book6-export-work/build_validate.py
python /mnt/data/book6-export-work/normalize_artifacts.py
pandoc <combined.md> -f markdown -t plain --wrap=none
pandoc <combined.md> -f markdown -t html5 --standalone
pandoc <combined.md> -f markdown -t docx --reference-doc <reference.docx>
pandoc <epub-source.md> -f markdown -t epub3 --toc --toc-depth=1
libreoffice --headless --convert-to pdf --outdir <qa> The-Pattern.docx
pdftoppm -png -r 90 The-Pattern.pdf <qa/page>
```

## Visual review

All four contact sheets were inspected. No clipping, overlap, missing glyph, accidental blank page, broken chapter heading, lost scene break, malformed footer, or back-matter layout defect was observed.

## Gate disposition

The assembled artifacts are structurally clean and source-identical, but export completion must not be recorded until EPUBCheck/CI passes on the pull-request branch.
