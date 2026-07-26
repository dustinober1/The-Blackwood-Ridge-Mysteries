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

## Cover image prompt

**Primary (Midjourney) — Concept A, The Marked Ledger:**

```
An antique brass map weight resting on an open county survey ledger on a dark oak table, the yellowed page ruled with faint survey lines and a small precise graphite pencil mark in the margin. An ornate brass magnifying glass leans against the weight, warm amber lamplight catching its beveled glass and the brass rim. Beyond the table, a tall old map-room window admits pale spring light through faint river fog. Background fades from warm amber lamplight near the ledger to deep shadowy plum and charcoal tones at the edges. Painterly fine-art illustration, rich textures, aged paper grain, brass gleam, fine graphite linework. Atmospheric literary mystery, quiet and investigative, elegant. Leave generous negative space at the top and bottom for typography. --ar 5:8 --s 250 --q 2
```

**Alternate (DALL·E / Stable Diffusion) — Concept A:**

```
1600x2560 px portrait. An antique brass map weight resting on an open county survey ledger on a dark oak table, the aged yellowed page ruled with faint survey lines and one small precise graphite pencil mark in the margin. An ornate brass magnifying glass leans against the weight, warm amber lamplight reflecting off the beveled glass and the brass rim. Behind the table, a tall old map-room window admits pale spring light through soft river fog. Background transitions from warm golden lamplight near the ledger to deep plum and shadowy charcoal at the edges. Painterly fine-art illustration, not photorealistic. Rich textures: aged paper grain, brass gleam, fine graphite linework, old window glass. Atmospheric, literary mystery, quiet and investigative, elegant. Leave the top quarter and bottom quarter clean for title and author text overlay. No text rendered in the image itself.
```

**Concept B alternate (the map room window):**

```
A tall arched window in an old Grange map room at dusk, river fog drifting past the glass outside. Rolled survey maps stand in a wooden rack beneath the sill. A single brass map weight sits on a low table in the foreground, catching the last warm light, an antique brass magnifying glass beside it. Deep plum and charcoal shadows fill the room's corners; aged-ivory paper tones and restrained winter blue-green light from the window. Painterly watercolor illustration, rich layered detail. Atmospheric small-town mystery, literary. Generous negative space at top and bottom for typography. --ar 5:8 --s 250
```

### Avoid

- Any depiction of a body, a weapon, a struck blow, or a confrontation — the map weight must read as a historical object, never as the murder weapon.
- Police tape, warrants, evidence bags, or procedural imagery — this is not a police-procedural cover.
- Thriller/horror shadows, blood, or threatening figures.
- Any legible document text that could be mistaken for the actual case records (payment ledger, warrant, or route annotations) — keep ledger/map text illegible or invented.
- Breaking the series template — font family, title size/weight/tracking, author-name placement, series-label position, and base palette (plum, gold, ivory, blue-black ink) must match Books 1–5; only the focal object and accent motif rotate.

## Notes for the author

- **Selected cover direction (recommended): Concept A — The Marked Ledger.** It keeps the series' object-language (brass magnifying glass, warm lamplight fading to plum/charcoal, aged paper) while rotating the book-specific signal to a survey ledger and graphite pencil mark — spoiler-safe references to the annotation-steering hook without depicting the murder or naming anyone.
- **Series-continuity checklist before finalizing:**
  - [ ] Font family matches Books 1–5 exactly.
  - [ ] Title size, weight, and tracking match the established series treatment.
  - [ ] Author name size, color, and placement match the series.
  - [ ] Series label is in the same position, same size, reading "Book 6."
  - [ ] Frame/border (if any) is identical to prior books.
  - [ ] Base palette (plum, gold, ivory, blue-black ink) is unchanged; only the accent rotates.
  - [ ] The brass magnifying glass appears somewhere on the cover.
- Add title + author name + series label in Canva, Photoshop, or similar after generating the base image. Most AI image generators mangle text — do not attempt to render the title inside the prompt.
- KDP requires JPEG or TIFF, 72+ ppi, under 50 MB. Convert the generated PNG to JPEG.
- Recommended export: 1600 × 2560 px JPEG at 300 ppi (KDP downsamples for display).
- No embedded cover in the EPUB is required — KDP uses the separately uploaded cover image (already handled in the release-build stage).

## Approval rule

An image is not approved merely because it exists. After the author explicitly approves the final asset, `cover-approval.json` must record:

- `status: approved`;
- the canonical cover path;
- the approving name;
- the approval date;
- the exact SHA-256 of the approved file.

The workflow independently recomputes the cover hash and refuses the release build if the file and approval record differ. Visual review must also confirm title/author/series text, Book 6 designation, thumbnail legibility, crop safety, series consistency, and absence of spoiler-heavy imagery.
