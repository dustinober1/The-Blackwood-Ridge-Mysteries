---
name: series-continuity
description: "Audit character status, resolved vs lingering secrets, timeline chronology, and spent promises across multiple books in a series to prevent cross-book plot holes. Use when user says 'series continuity check', 'check across books', 'audit series consistency', 'multi-book consistency', or 'series continuity audit'."
metadata:
  author: Storycraft Skills
  version: "1.0.0"
  category: fiction-editing
---

# Series Continuity Auditor

Audits multi-book consistency across drafted and released volumes in a series. Verifies that character physical states, emotional trajectories, world changes, and spent plot points remain coherent from Book 1 to Book N.

## Dimensions Audited

1. **Character State Persistence:**
   - Physical scars, chronic conditions, age progression, family/relationship status.
   - Professional titles, jurisdictions, and legal constraints.
2. **Spent Mysteries & Secret Protection:**
   - Verifies that secrets solved in Book N are not re-treated as unknown in Book N+1.
   - Ensures information asymmetry between characters remains realistic.
3. **World Chronology & Seasons:**
   - Weather, seasons, calendar elapsed time across book gaps.
4. **Series Promise & Thread Ledger:**
   - Cross-checks `Wiki/Story/series-arc.md` and deferred promises in `promises.yaml`.

## Procedure

1. Read `Wiki/Story/series-arc.md` and `Wiki/Characters/`.
2. Inspect latest chapters of Book N-1 and opening chapters of Book N.
3. Output continuity report into `_Edits/Book-N/Series_Continuity_Report.md`.
