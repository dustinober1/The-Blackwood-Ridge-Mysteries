---
name: nonfiction-audience
description: "Map reader's current knowledge, objections, and required prerequisites. Use when user says 'define audience', 'who is this for', 'target reader', 'reader profile', 'prerequisites', or before running nonfiction-concept."
metadata:
  author: Nonfiction Toolkit
  version: "1.1.0"
  category: nonfiction-writing
  output-format: markdown
---

# Nonfiction Audience Definer

**Output:** `Wiki/Concept/audience.md` in the project's `Wiki/` folder. All inputs come from `Wiki/` Markdown files; all output is written back into `Wiki/`.

## Step 1: Locate the Project and Load Context

The project may live in a subfolder, so search for:

- `**/Wiki/Concept/thesis.md`: Optional (audience often runs right after concept; it exists by then in the standard workflow). For: thesis, reader_transformation, big_idea. If it exists, read it to ensure audience aligns with promised transformation.
- `**/Wiki/Concept/structure.md`: Optional. For: chosen architecture, which may imply audience sophistication level.

If no `Wiki/Concept/thesis.md` exists, proceed — audience definition can precede and inform the concept.

## Step 2: Gather User Input

Ask the user for the target reader profile using the host's normal question mechanism:

**Question, Target Reader Archetype:**
- **Practitioner** — Wants to apply this in their work tomorrow (engineers, managers, clinicians, designers)
- **Aspirant** — Wants to enter this field or level up (students, career changers, early-career)
- **Decision-Maker** — Needs to evaluate/buy/approve this (executives, investors, policy makers, buyers)
- **Curious Generalist** — Wants to understand this domain (educated layperson, interdisciplinary thinker)
- **Skeptic/Critic** — Needs to be convinced (academics, reviewers, competitors, regulators)
- **Not sure, recommend based on concept** — Derive from thesis and transformation

**Follow-up questions (ask sequentially):**
1. "What does your reader already know about this topic? (Novice / Some exposure / Practitioner / Expert)"
2. "What are their top 3 objections or reasons they'd put this book down?"
3. "What prerequisites must they have before page 1? (Tools, knowledge, access, mindset)"

## Step 3: Generate with an Isolated Worker When Available

To keep the main conversation context clean, use an isolated worker when the host supports one. Give it: the user's archetype choice and follow-up answers, the resolved paths to any existing Wiki files, the project root, and the full instructions in Steps 4 through 6 below. The worker writes the file and returns the full profile text for review.

If the host does not support isolated workers, or if you are already running as the dedicated worker for this task, do Steps 4 through 6 directly instead of delegating again.

## Step 4: Load Audience Reference

Read the archetype-specific reference file:

- Practitioner → [references/audience-practitioner.md](references/audience-practitioner.md)
- Aspirant → [references/audience-aspirant.md](references/audience-aspirant.md)
- Decision-Maker → [references/audience-decisionmaker.md](references/audience-decisionmaker.md)
- Curious Generalist → [references/audience-generalist.md](references/audience-generalist.md)
- Skeptic/Critic → [references/audience-skeptic.md](references/audience-skeptic.md)
- Not sure → [references/audience-archetype-matrix.md](references/audience-archetype-matrix.md) to match concept to archetype, then read that archetype's file

Always also read [references/audience-archetype-matrix.md](references/audience-archetype-matrix.md) to check for concept-archetype compatibility conflicts. Flag conflicts explicitly. For example:
- Highly theoretical thesis aimed at Practitioner (who needs immediate application) is a CONFLICT.
- Simplified framework aimed at Skeptic/Critic (who demands rigor) is a CONFLICT.
- Advanced prerequisites aimed at Aspirant (who lacks them) is a CONFLICT.

Extract from the archetype file: knowledge assumptions, objection patterns, prerequisite norms, structural expectations (depth, length, format), credibility signals needed.

## Step 5: Generate the Audience Profile

Cover every field in [references/json-schema.json](references/json-schema.json) as a frontmatter key or a `##` section. That schema is the field checklist only; the deliverable is Markdown.

Field derivation:

- **archetype**: Use the user's choice exactly. If "recommend", derive from concept thesis and transformation: immediate application → Practitioner; career entry → Aspirant; evaluation need → Decision-Maker.
- **knowledge_level**: Use the user's answer (Novice / Some exposure / Practitioner / Expert). If concept exists, verify alignment.
- **reader_persona**: One paragraph sketch: title/role, daily context, pain points, goals, how they consume information. Make it a specific person, not a demographic.
- **current_knowledge**: What they know *coming in*. List 5-8 specific concepts, tools, frameworks, or experiences they already have. Be concrete: "Knows what a REST API is" not "Knows APIs."
- **knowledge_gaps**: What they *don't* know but need to for the thesis to land. List 5-8 specific gaps. These become your explanatory burden.
- **objections**: Top 3-5 objections the reader brings. Each: `objection` (their words), `root_cause` (why they believe it), `book_response` (how your argument/evidence addresses it). Derive from user input + archetype patterns.
- **prerequisites**: What they must have *before page 1*. Categories: `knowledge`, `tools`, `access`, `mindset`, `time_commitment`. Each with `item` and `why_required`. If missing prerequisites block the transformation, flag in Compatibility Warnings.
- **credibility_signals**: What the reader needs to trust you. `authority` (credentials, experience), `social_proof` (case studies, testimonials), `rigor` (citations, data), `transparency` (limitations acknowledged), `practicality` (immediate applicability). List 3-5 specific signals for *this* book.
- **structural_expectations**: `depth_level` (overview / deep-dive / reference), `preferred_format` (narrative / framework / playbook / reference / hybrid), `chapter_length_words` [min, max], `total_word_count` [min, max], `visual_density` (low / medium / high), `actionability_ratio` (theory:practice balance as percentage).
- **compatibility_assessment**: Explicit compatibility check against concept (if exists) and archetype norms.

Write `Wiki/Concept/audience.md` in this shape (create the `Wiki/Concept/` folder if missing):

```markdown
---
archetype: Practitioner
knowledge_level: Practitioner
---

# Audience Profile

## Reader Persona
[One paragraph: title/role, daily context, pain points, goals, how they consume information. A specific person.]

## Current Knowledge
- [Specific concept/tool/framework/experience 1]
- [Specific concept/tool/framework/experience 2]
- ...
- [Specific concept/tool/framework/experience N]

## Knowledge Gaps
- [Specific gap 1 — what they don't know but need to]
- [Specific gap 2]
- ...
- [Specific gap N]

## Objections
### Objection 1
- **objection:** "[Reader's words]"
- **root_cause:** [Why they believe this]
- **book_response:** [How your argument/evidence addresses it]

### Objection 2
...

## Prerequisites
### Knowledge
- **item:** [Specific prerequisite knowledge]
- **why_required:** [Why the thesis fails without it]

### Tools
- **item:** [Specific tool/software/account]
- **why_required:** [Why the transformation requires it]

### Access
- **item:** [Specific access: people, data, environments]
- **why_required:** [Why the transformation requires it]

### Mindset
- **item:** [Specific belief/attitude]
- **why_required:** [Why the transformation requires it]

### Time Commitment
- **item:** [Hours/weeks required]
- **why_required:** [Why the transformation requires it]

## Credibility Signals
- [Signal 1: e.g., "10 years leading 200-person engineering orgs at Series B-D startups"]
- [Signal 2: e.g., "Framework used by 50+ companies including [names]"]
- [Signal 3: e.g., "Peer-reviewed study with n=500 showing 23% improvement"]
- [Signal 4: ...]
- [Signal 5: ...]

## Structural Expectations
- **depth_level:** [overview | deep-dive | reference]
- **preferred_format:** [narrative | framework | playbook | reference | hybrid]
- **chapter_length_words:** [min, max]
- **total_word_count:** [min, max]
- **visual_density:** [low | medium | high]
- **actionability_ratio:** [theory_percentage:practice_percentage]

## Concept-Audience Compatibility
- [Assessment: ALIGNED | TENSION | CONFLICT]
- [Specific tensions: e.g., "Thesis requires statistical literacy but audience is Practitioner with no stats background"]
- [Recommended adjustments: e.g., "Add statistical appendix; move formulas to footnotes; use visual intuition builders"]

## Compatibility Warnings
- [Only if conflicts detected: the specific conflict and a recommendation for adjusting either the concept scope or the audience target]
```

Frontmatter must be conservative YAML: block lists one item per line, never inline `[a, b]` lists in frontmatter, quote strings containing colons. The `[min, max]` pairs live in the body bullets, not the frontmatter.

**Hard rules:**
- Knowledge gaps and prerequisites are *specific*, not generic. "Knows Python" → "Can write a list comprehension; has used pandas; has debugged a KeyError."
- Objections must be in the *reader's voice*, not your interpretation. "This won't work for me" not "They doubt applicability."
- If prerequisites are substantial, the book must either teach them or explicitly gate the audience.
- If the audience work surfaces forbidden assumptions (e.g., "assumes US corporate context"), write them to `Wiki/Concept/assumptions.md` (one `- assumption: [context]` bullet per line).

## Step 6: Present and Confirm

Show the full profile to the user and ask: "What should I change?" Apply revisions by editing `Wiki/Concept/audience.md` in place. For large rewrites, use the same isolated-worker mechanism when available. Continue until approved.

When approved: "Next: use `nonfiction-concept` to define your book's central argument and transformation."
