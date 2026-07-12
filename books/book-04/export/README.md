# Book 4 Export Pipeline

## Authoritative source

- Combined reader-facing Markdown: `manuscript-combined.md`
- Plain text: `manuscript-combined.txt`
- Standalone HTML: `manuscript-combined.html`
- Front matter: `../front-matter/`
- Back matter: `../back-matter/`
- Authoritative prose: `../manuscript/ch-01.md` through `ch-08.md`

## Reproducible build

From the repository root:

```bash
bash books/book-04/export/build.sh
```

Required tools: Python 3, Pandoc, LibreOffice, Poppler (`pdftoppm`), and the Python packages listed by import in `finalize-package.py`. `epubcheck` is used when available; an internal EPUB 3 structural validator always runs.

## Validated toolchain

- **python:** 3.14.6
- **pandoc:** pandoc 3.10
- **libreoffice:** not available
- **pdftoppm:** not available
- **epubcheck:** not available

## Commands executed by the pipeline

```text
python3 books/book-04/export/finalize-package.py
pandoc manuscript-combined.md --from=markdown --to=plain --wrap=none -o manuscript-combined.txt
pandoc manuscript-combined.md --from=markdown --to=html5 --standalone -o manuscript-combined.html
pandoc manuscript-combined.md --from=markdown --to=docx --reference-doc reference.docx -o dist/The-Archive-Fire.docx
libreoffice --headless --convert-to pdf --outdir qa/docx-render dist/The-Archive-Fire.docx
pdftoppm -png -r 72 qa/docx-render/The-Archive-Fire.pdf qa/docx-pages/page
pandoc manuscript-combined.md --from=markdown --to=epub3 --toc --toc-depth=1 -o dist/The-Archive-Fire.epub
epubcheck dist/The-Archive-Fire.epub  # when available
```

## Build outputs

The pipeline generates:

- `manuscript-combined.md`
- `manuscript-combined.txt`
- `manuscript-combined.html`
- `dist/The-Archive-Fire.docx`
- `dist/The-Archive-Fire.epub`
- temporary DOCX render-proof pages and contact sheets under `qa/`

Binary and visual-QA outputs are intentionally excluded from Git by `export/.gitignore`, matching the repository’s established source-first export convention. Their exact sizes and SHA-256 hashes are committed in `artifact-manifest.json` and `word-count-report.md`.

## Publication status

Export is technically complete and reproducible. The book has not been uploaded or published. The overall package remains incomplete until a valid cover is supplied and author-controlled retailer decisions are made.
