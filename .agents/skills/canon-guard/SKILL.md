---
name: canon-guard
description: "Safeguard locked canon files during writing, execute impact analysis scans across drafted chapters before intentional canon updates, and safely reconcile world, character, or timeline revisions. Use when user says 'update canon', 'change world rule', 'canon conflict', 'character change impact', or 'modify canon safely'."
metadata:
  author: Storycraft Skills
  version: "1.0.0"
  category: cross-cutting
---

# Canon Guard & Update Manager

Protects core narrative truth from accidental drift during drafting, and manages deliberate, controlled updates to locked reference files (`Wiki/Characters/`, `Wiki/World/`, `Wiki/Story/timeline.md`, or voice bibles).

## Core Rules

1. **Canon is Read-Only by Default:**
   - Skills writing drafts (`fiction-writechapter`, `fiction-revise`) cannot silently mutate canon files when prose encounters an apparent mismatch.
2. **Impact Scan Before Edit:**
   - Before modifying a canon rule or character trait, run an impact scan across all existing chapters (`Chapters/Book-N/`) to identify references that will become obsolete or contradictory.
3. **Explicit Confirmation & Re-Gating:**
   - Present the affected lines, obtain user confirmation, unlock the single target file, apply the update, and flag impacted chapters for `gate-check` re-verification.

## Procedure

### Step 1: Define Canon Change
- Identify target file (e.g., `Wiki/Characters/cross.md`).
- Specify old fact vs. proposed new fact.

### Step 2: Run Impact Scan
- Scan drafted chapters across all books for occurrences of the old fact, trait, or location.
- Categorize impacts:
  - **Direct Contradictions:** Explicit statements in prose that directly violate the new rule.
  - **Implicit Tension:** Subtext or references that need tone adjustment.

### Step 3: Present Scan & Confirm
- Render table of chapter numbers, line excerpts, and required prose edits.
- Prompt for user confirmation.

### Step 4: Apply & Register
- Write the change to the target Wiki file with an audit timestamp.
- Append a re-gate reminder in `_Edits/Book-N/re-gate-needed.md`.
