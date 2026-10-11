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
**Draft word count**: 2707
**Checker**: continuity-checker discipline run inline (project agent-dispatch workaround); zero prior FAILs.

### Verdict: PASS

### Major Issues

| # | Location | Issue | Canon reference |
|---|----------|-------|-----------------|
| — | — | None. This chapter carries the CANONICAL form of the yellow-rose stakes ("Ambition. Betrayal. Folly."); the drift is ch8's (F005). | canon/world-rules.md (floriography vocabulary) |

### Minor Issues

| # | Location | Issue |
|---|----------|-------|
| 1 | prose L46 | Lint `pov_leak`: "the qualities Marguerite had wanted to name" — reads as Callie's inference about a dead woman's documented intent; strict-POV call → F026. |
| 2 | prose L104 | Ambiguous sentence: "the woman lying in the bed she was kneeling in had tried..." — "bed" parses as flower bed vs. kneeling body; reader tripping hazard → F027. |
| 3 | lint L53/L75/L83 | Dialogue punctuation: two genuine (capitalized tag / period-before-tag), one action-beat false positive ("He said" after quoted sentence is correct punctuation) → F025. |

### Escalate (ambiguous — not a clean pass/fail)

| # | Location | Ambiguity | Why it can't be resolved here |
|---|----------|-----------|-------------------------------|
| — | — | — | — |

### Whole-manuscript checks

- Crutch phrases: within book texture → F022. Style sheet: `late-spring`, `pulled-up`, `not-quite` touch this chapter → F021.
- Promises: P003 (Doris's demand) made here, paid ch8 — matches prose exactly.
- Canon: Doris (seventy-or-near, flat palms ×2, rationed voice), Mae (lavender thinner, casserole, "honey" welcome-and-wall), garden vocabulary, 1994 stone, photo facing the room — all match canon.

### Value-shift verification (sweep override)

- Scene 1 `outsider reader → tested guest`: lands — the silence test ("she had passed a small corner of it by not filling it") and "You can walk it."
- Scene 2 `estrangement → a new, careful geometry`: lands — Mae at the gate, not through it; "the absence of the begging was its own sentence."
- Scene 3 `sympathy from a distance → bound`: lands — "You find it, and you bring it to me... You understand." / "I understand."

### Resolution

- [ ] Minor issues fixed or accepted (F025/F026/F027 pending author approval)
- [ ] STATE.yaml updated (batched at sweep end)
