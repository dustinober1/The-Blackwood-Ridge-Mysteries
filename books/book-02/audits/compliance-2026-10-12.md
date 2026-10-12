# Skills Compliance Audit — Book 2: The Botanical Confession

**Date:** 2026-10-12 · **Scope:** the project-local skill battery added in commit `00c6654`, run report-first against the post-revision published text (`manuscript/ch-01..08.md`, 22,463 words)
**Verdict: COMPLIANT.** No skill found a defect requiring repair in the published text. Two independent methods (drift-check statistics and a blind cold read) converge on one craft watch-item for the series, and a handful of style-sheet notes carry forward to Book 3.

Raw mechanical output: [mechanical-scan-2026-10-12.json](mechanical-scan-2026-10-12.json)

## What ran, and results

| Skill | Verdict | Headline |
|---|---|---|
| promise-tracker / fiction-promises | **PASS** | `promises.py --ledger reverse/book-02/promises.yaml --final` exit 0: 12/12 paid or deliberately deferred; deferred threads (P008–P012) trace into `series-outline.md` (Book 3 ends with Beech arrested and seeds the records thread; Book 4 is the archive book) |
| drift-check (drift.py, ch1–8) | **PASS + 1 watch** | Specifics density flat (35.8 vs 35.6/1k — no back-half thinning). Closer dies: none at script threshold. Pet words are scene-anchored nouns (ch7 dive: water/dark/ring), not tics. **Watch:** negation-pivot density rising — front half 8.5/1k vs back half 12.6/1k (peak ch6: 17.4) |
| burstiness-check (measure.py ×8) | **PASS + watch** | Sentence-length σ: book mean ≈15.8; ch4 flattest at 12.79, ch5 borderline (13.48), ch7 most varied (22.07). Interiority risk HIGH in ch1/2/8 (dialogue 9–14%) — structural, matches the panel's known profile; A01 re-read verdict was "reads human," so these are look-closer flags, not findings. "She" sentence-openers 21.7–28.7% in ch2/3/5/6/8 (close-third POV cost; ch8's 28.7% + 7-sentence same-opener run is the outlier) |
| fiction-aiism-editor criteria | **PASS** | Forbidden AI words: **0** (6× "rhythm," all literal-arrangement/narrative uses). Math/analytical metaphor: **0**. Self-announcing narration: **0**. Over-qualified adverbs: **0**. "wasn't X, it was Y": **0**. Em-dash 11.4–20.4/1k — dispositioned voice-band per F023 (reread triage) |
| kill-acronym | **PASS** | Zero initialisms in the manuscript |
| kill-hedge | **PASS** | Near-zero: quite ×11, "kind of" ×13 (mostly dialogue), rather ×4, everything else ≤1 |
| kill-passive | **PASS** | 2 explicit-agent passives book-wide, both defensible ("It was planted by meaning" is the garden-as-text thesis) |
| kill-soft | **PASS** | 2 uses (ch7), both literal ("mud was black and soft," "paper gone soft with age") |
| kill-flat | **PASS** | 22 uses — all literal (the registered "hands flat, palms down" motif) or Doris-accurate per voice-dna ("Dry, almost flat"). "Her voice was flat and final" is her registered register |
| kill-opinion-personification | **PASS** | 0 uses |
| kill-the-whole | **WATCH (minor)** | 11 uses; ch3 ×5. In-voice intensifier, slightly hot in one chapter |
| kill-person-who | **PASS + watch** | 22 uses ("the [quality] of a man/woman who"), ≤4/chapter. The motif's founding phrasing is *registered canon* (ledger P004, open palm). Voice device, not a die — but the rate is a Book 3 style-sheet item |
| kill-simile | **PASS + watch** | "the way" ×50, "as if" ×13 (ch1 heaviest: 10+8). Sanctioned: voice-dna POV diction ("reaches for historical analogies"), garden-as-text signature. Ch1's comparison load is the note |
| kill-crutch | **PASS + watch** | seemed ×0 (notable), really ×2, slightly ×0. "just" ×30 with a back-half rise (ch6/7/8: 6/7/7) — sampled: load-bearing "merely" and the registered ch7 payoff "the hand becoming just a hand"; the trend is the note, not the uses |
| levelup (filter words) | **PASS** | Light for close-third: felt ×15, looked ×51 (mostly literal gaze verbs), noticed ×2–5/ch. Panel post-revision rated prose texture 4.5–5; a dedicated cut pass not warranted |
| nominalization-hunt | **PASS** | Hits are the book's registered free-indirect cataloguing ("the not-X" as filed emotion) — bible-licensed, not the abuse pattern the skill hunts |
| fragment-hunter (pass 1 + judgment) | **PASS** | 176 candidates; sampled pass 2: overwhelmingly bible-licensed emotional-peak fragments ("The book waited.", "Palms down.", one-word decode beats) plus splitter false positives (dialogue tags, scene breaks). Voice-dna explicitly registers fragments at peaks; blanket kills would violate the bible. Performable for narration |
| gate-check (canon / POV / closers, book-level) | **PASS** | Timeline arithmetic verified (1994 + 32 = 2026 present; estate lot consigned pre-death — Eli flags it: "I didn't put it together when the lot first came in"); Cedar Lake/Blackwater Cove nesting correct; archive rekeying escalates Book 1's revoked access; Doris/Wells/Mae/Eli/Cross states match bible. POV holds — both panel-flagged intrusion spots are now framed as Callie's inference (her registered skill); one residual free-indirect slide into Wells's interior remains in ch7 (one sentence, "the not-knowing was the floor dropping out") — cosmetic only |
| series-continuity (vs Book 1) | **PASS** | Book 1 ending hand-off verified: the unknown hand described identically, the two-knock motif minted in Book 1's final lines, glass-on-felt-rest, Ralston/Ridgeway/Eli references all consistent. Deferred promises registered at series level (series-outline.md serves as the promise map — note: no `series-arc.md` file exists; the fiction-promises skill's canonical path) |
| coldread (isolated agent, general-reader) | **CONVINCING** | Claim tested: close third on Callie Thorne, cataloguing intelligence filtering grief, small-town Virginia present day. "The close third is airtight, the cataloguing intelligence is the book's actual engine." Caveats below |
| reader-persona-review / review-panel | **COVERED** | Panel cycle CLOSED 2026-10-11 (mean 3.75★→4.25★, zero convergent issues on re-read, A01 verdict now "reads human"). Not re-run; no major revisions since |

Skipped as not-audit skills (generative/planning, wrong domain, or already-built outputs): fiction-outline/synopsis/series-outline/theme/world/characters/places/polities/religions/factions/psych/audience/genre/story-sparks/voiceprompt/writechapter/revise/scenes/dialogue-preflight, nonfiction-* (wrong domain), fantasy-settlement / town-generator / name-generator (worldbuilding generators), book-packaging & compile-manuscript (assets/exports already exist), chapter-pipeline (drafting workflow), pangram (redundant with burstiness-check per its own pairing note), skill-builder (meta), fiction-style (generator — but its review-guide criteria were the aiism scan's reference).

## The one convergent watch-item

**Negation-inversion cadence accelerating through the back half.** drift-check measures it (8.5 → 12.6/1k, ch6 peak 17.4); the blind cold reader *independently* reported "by the final two chapters I was predicting sentence shapes before reading them." The "Not X. Y." / "the not-X was Y" move is this book's registered voice (the cataloguing mind), and ch7's five "not X but Y" instances were individually judged earned (two are registered motif payoffs — "collapsed, not into a fist but into a closing"). This is a **rationing question for Book 3, not a Book 2 defect**: consider registering a soft per-chapter budget in voice-dna, and have Book 3's line-edit pass watch the density curve from chapter 1 rather than after it.

## Carry-forward notes (no action required on Book 2)

1. **Closer die:** ch6 and ch8 both close on "She thought of Doris…" refilled with different details — below drift.py's similarity threshold but the only repeated chapter-ender frame in the book.
2. **ch3** holds the book's hot spots for "the whole" (×5) and is, with ch1, the heaviest comparison chapter — fine at novella scale, worth style-sheet attention if the series novellas grow.
3. **Cold-read friction for series newcomers:** Pike's name dangles unanchored in ch1's loupe scene (Book 1 shorthand elsewhere self-explains), and two "convenient acuity" beats (half-heard confession through a wall; Ambler instantly knowing about the Dabney books) lean on luck rather than method. Both are singletons; the panel did not flag them.
4. **Cold read soft spots (absences, not contradictions):** Callie's mid-life and the present day are implied rather than enforced on the page.
5. **Infrastructure:** this repo uses the `bible/` layout, not the skills' canonical `Wiki/` layout — the promise ledger lives at `reverse/book-02/promises.yaml` and must be passed via `promises.py --ledger`. Books 3+ may want the ledger moved into each book's own folder.

Because Book 2 is published and its marketing is held only for the audiobook, nothing above justifies a text change now — any prose edit would flow through the audiobook re-delivery workflow instead. The audit's purpose is confirmation: **Book 2 is in compliance with the full skill battery as published.**
