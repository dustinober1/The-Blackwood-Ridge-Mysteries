---
name: review-panel
description: "Build and run a persona review panel for fiction and non-fiction: distinct reader personas, each with a stake, a way of being wrong about THIS book, fixed output flags, and a copy-paste prompt block; run them one at a time in isolated passes, verify every quoted line before filing, and synthesize cross-persona findings. Maintains Wiki/Review/panel.md and Wiki/Review/personas/. Use when user says 'review panel', 'run a persona', 'beta read', 'reader panel', 'what would a reader think', or when Book 1 reaches review."
metadata:
  author: Fiction Toolkit
  version: "1.1.1"
  category: fiction-writing
  output-format: markdown
---

# Review Panel — readers with different ways of being wrong

One reviewer sees one book. A panel sees the friction between reviewers. The value is
not more opinions — it is opinions that cannot blend: the continuity hawk catches what
the cold reader forgives; the genre-native reader's contract breach is the newcomer's
favorite scene. A persona that shares another persona's blind spot is a wasted seat.

This skill builds the panel file and the persona roster for THIS series, runs personas
against chapters or acts, and files verified findings in `Wiki/Review/`. It replaces
nothing: `coldread` tests one isolated claim about one unit; `fiction-reviewchapter`
audits craft against canon; the panel answers the question neither can — *what does
each kind of reader experience?*

## The panel design rules

These rules come from a twelve-persona panel run end to end on a full manuscript; they
are the difference between a panel and a pile of prompts.

1. **A persona is a stake, a way of being wrong, and a fixed output format.** "Romance
   reader" is not a persona. "A romance reader who DNFs the moment the leads talk
   around a misunderstanding for the third time" is. Derive each persona's attack
   vectors from THIS book's genre contract, synopsis, and known risks — the book's own
   `Wiki/Style/genre.md` and `Wiki/Story/Book-N/synopsis.md` say what this book claims
   to be; personas exist to test those claims from seats the drafting process cannot
   occupy.
2. **Never blend personas.** One persona per pass, one pass per fresh isolated worker.
   Blending produces the average reader, who does not exist.
3. **Fixed, typed output flags.** Each persona reports in its own flag vocabulary
   (examples below), every flag with a quoted line. Typed flags make findings countable
   and comparable across chapters.
4. **Count, don't gesture.** For repeated constructions, the persona's brief says
   *count them and report the density*, not "some repetitive phrasing." A count of 24
   per chapter that doubles in the back half is a finding; "a bit repetitive" is not.
5. **Verify every quote before filing.** Persona passes hallucinate — in panel runs to
   date, multiple flag quotes per report failed verification at their cited lines.
   Before any finding is filed, grep the quoted text at the cited location in the
   snapshot under review. Drop or correct what does not verify. A false finding costs
   the repair pass more than the true finding earned.
6. **Every report carries a positive ledger.** What survived scrutiny, stated as
   findings. A panel that only condemns trains the author to ignore it; the positive
   ledger is what the repair pass must not sand off.
7. **Record what was read.** Each report header states the scope, the snapshot (file
   paths or commit), and the method. Findings attach to a text, not to the book's vibe.
8. **Repair plans carry guard-rails.** Findings route to the skill that owns the fix
   (`fiction-reviewchapter`, `fiction-line-editor`, `fiction-divergence`,
   `fiction-promises`, `drift-check`, `nonfiction-factcheck`, `nonfiction-clarity-edit`,
   `nonfiction-structure`), and every repair plan states what NOT to do — the voice,
   structure, and choices the panel validated stay untouched.

## Step 1: Build or load the panel

If `Wiki/Review/panel.md` exists, load it and use its personas as written. Otherwise
build the panel: write `Wiki/Review/panel.md` (the roster and sequencing table) and one
file per persona in `Wiki/Review/personas/`.

Seed the roster from the archetypes below, then customize every seat against this
book's genre contract and known risks. A seat that would attack something this book
does not risk is cut; a risk this book has that no archetype covers gets a new seat.

**The fiction archetype seats** (each persona file follows the same skeleton — Who / Cares
about / Attack vectors / Output flags / Prompt block):

1. **Genre-native reader** — deep in this genre's shelf. Attacks: trope delivery against
   `genre.md` commitments, expectations the book signs and forgets. Flags: TROPE-MISS /
   CONTRACT-BREACH / DELIVERED.
2. **Cold general reader** — smart, outside the genre's in-jokes, reads cold with no
   Wiki access. Attacks: unexplained world terms, references that assume a prior book,
   humor that needs ownership of a reference. Flags: INSIDER-ONLY / LOST-ME / FOLLOWED-IT.
3. **Series newcomer** — has not read the earlier books; enters at the unit under
   review. Attacks: coined terms re-used cold at distance, relationship shorthand
   un-re-anchored, history referenced as known. Flags: COLD-ENTRY / UNANCHORED /
   FOLLOWED-IT.
4. **Craft editor** — professional eye for rhythm and repetition. Attacks: one
   rhetorical move at scale (counted per chapter), opener/closer formulas repeated
   across chapters, register thinning in exposition stretches, pacing by act. Flags:
   VOICE / REPETITION (with counts) / PACING; one-line verdict per chapter: keep /
   tighten / rework open / cut.
5. **Seam hunter** — assumes the text is machine-drafted until convinced otherwise.
   Attacks: the house style executed at superhuman uniformity (the tell is the *absence
   of variation*, not any one sentence), noun-swapped template repeats ("dies"), lived
   detail thinning where the stakes peak. Verdict per chapter: reads human /
   reads edited-machine / reads machine, with the lines that convinced either way.
6. **Continuity hawk** — the only seat allowed to read canon. Attacks: references to
   specific prior moments that did not happen as described (false callbacks), floating
   quantities (army sizes, distances, money, ages), claims the Wiki does not support.
   Flags: FALSE-CALLBACK / UNSUPPORTED / DRIFT.
7. **Plausibility reader** — reads power and institutions. Attacks: structural problems
   resolved by one person's conscience, characters acting with authority they do not
   hold, institutions that exist only to be wrong. Flags: AUTHORITY-SLIP /
   CONVENIENCE / HELD-UP.
8. **Pacing reader** — reads stay-up-late behavior. Attacks: chapter-entry toll (how
   much must I remember before this scene makes sense), chapters that end where the
   tension peaked instead of after it, mid-book sag by act. Flags: TOLL /
   STOPPED-READING / READ-ON, plus the one line that kept them up.

**The non-fiction archetype seats** (each persona file follows the same skeleton — Who / Cares
about / Attack vectors / Output flags / Prompt block):

9. **Subject-matter expert** — deep in the field. Attacks: factual accuracy, evidence quality, counterarguments, overclaiming. Flags: UNSUPPORTED-CLAIM / EVIDENCE-THIN / COUNTERARGUMENT-MISSING / OVERCLAIM
10. **Intelligent novice** — smart but outside the field. Attacks: jargon walls, unexplained terms, abstraction density. Flags: JARGON-WALL / UNEXPLAINED / LOST-ME / ABSTRACTION-THICK
11. **Skeptic/practitioner** — reads to find what's wrong. Attacks: cherry-picked evidence, false balance, omitted data, authority without scars. Flags: CHERRY-PICK / FALSE-BALANCE / MISSING-DATA / AUTHORITY-SLIP
12. **Editorial gatekeeper** — professional editor eye. Attacks: argument flow, chapter structure, signposting, reader payoff. Flags: STRUCTURE / SIGNPOSTING / PAYOFF-THIN / FLOW

The full persona files for the four non-fiction seats — Who / Cares about / Attack vectors / Output flags / a copy-ready Prompt block each — live in [references/nonfiction-personas.md](references/nonfiction-personas.md); copy them into `Wiki/Review/personas/` when building the panel.

**Optional ninth seat — the hostile advocate:** argues the book's opposite on purpose,
used once per act on the act the author is proudest of, to find where a choice is
convention defended as conviction. Output: three places where the book takes the easy
route and calls it a stance.

## Step 2: Sequence the panel

Add a sequencing table to `panel.md` — which seats run at which stage. The default:

### Fiction sequencing

| Stage | Seats |
|---|---|
| Per chapter, after `fiction-reviewchapter` passes | craft editor |
| Per act | genre-native, pacing reader |
| Book milestones (midpoint, end) | seam hunter, continuity hawk |
| Late-series or bridge chapters | series newcomer |
| Whole book, before calling it done | all seats, one unit each, plus the hostile advocate on the strongest act |

### Non-fiction sequencing

| Stage | Seats |
|---|---|
| Per chapter, after nonfiction-factcheck passes | editorial gatekeeper |
| Per part | subject-matter expert, skeptic/practitioner |
| Whole book, before calling it done | all seats, one unit each |

Domain lanes hold: the seam hunter does not audit canon (continuity hawk's lane); the
continuity hawk does not judge voice (craft editor's lane). A finding outside a
persona's lane is discarded even when correct — the lanes are what keep the friction
honest.

## Step 3: Run a persona

For each run: take one persona's prompt block, the unit under review (chapter, act, or
book), and nothing else — unless the persona's lane explicitly grants canon access
(continuity hawk). Run it in a fresh isolated worker when the host supports one.

A persona prompt block names the role, the stake, the read instruction, and the flag
vocabulary, and always ends with the discipline clause. Model:

> You are [name], [who]. You came to this book because [stake]. Read the unit as this
> person, not as an editor. Flag [attack vectors], in [flag vocabulary], every flag
> quoting the exact line. Count repeated constructions and report densities, not
> impressions. End with the verdict your flags imply and a positive ledger: what this
> unit does well enough that a repair pass must not break it. Assume nothing about the
> author's intent; the page is the whole record.

## Step 4: Verify, file, synthesize

1. **Verify** every quoted line in every returned report against the snapshot (grep the
   quote; check the cited chapter). Correct or drop failures. Note the correction count
   in the filed report — it is evidence about the panel's reliability.
2. **File** the verified report at `Wiki/Review/Book-N/<persona>-<unit>.md` with the
   header (persona, scope, snapshot, method) and its flag ledger.
3. **Synthesize across personas** — the step no single pass can do. Compare reports for:
   - **Contradictions between seats** (the genre-native reader's favorite scene is the
     newcomer's wall) — these are usually real trade-offs to surface to the user, not
     bugs.
   - **The same hole from two seats** (a gap the pacing reader felt and the newcomer
     named) — highest-confidence findings.
   - **Gradients** — findings that worsen across the book (densities rising, register
     thinning late). A gradient is invisible per chapter; route it to `drift-check` for
     measurement and to the act-level repair, not to one-chapter fixes.
4. **Report to the user**: the per-seat verdicts, the cross-persona findings, and the
   routing — which findings go to `fiction-reviewchapter`, which to `fiction-line-editor`,
   which are outline-level (`fiction-divergence`), which are ledger entries
   (`fiction-promises`), which go to `nonfiction-factcheck`, which to `nonfiction-clarity-edit`,
   which to `nonfiction-structure`. The panel proposes; the user disposes.

Return: the panel path (or the existing panel used), seats run, verified flag counts,
corrections made during verification, and the synthesis.
