# Book 3 Package Readiness — The Challenger

**Original package-readiness pass:** 2026-06-30  
**Approved-cover correction:** 2026-07-25  
**Repository:** `dustinober1/The-Blackwood-Ridge-Mysteries`  
**Default branch:** `main`

## Historical package state

The 2026-06-30 pass created Book 3 package guidance, draft retailer listing material, and marked the package stage complete while retaining `publish: pending`. At that time the final cover still required manual production and approval. Those historical facts remain valid.

A later release workflow generated a mechanically valid cover substitute. The substitute was embedded in the EPUB and copied into the upload package, but it was not the author-approved production cover. Its SHA-256 was:

`e39da2e0a6102373888302b8d9cd8270d6fa1ebecff1757d00bed007770683e7`

That hash and every artifact containing it are superseded for upload purposes.

## Corrective package authority

The author-approved assets are now checked in at:

- `books/book-03/package/approved/The-Challenger-cover-source.png`
- `books/book-03/package/approved/The-Challenger-cover.jpg`
- `books/book-03/package/approved/approved-cover.json`

The approved production JPEG is JPEG/RGB, 1,600 × 2,560 px, 2,105,356 bytes, SHA-256:

`e96585dacae4e7aacb4aaabbec939c9efeac61560216f86fd99feae480ffdbaf`

The approval record locks the title, author, series, series number, paths, image properties, exact approved text, and independent checksum.

## Pipeline correction

The active release path now:

1. validates the approval authority before creating output;
2. copies the checked-in approved JPEG directly;
3. embeds those same bytes in the EPUB;
4. copies those bytes into the nested upload ZIP;
5. validates standalone and embedded hashes against the approved hash;
6. records approved-cover provenance in `validation.json`;
7. fails closed for missing, unreadable, malformed, modified, or mismatched cover assets.

The former programmatic generator was removed from the repository. It is not invoked by the build or workflow.

## Regression coverage

The release suite verifies:

- the checked-in approval record matches the approved JPEG;
- a missing approved JPEG fails;
- a modified approved JPEG fails the locked checksum;
- a dimensionally correct substitute fails;
- standalone and EPUB-embedded covers must match the approved bytes;
- the nested upload ZIP preserves the standalone cover bytes;
- the active build and workflow do not invoke the former generator.

## Replacement workflow baseline

- Workflow: `Book 3 release package`
- Run ID: `30183982603`
- Source commit: `00840da785c553b1b0658cec406cef1ac7ba27df`
- Result: `success`
- Artifact: `book-03-release-package`
- Artifact ID: `8626458510`
- Artifact digest: `sha256:a8e8d3bb6705b1072ebe90f6980f11c30b430145ade650668fb972c0ac9ae95e`
- Expiration: 2026-08-25 UTC

The baseline artifact reports `PASS`, 24,212 story words, 24,486 retail words, eight chapters, one locked ending, and EPUBCheck v4.2.6 with zero fatals, errors, warnings, or infos.

## Status

The package stage remains complete. The corrected release package is suitable for upload-readiness verification, but the title has not been uploaded, submitted, accepted, distributed, or published.

`books/book-03/progress.yaml` must continue to state:

```yaml
publish: pending
```
