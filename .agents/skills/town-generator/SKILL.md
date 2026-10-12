---
name: town-generator
description: Generate fantasy town, city, and settlement proper names using a Markov chain model trained on place name lists. Use when user says "generate town names", "settlement names", "village names", "city names", or "town generator" for naming settlements. Do not use for character names or full settlement dossiers/profiles (use fantasy-settlement).
metadata:
  author: Custom
  version: "1.1.0"
  category: utilities
---

# Fantasy Town Name Generator

Skill resources are relative to this `SKILL.md`.

Generates fantasy town and settlement names using a Markov chain model trained on place name lists in `data/`.

## Default Behavior: Full Sweep

By default, generate **3 names from every list** in `data/` and present them grouped by style/culture. Do NOT ask questions first — just run it and show results.

Enumerate every `data/*.txt` file. For each file, use [scripts/generate.py](scripts/generate.py) with the host's available Python interpreter and these arguments:

```text
--list <data-file> --count 3 --min-len 4 --max-len 14 --order 2
```

Use the data filename without `.txt` as the style/culture heading.

## Epitheted settlement names

For major cities and capitals, the dedicated town script adds heraldic epithets ("Vorheim, the Throne of the Dead") from [scripts/epithet.py](scripts/epithet.py). This is what the world-building skills invoke when they need epitheted capitals:

```text
python3 scripts/generate_town.py --list <data-file> --count 15 --order 2 --epithet-chance 0.3
```

`--prefix-file <data-file> --prefix-chance 0.35` adds cultural prefixes (e.g. San/Santa/Monte with `data/spanish-prefixes.txt`). Use epitheted names sparingly — major settlements only; bare names for minor ones.

## Refreshing a corpus

The `data/*.txt` lists come from the tekeli.li onomastikon. To add or refresh a list, use [scripts/scrape.py](scripts/scrape.py): `python3 scrape.py <url> [output_name]` saves to `data/`, or `python3 scrape.py --batch urls.txt` for the curated batch. Treat scraped output as a starting list — skim it for duplicates and artifacts before relying on it.

Present output as a clean grouped list:

**Anglo-Saxon** — Aldenmere, Wulfhaven, Eadburgh
**Norse** — Grimholt, Skaldvik, Bjornstad
...

## After Showing Results

Offer to:
- Re-roll the full sweep
- Generate more from a specific style
- Adjust count or Markov order
