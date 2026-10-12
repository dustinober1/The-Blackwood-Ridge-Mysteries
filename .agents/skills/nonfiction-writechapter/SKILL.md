---
name: nonfiction-writechapter
description: "Draft a non-fiction chapter from an established chapter plan. Explanatory clarity, signposting, concrete examples, varied evidence types. Follows the chapter plan's argument architecture. Use when the user asks to write a chapter or continue writing; use nonfiction-chapter-plan when the chapter's argument structure is not yet settled."
metadata:
  author: Nonfiction Toolkit
  version: "1.0.1"
  category: nonfiction-writing
  output-format: markdown
---

# Nonfiction Write Chapter

Draft the assigned chapter as finished prose. The book's instructions and chapter plan own the argument architecture; this skill executes the draft without redesigning the argument.

## Authority and scope

Use this order of authority:

1. The user's current instructions.
2. The book's `AGENTS.md`, `CLAUDE.md`, and applicable nested instructions.
3. The book's established source and filename conventions.
4. The book's chapter plan, outline, style guide, and voice guidance.
5. This skill's generic defaults.

Read the book instructions before writing. Do not create a new argument direction, planning artifact, review report, or parallel chapter directory. If the assigned chapter lacks a sufficient chapter plan to draft without inventing its argument, stop and recommend `nonfiction-chapter-plan` for that chapter.

## Identify the chapter and destination

Use the project or chapter named by the user. Otherwise infer the selected book from the current working context and project tracking files; if multiple books remain plausible, ask which one.

Resolve the book root, target chapter plan, target outline entry, style guide, voice guidance, previous authoritative chapter, and exact output path. Read the outline only when it adds information missing from the chapter plan.

Follow neighboring chapter filenames and the book's instructions. When no local convention exists, use `<book-root>/Chapters/Chapter-[NNN].md` and put the title inside the Markdown file. Never create `[WorkingTitle]_Chapters` or another independently editable copy.

## Use a focused writing worker

When isolated workers are supported, use one focused worker for the chapter so its context contains only relevant book material. Give it the resolved paths and the instructions below. If workers are unavailable, follow the same instructions directly.

Pointing a worker at a rules file does not make that file binding: naming only some mechanical rules in the brief turns the unnamed ones into a whitelist the worker is free to violate. In every drafting brief, either quote every binding mechanical rule from the style and review guides verbatim, or state that every rule in those files is binding whether or not the brief quotes it. After the draft returns, search the prose for the rules the brief did not name before accepting the completion check — the worker's own compliance tally will mirror what the brief named.

## Worker instructions

Write the assigned chapter as finished prose.

### Read only drafting context

Read, in this order:

1. Relevant current-status and continuity sections from project tracking files.
2. The target chapter plan (claim, evidence blocks, transitions, reader takeaway).
3. The target outline entry only when the chapter plan does not fully state the required outcome.
4. The style guide and voice guidance. Treat the stricter book-specific rule as binding.
5. The previous authoritative chapter for immediate continuity (terminology, defined terms, argument threads).
6. Key sources cited in the chapter plan for accuracy verification.

Do not load the entire research corpus, bibliography, or all chapter plans by default. Retrieve additional context only when an evidence block, continuity question, or proper noun requires it.

Before drafting, extract a compact working brief:

- Voice, tone, and register constraints;
- Opening: the claim and stakes established immediately;
- Required evidence blocks in order with their turns;
- Facts and defined terms carried from previous chapters;
- Named concepts, studies, figures, and canon terms the chapter expects.

The chapter plan has already decided argument architecture. Honor its required claim, evidence blocks, turns, transitions, and synthesis. You may shape connective prose, illustrative examples, local signposting, and sentence-level clarity, but do not replace the plan with a new argument.

### Research every proper noun and citation in the chapter plan

Every proper noun, study, statistic, quote, and specialized term used in the chapter must be verified against the book's research corpus or the chapter plan's cited sources. This includes:

- Researchers, authors, historical figures, institutions
- Study names, experiment labels, dataset names
- Theoretical frameworks, model names, coined terms
- Statistics, percentages, dates, measurements
- Quotes and their exact wording and attribution

For each planned reference:

1. Search the book's research files recursively.
2. Read the supporting context.
3. Confirm exact spelling, capitalization, numbers, attribution, and facts relevant to this chapter.

The book's own research corpus is the only authority. A previous chapter, another book's files, general memory, or the draft itself is not sufficient evidence. Do not guess, silently invent, or import a name. If an unsupported reference is not essential, use an accurate generic description. If replacing it would materially alter the chapter plan, report the missing canon and do not mark the chapter complete.

### Draft the prose

Use the book's requested length; otherwise aim for roughly 2,500–4,000 words for a full argument chapter. Follow the project's chapter-heading and section-break conventions.

**Structure requirements from the plan:**

- Open with the **claim** and **stakes** — the reader must know what's being proven and why it matters.
- Each **evidence block** becomes a major section (or subsection) with:
  - Clear signpost: "To prove [sub-claim], we examine [evidence type]..."
  - The concrete evidence presented with precision (study design, quote context, data specifics).
  - The **turn** rendered as insight, not announcement: show the reversal/complication/synthesis through the evidence itself.
  - Explicit **transition** to the next block: "This [finding/complication] forces us to ask..." or "But [evidence] only holds if [assumption]..."
- Close with the **synthesis** — the new understanding, not a summary.
- Deliver the **reader takeaway** and **forward hook** as the final beats.

For ready-made evidence-presentation templates (narrated study, data-first, integrated quote, and the variety rule), read [references/evidence-presentation.md](references/evidence-presentation.md).

**Clarity mechanics (apply throughout):**

- **Signpost every move:** "We argue X because Y." "This matters because Z." "Having shown A, we now turn to B."
- **Concrete before abstract:** Lead with the specific study, case, number, quote — then generalize.
- **Vary evidence presentation:** Don't stack three studies the same way. Mix: one narrated experiment, one quoted expert, one data visualization description, one historical scene.
- **Define terms at point of use:** Not in a glossary, not upfront — when the term first does argumentative work.
- **Active cognitive stance:** "We find," "The data show," "This implies" — not "It is found that," "It has been shown."
- **Calibrated certainty:** Match language to evidence strength. "Suggests," "indicates," "is consistent with" for correlational; "demonstrates," "establishes" for causal.
- **Counter-argument integration:** When the plan includes a counter-argument block, steel-man it fully before the rebuttal. The reader must feel the force of the objection.

For a pattern library of signposting moves (openings, block transitions, complication reversals), read [references/signposting-patterns.md](references/signposting-patterns.md).

**End with forward movement:** The final paragraph must land the synthesis and instantiate the forward hook — the specific question, stakes escalation, or practical imperative that pulls the reader to the next chapter.

### Verify before saving

Perform a focused completion check, not a full editorial review:

1. Confirm every required evidence block, turn, and transition from the plan is present.
2. Confirm voice, tone, register, terminology consistency, and defined-term usage.
3. Scan the title and prose for every proper noun, study name, statistic, and quote. Verify each against the research corpus and chapter plan citations. Correct every unsupported or inconsistent use.
4. Remove analytical drafting language ("in this section we will," "as discussed above," "the next section shows") — replace with argumentative signposting.
5. Verify every exact count, percentage, date, and quotation against the source. Recast any assertion the source disproves; never adjust the source to fit the count.
6. Scan for verbatim duplication: a sentence or block rendered twice in near-identical form. A deliberate callback varies its framing; an artifact repeats. Cut the artifact copy.
7. Check signposting density: every major transition must be explicitly marked. No "hidden" argument moves.

Leave broader prose diagnosis, clarity editing, and fact-checking to `nonfiction-clarity-edit` and `nonfiction-factcheck`.

## Save and hand off

Save only to the resolved authoritative chapter path. Do not overwrite a different existing chapter or create a parallel manuscript copy.

Update project tracking minimally:

- Last written chapter, next chapter, title, and word count;
- Concrete continuity created or changed: defined terms, argument threads, open questions, key citations;
- Unresolved canon questions that affected drafting.

Do not recalculate argument architecture, evidence strategy, or chapter necessity during the writing pass unless the book's own instructions explicitly require that update. Those are planning and review judgments.

Return the chapter path, title, word count, and any genuine canon blocker. Offer the next appropriate action: fact-check this chapter, clarity-edit this chapter, plan the next chapter, or continue writing when its chapter plan already exists.
