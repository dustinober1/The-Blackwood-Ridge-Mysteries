---
name: chapter-pipeline
description: "Run the complete end-to-end chapter production lifecycle from scene briefing to draft generation, gate verification, and line polish in a unified automated execution. Use when the user asks to 'run chapter pipeline', 'do chapter start to finish', 'draft outline and gate chapter', or 'execute full pipeline on chapter N'."
metadata:
  author: Storycraft Skills
  version: "1.0.0"
  category: fiction-writing
---

# Chapter Pipeline Orchestrator

Automates the multi-skill sequence required to produce a publication-ready chapter in a single command, enforcing checkpoints and halting only on genuine blockers.

## Pipeline Steps

1. **Scene Scaffolding & Verification:**
   - Verifies existence of `Wiki/Outline/Book-N/Chapter_[NN]_Scene.md` or generates it from book outline beats using `fiction-scenes`.
   - Halts if major beat gaps exist.
2. **Drafting:**
   - Invokes `fiction-writechapter` with scene brief, voice prompt (`fiction-voiceprompt`), and preceding chapter context.
   - Outputs draft to `Chapters/Book-N/Chapter-NNN.md`.
3. **Readiness Gate Check:**
   - Automatically runs `gate-check` against canon, Chekhov ledger, and prose linting.
   - Outputs `_Edits/Book-N/Chapter-NNN_Gate.md`.
4. **Automated Polish & Review:**
   - If gate is `PASS` or minor `WARN`: runs `fiction-aiism-editor` or `kill-chapter` for quick cadence cleanup.
   - If gate is `FAIL`: halts pipeline immediately and reports blockers with actionable fixes.
