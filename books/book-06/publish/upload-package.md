# The Pattern — Retailer Upload Worksheet

**Current state:** Package blocked by missing or unapproved cover. Do not upload yet.

## Files that will be uploaded after the cover gate passes

- Ebook manuscript: `The-Pattern.epub`
- Ebook cover: `The-Pattern-cover.jpg`

The release workflow must mechanically validate both, confirm the embedded EPUB cover is byte-for-byte identical to the separate upload cover, pass EPUBCheck with zero errors and warnings, and create the deterministic upload ZIP before this worksheet can be treated as final upload support.

## Book details

| Field | Enter |
|---|---|
| Title | The Pattern |
| Series | The Blackwood Ridge Mysteries |
| Series number | 6 |
| Author | Vesper Blythe |
| Language | English (`en-US`) |
| Edition | First digital edition; release date not yet selected |
| Primary audience | Adult |
| ISBN | Author decision; no ebook ISBN has been assigned in the repository |
| Primary marketplace | Author decision |
| Publishing rights / territories | Author decision; select only territories controlled by the author |
| Release or preorder date | Author decision |
| Ebook price | Author decision |
| DRM | Author decision |
| Exclusivity / KDP Select | Author decision |
| Publisher / imprint | Author decision, if used |

Use the full description, seven keyword phrases, category recommendations, clean-content positioning, and advisory in `books/book-06/listing/listing-copy.md`.

## Seven keyword phrases

1. `historical records mystery`
2. `small town Virginia mystery`
3. `antiquarian bookshop sleuth`
4. `clean mystery novella`
5. `female amateur sleuth`
6. `cold case mystery`
7. `atmospheric small town mystery`

## Category recommendations

- FICTION / Mystery & Detective / Cozy / General
- FICTION / Mystery & Detective / Amateur Sleuth
- FICTION / Mystery & Detective / Women Sleuths

Select the closest currently available retailer categories; dashboard labels may differ from BISAC wording.

## Final platform checks after the package exists

1. Upload the validated EPUB and separate cover image.
2. Open the retailer previewer or Kindle Previewer.
3. Inspect the cover, title/copyright material, navigation, all eight chapter starts, scene breaks, italics, final pages, and back matter.
4. Confirm exactly one reader-facing title page.
5. Confirm the cover is legible at thumbnail size and is not cropped.
6. Confirm the description, keywords, categories, price, territories, DRM, exclusivity, and release timing.
7. Answer the platform's content-disclosure questions from the actual production history.
8. Submit only after all fields are correct.

Do not mark `publish: complete` until retailer acceptance and the live detail page are confirmed.
