# Marketing Asset Pipeline — The Blackwood Ridge Mysteries

Template-driven social cards for the series pages (Instagram + Facebook).
One YAML spec per post produces a finished PNG plus its caption, hashtags,
and alt text. Cards are full-bleed photography with typographic overlays,
composed locally with typst — no raster editors involved.

**Pen name:** Vesper Blythe · **Brand palette & fonts:** `brand.yaml`
(single source of truth — templates read from it directly).

## Quickstart

```bash
# regenerate everything
python3 marketing/tools/generate.py all

# regenerate one card (after editing its spec)
python3 marketing/tools/generate.py 005-case-file-wren

# 2x resolution proofs for close review
python3 marketing/tools/generate.py all --ppi 288
```

Requires typst (0.15.x). Output lands in `marketing/generated/` at exact
social dimensions: 1080×1080 (square) and 1080×1350 (portrait 4:5).

## Layout

```
marketing/
  brand.yaml        palette, fonts, book metadata, availability lines
  calendar.md       the launch-month schedule and posting rules
  posts/            one YAML per post — the source of truth for content
  templates/        typst card templates + lib.typ (shared brand library)
  tools/
    generate.py     driver: spec → typst → PNG
    ridge_art.py    seeded SVG art generator (retired from cards; kept for
                    possible story-format use)
  assets/
    photos/         background photography + credits.yaml (licenses)
  generated/        output PNGs (committed deliverables)
```

## How a post works

Each `posts/NNN-slug.yaml` has two halves:

1. **Card fields** — template name, size, and whatever the template needs
   (quote + attribution, location copy, case-file fields, book key).
2. **`social:`** — `caption`, `hashtags`, `alt` (alt text). Captions are
   written for a human voice; alt text is required for every post.

The driver passes the spec path to typst as an `--input`; templates load
`brand.yaml` and the spec themselves. Card backgrounds are photographs
referenced by the spec's `photo:` field (root-relative path), toned with the
template's ink veil (`veil:` field overrides the default per template,
integer percent).

## Template catalog

| Template | Size | Used for | Key fields |
|---|---|---|---|
| `town-post` | square, portrait | "A Visitor's Guide" location cards | `eyebrow`, `plate`, `headline`, `sub`, `art:` |
| `quote-card` | square | Verbatim book quotes | `quote`, `attribution`, `book_line`, `quote_size` |
| `case-file` | square | County-records teasers, engagement verdicts | `stamp`, `fields` (label/value), `note`, `options` |
| `cover-feature` | portrait | Book promos with real cover art | `book` (key from brand.yaml), `hook` |
| `cross-promo` | square | Reading-order card, two covers | `covers` (two book keys), `tagline` |

Case-file values support `__R__` tokens, which render as redaction bars
(widths cycle deterministically). The `options` field renders two tilted
verdict stamps (e.g. PUBLISH IT / LET IT LIE) for A/B engagement posts.

## Background photography

Cards run on real imagery from `assets/photos/` — period paintings,
documents, and photographs sourced from Wikimedia Commons so the pages stay
commercially safe. The current library:

| File | Motif | Used by |
|---|---|---|
| `blue-ridge-fog.jpg` | Blue Ridge clouds (CC BY-SA 4.0) | welcome card |
| `gaslamp-street.jpg` | Grimshaw, *Boar Lane by Lamplight* (PD) | Town Square, reading order |
| `bookshop-2.jpg` | secondhand bookshop interior, Hay-on-Wye (CC BY-SA 4.0) | The Foxed Page |
| `survey-map.jpg` | 1860 county survey plat (PD) | Jacob Wren case file |
| `violet-plate.jpg` | 16th-c. sweet-violet gouache (PD) | Dabney case file |
| `letter-1865.jpg` | handwritten 1865 letter (PD) | verdict card |
| `books-candle.jpg` | leather book, candle, rose (PD) | quote cards |
| `books-still-life.jpg` | old-master still life with books and pistol (PD) | cover features |

Provenance, authors, and licenses: `assets/photos/credits.yaml`.

**Attribution duty:** the three CC BY-SA images (fog, bookshop, mansion)
require attribution when published. Cheapest compliant pattern: a pinned
comment or the page's About section reading "Background imagery: Wikimedia
Commons — PBarn424, Immanuel Giel (CC BY-SA 4.0). Paintings and documents
public domain." Full details in credits.yaml. If you'd rather use
your own AI-generated photography (matching the covers' pipeline), drop any
replacement file into `assets/photos/` and point the spec's `photo:` field
at it — the templates are agnostic.

The typst veil system (`ink-veil`, `bottom-scrim`, `top-scrim` in
`lib.typ`) grades every photo to the brand's plum dark; angles were verified
empirically — 270deg seats a gradient's first stop at the bottom edge, 90deg
at the top. Don't swap them.

## Content rules

1. **Quotes are verbatim** from the manuscripts. Never paraphrase a quote —
   pull it, or pick a different one. Attributions use only names that exist
   in canon.
2. **No spoilers past the published books.** Plot teasers come from the
   cross-promo copy in `series-launch/cross-promo/` and the series bible's
   premise; killer identities, reveals, and unpublished-book content stay
   off the page. Redaction bars exist so case files can gesture at secrets
   without stating them.
3. **Canon check**: locations, dates, and character details must match
   `series-bible/world.md` and `series-bible/recurring-characters/`. When in
   doubt, leave it out or redact it.
4. **Accessibility**: every post ships alt text (`social.alt`); paste it into
   the platform's alt-text field.
5. **Image licensing**: only images recorded in `assets/photos/credits.yaml`
   may appear on cards. Never pull random web images into the library —
   scraped stock is a takedown and legal risk on a commercial page. New
   images must be public domain, CC0, or CC BY/BY-SA (attribution then
   recorded in credits.yaml and honored on the page).

## Publishing workflow

1. Edit/create specs in `posts/`, regenerate, and review the PNGs.
2. Batch-schedule the approved set in **Meta Business Suite** (official
   scheduler) per `calendar.md`. FB: caption as post, store link in first
   comment. IG: alt text into the alt field.
3. First-hour comment replies are always human.

**Do not GUI-automate posting/liking/following on Meta accounts** — bot
detection restricts new accounts that do this. Computer use is for one-time
setup, research, and QA sweeps only; the content loop runs through Business
Suite or (later, if desired) the official Instagram Graph API.
