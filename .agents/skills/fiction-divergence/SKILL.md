---
name: fiction-divergence
description: "Anti-convergence pass over an outline or beat plan: for each planned beat, generate a default, an inversion, and a cost-shift candidate, keep the least-expected-but-earned version, check the structure against the genre's default template, and maintain a per-act surprise ledger. Use when user says 'divergence pass', 'make this less predictable', 'check for defaults', 'surprise ledger', or worries the outline is running on rails."
metadata:
  author: Fiction Toolkit
  version: "1.0.0"
  category: fiction-writing
  output-format: markdown
---

# Fiction Divergence — beat the defaults

Language models plan fiction toward the same destinations: the midpoint betrayal, the
all-is-lost loss of the ally, the climactic confrontation, the ally's death that buys
the third act. Each is fluent, competent, and exactly what a genre reader can call from
the premise alone. The failure is not bad writing — it is that every book runs the same
skeleton, so the reader is never surprised by structure, only by surface. This skill
exists to break that convergence at the planning level, where it is cheapest to fix.

The bar is **least-expected-but-earned**: a beat surprises, and the surprise is paid
for by setups already in the outline and canon. Unexpected-but-unearned is a twist the
reader resents; expected-but-earned is a promise kept. Both are failures here.

Run this pass after `fiction-outline` (on the whole outline, an act, or a chapter
range), or on a run of scene plans when a stretch of chapters feels like it is running
on rails. It never changes the story contract — the reader promise, the central
question, and every trope payoff still deliver. We vary the route, not the destination.

## Step 1: Locate inputs

Search the project's `Wiki/` for:

- `**/Wiki/Outline/Book-N/outline.md` (or legacy `**/Wiki/Outline/outline.md`): required.
  The beats under divergence. Read fully.
- `**/Wiki/Style/genre.md`: the tropes and their treatment roles — a divergence that
  drops a trope's setup/development/payoff is rejected, not proposed.
- `**/Wiki/Story/synopsis.md` (or the per-book synopsis in `**/Wiki/Story/Book-N/`):
  the story contract — premise, central question, reader promise, story answer.
- `**/Wiki/Characters/*.md`: what the cast has done and can do. A divergence must be
  payable by someone the canon has established.
- `**/Wiki/Story/Book-N/promises.yaml`, if present: the Chekhov ledger. Payoffs due
  soon constrain what a beat may change — a divergence cannot skip a debt.

## Step 2: Read the criteria

Read [references/divergence-criteria.md](references/divergence-criteria.md). It defines
the three candidate forms, the expectedness test, the earned-ness test, the
genre-default template slots, and the anti-patterns (divergence for its own sake,
escalation mistaken for novelty, quirk mistaken for surprise).

## Step 3: Generate candidates per beat

For each chapter's central event (from `what_must_happen`), write three candidates:

1. **Default** — the version you would generate first: the most predictable route that
   genre experience suggests. Write it honestly; a strawman default makes the pass
   useless.
2. **Inversion** — the beat's plot function delivered through the least-expected route:
   the confrontation that happens early instead of late, the confession that never gets
   spoken, the chase the antagonist wins on purpose.
3. **Cost-shift** — the same plot function, but the price lands on something else: the
   genre default pays in blood, this pays in trust; the default destroys the relationship,
   this destroys the alibi.

## Step 4: Select and record

For each beat, pick the least-expected candidate that passes the earned-ness test
(payable from setups and canon already in the outline — if it needs a new setup, name
the earlier chapter that must plant it). The Default wins when it is genuinely the best
version, but a Default that wins must be recorded as **chosen**, with one sentence on
why the expected route is right here. A beat that keeps its default silently is a beat
that was never diverged.

Record per beat: the three candidates, the selection, the reason, and any new setup
requirement (which chapter plants it).

## Step 5: Check the structural template

Compare the outline's skeleton against the genre-default template slots in the criteria
reference — midpoint, act-2 low, climax, and the endings the genre mandates. Flag every
slot filled by a default. A flagged slot is not a command to change; it is a demand to
choose. Defaults that survive Step 4 get their "chosen" reason.

## Step 6: Build the surprise ledger

Write `Wiki/Outline/Book-N/surprise-ledger.md` (create the folder if missing). Per act:

```
## Act N (chapters A–B)

- **Diverged:** ch 7 — confession moved to the midpoint's aftermath; the genre-default
  midpoint revelation never happens, and its information arrives as overheard damage
  control. Earned by: the servant's established route through the east gallery (ch 3).
- **Chosen default:** ch 9 — the ally's death stays: the story's promise is grief, and
  the divergence candidates all spent cheaper currencies.
- **Surprise inventory:** [what this act contains that a genre-standard version would
  not — an image, a structural choice, a domain collision, a payoff arriving early]
```

An act with an empty surprise inventory is running on defaults. That is the finding:
report it and either diverge a beat in that act or record that the act is deliberately
conventional comfort — in which case the *absence* of surprise is the chosen effect,
and it goes in the ledger as such.

## Step 7: Present

Show the selection table and the surprise ledger summary. Proposed changes to the
outline go in as revision instructions to `fiction-outline` (or direct edits to
`outline.md` when the user approves them for this pass), never silently. Return: beats
diverged, beats chosen-default, acts running on defaults, and the ledger path.
