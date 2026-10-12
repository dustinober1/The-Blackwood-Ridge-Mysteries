---
name: nonfiction-concept
description: "Define the book's central argument/thesis, target reader transformation, and 'big idea'. Use when user says 'define concept', 'what is this book about', 'central thesis', 'big idea', or when starting a non-fiction book."
metadata:
  author: Nonfiction Toolkit
  version: "1.1.0"
  category: nonfiction-writing
  output-format: markdown
---

# Nonfiction Concept Definer

**Output:** `Wiki/Concept/thesis.md` in the project's `Wiki/` folder. All inputs are read from `Wiki/` Markdown files; all output is written as Markdown. All work stays in the project's Markdown files.

## Step 1: Locate the Project and Load Context

The project may live in a subfolder of the working directory, so search for the upstream files:

- `**/Wiki/Concept/audience.md`: Recommended, not required — this skill runs first in the workflow. If it exists, read it for: target reader profile, knowledge level, objections, prerequisites. If missing, proceed; the concept can derive the reader from conversation, and `nonfiction-audience` pressure-tests it afterward.
- `**/Wiki/Concept/structure.md`: Optional. If it exists, read it for: chosen architecture, argument shape.

Treat the folder containing `Wiki/` as the project root. Read the frontmatter and `##` sections of each file that exists.

## Step 2: Load Reference Files

Read these craft knowledge files before generating:

- [references/argument-construction.md](references/argument-construction.md): how to build a central thesis that holds across a full book; what makes an argument deployable vs. abstract
- [references/transformation-mapping.md](references/transformation-mapping.md): how to define the reader's before/after state, what makes a transformation concrete and measurable
- [references/big-idea-frameworks.md](references/big-idea-frameworks.md): frameworks for identifying the "big idea" (one-sentence hook, unique mechanism, contrarian insight); how to differentiate from competing books

Extract: what makes a thesis load-bearing, what makes a transformation concrete and promise-able, how to find the unique angle in a crowded market.

## Step 3: Gather User Input

Ask the user for one piece of information using the host's normal question mechanism:

**Question:** "What is the one thing you want your reader to believe, understand, or be able to do after finishing this book? A sentence, a claim, a transformation — whatever you have. Or say 'derive from audience' and I'll build one from your reader's pain points and aspirations."

This question is intentionally open-ended. The concept skill pulls the core argument out of the writer.

## Step 4: Generate the Concept Engine

You may generate directly or, when the host supports one, use an isolated worker with the context gathered above to keep the main conversation clean; either way, apply the rules below. If the user provided a concept seed, build outward from their words and do not override their intent. If "derive from audience", build from the reader's stated problems and desired outcomes.

Cover every field in [references/json-schema.json](references/json-schema.json) as frontmatter or a section (checklist: thesis, reader_transformation, big_idea, unique_angle, core_promise, evidence_architecture).

**thesis**: A single declarative sentence — the central argument the book proves. If the user provided a seed, sharpen it into a claim that can be evidenced. If "derive from audience", build from the reader's most painful problem and the transformation you offer.

**reader_transformation**: The specific before/after state. Define:
- `from_state`: Where the reader starts (knowledge, belief, capability, pain)
- `to_state`: Where the reader ends (new knowledge, shifted belief, new capability, relief)
- `measure`: How the reader (or you) knows the transformation occurred — a concrete indicator, not a feeling

**big_idea**: The one-sentence hook that makes this book distinct in the marketplace. Format: "[Unique mechanism/insight] + [Reader outcome] + [Why it works]". Not a topic — a proposition.

**unique_angle**: What makes this argument different from the 50 other books on this topic. One paragraph: the contrarian insight, the missing step others skip, the synthesis nobody has made, the evidence nobody has gathered.

**core_promise**: What the reader gets if they do the work. One sentence, measurable, no fluff. "By the end of this book you will [specific outcome]."

**evidence_architecture**: The types of proof this argument will use (primary research, case studies, frameworks, data, personal narrative, expert interviews, historical analysis, counter-arguments addressed). List 3-6 types with one sentence each on why that evidence serves this thesis.

## Step 5: Save and Confirm

Write the result to `Wiki/Concept/thesis.md` under the project root found in Step 1. Create the `Wiki/Concept/` folder if it does not exist. `Wiki/Concept/thesis.md` is the single source of truth for concept; downstream skills (audience, structure, chapter-plan) read it from that exact path.

File shape:

```markdown
---
thesis: "The central argument as a single declarative sentence. Quote it; it may contain colons."
big_idea: "The one-sentence marketplace hook."
core_promise: "By the end of this book you will [specific outcome]."
---

## Reader Transformation

### From State
[Where the reader starts — knowledge, belief, capability, pain. 2-3 sentences.]

### To State
[Where the reader ends — new knowledge, shifted belief, new capability, relief. 2-3 sentences.]

### Measure
[Concrete indicator of transformation. Not a feeling. One sentence.]

## Unique Angle

[One paragraph: the contrarian insight, the missing step others skip, the synthesis nobody has made, the evidence nobody has gathered.]

## Evidence Architecture

### [Evidence Type 1]
[Why this evidence serves this thesis. One sentence.]

### [Evidence Type 2]
...

### [Evidence Type N]
...
```

Frontmatter must be plain, conservative YAML: scalar values only here, strings quoted when they contain colons. `##` sections for each major component so every field stays grep-able.

Then present the concept to the user in readable form (do not paste the raw file) and ask: "What should I change?"

If changes are needed, edit `Wiki/Concept/thesis.md` in place and re-present until approved.

When approved: "Next: use `nonfiction-structure` to choose and scaffold your argument architecture."
