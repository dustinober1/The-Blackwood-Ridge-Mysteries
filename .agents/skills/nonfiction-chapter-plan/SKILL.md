---
name: nonfiction-chapter-plan
description: "Create or revise non-fiction chapter plans. Each chapter's claim, evidence, transition, and reader takeaway. The non-fiction equivalent of fiction-scenes/psych — replaces beat sheets with argument architecture. Use when structuring a chapter's logical flow before drafting."
metadata:
  author: Nonfiction Toolkit
  version: "1.0.1"
  category: nonfiction-writing
  output-format: markdown
---

# Nonfiction Chapter Plan

Turn a chapter's core argument into a rigorous, writable plan. Every chapter must earn its place by advancing the book's central thesis through claim, evidence, and synthesis — not merely covering a topic.

## Authority and destination

Use this order of authority:

1. The user's current instructions.
2. The book's `AGENTS.md`, `CLAUDE.md`, and nested instructions.
3. The project's established source of truth and file conventions.
4. This skill's generic defaults.

Do not impose Wiki-only storage, integer numbering, or `Chapter_XX_Plan.md` when the project uses decimal or interlude chapters, or a different planning convention. An explicit output path wins. Otherwise, revise the existing assigned file. For a new file, follow neighboring chapter files; use `Wiki/Outline/Book-N/Chapter_[NN]_Plan.md` only when no project convention exists.

Do not create a diagnostic, receipt, research dump, or separate argument map unless the user asks or book instructions require it. Record unresolved research questions inside the requested artifact only when they affect drafting.

## Choose the lightest useful mode

Infer the mode from the request; do not ask when it is clear.

- **Edit in place:** The user asks to adjust, regenerate, fix, or tighten an existing chapter plan. Read the current file, apply the requested changes throughout it, and verify stale material is gone.
- **Compact plan (default for one chapter):** Create a concise chapter argument spine and 3–6 evidence blocks. Include only what the writer needs to draft without guessing.
- **Full plan document:** Use when the user asks for detailed evidence inventory, the downstream generator requires structured fields, or several writers/tools will consume the artifact. Read the full-mode references below.
- **Batch plans:** Use for a chapter range. Preserve cross-chapter argument continuity and vary evidence types.

Do not silently escalate a compact plan into a full evidence dossier.

## Context

Read only context that can change the plan:

- Assigned outline, proposal, existing chapter plans, or chapter directive;
- The book's central thesis and argument architecture;
- Relevant current-canon research, sources, and established facts;
- Adjacent chapter plans needed for argument continuity;
- The project's style/voice source only when the plan includes drafting guardrails or the user names it.

Use the project's required retrieval method first. If the book has a preferred index or semantic-search rule, follow it. Search narrowly after semantic retrieval for exact facts. Do not load every source file by default.

Separate **established**, **author-directed**, **proposed**, and **unknown** facts. Never convert a possibility into canon merely to fill a field. Avoid inventing statistics, studies, quotes, or technical mechanics unless the argument cannot work without them; mark any necessary invention as proposed.

## Argument gate: do this before expanding evidence blocks

Write the chapter's argument spine in one or two sentences and test it:

1. **Claim:** What is the chapter's central assertion? (One declarative sentence the chapter proves.)
2. **Stakes:** Why does this claim matter to the book's thesis? What fails if the reader doesn't accept it?
3. **Evidence strategy:** What types of evidence will carry the proof? (Empirical, anecdotal, theoretical, historical, counter-argument, synthesis)
4. **Synthesis:** What new understanding does the reader possess at the end that they lacked at the start?
5. **Necessity:** What future chapter, argument, or option would collapse if this chapter were cut?

If the spine cannot answer all five, repair the spine before adding evidence. Coverage, background, literature review, and definitions are not argument unless they serve the claim.

Prefer one primary evidence type per block and at most one supporting type. Consult [evidence-types.md](references/evidence-types.md) when the strategy is unclear or when planning a batch. Use [anti-flat-chapters.md](references/anti-flat-chapters.md) when a chapter risks becoming summary, survey, or exposition without argument.

## Build evidence blocks around turns

Use 3–6 evidence blocks according to real changes in evidence type, sub-claim, or rhetorical register. One sustained block is valid when it carries the full argument; do not split it merely to satisfy a count.

Each evidence block should establish:

- The sub-claim or step in the argument;
- The evidence type(s) deployed;
- Concrete evidence: specific study, quote, data point, case, historical moment, or logical step;
- The turn: the insight, reversal, complication, or synthesis that advances the argument;
- The consequence carried into the next block;
- A specific transition beat with forward pull.

Research belongs inside decisions and synthesis. Keep citations selective. A single load-bearing study or case usually carries more argument than a bibliography.

Do not duplicate the same material across claim, evidence, transition, and takeaway. Add a field only when it gives the eventual drafter new information.

## Compact plan format

Adapt to the project's neighboring files. A useful default is:

```markdown
# Chapter [number]: [title]

## Argument Spine
- **Claim:** ...
- **Stakes:** ...
- **Evidence strategy:** [primary type + supporting type]
- **Synthesis:** [what the reader newly understands]
- **Why this chapter cannot be cut:** ...

## Evidence Block 1
- **Sub-claim:** ...
- **Evidence type:** [empirical / anecdotal / theoretical / historical / counter-argument / synthesis]
- **Concrete evidence:** [specific study, quote, data, case, moment, logical step]
- **Turn:** [insight, reversal, complication, or synthesis]
- **Transition to next:** ...

[Repeat for each block]

## Reader Takeaway
- **One-sentence takeaway:** ...
- **Actionable implication:** [what the reader can do/think differently]
- **Forward hook:** [what pulls them into the next chapter]
```

Add continuity or fact-status notes only where the drafter could otherwise contradict established research. Do not append a generic recommendations section after the plan is already usable.

## Full plan documents

Only in full mode, read:

- [evidence-schema.json](references/evidence-schema.json) as the structured field checklist;
- [continuity-tracking.md](references/continuity-tracking.md) for argument threads, defined terms, carried metaphors, and open questions;
- [chapter-hooks.md](references/chapter-hooks.md) when the ending lacks forward pull;
- [anti-flat-chapters.md](references/anti-flat-chapters.md) and [evidence-types.md](references/evidence-types.md) as needed.

Use [plan-template.md](assets/plan-template.md) or [evidence-schema.json](references/evidence-schema.json) only when their format matches the project or downstream tool. Field-length examples are guidance, not quotas. An evidence description should be long enough to draft the block and no longer. Synthesis fields must add argumentative causality rather than paraphrase evidence.

For each structured block, populate the fields required by the project's generator. Resolve proper nouns exactly when machine ingestion depends on them. If a valid provisional name cannot resolve, flag it; do not silently replace it or create unrelated canon.

## Workers

Handle a single chapter or focused revision directly unless an isolated worker would clearly improve a large-context or multi-chapter task. Consider one worker for a substantial range or large research corpus; use one when book instructions require isolation. Do not delegate merely because the capability exists.

When using a worker, tell it the selected mode, exact target path, permitted side effects, authority order, and whether it may create reports. The coordinating agent must review the actual edited artifact before reporting completion.

## Revision verification

For edits, check every user-requested addition, removal, and reframing across the entire artifact, including continuity notes, hooks, guardrails, fact tables, and recommendations. Search exact banned terms, then read semantically for leftover concepts that use different words. Do not claim a concept is gone because one keyword no longer appears.

Before finishing, verify:

- The argument gate passes;
- Evidence supports the causal spine rather than competes with it;
- The claim drives the irreversible synthesis;
- Evidence blocks vary in type and register;
- No earlier chapter's argument or hook is merely repeated;
- Proposed facts remain labeled;
- Terminology and defined terms follow project authority;
- The requested file, and only requested ancillary files, were changed;
- Formatting checks pass when available.

Return a concise completion note with the file link and any true drafting blocker. Do not paste the artifact or produce a review report unless asked.
