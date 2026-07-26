# Book 6 Author Decision Checklist

These decisions are intentionally unresolved. None blocks preparation of metadata or tooling, but the approved cover blocks the final ebook package and upload-ready status.

## Required package blocker

- [ ] Supply the final ebook cover at `books/book-06/cover.jpeg`.
- [ ] Explicitly approve that exact cover.
- [ ] Confirm the title, author, series label, and Book 6 designation at thumbnail size.
- [ ] Confirm the cover contains no spoiler-heavy or contradictory imagery.
- [ ] Record the approval name, approval date, and exact cover SHA-256 in `books/book-06/package/cover-approval.json`.
- [ ] Run the release workflow and confirm the approval hash matches the canonical cover byte for byte.

## Retailer-controlled decisions

- [ ] Release now, schedule a release, or set a preorder date.
- [ ] Ebook list price.
- [ ] Primary marketplace.
- [ ] Territorial rights selection.
- [ ] DRM choice.
- [ ] KDP Select / Kindle Unlimited or other exclusivity choice.
- [ ] Ebook ISBN choice, if any.
- [ ] Publisher or imprint field, if any.
- [ ] Final retailer categories from the currently available dashboard labels.
- [ ] Platform content-disclosure answers based on the actual production history.

## Optional print decisions

No print package has been created. A print edition requires separate decisions for trim size, paper, ink, bleed, interior PDF, ISBN, barcode, list price, and full-wrap cover dimensions based on the final page count.

## Publication boundary

Do not mark `publish: complete`, `published`, `live`, or `retailer accepted` until the author has submitted the book, the retailer has accepted it, and the live detail page has been confirmed.
