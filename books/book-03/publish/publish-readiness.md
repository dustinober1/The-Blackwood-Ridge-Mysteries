# Book 3 Publish Readiness — The Challenger

**Original upload-preparation pass:** 2026-06-30  
**Approved-cover correction:** 2026-07-25  
**Release state:** **UPLOAD READY — NOT YET PUBLISHED**

## Governing metadata

| Field | Value |
|---|---|
| Title | The Challenger |
| Author | Vesper Blythe |
| Series | The Blackwood Ridge Mysteries |
| Series number | 3 |
| Story words | 24,212 |
| Retail-package words | 24,486 |
| Chapters | 8 |
| Locked ending | `She did not need the bell to ring before she began.` |
| Publish state | `pending` |

## Cover-approval correction

The earlier release package mechanically validated a programmatically generated cover substitute. That substitute was not the author-approved production cover and must not be uploaded. Its SHA-256 was:

`e39da2e0a6102373888302b8d9cd8270d6fa1ebecff1757d00bed007770683e7`

The governing author-approved cover is now:

`books/book-03/package/approved/The-Challenger-cover.jpg`

Approved SHA-256:

`e96585dacae4e7aacb4aaabbec939c9efeac61560216f86fd99feae480ffdbaf`

The human-readable and machine-readable approval sources are:

- `books/book-03/package/approved/The-Challenger-cover-source.png`
- `books/book-03/package/approved/approved-cover.json`

The approved cover contains only the series line, title, and author name. It includes no subtitle or tagline.

## Release gate

The corrected pipeline now fails closed unless:

- the checked-in approval record reports `APPROVED`;
- the approved JPEG exists and matches its locked checksum, size, format, mode, and dimensions;
- the standalone release cover matches the approved JPEG;
- the EPUB-embedded cover matches the approved JPEG;
- the nested upload ZIP contains the standalone cover bytes;
- the former generated substitute is not invoked by the active build or workflow.

## Replacement verification baseline

Workflow run `30183982603`, source commit `00840da785c553b1b0658cec406cef1ac7ba27df`, completed successfully and produced artifact `8626458510`.

The downloaded artifact independently verified:

- `validation.json`: `PASS`, no errors;
- approved, standalone, nested, and embedded cover SHA-256: `e96585dacae4e7aacb4aaabbec939c9efeac61560216f86fd99feae480ffdbaf`;
- EPUBCheck v4.2.6: zero fatals, zero errors, zero warnings, zero infos, exit status zero;
- story words: 24,212;
- retail words: 24,486;
- chapter count: 8;
- locked ending: exactly once;
- correct title, author, language, series, and series-position metadata;
- no missing EPUB manifest resources;
- identical duplicated files between the outer artifact and nested upload ZIP.

The retail-manuscript SHA-256 remains `4ba88471787e6719995b81535ec10e900844e3b0540e2ed221adb395bc09352d`, matching the previously verified retail output. No manuscript source file is changed by this corrective pull request.

## Retailer materials

The canonical listing at `books/book-03/publish/listing.md` supplies:

- primary and mobile descriptions;
- seven keyword phrases;
- three category recommendations;
- content advisory;
- $2.99 launch-price recommendation;
- explicit instruction to leave the subtitle blank.

## Remaining author-controlled actions

The repository has not performed a retailer upload or publication action. The author must deliberately choose the release date, territories, DRM, KDP Select/Kindle Unlimited treatment, preview the replacement EPUB and approved cover, and authorize submission.

Until retailer acceptance and a live detail page are confirmed:

```yaml
publish: pending
```
