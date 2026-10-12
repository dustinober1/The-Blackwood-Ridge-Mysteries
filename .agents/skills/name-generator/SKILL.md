---
name: name-generator
description: Generate character and people proper names using a Markov chain model trained on culture/style name lists. Use when user says "generate character names", "character names", "people names", "create names", "fantasy names", or "name generator" for characters. Do not use for settlements, towns, or geographic places.
metadata:
  author: Custom
  version: "1.2.0"
  category: utilities
---

# Markov Name Generator

Generates names using a Markov chain model trained on name lists in `data/`.

## Default Behavior: Full Sweep

By default, generate **3 names from every list** in `data/` and present them all grouped by culture. Do NOT ask questions first — just run it and show the results.

Enumerate every `data/*.txt` file. For each file, use [scripts/generate.py](scripts/generate.py) with the host's available Python interpreter and these arguments:

```text
--list <data-file> --count 3 --min-len 4 --max-len 12 --order 2
```

Use the data filename without `.txt` as the culture heading.

When the caller needs names from a *specific* culture rather than a full sweep, read [references/culture-map.md](references/culture-map.md) to match the setting's culture to the right `data/` list (or lists), then generate from those lists only. The culture map is what the world-building skills consult when they route name generation here.

Present the output as a clean grouped list, e.g.:

**Anglo** — Wulfstan, Eadric, Aethelmere
**Aztec** — Coyotl, Xiuhtla, Huitzin
...

## After Showing Results

Offer to:
- Generate more from a specific list
- Re-roll the full sweep
- Adjust count or Markov order

## Before a Name Enters Canon

A generated name is a candidate, not canon. Before writing a name into a project's canon (character file, outline entry, world entry), collision-check the shortlist: search the web for each finalist against existing fictional characters, games, and brands, and prefer the cleanest name when candidates tie. Canonize the winner everywhere the project requires it, so no placeholder survives.

If a character's anonymity is deliberate — the story treats them as unnamed — leave them unnamed: resolve any placeholder with an accurate description instead of inventing a name.

## Refreshing a corpus

The `data/*.txt` lists come from the tekeli.li onomastikon. To add or refresh a list, use [scripts/scrape.py](scripts/scrape.py): `python3 scrape.py <url> [output_name]` saves to `data/`, or `python3 scrape.py --batch urls.txt` for the curated batch in `scripts/urls.txt`. Treat scraped output as a starting list — skim it for duplicates and artifacts before relying on it.
