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
**Draft word count**: 2897
**Checker**: continuity-checker discipline run inline (project agent-dispatch workaround); zero prior FAILs.

### Verdict: PASS

### Major Issues

| # | Location | Issue | Canon reference |
|---|----------|-------|-----------------|
| — | — | None. Wells's open-palm grammar, Cross's tells (hat on, arms crossed, neck-rub vs jaw), and the decode skeleton (June 1994 / party / Lauren / Ambler beside yarrow / dock) all match canon exactly. | canon/characters.md; canon/world-rules.md |

### Minor Issues

| # | Location | Issue |
|---|----------|-------|
| 1 | lint L49/L69/L83 | All four dialogue punctuation/tag flags are action-beat false positives ("He smiled." / "He said" as new sentences after quoted speech is correct punctuation; no genuine tag violations found in prose). |

### Escalate (ambiguous — not a clean pass/fail)

| # | Location | Ambiguity | Why it can't be resolved here |
|---|----------|-----------|-------------------------------|
| — | — | — | — |

### Whole-manuscript checks

- Crutch phrases: "of a man" cluster concentrates in ch3–ch7 → F022. Style sheet: `coming apart`, `end of`, `late-spring` touch this chapter → F021.
- Promises: P004 (open palm) and P005 (two stories) made here; both paid ch7 per ledger — matches prose (party+home told to Callie; Carmody lie documented ch4).
- POV: strong — Wells's interior rendered only through observable cues ("the smile... stayed exactly where it was... a thing that was being held").

### Value-shift verification (sweep override)

- Scene 1 `puzzle → accusation-shape`: lands — "Not a sentence, exactly. A ledger." + the skeleton.
- Scene 2 `wariness → liking (and watching the liking)`: lands — "She liked him. That was the thing to watch."
- Scene 3 `respect → adversarial caution`: lands — "she had begun, very quietly, to look sideways at a man the whole town loved."

### Resolution

- [ ] STATE.yaml updated (batched at sweep end)
