---
name: pangram
description: "Diagnostic-only statistical uniformity scan for a single chapter or scene: sentence-length variance, opener diversity, lexical repetition, paragraph and punctuation uniformity, register monotony, choppy constructions, and known AI-favored phrasing. A mechanical proxy that correlates with detector risk — it does not reproduce Pangram's learned-tells classifier (see the caveat). Pairs with burstiness-check, which compares chapters against each other. Never edits text. Use for Pangram risk assessment or statistical uniformity reviews on one unit."
metadata:
  author: Fiction Toolkit
  version: "2.0.0"
  category: fiction-editing
---

# Pangram Risk Scan

A measurement pass for one chapter or scene. It reports where the text is
statistically uniform — the shape a detector-trained ear hears as machine-flat —
in plain numbers and flagged locations, then routes the fix to the skill that
owns it. **This skill never edits text and never proposes rewrites.**

**Caveat on the name — read before trusting the score.** Pangram's own technical
report (Emi & Spero, 2024, arXiv:2402.14873) states that Pangram is *not* a
perplexity/burstiness classifier — that is the older GPTZero approach this scan's
heuristic vocabulary comes from. Pangram is a transformer trained via
hard-negative-mining on matched human/AI pairs to catch *learned stylistic tells*
(generic phrasing, LLM-typical constructions — the paper's own examples are
overusing "delve" and "it is important to note"). Treat this scan's statistics as
a proxy that correlates with detector risk, and treat any phrasing-tell findings
as the likelier real culprit. This skill deliberately does **not** suggest
"injecting unpredictability" or rotating in flashier synonyms to dodge a detector:
that path produces purple prose fighting the project's style rules. Route fixes
to the skills that edit against the book's actual voice (below).

Pairs with `burstiness-check`: that skill needs 2+ files and finds which chapters
run flat against the book's own baseline; this one works on a single unit and
profiles *why* it reads flat.

## Arguments

The request arguments — one chapter or scene reference (a number, filename, or
path). If omitted, ask which file to scan. For multi-chapter comparisons, use
`burstiness-check` instead.

## What to measure

Work through the chapter section by section. Every measure reports numbers and
flagged locations with exact quoted text — never replacements.

1. **Sentence-length variance.** Average and spread of sentence lengths. Flag
   when sentences cluster in one length band with no short punches or long runs.
2. **Opener diversity.** First word of every sentence. Flag: more than 15% of
   sentences starting with "The", more than 10% starting with "He/She", 3+
   consecutive sentences sharing an opener, pronoun-dominated openings.
3. **Lexical repetition.** Non-common words used more than twice per 500 words,
   repeated descriptive phrases, the same verb more than 3 times in a scene.
4. **Paragraph uniformity.** Paragraphs of near-identical length or identical
   internal structure (every paragraph one topic sentence plus support, for
   example).
5. **Punctuation distribution.** Comma patterns that repeat mechanically; absence
   of semicolons, colons, or dashes; every sentence ending in a period.
6. **Register monotony.** Long passages holding one register with no voice
   intrusion, aside, or tonal shift.
7. **Choppy constructions.** Verbless fragments standing as description, colon-list
   constructions, ellipsis-separated lists, paragraphs that read like bulleted
   lists, overused rapid-fire action fragments.
8. **Known AI-favored phrasing.** "practiced precision/ease", "a mix/mixture/
   combination of [X] and [Y]", "couldn't help but [verb]", "found himself/herself
   [verbing]", "something akin to", "a sense of"; gerund chains; emotion-body
   formulas ("dread coiled in his stomach"); paired mood adjectives ("cold and
   unforgiving"); rule-of-threes lists. Count every instance with its location.

## Report format

```markdown
## Pangram Risk Scan: [filename]

[2-3 sentence assessment: overall uniformity, dominant pattern, likely detector
exposure]

### Measures
| Measure | Result | Flag |
|---|---|---|
| sentence-length σ | {value} | low/ok |
| "The"-openers | {n}% | ok/flag |
| He/She-openers | {n}% | ok/flag |
| longest same-opener run | {n} | ok/flag |
| repeated lexical items | {list with counts} | ok/flag |
| paragraph-length spread | {value} | ok/flag |
| punctuation variety | {note} | ok/flag |
| register shifts | {count} | ok/flag |
| choppy constructions | {count} | ok/flag |
| AI-favored phrasing | {count, by phrase} | ok/flag |

### Flagged locations
[each flag: measure, line, exact quoted text, count]

### Risk level
[Low / Medium / High] with the two or three findings that drive it.
```

## Routing (never edit here)

- **AI-favored phrasing, emotion-body formulas, banned words** →
  `fiction-aiism-editor` — the learned-tells lane, and per the caveat above the
  likelier real detector trigger.
- **Choppy constructions, sentence/opener/paragraph variance** →
  `fiction-prose-editor`.
- **"Is this chapter flat relative to the rest of the book?"** →
  `burstiness-check` across a range for the baseline comparison.
- Structural risk from dialogue-light shape (the interiority pattern) →
  `burstiness-check`, whose dialogue-ratio signal owns that diagnosis.
