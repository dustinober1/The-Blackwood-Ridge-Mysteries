# Book 3 Final Publication Audit — The Challenger

**Original audit date:** 2026-07-25  
**Approved-cover corrective addendum:** 2026-07-25  
**Repository:** `dustinober1/The-Blackwood-Ridge-Mysteries`  
**Corrective branch:** `agent/book-03-approved-cover-release-repair-20260725`  
**Draft pull request:** `#39`

## Scope

This corrective audit is limited to Book 3 release packaging, approved-cover provenance, the Book 3 workflow, and directly affected readiness records. It does not alter manuscript prose, upload to a retailer, publish or distribute the title, merge the pull request, or begin work on Books 4–8.

## Historical finding corrected

The original final-publication audit treated a generated cover as if mechanical visual validation established author approval. That conclusion was too broad.

The prior generated cover:

- was produced by `books/book-03/package/generate-cover.py`;
- was automatically invoked by the release build;
- passed JPEG/RGB/dimension and standalone/embedded equality checks;
- had SHA-256 `e39da2e0a6102373888302b8d9cd8270d6fa1ebecff1757d00bed007770683e7`;
- was not the later-saved author-approved production asset;
- included unapproved additional cover text.

The earlier workflow and EPUBCheck evidence remains valid as historical mechanical evidence, but its cover-approval conclusion and upload-readiness verdict are superseded.

## Approved-cover authority

The approved source and production assets are:

- `books/book-03/package/approved/The-Challenger-cover-source.png`
- `books/book-03/package/approved/The-Challenger-cover.jpg`

Machine-readable authority:

- `books/book-03/package/approved/approved-cover.json`

Approved production JPEG:

- blob SHA: `eb457e2931e9e1e17a6f194cf1edf61bd55018a8`
- mode: `100644`
- format/mode: JPEG/RGB
- dimensions: 1,600 × 2,560 px
- size: 2,105,356 bytes
- SHA-256: `e96585dacae4e7aacb4aaabbec939c9efeac61560216f86fd99feae480ffdbaf`

Approved source PNG:

- blob SHA: `e9f756511ddbb35d5dbe243ee79b94beaa74c975`
- mode: `100644`
- format/mode: PNG/RGB
- dimensions: 992 × 1,586 px
- size: 2,668,188 bytes
- SHA-256: `5ee78546868a78aeec836ac94f8b8d8027027f6e1b0c0125792d55e297685f62`

## Files inspected

- `.github/workflows/book-03-release-package.yml`
- `books/book-03/package/approved/The-Challenger-cover-source.png`
- `books/book-03/package/approved/The-Challenger-cover.jpg`
- `books/book-03/package/approved/approved-cover.json`
- former `books/book-03/package/generate-cover.py`
- `books/book-03/package/packaging.md`
- `books/book-03/package/package-readiness.md`
- `books/book-03/export/build.sh`
- `books/book-03/export/assemble-retail.py`
- `books/book-03/export/cover_provenance.py`
- `books/book-03/export/create_upload_package.py`
- `books/book-03/export/test_create_upload_package.py`
- `books/book-03/export/test_cover_provenance.py`
- `books/book-03/export/validate-release.py`
- `books/book-03/export/metadata.yaml`
- `books/book-03/export/manuscript-combined.md`
- `books/book-03/publish/listing.md`
- `books/book-03/publish/upload-package.md`
- `books/book-03/publish/publish-readiness.md`
- `books/book-03/publish/final-release-readiness.md`
- `books/book-03/progress.yaml`
- `progress.yaml`

## Corrective changes

- Added an author-readable, machine-verifiable approved-cover record.
- Added fail-closed cover-provenance validation.
- Replaced generated-cover creation with direct copying of the approved JPEG.
- Removed the non-governing programmatic generator.
- Added regression tests for missing, modified, substituted, standalone/embedded-mismatched, nested-package, and active-release-path cover cases.
- Added explicit EPUBCheck version, exit status, and message counts to `validation.json`.
- Recorded the actual corrective branch-head source commit instead of the transient pull-request merge ref.
- Reconciled affected package and publish records without claiming retailer submission or publication.

No manuscript chapter, combined-manuscript source, outline, canon record, or story prose was changed.

## Replacement verification baseline

Workflow run `30183982603` completed successfully from source commit `00840da785c553b1b0658cec406cef1ac7ba27df`.

- Job: `build-and-validate` — success
- Regression tests — success
- Release build and validation — success
- Artifact upload — success
- Artifact: `book-03-release-package`
- Artifact ID: `8626458510`
- Artifact size: 8,662,940 bytes
- Artifact digest: `sha256:a8e8d3bb6705b1072ebe90f6980f11c30b430145ade650668fb972c0ac9ae95e`
- Expiration: 2026-08-25 UTC

## Independent artifact result

The outer artifact contains exactly six required files. The nested upload ZIP contains exactly seven required files. All duplicated files compare byte-for-byte.

`validation.json` reports:

- status `PASS`;
- zero errors;
- source commit `00840da785c553b1b0658cec406cef1ac7ba27df`;
- approved-cover status `APPROVED`;
- approved, standalone, and embedded hash `e96585dacae4e7aacb4aaabbec939c9efeac61560216f86fd99feae480ffdbaf`;
- story word count 24,212;
- retail word count 24,486;
- chapter count 8;
- locked ending occurrence count 1;
- EPUBCheck v4.2.6, exit 0, zero fatals/errors/warnings/infos.

The EPUB declares title `The Challenger`, creator `Vesper Blythe`, language `en-US`, collection `The Blackwood Ridge Mysteries`, and group position `3`. It contains 18 manifest resources, no missing resource, and embedded cover `EPUB/media/The-Challenger-cover.jpg` matching the approved bytes.

## Cover visual result

Full-size and approximately 150-pixel thumbnail inspection confirms:

- correct series line, title, and author;
- no subtitle or tagline;
- no misspelling, malformed letter, clipped typography, border clipping, or visible corruption;
- visible red and blue annotations;
- visible pale marble bookend;
- visible brass magnifying glass;
- visible warm lamp and archival documents/books;
- readable thumbnail hierarchy consistent with the atmospheric Blackwood Ridge series direction.

## Publication status

`books/book-03/progress.yaml` retains `publish: pending`. The root tracker may retain Book 3 as `upload_ready` because the replacement package passes the corrective release gate.

No retailer upload, submission, acceptance, live listing, publication, or distribution was performed. Draft pull request #39 remains unmerged.

## Corrective verdict

**UPLOAD READY**

The next precise action is for the author to review the replacement artifact and approved cover, explicitly authorize draft pull request #39 for merge, merge it deliberately, run one final release workflow from the resulting authoritative `main`, verify the post-merge artifact, and only then proceed to retailer upload and preview.
