---
name: promise-tracker
description: "Track and audit promises — setups the text tells the reader to remember. For fiction: Chekhov's guns, questions, threats, relationships, mysteries, prophecies, rules. For non-fiction: thesis threads, unresolved tensions, 'we'll return to this', promised counterarguments/definitions. Maintains a ledger at Wiki/Story/Book-N/promises.yaml and reports overdue, due, and undated promises. Use when checking promises, loose ends, unresolved setups, or before closing a book. Works for both fiction and non-fiction projects."
metadata:
  author: Storycraft Skills
  version: "1.0.1"
  category: cross-cutting
  output-format: yaml
---

# Promise Tracker — the unified ledger for setups and payoffs

Every text makes implicit contracts with its reader. A detail introduced with weight creates an expectation: it should return in a satisfying way, or the reader will feel cheated. This skill tracks those contracts as "promises" in a simple ledger.

For **fiction**, these are classic Chekhov setups (guns, threats, questions, mysteries, prophecies, relationships). For **non-fiction** (essays, books, dissertations, reports), these are thesis threads, unresolved tensions, explicit forward references ("we'll return to this"), counterarguments promised but not yet addressed, or definitions promised but not yet given.

The ledger lives at `Wiki/Story/Book-N/promises.yaml`, one ledger per book/work unit. A setup deliberately withheld for a later volume can be marked `deferred_to_series: true` and must appear in the inter-book/series promise map.

## Step 1: Locate the book/work unit and the ledger

Identify the book/work unit from the user's request or from `**/Wiki/Story/active-context.md`. The ledger path is `Wiki/Story/Book-N/promises.yaml` for that unit.

If there is no ledger yet, copy [assets/promises.yaml](assets/promises.yaml) to `Wiki/Story/Book-N/promises.yaml` (create the folder if missing) and remove the blank scaffold entry. Tell the user a ledger was created.

## Step 2: Read the ledger and the relevant text

Read the whole ledger, then read the chapter/section the user names (or the most recent per active context). Read as a reader: anything given weight registers as a promise.

## Step 3: Harvest new promises

Ask: *what did this text tell me to remember?*

**Fiction cues:**
- An object introduced with more detail than the scene needs
- A question a character asks and nobody answers
- A skill, tool, or ability mentioned in passing
- A threat, a debt, a vow, a prophecy
- A stranger named with weight
- Any rule of the world demonstrated in a way that begs a later exception
- Explicit forward references ("before the harvest festival", "when we reach the capital") — these are loud promises; `payoff_by_ch` should reflect the stated deadline

**Non-fiction cues:**
- A thesis claim teased as needing development later
- An unresolved tension stated explicitly
- Forward references: "we'll return to this in Chapter X" or "more on this later" with an implied scope
- A counterargument promised ("we'll consider objections...") but not yet addressed
- A definition promised ("we'll define X precisely...") but not yet given
- A term, concept, or framework introduced as needing fuller treatment
- A data point, example, or case study mentioned as forthcoming
- An open question raised by the argument that demands an answer

Record each in the ledger with:

- **promise**: what the reader now expects, written from the reader's side — concrete and testable
- **introduced_ch**: the chapter/section where it was made (e.g. `ch3`, `sec2.1`, or just a number)
- **kind**: Choose the best fit. Fiction: `object | skill | threat | question | debt | relationship | mystery | prophecy | rule`. Non-fiction: `thesis-thread | tension | forward-ref | counterargument | definition | concept | example | open-question | other`
- **weight**: how loudly the text made it — `whisper` (passing mention), `plain` (normal weight), `loud` (explicit promise, heading, repeated)
- **payoff_by_ch**: the chapter/section by which the reader will feel cheated. **Every promise needs one.** If the honest answer is "not this book/work unit", set `deferred_to_series: true` and add to the series promise map instead of leaving undated.
- **project_type**: `fiction` or `nonfiction` (helps with filtering/reporting; optional but useful)

## Step 4: Record payoffs

When a promise is satisfied, fill in `paid_in_ch` and `paid_how`. Both or neither — a payoff recorded without explanation is weak. The payoff must be **on the page** (stated, resolved, delivered).

## Step 5: Run the ledger report

With the host's Python interpreter:
```bash
python3 <skill-dir>/scripts/promises.py --chapter chNN
```

The script walks up from the working directory to find `Wiki/`, picks the ledger (pass `--book Book-N` when multiple exist), and buckets promises: paid, overdue, due this chapter, due soon, undated, open, deferred. If Python/PyYAML unavailable, read the ledger manually and bucket by the same rules.

## Step 6: Act on what's due

- **Overdue** → Reader is already owed this. Pay it soon, or deliberately re-plan and move the date with explanation in `notes`. Don't silently push deadlines.
- **Due this chapter/soon** → Surface these to the drafting brief.
- **Undated** → Date it now, or defer it now. Undated promises accumulate silently.
- **Deferred** → Confirm each appears in the series/inter-book promise map (e.g. `Wiki/Story/series-arc.md`). If missing, note it.

## Before closing a book/work unit

Run with `--final` (exit status 1 if anything unpaid and not deferred):
```bash
python3 <skill-dir>/scripts/promises.py --final
```

A finished unit should not leave unpaid, undeferred promises. Pay them, defer them, or record a deliberate ruling in `notes`.

Return: the bucketed report, counts of harvested/paid this session, and any ledger edits made.
