# The Challenger — KDP Upload Sheet

## Upload these two files

- Ebook manuscript: `The-Challenger.epub`
- Ebook cover: `The-Challenger-cover.jpg`

Both are generated together by `books/book-03/export/build.sh` and must pass `books/book-03/export/validate-release.py` before the package ZIP is accepted.

## Book details

| Field | Enter |
|---|---|
| Title | The Challenger |
| Subtitle | None approved; leave blank |
| Series | The Blackwood Ridge Mysteries |
| Series number | 3 |
| Author | Vesper Blythe |
| Language | English |
| Edition | First digital edition |
| Publication date | Not set in repository; choose deliberately in the retailer dashboard |
| ISBN | Leave blank unless deliberately assigning one; do not invent an ISBN |
| Primary marketplace | Use the same marketplace as Books 1 and 2 |
| Publishing rights | Select only territories for which the author controls digital rights |
| Territorial rights | Author confirmation required at upload time |
| DRM | Recommendation: use the same policy as Books 1 and 2; author decision required |

Use the primary description, seven keyword phrases, and category recommendations in `books/book-03/publish/listing.md`.

## Commercial recommendation

- Recommended launch list price: **$2.99**.
- Link the title to **The Blackwood Ridge Mysteries** as **Book 3**.
- Enroll in KDP Select / Kindle Unlimited only if deliberately continuing the Books 1 and 2 exclusivity strategy.
- Choose the release date or preorder date in the retailer dashboard; no date is established by this file.

## Required final platform checks

1. Obtain the validated workflow artifact produced from the reviewed release commit.
2. Confirm its manifest reports `PASS` and matches the commit being uploaded.
3. Upload `The-Challenger.epub` and `The-Challenger-cover.jpg`.
4. Open the KDP online previewer or Kindle Previewer.
5. Inspect the title page, copyright page, contents/navigation, all eight chapter starts, scene breaks, italics, ending, and back matter.
6. Confirm the cover is legible at thumbnail size and is not cropped.
7. Confirm the description, keywords, categories, price, territories, DRM choice, and KDP Select choice.
8. Answer the retailer's content-disclosure questions from the actual production history.
9. Submit for publication only after the preview and metadata review pass.

Do not mark `publish: complete` in the repository until retailer acceptance and the live detail page are confirmed.
