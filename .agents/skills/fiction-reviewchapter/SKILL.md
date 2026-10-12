---
name: fiction-reviewchapter
description: "Review chapters against style guide, characters, and world for actionable edits. Use when user says 'review chapter', 'edit chapter', 'check my chapter', or after writing."
metadata:
  author: Fiction Toolkit
  version: "2.6.0"
  category: fiction-writing
---

# Review Chapter — Orchestrator

This skill runs in an isolated worker when the host supports one, to keep the main conversation context clean. If isolated workers are unavailable, follow the same review instructions directly.

## Step 1: Identify Project and Chapter

Use the project or chapter named by the user. Otherwise identify the selected book from the current context and `**/Wiki/Story/active-context.md`. Read that book's `AGENTS.md`, `CLAUDE.md`, and applicable nested instructions before reviewing.

Find the requested chapter in the book's authoritative chapter source. If the user did not specify one, use the most recent chapter recorded by active context. Prefer the existing `<book-root>/Chapters/` convention, but obey book-specific authority such as `Published/`, volume folders, decimal chapters, or another established source. Never assume `*_Chapters/`.

Also locate these project files:
- **Review guide** (editing rules, forbidden words, AI-tells): `**/Wiki/Style/review_guide.md` or legacy `**/Wiki/Style/Review Guide.md`
- **Style guide** (writing voice, POV): `**/Wiki/Style/style_guide.md` or legacy `**/Wiki/Style/Style Guide.md`
- **Characters** (voices, relationships): `**/Wiki/Characters/**/*.md` (one file per character)
- **World** (setting, rules): use the book's own world-layout convention when its instructions define one (for example `**/Wiki/World/**/*.md`); otherwise fall back to `**/Wiki/Locations/**/*.md`, `**/Wiki/Systems/**/*.md`, `**/Wiki/Organizations/**/*.md` — capture the Wiki root directory path
- **Outline** (chapter purposes and trope obligations): `**/Wiki/Outline/**/outline.md`
- **Surprise ledger** (planned divergences, when the divergence pass ran): `**/Wiki/Outline/Book-N/surprise-ledger.md` for the selected book, when present
- **Scene plan**: the book's established beat or scene file for the reviewed chapter, when present
- **Promise ledger** (the Chekhov ledger): `**/Wiki/Story/Book-N/promises.yaml` for the selected book, when present (maintained by `fiction-promises`)

Also find the previous chapter (for continuity checking).

Also locate these genre contract files:
- **Genre file**: search for `**/Wiki/Style/genre.md`
- **Synopsis** (for the trope payoff plan): `**/Wiki/Story/synopsis.md` (series) or the per-book `**/Wiki/Story/Book-N/synopsis.md`, whichever exists

**Do NOT read these files.** Just get their paths.

## Step 2: Launch the Review Worker

When the host supports isolated workers, start one with the description `Review latest chapter of [WorkingTitle]` and give it everything from the **"## Worker Instructions"** section below, replacing the placeholders:
  - `{{CHAPTER_PATH}}` → the chapter to review
  - `{{PREV_CHAPTER_PATH}}` → previous chapter path, or "not found"
  - `{{REVIEW_PATH}}` → `Wiki/Style/review_guide.md` or legacy `Wiki/Style/Review Guide.md` path, or "not found"
  - `{{STYLE_PATH}}` → `Wiki/Style/style_guide.md` or legacy `Wiki/Style/Style Guide.md` path, or "not found"
  - `{{CHARACTERS_DIR}}` → `Wiki/Characters/` directory path, or "not found"
  - `{{WIKI_DIR}}` → Wiki root directory path, or "not found"
  - `{{OUTLINE_PATH}}` → `Wiki/Outline/**/outline.md` path, or "not found"
  - `{{SURPRISE_LEDGER_PATH}}` → the book's `surprise-ledger.md` path, or "not found"
  - `{{SCENE_PATH}}` → scene plan or beat source for this chapter, or "not found"
  - `{{LEDGER_PATH}}` → the book's promises.yaml ledger path, or "not found"
  - `{{GENRE_PATH}}` → `Wiki/Style/genre.md` path, or "not found"
  - `{{SYNOPSIS_PATH}}` → `Wiki/Story/synopsis.md` path, or "not found"
  - `{{WORKING_TITLE}}` → the working title
  - `{{WORKING_DIR}}` → the current working directory

If isolated workers are unavailable, or if you are already the dedicated worker for this task, follow the same instructions directly.

## Step 3: Save and Present Results

When the worker returns:
1. Save the review to `_Edits/Book-N/Chapter-NNN_Review.md` — the same `Book-N` folder level as the chapter's `Chapters/Book-N/` location, three-digit chapter number (create `_Edits/Book-N/` if it doesn't exist). Older projects that keep chapters at `_Edits/` root may keep reviews there.
2. Display the full review with actionable edits.
3. Offer: "Would you like me to apply these edits (via `fiction-revise`, which verifies every quote and keeps a change ledger), plan the next chapter, or return to the outline?"
4. If the user wants edits applied, route to `fiction-revise` with the approved item numbers — do not edit the chapter from the review pass directly.

---

## Worker Instructions

You are reviewing the most recently written chapter for revision opportunities.

**Working directory**: `{{WORKING_DIR}}`

### Step 1: Read Project Files

**Required**: Read `{{CHAPTER_PATH}}`

**Also read if they exist**:
- `{{PREV_CHAPTER_PATH}}` - for continuity checking
- `{{REVIEW_PATH}}` - forbidden phrases, AI-tells, mechanical checklist (primary editing reference)
- `{{STYLE_PATH}}` - POV, voice, character voices (for context only)
- `{{CHARACTERS_DIR}}` and `{{WIKI_DIR}}` - search the entire book Wiki for the proper nouns and canon claims actually present in the chapter or scene plan; read the supporting files, not every file by default
- `{{OUTLINE_PATH}}` - chapter purposes, and the reviewed chapter's `trope_obligations` entry: which tropes this specific chapter owes and in which treatment
- `{{SURPRISE_LEDGER_PATH}}` - planned divergences and chosen defaults per act (if found)
- `{{SCENE_PATH}}` - required choices, consequences, emotional movement, motifs, arc movement, genre beats, and other chapter-specific obligations
- `{{LEDGER_PATH}}` - the Chekhov ledger: setups awaiting payoff (audit in Step 6)

**Genre contract files** (read if found):
- `{{GENRE_PATH}}` — if not "not found", read it and extract:
  - `## Core Tropes` — each mandatory trope name and description
  - `## Genre-Specific Craft Notes` — rules for this genre (what to always do, what to never do)
  - `## Reader Expectations` — especially the Resolution field (HEA/HFN requirement, tragic ending rule, etc.)
  If one of these headings is absent, extract the same content from whatever heading carries it — projects rename these sections (e.g. `## Trope Commitments` for core tropes). A renamed heading is not a missing genre contract.
- `{{SYNOPSIS_PATH}}` — if not "not found", read it and extract `## Trope Payoff Plan` (each trope's role and its setup/development/payoff). Older projects may carry the same contract under `## Genre Architecture` with Contract Validation / Mandatory Beat Sequence / Twist Map tables — read whatever section carries the trope contract.
- `{{SURPRISE_LEDGER_PATH}}` — if not "not found", read the act entries covering this chapter: planned divergences (and chosen defaults) are this project's twist schedule.

Store everything extracted from these files as the **genre contract** for this review. If `{{GENRE_PATH}}` is "not found", genre compliance checking is skipped.

If files are missing, note which criteria cannot be fully evaluated.

### Step 2: Read References

Read:
- [references/review-criteria-detailed.md](references/review-criteria-detailed.md)
- [references/common-issues.md](references/common-issues.md)
- [references/panel-harvest-criteria.md](references/panel-harvest-criteria.md) — failure modes harvested from full-panel persona reads; check each against the chapter

### Step 3: Build Review Context

**From review.md (primary):**
- Forbidden phrases and words
- Crutch words, punctuation rules, triadic list ban
- Dialogue tag rules
- Protagonist voice check questions

**From style.md (context):**
- POV character and voice requirements
- Genre-specific expectations
- Pacing guidelines

**From character files (`Wiki/Characters/`):**
- Speaking patterns and verbal tics
- Relationship dynamics
- Character motivations

**From world files (the book's world-layout folders — e.g. `Wiki/World/` when its instructions define that, else legacy `Wiki/Locations/`, `Wiki/Systems/`, `Wiki/Organizations/`):**
- Setting rules and constraints
- Location details
- Cultural rules

### Step 4: Evaluate Against 10 Criteria

1. **POV Voice & Agency** - Is voice present? Are they active?
2. **Scene-Plan Delivery & Plot Advancement** - Are the required choices, consequences, chapter-specific obligations, and ending movement present without becoming mechanical?
3. **Continuity Check** - Flows from previous? No contradictions?
4. **Character Authenticity** - Voices match? Consistent behavior?
5. **Reader Appeal & Genre Fit** - Meets expectations? Right pacing?
6. **Plot Logic** - No holes? Decisions make sense?
7. **Sensory Atmosphere** - Setting present? Physical sensation?
8. **World-Building Accuracy** - Locations correct? Rules followed?
9. **Style Guide Compliance** - No forbidden phrases? Format correct?
10. **Genre Compliance** - See detailed instructions below.

#### Criterion 10: Genre Compliance

Only evaluate this criterion if `{{GENRE_PATH}}` was found and the genre contract was successfully extracted. If the genre file was not found, skip this criterion entirely and note: "Genre file not found — genre compliance check skipped."

Check each of the following:

**A. Mandatory trope delivery**: For each mandatory trope from the genre contract, determine whether this chapter advances, establishes, or satisfies it. If a mandatory trope has no evidence in this chapter AND the outline position suggests it should have appeared by now, flag it as at risk or falling behind.

**B. Chapter trope obligations**: Check the reviewed chapter's `trope_obligations` entry in the outline (each trope the outline assigns to this chapter, with its treatment — setup / development / payoff / texture / subversion). Determine whether the chapter delivers each assigned obligation fully, partially, or not at all. Flag missing or partial obligations.

**C. Genre craft rule violations**: Check the chapter against every rule in `## Genre-Specific Craft Notes`. Flag each violation specifically — quote the offending passage and name the rule broken.

**D. Resolution trajectory**: If the genre requires HEA or HFN (from `## Reader Expectations`) and this is the final chapter, verify it delivers. If the genre forbids a tragic ending and this chapter ends tragically, flag it as a contract breach.

**E. Scheduled divergence**: If the surprise ledger plans a divergence for this chapter or its act, check whether the chapter delivers it and whether it lands with sufficient setup. Older projects may carry a `### Twist Map` table in the synopsis instead; use whichever exists.

Output this section in the review report using the following format:

```markdown
## Genre Compliance

**Genre:** [subgenre from genre.md]
**Trope Obligations for This Chapter:** [from the outline entry's trope_obligations, or "none assigned"]
**Obligation Delivered:** Yes / No / Partial — [one sentence explanation per assigned trope]

**Trope Tracking:**
| Trope | Status in This Chapter | Cumulative State |
|-------|----------------------|-----------------|
| [Trope name] | advances / absent / established / at risk | on track / falling behind / complete |

**Craft Rule Violations:** [bulleted list of violations with quoted passage and rule name, or "none found"]
**Divergence Scheduled Here:** [from the surprise ledger, or "none"]
**Resolution Trajectory:** [flag if contract breach, or "on track" or "not yet applicable"]
```

### Step 5: Audit the chapter's canon assertions

Extract every specific canon fact the chapter asserts: proper nouns (people, places, organizations, items, events), dates and durations, counts and distances, injuries and physical states, possessions, and relationship or knowledge facts new to this chapter. For each assertion, search the book Wiki and the scene plan for the source that establishes it. An unsupported assertion is a finding, not texture: flag it with the line reference, the missing source, and a fix — name the canonical fact, replace the specific with an accurate generic description, or mark it for canonization. The draft itself, a previous chapter, and general memory are not evidence. Report unsupported assertions among the Proposed Edits tagged `[Canon]`.

References to the book's own past are canon assertions too. Every callback to a specific prior moment — "as she had promised in the tower," "the wound from the river crossing," "what he said at the funeral" — must be verified against the chapter or scene where the moment supposedly happened: the moment exists, and it happened as this chapter describes. A false callback is worse than an unsupported detail. The book trains readers to trust its references; one check that pays out empty dents the trust everywhere else. Flag the false callback with both locations — where the callback claims, and what the claimed source actually says.

### Step 6: Audit the Chekhov ledger

If `{{LEDGER_PATH}}` is "not found", skip this step and note: "No promise ledger found — run `fiction-promises` to start tracking setups." Otherwise read the whole ledger and:

1. **Harvest new promises.** Read this chapter as a reader, not as the author — what did it tell you to remember? An object introduced with more detail than the scene needs, a question asked and left, a skill mentioned in passing, a threat, a debt, a stranger named with weight. Add each to the ledger with: `promise` (reader-side phrasing, e.g. "the locked drawer in Elena's study"), `introduced_ch`, `kind`, `weight` (whisper/plain/loud), and a required `payoff_by_ch` — an undated promise is one nobody will remember to pay. If the honest answer is "not this book", set `deferred_to_series: true` and confirm it appears in the inter-book promise map in `Wiki/Story/series-arc.md`.
2. **Record payoffs.** Anything this chapter pays on the page gets `paid_in_ch` and `paid_how` — both fields or neither. A payoff must be on the page: a gun that goes off in the author's head between chapters is still loaded.
3. **Report what's due.** In the review output, list OVERDUE (payoff_by_ch earlier than the next chapter), DUE NEXT CHAPTER, and undated promises. Overdue means the reader is already owed this: either it is paid in the next chapter or the payoff is deliberately re-planned and the date moved with a note in the ledger. Silently moving a deadline is how a promise stays permanently eighteen chapters away. Report ledger changes among the Proposed Edits tagged `[Ledger]`.

### Step 7: Verify Every Claim on the Page

Before an issue may be listed as actionable, verify it against the chapter's text: quote the exact offending line from the file and confirm the quote is really there, word for word. Drop any finding whose premise cannot be verified on the page — a device the chapter does not contain, a line that does not exist, a fact recorded in a prior review but absent from the current text. Reviews inherit each other's false premises; an unverified finding costs a triage pass and can send the revision the wrong way.

When the project keeps a record of prior rulings and fixes, let the record govern dispositions (what has already been ruled, and why) but let the page govern facts: re-derive every count, date, and quotation from the current text instead of trusting a prior verification.

Separate compliance from craft. A line that violates the style guide is a compliance finding. A line that complies with the guide but would genuinely read better changed is a craft proposal: report it with before/after text and a recommendation, clearly marked as a proposal, and leave the decision to the author. Do not dismiss a craft proposal just because the guide permits the line, and do not apply one unilaterally.

### Step 8: Generate Actionable Output

This is an EDITING PASS. For each issue found:

1. **Issue**: What's missing or weak (with line reference)
2. **Fix**: Specific text to revise
3. **Example**: Draft improved version

**Final output:**
- **Proposed Edits**: Numbered list with locations
- **New Lines to Add**: Draft text ready to insert
- **Lines to Cut**: What weakens the chapter

Do NOT provide ratings. Provide actionable edits.

Return the complete review report.
