# Book 5 Package-Readiness Validation

- Status: **blocked**
- Checks passed: **12/13**
- Publication status: **pending; not published**

## Checks

- [x] Retailer description exists — `books/book-05/listing/retailer-description.html`
- [x] Retailer description is within 4,000 characters — 1,340 characters including HTML
- [x] Retailer description uses supported basic HTML — `b`, `em`, and `p`
- [x] Exactly seven keyword phrases — 7 unique phrases
- [x] Accepted word counts retained — 25,174 manuscript / 25,501 reader-facing
- [x] Accepted proof/export validation retained — 207/207
- [x] Combined reader-facing manuscript exists — `books/book-05/export/manuscript-combined.md`
- [x] Eight locked chapter headings remain in order — Chapters 1–8 match the accepted sequence
- [x] Locked final line appears exactly once — `She closed the file.`
- [x] Exact provenance appears once — `Found in returned Mercer volume by M. Hartwell; prior loose-paper location not established.`
- [x] Combined manuscript contains no internal markers — clean
- [x] Accepted export EPUBCheck remains clean — 0 fatals / 0 errors / 0 warnings / 0 infos
- [ ] Approved ebook cover passes technical and approval gates — cover missing; `cover-approval.json` remains pending

## Blocker

- Missing or unapproved ebook cover: supply `books/book-05/cover.jpeg` as JPEG/RGB/1,600×2,560/under 50 MB, then record explicit author approval and the matching SHA-256 in `books/book-05/package/cover-approval.json`.

No final cover-embedded EPUB, upload cover, upload ZIP, release manifest, final package hashes, or permanent release snapshot was generated. This report does not mark the book upload ready, uploaded, accepted, distributed, or published.
