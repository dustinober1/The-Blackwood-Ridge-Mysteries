# Book 6 Word-Count and Export Report

- **Book:** The Pattern
- **Author:** Vesper Blythe
- **Series:** The Blackwood Ridge Mysteries — Book 6
- **Controlled proofread manuscript-prose count:** **25,646**
- **Repository Markdown-aware manuscript-body count:** **25,613**
- **Front/back-matter count:** **257**
- **Chapter-heading count:** **48**
- **Combined reader-facing count:** **25,918**
- **Reconciliation:** 25,613 + 257 + 48 = 25,918
- **Chapters:** **8**
- **Scene breaks:** **39**
- **DOCX render:** **71 pages**
- **Page images:** **71**
- **Contact sheets:** **4**
- **EPUBCheck:** W3C 5.1.0; 0 fatals, 0 errors, 0 warnings, 0 infos; exit 0

The controlled source count is the accepted whitespace-delimited chapter count locked by the post-PR-#31 chapter metadata and exact Git blobs. The repository-standard Markdown-aware counter treats Markdown and documentary punctuation differently; its source subtotal is shown so the combined reader-facing count reconciles exactly.

## Chapter counts and controls

| Ch. | Title | Controlled words | Markdown-aware words | Source blob | Scene breaks | Locked final line |
|---:|---|---:|---:|---|---:|---|
| 1 | The Box at Closing | 3,266 | 3,262 | `c9a12f2305b08b1cf81ea88c1ef49e94e7a453c6` | 4 | `The ladder had not rolled.` |
| 2 | A Fall That Did Not Fit | 3,135 | 3,136 | `6404737d8d0610908608f7d8ab45c02cd75158fd` | 4 | `One had been cleaned.` |
| 3 | The Surveyor’s Missing Line | 3,130 | 3,122 | `59575d837b6c51d22d57ff4033e6a09bc218a409` | 5 | `Sheet 47 had described a public right-of-way through Bellweather river land.` |
| 4 | Marks Made Later | 3,150 | 3,142 | `401d46dad388ddb6ca7df6041c464465a19a48c5` | 5 | `South line retrieval.` |
| 5 | The Road Through Bellweather | 3,100 | 3,104 | `81fad0335b3781712b38d4d3139d92ffe94b3476` | 6 | `The road through Bellweather did not contain the missing thirty-nine minutes.` |
| 6 | What the Ledger Withheld | 3,279 | 3,281 | `6b43203b07287771b99ef87240955ec31206e996` | 5 | `It was enough to ask where Dana had put the rest.` |
| 7 | The Weight of the Map | 3,105 | 3,095 | `9ffbb201458d822bafcdf24ffe3b28df283b635a` | 5 | `The route field remained blank.` |
| 8 | The Pattern | 3,481 | 3,471 | `be9f1a5531c3a6d61430483b76ed01472d0a03e4` | 5 | `Who knew which page she would open next?` |

## Artifact checksums

| Format | File | Classification | Bytes | SHA-256 |
|---|---|---|---:|---|
| Markdown | `manuscript-combined.md` | canonical reader-facing export; generated locally, repository integration pending | 167,821 | `46a4a608c86f98fc7a90de31ceea89d313298a8b2db5d9744c53fe697ae381a0` |
| TXT | `manuscript-combined.txt` | canonical reader-facing export; generated locally, repository integration pending | 171,225 | `82f8ee17eb9757abca5dd83ca5b5cd2c4424333bab56bcfcaf22765e94bf11b1` |
| HTML | `manuscript-combined.html` | canonical reader-facing export; generated locally, repository integration pending | 181,943 | `f0235f54163f83ad9c13346a1255f552948e0742676696fb7b4722b23a629463` |
| DOCX | `The-Pattern.docx` | reproducible reader-facing review artifact | 90,956 | `adb45d52f4d41bfa9a86f901e3542772a408964a47f0b89849cfd213037fac94` |
| EPUB | `The-Pattern.epub` | reproducible reader-facing review artifact | 79,206 | `66aa8e30c513fdbf2c5fc28abbf5b774b6dfa42d6d1b7168f5c4d1ae0ff2b420` |
| PDF | `The-Pattern.pdf` | build-specific validation artifact | 518,205 | `8e681aba4789913418f339c3e72d3c543f4c272987fbb9d092eefcdc4d8b4e96` |

The first five reader-facing artifact checksums reproduce PR #32 exactly. The PDF render checksum is build-specific because LibreOffice embeds changing PDF metadata and identifiers. Its byte size, 71-page count, extracted text, and visual layout remained stable; no byte-reproducibility claim is made for the validation PDF.
