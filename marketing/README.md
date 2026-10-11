# Marketing Asset Pipeline — The Blackwood Ridge Mysteries

Template-driven social cards for the series pages (Instagram + Facebook).
One YAML spec per post produces a finished PNG plus its caption, hashtags,
and alt text. Everything is generated locally with typst — no external
services, no raster editors.

**Pen name:** Vesper Blythe · **Brand palette & fonts:** `brand.yaml`
(single source of truth — templates and the art generator read from it or
mirror it).

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
    generate.py     driver: spec → (art SVG) → typst → PNG
    ridge_art.py    deterministic SVG background art (seeded)
  generated/        output PNGs + art SVGs (committed deliverables)
```

## How a post works

Each `posts/NNN-slug.yaml` has two halves:

1. **Card fields** — template name, size, and whatever the template needs
   (quote + attribution, location copy, case-file fields, book key).
2. **`social:`** — `caption`, `hashtags`, `alt` (alt text). Captions are
   written for a human voice; alt text is required for every post.

The driver extracts `template:` and any `art:` block, renders the background
art if there is one, then compiles the template with the spec path as a
typst `--input`. Templates load `brand.yaml` and the spec themselves.

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

## Background art styles (`ridge_art.py`)

Seeded and deterministic — the same style+seed always renders the same SVG.

- `valley-dusk` — ridgelines, stars, horizon glow, town lamps (welcome card)
- `gaslight` — lamp standards in fog over the square
- `window` — the Foxed Page's lit window with book silhouettes
- `garden` — planted rows of flowers with gold "words" (botanical cipher; reserved for Book Two pushes)

Change a card's mood by bumping its `seed`; add a style by writing a
function and registering it in `STYLES`.

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
