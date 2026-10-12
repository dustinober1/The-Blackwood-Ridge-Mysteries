---
name: nonfiction-structure
description: "Choose and scaffold the argument architecture (problem-solution, chronological, conceptual, hybrid). Use when user says 'structure my book', 'choose architecture', 'organize chapters', 'argument structure', or after running nonfiction-concept."
metadata:
  author: Nonfiction Toolkit
  version: "1.1.0"
  category: nonfiction-writing
  output-format: markdown
---

# Nonfiction Structure Architect

**Output:** `Wiki/Concept/structure.md` in the project's `Wiki/` folder. All inputs are read from `Wiki/` Markdown files; all output is written as Markdown. All work stays in the project's Markdown files.

## Step 1: Locate the Project and Load Context

The project may live in a subfolder of the working directory, so search for the upstream files:

- `**/Wiki/Concept/thesis.md`: Required. For: thesis, reader_transformation, big_idea, evidence_architecture. If missing, tell the user: "No concept found. Run `nonfiction-concept` first."
- `**/Wiki/Concept/audience.md`: Required. For: archetype, knowledge_level, structural_expectations, prerequisites. If missing, tell the user: "No audience profile found. Run `nonfiction-audience` first."

Treat the folder containing `Wiki/` as the project root. Read the frontmatter and `##` sections of each file that exists.

## Step 2: Load Reference Files

Read these craft knowledge files before generating:

- [references/architecture-patterns.md](references/architecture-patterns.md): the four primary nonfiction architectures (problem-solution, chronological, conceptual, hybrid), their logic, when each fits, chapter-level templates
- [references/argument-mapping.md](references/argument-mapping.md): how to map thesis clauses to chapters; how to sequence for logical flow vs. pedagogical flow vs. narrative flow
- [references/chapter-design.md](references/chapter-design.md): chapter archetypes (frame, evidence, application, synthesis, transition), their internal structure, how to design for the reader's cognitive load
- [references/structure-templates.md](references/structure-templates.md): ready-to-adapt chapter grids for each architecture; act/part breakdowns; pacing guides

Extract: which architecture serves this thesis + audience; how to sequence evidence for maximum persuasion; how to design chapters that teach *and* argue.

## Step 3: Gather User Input

Ask the user for their structural preference using the host's normal question mechanism:

**Question, Architecture Preference:**
- **Problem-Solution** — Reader has a problem; book diagnoses it, then delivers the solution (best for Practitioner, Decision-Maker)
- **Chronological/Process** — Reader follows a timeline or process from start to finish (best for Aspirant, how-to)
- **Conceptual/Principle-Based** — Reader builds a mental model through principles (best for Generalist, Skeptic, frameworks)
- **Hybrid** — Combines two above (specify which: e.g., "Problem-Solution with Chronological case studies")
- **Not sure, recommend** — Derive from thesis type + audience archetype

**Follow-up (if Hybrid or Not sure):**
- "Should the book front-load the 'answer' (thesis first) or build to it (mystery structure)?"

## Step 4: Generate with an Isolated Worker When Available

To keep the main conversation context clean, use an isolated worker when the host supports one. Give it: the user's architecture choice, the resolved paths to `Wiki/Concept/thesis.md` and `Wiki/Concept/audience.md`, the project root, and the full instructions in Steps 5 through 7 below. The worker writes the file and returns the full structure text for review.

If the host does not support isolated workers, or if you are already running as the dedicated worker for this task, do Steps 5 through 7 directly instead of delegating again.

## Step 5: Select and Validate Architecture

**Selection Logic:**

| If Thesis Is... | And Audience Is... | Recommend Architecture |
|-----------------|-------------------|------------------------|
| "How to do X" (prescriptive) | Practitioner | Problem-Solution |
| "How to become X" (developmental) | Aspirant | Chronological/Process |
| "Why X works / The truth about X" (explanatory) | Generalist | Conceptual |
| "The evidence for/against X" (evaluative) | Skeptic | Conceptual (evidence-ordered) |
| "How to decide on X" (decision) | Decision-Maker | Problem-Solution (decision-framework variant) |
| Multi-clause thesis with distinct evidence types | Any | Hybrid |

**Validation Checks (must pass before generating):**
1. **Thesis Coverage**: Every clause in the thesis maps to at least one chapter/part
2. **Evidence Fit**: The evidence_architecture types from thesis.md are distributable across the chosen architecture
3. **Audience Alignment**: The architecture's cognitive demands match audience.knowledge_level and structural_expectations
4. **Transformation Path**: The chapter sequence moves the reader from audience.from_state → to_state with measurable milestones
5. **Prerequisite Ordering**: Prerequisites from audience.md are taught *before* they're needed (or explicitly gated)

If any check fails, report the conflict and recommend: architecture adjustment, thesis refinement, or audience rescoping.

## Step 6: Generate the Structure Scaffold

Cover every field in [references/json-schema.json](references/json-schema.json) as frontmatter or a `##` section.

**architecture**: One of: `problem_solution`, `chronological`, `conceptual`, `hybrid`. If hybrid, specify `primary` and `secondary`.

**thesis_clause_map**: Array mapping each thesis clause → chapter/part numbers. Ensures full thesis coverage.

**parts**: High-level divisions (3-5 typical). Each part: `title`, `purpose` (what this part achieves for the argument), `thesis_clauses_addressed`, `reader_milestone` (what transformation milestone the reader reaches).

**chapters**: One entry per planned chapter (12-24 typical). Each chapter:

- `chapter_number`: Sequential integer
- `title`: Working title (evocative, not generic)
- `chapter_type`: `frame` | `evidence` | `application` | `synthesis` | `transition` (see chapter-design.md)
- `thesis_clause`: Which thesis clause this chapter advances (primary)
- `evidence_types`: Which evidence types from thesis.md deploy here
- `reader_milestone`: Micro-transformation — what the reader can now do/think/see
- `key_frameworks`: Named frameworks/models introduced here (max 2)
- `exercises_or_artifacts`: What the reader produces/uses (templates, checklists, decisions)
- `opens_with`: Hook (question, story, paradox, data, scene) — 1 sentence
- `closes_with`: Bridge to next chapter — 1 sentence
- `cognitive_load`: `low` | `medium` | `high` (for pacing)
- `prerequisites_required`: From audience.prerequisites — what must be true before this chapter

**pacing_notes**: Where to accelerate, where to scaffold, where to reflect. Flag any "cognitive cliffs" (high-load chapters back-to-back).

**navigation_aids**: Planned: part overviews, chapter summaries, "start here if..." guide, framework index, template index.

Write `Wiki/Concept/structure.md` in this shape (create the `Wiki/Concept/` folder if missing):

```markdown
---
architecture: problem_solution | chronological | conceptual | hybrid
primary_architecture: [if hybrid]
secondary_architecture: [if hybrid]
thesis_clause_map:
  - clause: "[Thesis clause 1]"
    chapters: [1, 2, 3]
  - clause: "[Thesis clause 2]"
    chapters: [4, 5, 6]
---

# Structure Scaffold

## Architecture Rationale
[2-3 paragraphs: why this architecture serves this thesis + audience; what alternatives were considered and rejected; how the architecture enables the reader transformation]

## Part Breakdown

### Part I: [Title]
- **Purpose:** [What this part achieves for the argument]
- **Thesis Clauses:** [Which clauses addressed]
- **Reader Milestone:** [Transformation milestone at part end]
- **Chapters:** [Chapter numbers]

### Part II: [Title]
...

## Chapter Grid

| Ch | Title | Type | Thesis Clause | Evidence Types | Reader Milestone | Frameworks | Artifacts | Load | Prereqs |
|----|-------|------|---------------|----------------|------------------|------------|-----------|------|---------|
| 1  | [Title] | frame | [Clause] | [Types] | [Milestone] | [Names] | [Items] | L/M/H | [List] |
| 2  | [Title] | evidence | ... | ... | ... | ... | ... | ... | ... |
...

## Pacing Notes
- [Acceleration zones: e.g., "Chapters 3-4 are high-load; insert reflection pause after Ch 4"]
- [Scaffolding zones: e.g., "Chapters 1-2 front-load prerequisites from audience.md"]
- [Cognitive cliffs: e.g., "Chapters 8-9 both high-load; consider splitting or inserting synthesis chapter"]

## Navigation Aids
- **Part Overviews:** [Yes/No — 1-page framing at each part start]
- **Chapter Summaries:** [Yes/No — 3-bullet recap at each chapter end]
- **Start Here Guide:** [Yes/No — for readers with different entry points]
- **Framework Index:** [Yes/No — alphabetical list with chapter refs]
- **Template/Artifact Index:** [Yes/No — every steal-this item with chapter]

## Validation Checklist
- [ ] Every thesis clause mapped to chapters
- [ ] Every evidence type from thesis.md deployed
- [ ] Audience prerequisites taught before needed
- [ ] Reader milestones form coherent transformation arc
- [ ] Chapter types vary (not all evidence, not all application)
- [ ] Cognitive load distributed (no 3+ high-load in a row)
- [ ] Part milestones align with the concept's reader-transformation milestones
- [ ] Architecture serves thesis, not vice versa
```

Frontmatter must be conservative YAML: block lists only, quote strings with colons. The chapter grid is a Markdown table for readability; each chapter also gets a `## Chapter NN: Title` section below the table with full detail.

Then present the structure to the user in readable form (show the rationale, part breakdown, and chapter grid) and ask: "What should I change?"

If changes are needed, edit `Wiki/Concept/structure.md` in place and re-present until approved.

When approved: "Next: use `nonfiction-chapter-plan` to turn each chapter's entry into a writable chapter plan."

## Step 7: Detailed Chapter Sections (Below Grid)

After the chapter grid table, write a `## Chapter NN: Title` section for each chapter with:

```markdown
## Chapter 01: [Title]

- **chapter_number:** 1
- **chapter_type:** frame | evidence | application | synthesis | transition
- **thesis_clause:** [Primary clause advanced]
- **evidence_types:** [List from thesis.md]
- **reader_milestone:** [Micro-transformation]
- **key_frameworks:** [Named frameworks/models, max 2]
- **exercises_or_artifacts:** [Templates, checklists, decisions, outputs]
- **opens_with:** [Hook: question / story / paradox / data / scene]
- **closes_with:** [Bridge to next chapter]
- **cognitive_load:** low | medium | high
- **prerequisites_required:** [From audience.prerequisites]
- **what_must_happen:** [Directive: what this chapter must show/teach/prove. 3-5 sentences. Imperative.]
- **argument_function:** [How this chapter advances the thesis: poses / evidences / complicates / synthesizes / applies]
- **audience_service:** [How this chapter serves the archetype: quick win / mental model / decision tool / narrative payoff / rigor]
```

This detailed section is the writer's brief for each chapter.
