---
status: blocked-cover-required
format: ebook-first
target_dimensions: "1600x2560 px (1:1.6)"
series_book: 6
cover_asset_present: false
cover_asset_approved: false
cover_approval_record: "books/book-06/package/cover-approval.json"
publish_status: pending
platform_requirements_checked: "2026-07-26"
---

# Packaging — The Pattern

## Package role

This file defines Book 6 cover and ebook-package requirements. It does not authorize a cover design, upload, distribution, submission, or publication.

## Exact blocker

The repository does not contain an approved Book 6 ebook cover at the canonical path:

`books/book-06/cover.jpeg`

The explicit approval record at `books/book-06/package/cover-approval.json` remains `pending`. The final retailer EPUB, separate upload cover, deterministic upload ZIP, stable release manifest, and permanent `books/book-06/release/` snapshot cannot be completed or validated until the cover exists and its exact SHA-256 is recorded as approved.

## Required cover text

- Title: `The Pattern`
- Author: `Vesper Blythe`
- Series label: `The Blackwood Ridge Mysteries · Book 6`

All three elements must remain legible at approximately 150 px thumbnail width.

## Technical requirements

The repository release pipeline requires the canonical approved upload asset to be:

- JPEG at `books/book-06/cover.jpeg`;
- exactly 1,600 × 2,560 px;
- RGB color mode;
- less than 50 MB;
- minimally compressed, without crop, banding, halo, or visible artifact damage;
- visually bounded if the background is very light.

Official KDP guidance checked on 2026-07-26 accepts JPEG or TIFF, identifies 2,560 × 1,600 px and at least a 1.6:1 height-to-width ratio as ideal, requires RGB, and limits the file to less than 50 MB. The repository narrows this to one canonical JPEG for deterministic cover identity and byte-for-byte EPUB comparison.

## Series-branding requirements

- Elegant serif title treatment in the established gold/cream hierarchy.
- Deep plum or charcoal shadows, aged-ivory paper, restrained winter blue/green, and blue-black ink accents.
- Brass magnifying glass retained as the recurring visual anchor.
- Author name placed and scaled consistently with the existing series covers.
- Quiet, bookish, investigative atmosphere rather than police-procedural, thriller, horror, or cheerful-pastel signals.

## Spoiler-safe Book 6 visual language

Suitable motifs include brass map weights, aged county survey sheets and ledgers, an old Grange map-room window, graphite pencil marks on historical paper, river fog, and spring Virginia light, alongside the brass magnifying glass. Do not depict a body, the murderer, the map weight as a weapon, a confession, warrant evidence, the hidden curation route, or any image that identifies the solution.

## Approval rule

An image is not approved merely because it exists. After the author explicitly approves the final asset, `cover-approval.json` must record:

- `status: approved`;
- the canonical cover path;
- the approving name;
- the approval date;
- the exact SHA-256 of the approved file.

The workflow independently recomputes the cover hash and refuses the release build if the file and approval record differ. Visual review must also confirm title/author/series text, Book 6 designation, thumbnail legibility, crop safety, series consistency, and absence of spoiler-heavy imagery.
