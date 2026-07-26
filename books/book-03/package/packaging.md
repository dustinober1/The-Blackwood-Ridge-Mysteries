---
status: complete
format: ebook
target_dimensions: "1600x2560 px (1:1.6)"
series_book: 3
approved_cover_record: "approved/approved-cover.json"
approved_cover: "approved/The-Challenger-cover.jpg"
---

# Packaging — The Challenger

## Governing production assets

The author-approved Book 3 cover is:

`books/book-03/package/approved/The-Challenger-cover.jpg`

Its editable/source image is:

`books/book-03/package/approved/The-Challenger-cover-source.png`

The machine-readable approval authority is:

`books/book-03/package/approved/approved-cover.json`

The production JPEG is the sole governing cover for the standalone retailer upload, EPUB embedding, nested upload ZIP, release validation, and deterministic release checksums.

## Locked approved text

The cover contains only:

1. `THE BLACKWOOD RIDGE MYSTERIES · BOOK 3`
2. `THE CHALLENGER`
3. `VESPER BLYTHE`

No subtitle, tagline, alternate series label, or additional marketing line is approved for the cover.

## Approved production specification

| Field | Locked value |
|---|---|
| Format | JPEG |
| Color mode | RGB |
| Dimensions | 1,600 × 2,560 px |
| Aspect ratio | 1:1.6 |
| Size | 2,105,356 bytes |
| SHA-256 | `e96585dacae4e7aacb4aaabbec939c9efeac61560216f86fd99feae480ffdbaf` |

The source PNG is RGB, 992 × 1,586 px, 2,668,188 bytes, SHA-256 `5ee78546868a78aeec836ac94f8b8d8027027f6e1b0c0125792d55e297685f62`.

## Approved design

The approved cover preserves the Blackwood Ridge series direction:

- deep plum and charcoal atmospheric background;
- tarnished-gold ornamental frame and typography;
- antique archive books and documents;
- warm brass reading lamp;
- red and blue manuscript annotations;
- brass magnifying glass;
- pale marble bookend;
- strong title/author/series hierarchy at approximately 150-pixel thumbnail width.

## Release-pipeline rule

`books/book-03/export/build.sh` copies the checked-in approved JPEG directly. The retired programmatic generator has been removed and may not be substituted when the approved asset is absent or invalid.

The release fails closed when the approved asset or authority record is missing, unreadable, malformed, dimensionally invalid, checksum-invalid, or different from either the standalone release cover or the EPUB-embedded cover.

## Historical correction

The release artifact produced before this correction used a programmatically generated substitute with SHA-256 `e39da2e0a6102373888302b8d9cd8270d6fa1ebecff1757d00bed007770683e7`. That image passed mechanical size and embedding checks but was not the author-approved production cover and included unapproved additional text. It is superseded and must not be uploaded.

## Package status

The approved-cover integration passed the replacement release workflow baseline on run `30183982603`, source commit `00840da785c553b1b0658cec406cef1ac7ba27df`, with artifact `8626458510`.

This package record does not upload, submit, publish, or distribute the title. `publish: pending` remains required.
