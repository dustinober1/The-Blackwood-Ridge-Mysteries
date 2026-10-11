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
**Draft word count**: 3408
**Checker**: continuity-checker discipline run inline (project agent-dispatch workaround); zero prior FAILs.

### Verdict: FAIL

### Major Issues

| # | Location | Issue | Canon reference |
|---|----------|-------|-----------------|
| 1 | prose L22 | "She **drove** out past the school... she parked behind Cross's cruiser and she sat for a moment with the **engine off**" — Callie has no car (series canon from Book 1's continuity fixes). Confirms ledger **F003** (MUST-FIX), passage 1 of 2. | canon/world-rules.md "Callie's transportation" |
| 2 | prose L64 | "She **drove** back down the lake road. In the **rearview mirror**..." — same contradiction, passage 2 of 2. Note: later the same day she "walked across the square to the shop" (L140), underscoring the anomaly. | canon/world-rules.md "Callie's transportation" |
| 3 | prose L26 | "she felt the place **as the bible had said she would**: heavy" — production-bible meta-leak; no in-world text has said the cove is heavy. Confirms ledger **F006** (MUST-FIX). Replace with the in-world phrasing ch5 already uses ("the place felt wrong in a way no one had ever named"). | findings.yaml F006; canon/world-rules.md |

### Minor Issues

| # | Location | Issue |
|---|----------|-------|
| 1 | prose L62 | "She nodded." — action beat, lint tag false positive. |

### Escalate (ambiguous — not a clean pass/fail)

| # | Location | Ambiguity | Why it can't be resolved here |
|---|----------|-----------|-------------------------------|
| — | — | — | — |

### Whole-manuscript checks

- Crutch phrases: "of a man" cluster, "did not say" → F022. Style sheet: `late spring`, `coming apart`, `setting-down` touch this chapter → F021.
- Promises: P004 (palm collapses ✓ "not into a fist but into a closing"), P005 (confession names the Harlow-barn lie ✓), P006 (dive executed ✓) all paid here; P009 (legal process) made here ✓ — all consistent with the ledger.
- Canon: dive entry 6:12, ring 8:14, remains at nine ✓; cove geography (eastern shore, ~40 yd, four pilings, willows, dock gone) ✓; confession content matches H2/H3 exactly; "Tell me the man is real" ✓; no handshake ("the shape of a door that existed but was not opened") ✓.
- Word count 3408 — largest chapter, within ±25% tolerance.

### Value-shift verification (sweep override)

- Scene 1 `dread → evidence`: lands — ring then remains; "this is a body now."
- Scene 2 `mask → collapse`: lands — "Not a tremor. A fine, invisible shaking... Now the deliberation was failing."
- Scene 3 `confession → process`: lands — "The arrest was not justice. It was the beginning of a process."

### Resolution

- [ ] Major issues fixed (awaiting author approval via F003/F006)
- [ ] Minor issues fixed or accepted
- [ ] STATE.yaml updated (batched at sweep end)
