# Book 2 Canon Decisions & Fix Worklist — reverse/book-02

Companion to `reverse-scaffold-analysis.md` and `findings.yaml`. Book 2 is
PRE-PUBLICATION and editable; per the author's standing instruction
(2026-10-11): fill the gaps, fix what the audit proves broken, and record
every decision here.

## MUST-FIX worklist (APPROVED & APPLIED 2026-10-11)

Four defects, all mechanically verified. None required re-drafting beyond
the flagged passages. **Author approval received 2026-10-11** ("Do what you
recommend," via the persona-panel triage in `books/book-02/reviews/
triage-2026-10-11.md`); all four applied to `books/book-02/manuscript/` the
same day — see findings.yaml F003–F006 resolution notes for the exact
applied forms. The panel independently confirmed the F006 meta-leak (R05
flagged 7:828 without knowing the ledger).

| # | Finding | Location | Problem | Proposed fix |
|---|---------|----------|---------|--------------|
| 1 | F003 (major) | ch7, two passages | **Callie drives** ("She drove out past the school... parked behind Cross's cruiser... engine off"; "She drove back down the lake road") — contradicts series canon: Callie has no car (Book 1 ch2 "drive home → walk home" audiobook continuity fix; Book 1 text "the long walk home"). | Rework transit: Cross collects her before dawn (in keeping with "I want you there" and "wear boots"), and she rides back with him or the dive team's vehicle; adjust the rearview-mirror beat to what she sees from the passenger window. ~4–6 sentences touched; voice intact. |
| 2 | F006 (major) | ch7 (cove description) | **Meta-leak**: "she felt the place as the bible had said she would: heavy" — the narration cites "the bible"; no in-world text has said this. | Replace with the in-world form the book already established in ch5: e.g. "she felt the place as the town's silences had always said she would: heavy" (or tie to "wrong in a way no one had ever named"). One clause. |
| 3 | F004 (major) | ch6 (Cross's call) | **Mae's diaper line**: "a man whose diapers she had changed" — impossible against Book 1's pinned ages (Mae ~59–60 by text arithmetic; Cross mid-fifties). | Rephrase to the compatible, bible-supported form: "a man she had known since he was a young deputy" (Book 1 bible's alternative) or "a man she had known since he was a boy deputy." One clause. |
| 4 | F005 (moderate) | ch8 (garden re-read) | **Yellow rose meaning drift**: ch2 "Ambition. Betrayal. Folly." vs ch8 "Ambition. Infidelity. Folly." — same cipher object, two meanings. | Harmonize ch8 to "Betrayal" (the book's established vocabulary; ch2 is the definition scene). One word. |

Not must-fix (recorded, no action unless the author wants them): the LOW
CONFIDENCE items in findings.yaml F017–F020 (estate-paperwork compression,
"two weeks" vs ~10 days, the Sunday reconstruction, the December lot's mixed
contents) — each reconcilable as written; fixing any would cost more prose
than it saves. The serial comma is a profile note, not a defect.

## Fills (decisions under the standing instruction)

| # | Item | Decision | Source |
|---|------|----------|--------|
| 1 | The botanical's title | **Flora's Lexicon of the Virginias (1873)** — adopted as the series reference name; the text never prints it, so no contradiction. | `[bible]` book-02/bible/premise.md |
| 2 | Wells's age | ~51 (nineteen in summer 1994 — "the summer we graduated"). | `[text-derived]` |
| 3 | Story-present | Late May – mid June 2026; ~6 months post-Book-1. | `[text+bible]` |
| 4 | Gus's legal process | **Tried** ("a murder trial six months ago") — fills Book 1's blank; imprisonment stands. | `[text ch5 + bible carry-forward]` |
| 5 | Helen Carmody | Relay-witness only in 1994; present-day status deliberately open (Book 3+ available). | `[text + bible rename note]` |
| 6 | Doris's age | "seventy or near it" (narrated estimate) — text-confirmed. | `[text ch2]` |

## Left open — deliberate doors (tracked in findings.yaml / promises.yaml)

- The Book 1 knock's identity (never claimed on the page).
- The rekeying's end (Book 3's records dispute).
- Wells's legal outcome beyond arrest (later books; Gus precedent applies).
- "The job" Lauren was leaving for.
- Wells's wife/children; Doris's husband; Marguerite's age and heirs.
- Harlan Beech's next book role (planted, unpaid — do not consume early).

## Bible alignment (reconciliation in brief)

- The text honors every carry-forward constraint: pariah state held; Mae
  knocks; Cross procedural (no handshake this time); Eli background + seed
  (the apprenticeship stays background, formalized only in the last chapter);
  the founding fraud not re-exposed; the botanical provenance continuous
  with Book 1 ch8 (found December; rest of lot arrives late May).
- The premise's "thirty-year-old accusation" is loose theme copy; the text
  is consistent at thirty-two years (1994→2026). Text stands.
- The bible's Helen Carmody rename (from a draft "Helen Ralston") is
  confirmed in the text — no collision with Book 1's disgraced family.
- One bible flavor line ("diapers") leaked into ch6 and is the F004
  must-fix — the bible's own compatible alternative ("known him since he
  was a deputy") is the fix source.

## Author-approved rulings — 2026-10-12 (decision sheet: books/book-02/audits/author-decision-sheet-2026-10-12.md)

| # | Item | Decision |
|---|---|---|
| 7 | F021 — hyphenation compounds | Resolved by rule, no prose edits: hyphenate only compound modifiers before a noun; open noun phrase is the default. Nominalized "the not-X" always hyphenated (registered free-indirect construction). "almost right" open as predicate; hyphenated modifier uses are motif phrasings. Rulings tabled in `style-sheet.md` § Compound rulings. |
| 8 | F022 — repeated phrases | Six deliberate refrains registered in `book.config.yaml` `voice_rules.motifs` (plain strings): of a man, of a woman, the back room, the bell rang, for thirty-two years, did not say. Connective-tissue repeats ("went to the", "for a moment", …) left as-is in published text; budgets for future books live in Book 3's style addendum. |
| 9 | F023 — voice-band lint tuning | Approved. `lint_suppressions`: tense_drift "all" (66 hits verified free-indirect/gnomic); em_dash_rate "all" (11.4–20.4/1k is the anaphoric signature). Suppression is recorded — reports still show counts. |
| 10 | F026 — POV-leak hits | The four hits (Marguerite had wanted; Mae knew it; Doris loved; Doris already knew) declared marked free-indirect inference — Callie's registered hand-reading skill. pov_leak suppressed in [ch02, ch06, ch08] only, so genuine head-hops elsewhere still report. |
| 11 | F024 — ch8 "she" openers | Accepted as voice-band for dialogue-light solo chapters (28.7% at 9% dialogue; AI-tell panel re-read passed the chapter). Tripwire moved to Book 3's style addendum: >20% she-openers + <15% dialogue = run interiority checks. |
| 12 | F025 + F027 — prose errata | Staged, not applied: `books/book-02/audits/errata-pending.md`. To be applied in one pass during the audiobook cycle (Annette re-delivery captures them in the highlighted PDF). 2026-10-12 re-verification: ch02's four sweep hits are false positives (no fix); ch05 "repeated" sanctioned in config; true errata = ch04 "said carefully" + F027's bed sentence. Action-beat "false positive" flags are never edits. |
| 13 | F029 — series-bible enrichment | Approved and applied 2026-10-12: Mae ~60 (diaper framing retired), Callie born ~1990 / glass ~1999, Wendell Pike + historical-figures reference added, open doors recorded in story-memory, world.md corrected (keystone is the survey-records volume, not a Bible; fraud ~140 acres / five families), Book 3's bible timeline de-staled. Deferred promises P008–P012 registered in the series promise map (series-outline.md § Deferred promise map). |
| 14 | F030 — ch01 outline citation | Corrected to H7–H10 (the rows that exist and that ch01 draws on). Doc-only. |
