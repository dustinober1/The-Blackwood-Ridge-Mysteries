# Chapter GATE — Gate Report

Append a new run block each time the gate is run. Never overwrite prior runs:
the failure history is what drives escalation (2 failures on the same gate
sends the chapter to structural-editor).

No gate has run against this retrofit packet. Known must-fix findings for
this book are tracked in findings.yaml and canon-decisions.md; prose edits
happen only after author approval. Append any gate run below without
deleting this note.

---

## Run 1 — 2026-10-11 (audit-book full sweep)

**Checked against**: gates/readiness-checklist.md
**Draft word count**: 2437
**Checker**: continuity-checker discipline run inline (project agent-dispatch workaround); zero prior FAILs.

### Verdict: FAIL

### Major Issues

| # | Location | Issue | Canon reference |
|---|----------|-------|-----------------|
| 1 | prose L110 | "Mae had walked into the office of a man **whose diapers she had changed**" — impossible against Book 1's pinned ages (Mae ~59–60; Cross mid-fifties). Confirms ledger **F004** (MUST-FIX). Approved fix form: "Mae has known Cross since he was a young deputy." | Book 1 canon ages; findings.yaml F004 |

### Minor Issues

| # | Location | Issue |
|---|----------|-------|
| 1 | prose L32 | Lint `pov_leak` ×2: "Mae knew it" / "Doris loved the man she feared had killed her daughter" — free-indirect inferences in Callie's voice; strict-POV call → F026. |
| 2 | prose L84 | "He nodded, slowly." — action beat, lint tag false positive. |

### Escalate (ambiguous — not a clean pass/fail)

| # | Location | Ambiguity | Why it can't be resolved here |
|---|----------|-----------|-------------------------------|
| — | — | — | — |

### Whole-manuscript checks

- Crutch phrases: "of a man" cluster → F022. Style sheet: `garden club`, `not looking`, `holding in` touch this chapter → F021.
- Promises: P007 (apprenticeship) made here ✓; P006 paid ch7 (dive called here, executed ch7) — consistent.
- Canon: Linda Parrish ✓; Harlan's not-coming-in ("worse than the not-looking, because it meant he had decided") ✓ verbatim; Wells shaking hands with Beech on the square ✓; Cross's report spine "The location is specific enough" ✓; "Wear boots" ✓; rekeying letter Tuesday ✓; garden club Wednesdays ✓.
- Word count 2437 vs target 2760 — inside ±25% tolerance.

### Value-shift verification (sweep override)

- Scene 1 `said → shunned`: lands — three days rendered; "the deciding was not kind."
- Scene 2 `shunned → resolved alone`: lands — "She did not stop." (verbatim beat).
- Scene 3 `alone → threaded`: lands — Eli's ask accepted; Cross's call; "tomorrow they would go to the lake."

### Resolution

- [ ] Major issues fixed (awaiting author approval via F004)
- [ ] Minor issues fixed or accepted
- [ ] STATE.yaml updated (batched at sweep end)
