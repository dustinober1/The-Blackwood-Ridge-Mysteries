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
**Draft word count**: 2711
**Checker**: continuity-checker discipline run inline (project agent-dispatch workaround); zero prior FAILs.

### Verdict: PASS

### Major Issues

| # | Location | Issue | Canon reference |
|---|----------|-------|-----------------|
| — | — | None. All 7 lint Major hits are `tense_drift` on "has/is/have" in narration — the book's documented free-indirect/gnomic voice (e.g., "a woman who has learned that the town is looking at her"), not tense drift. Routed to metrics tuning, not prose edits (→ findings F023). | voice-bible.md "The narration" |

### Minor Issues

| # | Location | Issue |
|---|----------|-------|
| 1 | outline.md "Canon Load-Bearing Facts" | Cites timeline rows H7–H12; canon/timeline.md defines H1–H10 only. Doc nit → F030. |
| 2 | book-wide | Em-dash rate 16.2/1000 (lint NOTE) — consistent with the book's signature rhythm; band question → F023. |

### Escalate (ambiguous — not a clean pass/fail)

| # | Location | Ambiguity | Why it can't be resolved here |
|---|----------|-----------|-------------------------------|
| — | — | — | — |

### Whole-manuscript checks

- Crutch phrases: 118 shared phrases book-wide; ch1's top shares ("of a woman", "the back room") are setting/refrain texture → F022.
- Style sheet: 15 hyphenation contradictions book-wide; ch1 implicated in several (`almost right`, `coming-apart`, `garden-club`, `not-knowing`, `not quite`, `the door`) → F021.
- Promises: P001/P002 made here, paid ch5 per ledger — consistent with prose.
- POV: clean — no interiority leaks flagged or found.

### Value-shift verification (sweep override)

- Scene 1 `guarded routine → tested steadiness`: lands — "the reclamation had held, more or less, the way a set bone holds. You could walk on it. You did not quite trust it."
- Scene 2 `careful avoidance → the drawer opened`: lands — "had opened the drawer for her."
- Scene 3 `refusal → chosen curiosity`: lands — "the choice had already been made the moment she picked up the glass."

### Resolution

- [ ] Minor issues fixed or accepted (F023/F030 pending author approval)
- [ ] STATE.yaml updated (batched at sweep end)
