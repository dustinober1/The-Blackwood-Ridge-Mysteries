---
name: drift-check
description: "Diagnostic-only, book-level drift audit: measures across all chapters what per-chapter gates cannot see — pet words concentrating, rhetorical-move density accelerating, chapter openers and closers running on the same formula, and lived specificity thinning toward the back. Quality decays monotonically in long generation runs while per-chapter checks stay green; this skill finds the gradient. Also measures non-fiction drift: claim density, evidence-to-claim ratio, abstraction ladder variance, and definition reintroduce rate. Never edits text. Use for drift checks, 'why does the back half feel flatter', 'pet word check', or drift-check with a chapter range."
metadata:
  author: Fiction Toolkit
  version: "1.2.0"
  category: fiction-editing
---

# Drift Check

A measurement pass across the whole book, not a rewrite pass. Per-chapter gates audit
each chapter against the rules; they cannot see the thing that actually happens in long
manuscripts: **the average chapter is fine, and the trend is not.** The rhetorical move
that appears 3 times in chapter 1 appears 12 times by chapter 20. The pet word starts as
texture and ends as a tic. Openers converge on one formula. The reader feels this before
they can name it — as "the back half is flatter" — and no single-chapter report ever
flags it, because no single chapter is broken.

**This skill never edits text.** It reports per-chapter numbers and trend flags, states
what each metric is a proxy for, and routes the fix: construction dies to
`fiction-line-editor` / `fiction-prose-editor`, template closers to
`fiction-divergence`, register thinning to `fiction-reviewchapter`, false intimacy with
one device to the author's style rules. Like all mechanical proxies, these statistics
correlate with the reader-experience problem but do not measure it directly; treat every
flag as "worth a closer read," not a verdict.

## Arguments

The request arguments — optionally a chapter range (e.g. `1-14`) to scope the audit;
default is every chapter in the book's chapter folder(s). Fewer than 4 chapters gives no
meaningful trend: run it anyway, but say so.

## Step 1: Resolve chapter files

Search the project for the book's chapter files (`**/Chapters/**/Chapter-*.md` or the
book's established chapter source per `active-context.md`), sort them, apply any range
from the arguments. Record the snapshot — findings attach to a text.

## Step 2: Run the measurement

With the host's Python interpreter:

```
python3 <skill-dir>/references/drift.py <chapter files in order>
```

The script reports, per chapter and for the book:

### Fiction metrics

1. **Pet-word ledger** — content words whose frequency per 1,000 words is skewed: a word
   running hot in one chapter (≥3× its book rate) or concentrating in the back half
   (≥70% of its occurrences after the midpoint while the front half reads normal). This
   is the "operational ×177, and 30 of them in one late section" finding: the lexicon
   narrows as the book proceeds.
2. **Negation-pivot density** — negation constructions per 1,000 words, per chapter,
   with the first-half vs second-half averages. A rising trend is the house style
   calcifying: the move that carried chapter 1 becomes a metronome by chapter 20.
3. **Opener formula reuse** — the first words of each chapter, clustered by shared
   opening pattern. Eleven consecutive chapters opening by recapping the previous
   chapter's ending is a serialized-recap habit the reader will see before chapter
   eleven.
4. **Closer die reuse** — pairwise similarity of chapter-final sentences. A high-similarity
   pair is a stamped closer: the same die refilled with fresh nouns. A refrain the
   author chose is legal; a die is the tell. The script finds the candidates; the
   human judgment call (refrain vs die) is made looking at the pairs.
5. **Specifics density** — proper-noun-ish tokens per 1,000 words, per chapter, as a
   trend. Falling specifics toward the back means the book is drifting from "a comment
   thread unresolved since March" toward "some paperwork" — lived texture thinning
   exactly where the stakes peak.

### Non-fiction metrics

6. **Claim density** — claims (assertions, arguments) per 1,000 words, per chapter. Falling claim density means the book is drifting from argument toward summary.
7. **Evidence-to-claim ratio** — evidence instances (examples, data, quotes, citations) per claim, per chapter. A falling ratio means assertions are going unsupported.
8. **Abstraction ladder variance** — ratio of abstract to concrete nouns per chapter. A narrowing ladder (fewer concrete anchors) means the book is drifting toward jargon.
9. **Definition reintroduce rate** — terms defined once then used cold at distance without re-anchoring.

## Step 3: Interpret and route

The script finds candidates; interpretation decides which are findings:

### Fiction routing

- **Rising negation-pivot density / hot pet words**: real when the word or move is doing
  the chapter's most rhetorical work at that rate. Ration the construction — keep the
  instances that carry weight (usually the first and the best), demote the rest. Route
  to `fiction-line-editor` with the flagged chapters.
- **Opener/closer clusters**: real when the shared pattern was not chosen. A deliberate
  refrain (a recurring closing line that develops) is recorded in the style rules as a
  motif and left alone. A noun-swapped die gets rewritten in one chapter's own words.
  Route template closers to `fiction-divergence` for alternates.
- **Falling specifics density**: route to `fiction-reviewchapter` for a canon-grounded
  texture pass on the flagged chapters — specifics must be real (the Wiki's, not
  invented), so this is a research-and-anchor job, not a decoration job.
- **All metrics flat**: say so plainly. Flat metrics with a "the back half feels
  flatter" complaint mean the problem is structural, not statistical — route to
  `fiction-dev-editor` or the review panel, not deeper linting.

### Non-fiction routing

- **Falling claim density** → route to `nonfiction-structure`
- **Falling evidence-to-claim ratio** → route to `nonfiction-factcheck`
- **Narrowing abstraction ladder** → route to `nonfiction-clarity-edit`
- **Definition reintroduce rate** → route to `nonfiction-writechapter`

Report: the per-chapter table, the trend flags, the refrain-vs-die ruling for each
closer cluster, and the routing. Never propose prose rewrites from the statistics
alone.
