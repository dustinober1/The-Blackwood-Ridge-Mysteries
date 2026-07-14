---
status: blocked-cover-required
format: ebook-first
target_dimensions: "1600x2560 px (1:1.6)"
series_book: 5
cover_asset_present: false
cover_asset_approved: false
publish_status: pending
platform_requirements_checked: "2026-07-14"
---

# Packaging — The Planted Page

## Package role

This file defines Book 5 cover and ebook-package requirements. It does not authorize a cover design, upload, distribution, submission, or publication.

## Exact blocker

The repository does not contain an approved Book 5 ebook cover at the canonical path:

`books/book-05/cover.jpeg`

The final retailer EPUB, separate upload cover, deterministic upload ZIP, stable release manifest, and permanent `books/book-05/release/` snapshot cannot be completed or validated without that asset.

## Required cover text

- Title: `The Planted Page`
- Author: `Vesper Blythe`
- Series label: `The Blackwood Ridge Mysteries · Book 5`

All three elements must remain legible at approximately 150 px thumbnail width.

## Technical requirements

The repository release pipeline requires the canonical approved upload asset to be:

- JPEG at `books/book-05/cover.jpeg`;
- exactly 1,600 × 2,560 px;
- RGB color mode;
- less than 50 MB;
- minimally compressed, without crop, banding, halo, or visible artifact damage;
- visually bounded if the background is very light.

Official KDP guidance checked on 2026-07-14 accepts JPEG or TIFF, identifies 2,560 × 1,600 px and at least a 1.6:1 height-to-width ratio as ideal, requires RGB, and limits the file to less than 50 MB. The repository narrows this to one canonical JPEG for deterministic cover identity and byte-for-byte EPUB comparison.

## Series-branding requirements

- Elegant serif title treatment in the established gold/cream hierarchy.
- Deep plum or charcoal shadows, aged-ivory paper, restrained winter blue/green, and blue-black ink accents.
- Brass magnifying glass retained as the recurring visual anchor.
- Author name placed and scaled consistently with the existing series covers.
- Quiet, bookish, investigative atmosphere rather than police-procedural, thriller, horror, or cheerful-pastel signals.

## Spoiler-safe Book 5 visual language

Suitable motifs include cream stationery, blue-black handwriting, a current repair ticket, an old judicial notebook, graphite trace, winter light, and the brass glass. Do not depict a body, the murderer, a confession, smothering, sedative tablets, warrant evidence, the hidden document route, or any image that identifies the solution.

## Approval rule

An image is not approved merely because it exists. The author must explicitly identify the final asset as approved, after which the package workflow must validate title/author/series text, Book 5 designation, dimensions, mode, file integrity, thumbnail legibility, crop safety, series consistency, and absence of spoiler-heavy imagery.
