---
name: reader-persona-review
description: "Run qualitative, persona-driven reader critiques on drafted chapters or full book exports across diverse archetypes, panel presets, and criteria, generating structured critique reports and panel synthesis. Use when the user asks for 'reader persona review', 'persona feedback', 'reader test', 'panel review', 'what would readers think', 'check pacing with personas', or 'anti-AI audit with reader personas'."
metadata:
  author: Storycraft Skills
  version: "1.0.0"
  category: cross-cutting
---

# Reader Persona Review

A multi-perspective qualitative review skill that evaluates drafted chapters or full manuscript exports through distinct reader archetypes. It uncovers pacing drags, mystery/fairness issues, character resonance, genre expectation alignment, and machine-cadence tells without leaking bibles or spoilers.

## Core Principles

1. **Strict Information Boundary:**
   - Reader/critic personas receive *only* reader-facing text: `Chapters/Book-N/Chapter-NNN.md` or exported `manuscript-combined.md`, plus title/blurb if testing packaging.
   - Reader personas **never receive** canon bibles, scene briefs, secret mission locks, or story outlines.
   - Only Craft & Continuity / Industry personas (Group D, E, F) may inspect bibles and world rules.
2. **Authentic Voice & Discipline:**
   - The review is voiced in the persona's authentic perspective, vocabulary, tolerance level, and biases.
   - Hostile or critical personas remain rigorous and fair, not cartoonish strawmen.
   - Every critique must be anchored by specific chapter and line/sentence citations.
3. **Chunked Chapter-by-Chapter Context Discipline:**
   - When evaluating an entire book or multiple chapters, evaluate chapter-by-chapter with a running brief to prevent context degradation.
4. **Standardized Panel Synthesis:**
   - Synthesize reviews into consensus findings (flagged by 3+ personas), polarizing reactions (split by 3+ rating points), and actionable singletons.

---

## Panel Presets

Load personas from `references/personas.md` or project-local `docs/reader-personas/personas.md`.

- **Quick Pulse (8 personas):** Rapid scan across core archetypes.
  - `R01` (Avid Cozy/Trad Mystery Reader)
  - `R05` (Pacing & Momentum Skeptic)
  - `M01` (Plot Fairness & Puzzle Tracker)
  - `M02` (Character Arc & Emotional Resonance Seeker)
  - `A01` (Cadence & Machine-Tells Auditor)
  - `L01` (Prose Stylist / Literary Sensitivity)
  - `I02` (Commercial Fiction Editor)
  - `H01` (Casual Audiobook / Commute Listener)
- **Standard Panel (16 personas):** Broad audience cross-section before revising.
- **Anti-AI Authenticity Sweep (A01–A06):** Deep dive on artificial cadence, tricolons, "not X but Y", neat aphorisms, and emotional tell repetition.
- **Series Continuity & Craft Panel (M01, K01–K06, F01–F03):** Verified checks on fair clues, continuity, and internal logic.
- **Pre-Release Packaging & Blurb Test:** Testing blurb, hook, and opening chapter alignment.

---

## Procedure

### Step 1: Identify Target & Review Scope
1. Determine the target book and chapter(s):
   - Single chapter: `Chapters/Book-N/Chapter-NNN.md`
   - Whole book / Act: `Chapters/Book-N/` or compiled export `export/manuscript-combined.md`.
2. Confirm the panel selection (preset or specified list of persona IDs).
3. Confirm prior knowledge constraint (Cold start vs. Series veteran).

### Step 2: Run Persona Review(s)
For each persona in the selected panel:
1. Load persona definition from `references/personas.md` (or project persona library).
2. Read the chapter text through the persona's lens.
3. Evaluate the persona-specific checklist:
   - Does the opening grab them?
   - Where did their attention wander?
   - Did any sentence feel unearned, repetitive, or artificial?
   - Did the ending satisfy their reading goal?
4. Generate the report following the standard schema:

```markdown
# [Persona Name] ([ID]) — Book [N], [Chapter/Full]: [Title]
**Entry point:** [Cold / Read Book 1 / etc.]  **Format:** [Print / Ebook / Audio]
**Stars:** ★☆☆☆☆ to ★★★★★  **Would read next?** [Yes / Maybe / No]  **Recommend?** [Yes / Maybe / No]
**DNF point (if any):** [None / Chapter-NNN at line/beat because...]

## Gut Reaction
[3–5 sentences in the persona's authentic voice]

## What Worked
- [Specific beat, quote, or line citation + why it resonated]

## What Didn't
- [Specific drag, artificial cadence, plot cheat, or flat characterization with citation]

## Persona Checklist & Tells Audit
- [Checklist item]: [Result: Clean / Present / Warning] — "[Quoted excerpt]"

## Public Review Draft
"[The review (80–200 words) this reader would post on Goodreads/Amazon/StoryGraph]"

## The One Change That Flips My Rating
[Single highest-leverage adjustment that would increase their score]
```

Save individual reports under:
`_Edits/Book-N/reviews/[ID]_[Chapter/Book].md` or `books/book-NN/reviews/[ID].md`.

### Step 3: Multi-Persona Panel Synthesis
When running 3 or more personas, compile `_synthesis.md`:

1. **Scoreboard & Aggregate Metrics:**
   - Average star rating, DNF frequency, completion enthusiasm.
2. **Consensus Flags (3+ personas agree):**
   - Universal strengths to protect.
   - Pervasive friction points, pacing dead zones, or recurring tells.
3. **Polarizing Elements (3+ star spread):**
   - Elements some readers loved but others hated (e.g., slow atmosphere vs. stagnant pacing).
4. **Actionable Revisions:**
   - Prioritized list of structural and prose revisions categorized by impact.
