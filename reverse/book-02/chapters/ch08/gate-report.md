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
**Draft word count**: 2743
**Checker**: continuity-checker discipline run inline (project agent-dispatch workaround); zero prior FAILs.

### Verdict: FAIL

### Major Issues

| # | Location | Issue | Canon reference |
|---|----------|-------|-----------------|
| 1 | prose L68 | Pulled-up bed's stakes read "*Ambition. **Infidelity**. Folly.*" — ch2 established the same cipher object as "Ambition. **Betrayal**. Folly."; world-rules pins "Betrayal" as canonical. Confirms ledger **F005** (MUST-FIX): change ch8 to "Betrayal". | canon/world-rules.md (floriography vocabulary); findings.yaml F005 |

### Minor Issues

| # | Location | Issue |
|---|----------|-------|
| 1 | prose L24 | Lint `pov_leak`: "She knew Doris already knew" — Callie's inference about Doris's knowledge; strict-POV call → F026. |
| 2 | prose L90 | "He nodded." — action beat, lint tag false positive. |

### Escalate (ambiguous — not a clean pass/fail)

| # | Location | Ambiguity | Why it can't be resolved here |
|---|----------|-----------|-------------------------------|
| — | — | — | — |

### Whole-manuscript checks

- Crutch phrases: "of a woman", "did not say" shares → F022. Style sheet: `almost-right`, `late spring`, `not knitting`, `the door` touch this chapter → F021.
- Promises: P003 paid here (demand broken, receipted via "Mae told me", survived — matches prose) ✓; P007 formalized ✓; the vow "not like this" minted (P012, series rule) ✓; P011 (Book 1's knock) correctly left unclaimed ✓.
- Canon: photo turned to wall and back ✓; "the grief could move now" ✓; cuttings line verbatim ("It won't be the same code. But the flowers will grow.") ✓; "Earlier than Marguerite." ✓; three-knock grammar ✓; timeline (third day → Friday next) matches beats 17–19 ✓.
- Ending: deliberately-earned lull (series close) — accepted, not a FLAT flag.

### Value-shift verification (sweep override)

- Scene 1 `frozen grief → moving grief`: lands — "the grief could move now... moving water is heavier than still water."
- Scene 2 `mirror → vow`: lands — "She had Marguerite's silence in her... not like this."
- Scene 3 `carried alone → threaded`: lands — Saturdays formalized; Mae's three knocks; "For now, that was enough."

### Resolution

- [ ] Major issues fixed (awaiting author approval via F005)
- [ ] Minor issues fixed or accepted
- [ ] STATE.yaml updated (batched at sweep end)
