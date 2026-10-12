---
name: gate-check
description: "Run comprehensive chapter gate checks combining mechanical linting, canon integrity assertions, Chekhov setup validation, and prose quality checklists to determine chapter production readiness. Use when user says 'gate check', 'is chapter ready', 'run chapter gate', 'validate chapter', or 'check chapter continuity'."
metadata:
  author: Storycraft Skills
  version: "1.0.0"
  category: fiction-editing
---

# Gate Check

The definitive readiness and continuity validator for a drafted chapter. Evaluates chapter prose against canon facts, scene commitments, voice constraints, Chekhov setups, and mechanical prose rules before declaring a chapter cleared for subsequent editing or final compilation.

## Gate Checklist Dimensions

Every gate run systematically evaluates 6 pillars:

1. **Canon Integrity (Hard Gate):**
   - Characters: names, physical states, active injuries, relationships match `Wiki/Characters/`.
   - World & Setting: locations, sensory anchors, physical distances match `Wiki/World/`.
   - Timeline: chronological continuity with preceding chapters and series timeline.
2. **Scene Contract & Beat Fulfillment:**
   - Evaluates drafted prose against `Wiki/Outline/Book-N/Chapter_[NN]_Scene.md` or scene plan.
   - All mandatory narrative beats, emotional shifts, and turning points must be present and dramatized.
3. **Chekhov & Promise Maintenance:**
   - Any clues, objects, or dramatic setups introduced in this chapter must be registered in `promises.yaml` via `fiction-promises`.
   - Any setups resolved here must be correctly retired.
4. **Voice & POV Integrity:**
   - Adherence to designated POV (Third Limited, First, etc.) with zero POV slips or head-hopping.
   - Dialogue cadence reflects character dialect/register from `Wiki/Characters/` and `voice-dna.md`.
5. **Mechanical & Machine Cadence Lint:**
   - Tricolon (rule-of-three) saturation rate.
   - "Not X but Y" negation density.
   - Em-dash clusters (>10 in a scene).
   - Paragraph-closing aphorisms.
   - Stock sensory repetitions (dust, paper must, brass warmth, creaking wood).
6. **Closing Beat & Transition:**
   - Chapter ending leaves a distinct forward momentum or deliberate unresolved hook (avoiding homogeneous quiet-tea reflective resolutions on 100% of chapters).

---

## Output Contract

Gate check produces a timestamped run report saved to:
`_Edits/Book-N/Chapter-NNN_Gate.md`

```markdown
# Chapter Gate Report: Chapter NNN (Book N)
**Timestamp:** YYYY-MM-DD HH:MM  **Status:** [PASS / WARN / FAIL]  **Run:** #1

## Summary
- **Canon Violations:** 0
- **Unfulfilled Scene Beats:** 0
- **Chekhov Debt (Unregistered setups):** 0
- **Cadence & Lint Warnings:** [N]

## Detailed Assessment

### 1. Canon & Timeline: [PASS / FAIL]
- [Details with line citations]

### 2. Scene Contract: [PASS / FAIL]
- [Target beats matched to chapter paragraphs]

### 3. Setup & Promise Register: [PASS / ACTION REQUIRED]
- Setups introduced: [List]
- Promises paid: [List]

### 4. POV & Dialogue Integrity: [PASS / WARN]
- [POV slips or dialogue notes]

### 5. Cadence & Lint Flags: [PASS / WARN]
- [Flagged sentences with exact quotes and line numbers]

## Action Verdict & Routing
- If **PASS**: Cleared for chapter progression or `fiction-full-editor`.
- If **FAIL (Structural / Canon)**: Route back to scene plan or invoke `canon-guard` if canon needs intentional amendment.
- If **WARN (Prose / Cadence)**: Route directly to `fiction-revise` or `kill-chapter`.
```
