# The Challenger — KDP Upload Sheet

## Upload these two files

Use only the files from a fresh, successful `book-03-release-package` workflow artifact produced from the reviewed release commit:

- Ebook manuscript: `The-Challenger.epub`
- Ebook cover: `The-Challenger-cover.jpg`

The standalone cover must match the author-approved production asset:

`books/book-03/package/approved/The-Challenger-cover.jpg`

Approved SHA-256:

`e96585dacae4e7aacb4aaabbec939c9efeac61560216f86fd99feae480ffdbaf`

The approval authority is `books/book-03/package/approved/approved-cover.json`. `validation.json` must report `APPROVED` provenance and identical approved, standalone, and EPUB-embedded cover hashes.

Do not use the superseded generated cover hash `e39da2e0a6102373888302b8d9cd8270d6fa1ebecff1757d00bed007770683e7` or any earlier artifact containing it.

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

Use the primary description, seven keyword phrases, category recommendations, and pricing guidance in `books/book-03/publish/listing.md`.

## Commercial recommendation

- Recommended launch list price: **$2.99**.
- Link the title to **The Blackwood Ridge Mysteries** as **Book 3**.
- Enroll in KDP Select / Kindle Unlimited only if deliberately continuing the Books 1 and 2 exclusivity strategy.
- Choose the release date or preorder date in the retailer dashboard; no date is established by this file.

## Required final platform checks

1. Obtain the validated workflow artifact produced from the reviewed corrective commit.
2. Confirm `validation.json` reports `PASS`, the exact source commit being uploaded, and approved-cover hash `e96585dacae4e7aacb4aaabbec939c9efeac61560216f86fd99feae480ffdbaf`.
3. Confirm the standalone, nested ZIP, and EPUB-embedded cover bytes match.
4. Upload `The-Challenger.epub` and `The-Challenger-cover.jpg`.
5. Open the KDP online previewer or Kindle Previewer.
6. Inspect the cover, title page, copyright page, contents/navigation, all eight chapter starts, scene breaks, italics, ending, and back matter.
7. Confirm the description, keywords, categories, price, territories, DRM choice, and KDP Select choice.
8. Answer the retailer's content-disclosure questions from the actual production history.
9. Submit for publication only after the preview and metadata review pass.

Do not mark `publish: complete` until retailer acceptance and the live detail page are confirmed.
