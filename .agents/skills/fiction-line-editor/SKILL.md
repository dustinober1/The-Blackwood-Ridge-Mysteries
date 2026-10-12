---
name: fiction-line-editor
description: Focused sentence-level line editing for fiction prose (voice, cliches, repetition, POV violations, awkward constructions). Use fiction-full-editor for general sentence editing; use this skill only when isolating the line-craft and voice layer without running full craft/AIism checks. Uses focused workers for 40-line chunk scanning.
metadata:
  author: Fiction Toolkit
  version: "5.2.0"
  category: fiction-editing
---

# Line Editor

Focused sentence-level line editing using focused workers when supported. Each worker reads 40 lines and checks against voice and line-craft criteria. For general sentence editing that also catches AI-tells and prose mechanics, use `fiction-full-editor`.

## Arguments

The request argument is a chapter reference (e.g., "5", "Chapter-5", "Chapter-5.md", "Chapters/Chapter-5.md").

## Step 1: Find Paths and Measure

1. Parse the request argument to determine the chapter. Accept number, filename, or path.
2. Search the project files for the chapter (e.g., `**/Chapter-5*`). If not found, ask.
3. Search for the project's review guide: `**/review_guide.md`. Fall back to `**/style_guide.md`.
4. Get the chapter's line count using the host's available file or line-count operation.

## Step 2: Read Criteria

Read [references/agent-instructions.md](references/agent-instructions.md).

Store its contents — you will inject them into each worker prompt.

## Step 3: Launch Focused Workers

Calculate 40-line chunks: lines 1-40, 41-80, 81-120, etc.

For EACH chunk, use one isolated worker with the task description `Line edit lines {start}-{end}`.

Launch all chunks in parallel when the host supports workers; otherwise process the chunks sequentially. Keep the work in the foreground so all findings can be compiled in this run.

**Worker prompt for each chunk:**

> You are a line editor scanning fiction prose. Check ONLY lines {start} through {end}.
>
> 1. Read the review/style guide at: {guide_path} — note project-specific rules, forbidden words, POV requirements, character voice patterns. If the file is not found, use general fiction craft principles.
> 2. Read the chapter using offset={start - 1} and limit=40: {chapter_path}
> 3. Check every line against ALL of the following criteria:
>
> {paste the full contents of agent-instructions.md here}
>
> 4. Return your findings in this EXACT format. Return NOTHING if no issues found in your chunk:
>
> ```
> **Line {N}:** `exact quoted text`
> Category: [Narrative Fragments | Cliches | AIisms | Repetition | Telling Over Showing | Awkward Constructions | POV Violations | Voice Violations | Paired Adjectives | Style Guide Violations]
> Problem: [why it's a problem]
> Fix: [specific replacement text]
> ```

## Step 4: Compile Report

Collect all worker results. Group issues by category. Sort by line number within each category. Compile into this format:

```
## Line Edit: [Chapter Title]

[1-2 sentence overall assessment — issue count, severity, patterns]

---

### Narrative Fragments
[issues sorted by line number]

### Cliches and Tired Phrasing
[issues]

### AIisms
[issues]

### Repetition
[issues]

### Telling Over Showing
[issues]

### Awkward Constructions
[issues]

### POV Violations
[issues]

### Voice Violations
[issues]

### Paired Adjectives
[issues]

### Style Guide Violations
[issues]

---

**Total issues: {count}**
```

Skip any category with zero findings.

## Step 5: Save and Report

1. Look for the chapter's `_Edits/Book-N/` folder (the same `Book-N` level as the chapter's `Chapters/Book-N/` location). If none exists, create it.
2. Save report as `Chapter-NNN_LineEdit.md` (three-digit number matching the chapter).
3. Tell the user: location, issue count, top 3 most common categories.
4. Offer to apply approved items with `fiction-revise`.
