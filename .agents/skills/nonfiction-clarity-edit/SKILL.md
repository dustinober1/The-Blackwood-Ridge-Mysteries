---
name: nonfiction-clarity-edit
description: "Default comprehensive non-fiction clarity pass: jargon density, abstraction ladder, cognitive load, and signposting, plus sentence-level mechanics. The non-fiction equivalent of fiction-full-editor. Uses focused workers for 40-line chunk scanning. Use when user says 'clarity edit', 'make it clearer', 'check readability', 'edit chapter', 'polish writing', or asks for general sentence-level editing of non-fiction."
metadata:
  author: Nonfiction Toolkit
  version: "1.1.0"
  category: nonfiction-editing
  output-format: markdown
---

# Nonfiction Clarity Edit

Runs every sentence-level clarity check in a single pass. Each focused worker scans its 40-line chunk against the complete criteria set: jargon density + abstraction ladder + cognitive load + signposting + sentence mechanics.

## Arguments

The request argument is a chapter reference (e.g., "5", "Chapter-5", "Chapter-5.md").

## Step 1: Find Paths and Measure

1. Parse the request argument to determine the chapter.
2. Search the project files for the chapter (e.g., `**/Chapter-5*`). If not found, ask.
3. Search for the project's style guide (`**/style_guide.md`) and review guide (`**/review_guide.md`). Use whichever exist.
4. Search for the chapter's plan (`**/Chapter_[NN]_Plan.md` or the project's planning convention from `nonfiction-chapter-plan`). The plan states the chapter's claim, evidence blocks, and required transitions — a clarity edit must not cut an argument move it mistakes for clutter, and must not pass prose that buries the plan's claim.
5. Get the chapter's line count using the host's available file or line-count operation.

## Step 2: Read All Criteria

Read ALL four reference files and combine their contents:

- [jargon-criteria.md](references/jargon-criteria.md)
- [abstraction-criteria.md](references/abstraction-criteria.md)
- [cognitive-load-criteria.md](references/cognitive-load-criteria.md)
- [signposting-criteria.md](references/signposting-criteria.md)

Also read the drafting-side clarity rules for known-good patterns: [clarity-rules.md](../nonfiction-writechapter/references/clarity-rules.md). Where a drafting rule and a detection criterion overlap, the detection criterion governs what gets flagged; the drafting rule supplies the fix pattern.

Combine them into a single criteria block for the worker prompts.

## Step 3: Launch Focused Workers

Calculate 40-line chunks. For EACH chunk, use one isolated worker with the task description `Clarity edit lines {start}-{end}`.

Launch all chunks in parallel when the host supports workers; otherwise process the chunks sequentially. Keep the work in the foreground so all findings can be compiled in this run.

**Worker prompt for each chunk:**

> You are performing a comprehensive non-fiction clarity edit. Check ONLY lines {start} through {end}.
>
> 1. Read the style guide at: {style_guide_path} (if it exists)
> 2. Read the chapter plan at: {plan_path} (if it exists) — note the chapter's claim, evidence blocks, and required transitions so argument moves are not flagged as clutter
> 3. Read the chapter using offset={start - 1} and limit=40: {chapter_path}
> 4. Check every line against ALL of the following criteria:
>
> {paste the combined contents of all four criteria files}
>
> 5. Return your findings in this EXACT format. Return NOTHING if no issues found:
>
> ```
> **Line {N}:** `exact quoted text`
> Category: [Jargon Density | Abstraction Ladder | Cognitive Load | Signposting | Sentence Mechanics | Style Guide Violations]
> Problem: [why it obstructs the reader]
> Fix: [specific replacement]
> ```
>
> Be thorough but avoid false positives. Technical terms of art are jargon only when the chapter's audience would not know them (check the plan's audience assumptions). A signpost is required only at a real argument move.

## Step 4: Compile Report

Collect all worker results. Deduplicate issues flagged across overlapping criteria: merge into a single finding under the primary category and keep the single best, most actionable fix. Never output contradictory rewrites for the same line.

Group into these top-level sections:

```
## Clarity Edit: [Chapter Title]

[2-3 sentence assessment — total count, severity, dominant pattern]

---

## Jargon Density Issues
### Undefined Terms of Art
### Jargon Stacking
### Banned Words

## Abstraction Ladder Issues
### Floating Abstractions
### Missing Concrete Rungs
### Ladder Inversions

## Cognitive Load Issues
### Overloaded Sentences
### Nested Clause Pileups
### One-Idea Violations
### Paragraph Load

## Signposting Issues
### Missing Transitions
### Topic Announcements
### Author-Centered Framing
### Hidden Argument Moves

## Sentence Mechanics Issues
### Passive Stance
### Nominalizations
### Hedge Mismatches

## Style Guide Violations
[any project-specific rule violations]

---

**Total issues: {count}**
**By severity:** {high/medium/low breakdown if clear}
```

Skip empty categories and sections.

## Step 5: Save and Report

1. Look for the chapter's `_Edits/Book-N/` folder (the same `Book-N` level as the chapter's `Chapters/Book-N/` location). If none exists, create it.
2. Save as `Chapter-NNN_ClarityEdit.md` (three-digit number matching the chapter).
3. Tell the user: location, total issue count, top 3 categories, and whether it's publishable or needs another pass.
4. Offer to apply approved items with `fiction-revise` (report-driven and book-agnostic).

## Ordering rule

Run `nonfiction-factcheck` first when the chapter contains statistics, quotes, or citations. Clarity edits reword sentences; rewording a sentence around a false fact wastes the edit and can launder the error into smoother prose.
