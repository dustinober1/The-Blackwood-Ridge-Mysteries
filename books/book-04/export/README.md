# Book 4 Export and Release Pipeline

## Authoritative source

- Combined reader-facing Markdown: `manuscript-combined.md`
- Plain text: `manuscript-combined.txt`
- Standalone HTML: `manuscript-combined.html`
- Front matter: `../front-matter/`
- Back matter: `../back-matter/`
- Authoritative prose: `../manuscript/ch-01.md` through `ch-08.md`
- Final ebook cover: `../cover.jpeg`

## Reproducible technical build

From the repository root:

```bash
bash books/book-04/export/build.sh
```

This runs the established manuscript, DOCX, EPUB, metadata, and preservation validation pipeline.

## Reproducible retailer release build

From the repository root:

```bash
python3 books/book-04/export/release-package.py
```

The release layer reruns the technical build, validates the 1,600 × 2,560 RGB JPEG cover, rebuilds the EPUB without a duplicate automatic title page, runs internal EPUB validation and EPUBCheck when installed, verifies that the embedded cover matches the separate upload cover, and creates the final upload ZIP.

## Release outputs

Generated under `export/dist/`:

- `The-Archive-Fire.epub`
- `The-Archive-Fire-cover.jpg`
- `The-Archive-Fire.docx`
- `The-Archive-Fire-upload-package.zip`
- `release-manifest.json`
- `release-validation.md`

The ZIP also includes the listing copy, HTML and plain-text retailer descriptions, and KDP upload sheet.

Generated binary and visual-QA outputs are excluded from Git by `export/.gitignore`. GitHub Actions publishes them as the `book-04-release-package` artifact.

## Publication status

Export and ebook packaging are technically complete and reproducible. The book has not been uploaded or published; retailer-controlled release choices remain. Keep `publish: pending` until retailer acceptance and a live detail page are confirmed.
