# Book 2 — Pending Errata (audiobook batch)

**Staged:** 2026-10-12, per the decision sheet ([author-decision-sheet-2026-10-12.md](author-decision-sheet-2026-10-12.md), rows F025 + F027). **Apply in one pass during the Annette audiobook re-delivery cycle** — fix text, rebuild the highlighted narration PDF, so the narrator's copy captures everything at once. Do not apply standalone.

## Item 1 — ch04, adverbial tag (F025)

> "I think she wrote down what she saw," Callie said carefully. "Not that he did it. She wouldn't write that. She wrote what she —"

**Fix:** cut the adverb — `"I think she wrote down what she saw," Callie said.` The care is in the hedged claim itself; the voice-bible's allowed tags are plain said/asked/answered/replied.

## Item 2 — ch02, ambiguous "bed" sentence (F027)

> That the woman lying in the bed she was kneeling in had tried, at the end, to make up for all the years she had not tried.

**Fix (minimal):** `That the woman lying in the flower bed she was kneeling in had tried, at the end, to make up for all the years she had not tried.` — names the bed, kills the body-in-a-bed misread. (The surrounding "turned earth of the remembrance bed" keeps the register.)

## Resolved without prose changes

- **ch05 "Cross repeated"** — the tag is semantically exact (he *is* repeating). Sanctioned instead: `repeated` added to `allowed_dialogue_tags` in `reverse/book-02/book.config.yaml` (2026-10-12). No text change.
- **ch02's four lint hits (L53/L75/L83/L105 in the sweep)** — re-verified against the current text 2026-10-12 and all are **false positives**: quoted speech that merely *begins* with "She asked…"/"They said…" (real tags are lowercase); a complete quoted sentence (`"I'm sorry."`) correctly ending before new narration; and "Mae nodded." as its own action-beat sentence. Never edits. The 2026-10-11 triage's "genuine punctuation fixes in ch02" no longer exist in the post-cadence-pass text.
