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
**Draft word count**: 2932
**Checker**: continuity-checker discipline run inline (project agent-dispatch workaround); zero prior FAILs.

### Verdict: PASS

### Major Issues

| # | Location | Issue | Canon reference |
|---|----------|-------|-----------------|
| — | — | None. All 13 lint Major hits are `tense_drift` voice-band (same disposition as ch01 → F023). Meadowsweet meanings, rekeying mechanism, cipher discipline, and Doris/Wells canon details all match. | canon/world-rules.md |

### Minor Issues

| # | Location | Issue |
|---|----------|-------|
| 1 | prose L138 | Adverbial tag "Callie said carefully" — voice-bible allows rare measured adverbs; config lint flags it → F025. |
| 2 | lint L51/L89/L113 | Dialogue punctuation/tag flags: action-beat false positives ("He nodded." / "He said" as new sentences). |
| 3 | prose L68 vs L56 | Timeline adjacency: "the council voted last week" + "He said it at the council meeting on Tuesday" coheres only under the Sunday-ch1 skeleton — already covered by ledger F019 (LOW CONFIDENCE); no new row. |

### Escalate (ambiguous — not a clean pass/fail)

| # | Location | Ambiguity | Why it can't be resolved here |
|---|----------|-----------|-------------------------------|
| — | — | — | — |

### Whole-manuscript checks

- Crutch phrases: "of a man" cluster → F022. Style sheet: `late-spring`, `not knitting`, `setting down` touch this chapter → F021.
- Promises: P005 advanced (Harlow-barn lie documented on the page); rekeying thread opened (STATE-tracked, P008) — consistent.
- POV: clean — Doris's interior via observable cues; Callie's inferences marked ("Callie knew she could not").

### Value-shift verification (sweep override)

- Scene 1 `suspicion → documented seeing`: lands — the tumbler turns; "she had seen, and she had done the careful thing, which was nothing."
- Scene 2 `open paths → closed`: lands — corroboration path shut before Thursday's archive pull.
- Scene 3 `the demand held → the demand broken ahead of its test`: lands — the unconditional claim becomes conditional ("You find the rest of it before you come to my kitchen again"); needles shake for the first time.

### Resolution

- [ ] Minor issues fixed or accepted (F025 pending author approval)
- [ ] STATE.yaml updated (batched at sweep end)
