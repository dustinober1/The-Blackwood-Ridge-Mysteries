---
name: fiction-revise
description: Apply approved edits from a review or edit report (_Edits/Chapter-NNN_*.md) directly to a chapter manuscript file with minimal, verified in-place edits and a change ledger. Use when user says "apply edits", "apply review fixes", "revise chapter", "apply fixes 1, 3, 5", or after running fiction-reviewchapter, fiction-full-editor, or another editing pass.
metadata:
  author: Fiction Toolkit
  version: "1.0.0"
  category: fiction-editing
---

# Fiction Revise — Apply Approved Edits

Applies approved review findings and edit recommendations directly to a chapter manuscript file.
Enforces strict in-place edits, verifies exact quoted text before touching files, skips stale
or conflicting items, and produces a complete change ledger.

## Arguments

The request accepts:
1. **Chapter reference** (e.g. `5`, `Chapter-005`, `Chapters/Book-1/Chapter-005.md`)
2. **Report reference** (optional; defaults to the most recent report in `_Edits/Book-N/` for that chapter)
3. **Selection filter** (e.g. `all`, `items 1, 3, 5-8`, `all AIisms`, or interactive confirmation)

## Step 1: Locate Chapter and Report

1. Resolve the chapter file (prefer canonical `Chapters/Book-N/Chapter-NNN.md`).
2. Locate the source edit report:
   - Check `_Edits/Book-N/` (or adjacent `_Edits/` folder).
   - Look for `Chapter-NNN_Review.md`, `Chapter-NNN_FullEdit.md`, `Chapter-NNN_LineEdit.md`, etc.
   - If multiple reports exist and the user didn't specify one, ask or default to the newest.
3. Read both the chapter and the report into context.

## Step 2: Parse and Select Edits

Extract all structured recommendations from the report:
- Item identifier / number
- Target line reference
- Quoted original snippet
- Proposed fix / replacement text
- Category / issue type

If the user gave specific item numbers (e.g. "apply 1, 4, 7-10"), select only those items.
If the user said "apply all", select all local line-edit items.
If the user did not specify, list the available items grouped by category and ask which to apply.

## Step 3: Pre-flight Verification & The Scrap-vs-Patch Guard

Before making any edit, check each selected item against two safety rules:

1. **The Scrap-vs-Patch Guard:**
   - If a finding is **structural** (e.g. missing required beat, wrong POV character, whole-scene causal failure), do NOT apply it line-by-line. Flag it as `SKIPPED: STRUCTURAL` — per project rules, structural problems require fixing the scene plan and re-drafting with `fiction-writechapter`.
2. **Quote Match Verification:**
   - Locate the exact quoted text in the current chapter manuscript.
   - If the exact quote cannot be found (e.g. earlier edits shifted text or changed phrasing), do NOT guess. Mark the item as `SKIPPED: STALE_QUOTE`.

## Step 4: Apply Edits (Minimal Perturbation)

Apply the validated items to the chapter file in place:
- Make the **minimal necessary change**: touch ONLY the targeted words or phrase specified in the fix.
- Do not rewrite unflagged adjacent sentences.
- Do not insert unsolicited adjectives, flourishes, or mood descriptors.
- Obey project style rules (e.g. no em dashes except dialogue interruptions; grounded physical sentences).
- If multiple approved edits target the same line or overlapping text, apply the primary fix and mark the subordinate edit as `MERGED`.

## Step 5: Report Change Ledger

Output a concise, structured ledger:

```markdown
## Revision Ledger: Chapter [NNN]

**Applied ({count}):**
- **Item [N] (Line {line}):**
  - *Before:* "..."
  - *After:* "..."

**Skipped ({count}):**
- **Item [N]:** [Reason: user excluded | STALE_QUOTE | STRUCTURAL (needs re-draft)]

**Next Step:**
Chapter manuscript updated. Run `fiction-reviewchapter` to re-gate the chapter.
```

Offer to leave staged or commit per project convention. Do not commit unless requested.
