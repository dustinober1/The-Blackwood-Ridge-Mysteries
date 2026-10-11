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
**Draft word count**: 2764
**Checker**: continuity-checker discipline run inline (project agent-dispatch workaround); zero prior FAILs.

### Verdict: FAIL

### Major Issues

| # | Location | Issue | Canon reference |
|---|----------|-------|-----------------|
| 1 | prose L62 | "Mae had used the word at the Dabney garden gate, **two weeks ago**" — the chapter's own skeleton (decode "for days"; gate visit Monday of the same week; crack Thursday) puts the visit ~3 days back. Confirms ledger **F018** (LOW CONFIDENCE → now gate-confirmed). Fix after author approval: reword ("days ago") or stretch the day skeleton (F019). | canon/timeline.md beats 3, 10 |

### Minor Issues

| # | Location | Issue |
|---|----------|-------|
| 1 | prose L60 | "Can I come in, honey." terminal period — Mae's flat statement-shaped register; intentional, leave. |
| 2 | prose L148 | Dialogue tag "repeated" — outside config's allowed list ("said/asked/answered/replied") → F025. |
| 3 | lint L59 ×4 | Dialogue punctuation flags: "She asked"/"She said" capitalized forms and "Can I come in, honey." — mostly register-intentional; the genuine items ride with F025. |

### Escalate (ambiguous — not a clean pass/fail)

| # | Location | Ambiguity | Why it can't be resolved here |
|---|----------|-----------|-------------------------------|
| — | — | — | — |

### Whole-manuscript checks

- Crutch phrases: "the bell rang", "for a moment" share → F022. Style sheet: `late-spring`, `holding-in` touch this chapter → F021.
- Promises: P002 paid here ("Say it." received and obeyed — matches prose verbatim); P006 made here (the cove ask), paid ch7.
- Canon: water lily and damask rose meanings ✓; "the place felt wrong in a way no one had ever named" — the IN-WORLD phrasing F006 says ch7 should use ✓; Cross reads every page before refusing ✓; hat not removed ✓; October visit matches H7 ✓.

### Value-shift verification (sweep override)

- Scene 1 `holding the cipher → aimed at`: lands — "the asking was in Callie's hands, and the hands were shaking, and she let them shake."
- Scene 2 `wall → threshold`: lands — Mae's confession ("I'm telling you now. That's what I've got.").
- Scene 3 `carrying alone → said`: lands — "Marguerite had written *say it*. Callie had said it. The rest was not hers."

### Resolution

- [ ] Major issues fixed (awaiting author approval via F018)
- [ ] Minor issues fixed or accepted
- [ ] STATE.yaml updated (batched at sweep end)
