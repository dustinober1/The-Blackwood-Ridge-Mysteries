---
name: fiction-series-outline
description: "Plan the series-level arc into Wiki/Story/series-arc.md: the per-book dramatic-question stack, the inter-book promise map for setups deferred across books, character arc spans, the escalation plan, and the handoff inventory each book must honor. Use when starting a series, before planning Book N+1, when user says 'series arc', 'plan the series', 'what carries into the next book', or when a per-book ledger defers a promise to a later book."
metadata:
  author: Fiction Toolkit
  version: "1.0.0"
  category: fiction-writing
  output-format: markdown
---

# Fiction Series Outline — the arc across books

A book's outline plans one contract. A series runs on several at once: the promise each
book makes and keeps, the promise the *series* makes that no single book can pay, and
the debts each book hands forward. Without a plan at that level, deferred setups become
loose threads, protagonists reset between books, and the stakes inflate by number
instead of by meaning. This skill writes the plan: `Wiki/Story/series-arc.md`.

Run it at series inception (after the series synopsis exists), and refresh it whenever
a per-book ledger marks a promise `deferred_to_series` or a book's ending changes what
the next book inherits. Per-book planning stays with `fiction-synopsis` and
`fiction-outline`; this skill only owns what crosses book boundaries.

## Step 1: Locate inputs

Search the project's `Wiki/` for:

- `**/Wiki/Story/synopsis.md`: the series synopsis. Required at series inception; if
  missing and any book synopsis exists, work from the book synopses and say the series
  contract is being inferred from below.
- `**/Wiki/Story/Book-N/synopsis.md`: per-book synopses, for every book that has one.
- `**/Wiki/Story/Book-N/promises.yaml`: per-book Chekhov ledgers. Every
  `deferred_to_series: true` entry must appear in the inter-book promise map — collect
  them all.
- `**/Wiki/Characters/*.md`: series-wide character files, including relationship
  checkpoints.
- `**/Wiki/World/**/*.md`: world rules that constrain how stakes can escalate.
- `**/Wiki/Story/series-arc.md`: the existing plan, if this is a refresh. Carry forward
  every ruling and paid entry; a refresh revises, it does not restart.

## Step 2: Contract gate

The series plan needs, at minimum: what the series is about (the question spanning all
books), what experience it promises the reader across books, and at least one book's
contract. If a deferred promise exists with no book planned to pay it, that is
acceptable at planning time — the map records it as **unassigned** — but an unassigned
promise with no planned book remaining is a finding to report, not a row to file.

## Step 3: Write the series arc

Write `Wiki/Story/series-arc.md` with these sections:

```
# Series Arc — <Series Title>

## Series contract
- **series_question:** the dramatic question spanning all books
- **series_promise:** the spoiler-light experience the series owes across books
- **series_answer:** the spoiler-containing answer the final book demonstrates
- **endgame:** what the last book must be able to pay with (powers, relationships,
  knowledge, costs) — the estate every earlier book is building or spending

## Book stack
| # | Title | Central question (spoiler-light) | What it escalates | Series promise it advances |
|---|-------|----------------------------------|-------------------|----------------------------|
| 1 | ...   | ...                              | ...               | ...                        |

Each book's central question must be askable from that book alone, and the stack must
escalate in meaning, not just scale: each question should cost the protagonist something
the previous question taught them to value.

## Inter-book promise map
| Promise | Made in | Pays in | How (planned or unassigned) |
|---------|---------|---------|------------------------------|

One row per `deferred_to_series` entry in any per-book promises.yaml, plus series-level
setups planted deliberately for later books. `Pays in` uses book and chapter when
planned, or **unassigned**. A promise cannot pay in the book that made it.

## Character arc spans
For each series protagonist and each series-long relationship:
- **Book N → N+1 waypoints:** the state they start in, the state each book ends with,
  and what the crossing costs. A character who ends each book where they started is a
  reset, not an arc.

## Escalation plan
Per book: what widens (scope, stakes, cast) and what deepens (cost, intimacy, moral
weight). Scale without deepening is inflation — the reader stops feeling it by book
three. Name the mechanism: the new books' stakes are paid in currencies the earlier
books established.

## Handoff inventory
Per book boundary (Book N → Book N+1): what the next book inherits — cast status and
where everyone stands, unresolved debts, knowledge asymmetries (who knows what they
shouldn't), open promises from the map, and anything the next book must not contradict.

## Reading-order constraints
Anything a reader must read in order for a payoff to land; publication-order exceptions,
if any.
```

## Step 4: Coverage pass

Before saving, verify:

- Every `deferred_to_series` entry in every per-book ledger has a row in the promise
  map; every map row names its source ledger entry.
- The book stack's escalation is in meaning or cost, not scale alone — at least one
  book deepens rather than widens.
- Every protagonist has at least one arc waypoint per planned book.
- The handoff inventory for the boundary into the next unplanned book is written from
  the last planned book's actual ending state, not intentions.
- The series answer is deliverable by the endgame estate: if the final book must pay
  with something no earlier book builds, that is a finding.

## Step 5: Save, sync, present

1. Save `Wiki/Story/series-arc.md`.
2. If any promise-map row is new or changed, say which per-book `promises.yaml` entries
   it corresponds to; if a ledger entry has no row, add the row. The map and the ledgers
   must agree in both directions.
3. Present the book stack and the promise map. For Book N+1 planning, hand off to
   `fiction-synopsis` to write that book's own synopsis from its row in the stack and
   its handoff inventory.

Return: the series-arc path, the book count planned, deferred promises mapped vs
unassigned, and any findings from the coverage pass.
