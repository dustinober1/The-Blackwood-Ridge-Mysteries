---
name: book-status
description: "Inspect manuscript health, chapter progress, gate check results, word counts, open Chekhov promises, and stylistic drift metrics across books and chapters. Use when user asks 'book status', 'manuscript dashboard', 'how far along is the book', 'what needs attention', or 'show project status'."
metadata:
  author: Storycraft Skills
  version: "1.0.0"
  category: cross-cutting
---

# Book Status Dashboard

Provides an executive summary of manuscript health, drafting completeness, gate checks, promise debts, and stylistic health across the entire book or series.

## Dashboard Metrics

1. **Chapter Ledger & Word Counts:**
   - Word count per chapter against target range.
   - Total book word count and pacing breakdown by act.
2. **Quality Gate Status:**
   - Status of `_Edits/Book-N/Chapter-NNN_Gate.md` for each chapter: `PASS`, `WARN`, `FAIL`, or `UNCHECKED`.
3. **Promise Ledger (`promises.yaml`):**
   - Active setups, due chapters, overdue promises, and deferred series threads.
4. **Editorial & Review Reports:**
   - Persona review coverage and consensus scores (`_synthesis.md`).
   - Unapplied revision items in `_Edits/Book-N/`.
5. **Drift & Cadence Health:**
   - Summarizes latest `drift-check` and `burstiness-check` findings.

---

## Procedure

1. **Scan `Chapters/Book-N/`:**
   - Count word totals and verify sequential numbering.
2. **Scan `_Edits/Book-N/`:**
   - Aggregate gate results, editor passes, and persona review tallies.
3. **Scan `promises.yaml`:**
   - Tally setup/payoff balance using `promises.py` status check.
4. **Render Markdown Dashboard:**
   - Output structured table with immediate blockers and recommended next actions.
