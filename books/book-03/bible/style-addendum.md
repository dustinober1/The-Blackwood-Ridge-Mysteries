# Book 3 Style Addendum — budgets, tripwires, pre-publication checklist

**Created:** 2026-10-12, from the Book 2 skills-compliance audit (`books/book-02/audits/compliance-2026-10-12.md`), the Book 2 panel carry-forwards (`books/book-02/reviews/triage-2026-10-11-reread.md`), and ledger rows F021–F031 (`reverse/book-02/findings.yaml`).
**Precedence:** `voice-dna.md` governs; this addendum adds numeric budgets and tripwires so Book 3's known drift patterns are watched from chapter 1 instead of discovered at chapter 8. Nothing here overrides a registered voice device — it rations the devices.

## A. Where Book 3 stands today (measured baseline, current manuscript)

Ran the same battery used on Book 2 (drift-check, burstiness-check, kill-family scans) on all 8 chapters. Raw output: `books/book-03/audits/mechanical-scan-2026-10-12.json`.

| Signal | Book 3 now | Book 2 (reference) | Read |
|---|---|---|---|
| Negation-pivot density, front → back half | 9.1 → 10.5/1k | 8.5 → **12.6**/1k | Within budget — the Book 2 failure mode is *not* repeating |
| "not X but Y" explicit inversions | **3** book-wide | 9 (5 in ch7 alone) | Clean |
| "of a man/woman who" constructions | **5** book-wide | 22 | Clean |
| "the whole" | 6 book-wide | 11 | Clean |
| "just" | 16 book-wide | 30, back-half rise | Clean |
| Forbidden AI words / opinion-personification / "wasn't X, it was Y" | **0 / 0 / 0** | 0 / 0 / 0 | Clean |
| Sentence-length σ, ch1–3 → ch4–8 | **12.8 → 7.2 (declining)** | 15.8 mean, ch7 peak 22.1 | **Watch — see B1** |
| Em-dash per 1k, ch1–3 vs ch4–8 | **9–12 vs 2–3 (thinning)** | 11.4–20.4 (voice-band) | **Watch — see B1** |
| Fragment candidates per chapter | 13–16 (ch1–3) → **34–67 (ch4–8, rising)** | 15–28 | **Watch — see B2** |
| Interiority risk | HIGH only ch2 (dialogue 12.6%); ch4–8 LOW | HIGH ch1/2/8 | Healthy |
| "She" opener peak | 22.7% (ch2) | 28.7% (ch8, accepted voice-band) | Within band |
| Chapter closers | Varied frames | — | One note, see B3 |

The headline is the opposite of Book 2's: **Book 3's back half is rhythmically flattening** — sentences converge on uniform mid-length, the em-dash anaphora signature drops 4×, and fragment density climbs into ch8. The dialogue ratios are healthy (12–30%), so this is rhythm, not interiority.

## B. Watch items (fix at this book's revision stage, not after release)

1. **Back-half rhythm flattening (ch4–8).** Sentence σ falling monotonically to 7.2 and em-dash rate to 2–3/1k is the statistically flat shape the burstiness skill warns about — Book 2's drift problem expressed in rhythm instead of negation. Before export: a rhythm pass on the two emotional-peak chapters (the midpoint inversion chapter and the confrontation chapter), restoring the long-short variation and selective em-dash anaphora at peaks only. Target: no chapter below σ ≈ 9 unless flatness is a deliberate quiet-chapter choice (say so in the outline if so).
2. **Fragment density rising into the back half (ch8: 67 candidates).** Book 2's fragments were bible-licensed decode-beats and SPAREd on judgment; Book 3's back-half count is 2–4× Book 2's. Run fragment-hunter on ch4–8 before the audiobook — either the density is the planned fracture register (then it's fine) or it's chop the narrator will stumble on.
3. **Closer note:** ch1 and ch2 both close on the almost-right tea motif. It's registered and developing (ch1: "not sure the almost was enough" → ch2's variation), so it's legal — but a third consecutive tea-closer in ch3 would make it a die. No other closer frames repeat.
4. **Legit hits to leave alone:** the one `statistic*` match (ch1) is Larter's stylometry — in-world, correct. WPA (ch2) and LOST (ch5) are intentional. Pet words (cross ×107, beech ×70, shelf/folios 90%+ back half) are scene-anchored antagonist/archive nouns, not tics.

## C. Drafting and line-edit budgets (per chapter, unless the outline says otherwise)

- "Not X. Y." / "the not-X was Y" / "not X but Y" inversion family: **≤3 explicit "not X but Y"**; the broader "the not-X" nominalization is the signature — keep it but ≤5.
- "the [quality] of a man/woman who": **≤2** (founding uses for a new character may take one more).
- "the whole": **≤2**. "just": **≤4**. Comparison family (the way / as if / like a): ~3–4 per 1k words is this voice's normal; **flag any chapter over 6/1k**.
- She-opener tripwire: **>20% "She" openers combined with <15% dialogue in one chapter** = run the interiority checks (break paragraphs on new action/sensory beats; lead with the concrete object).
- Inherited device caps from Book 2's cadence trim (F031): tumbler-turn ≤2 per book, "its own" ≤3, "Not a question. A naming." ≤2 — Book 3 starts at the trimmed budget, not Book 2's pre-trim density.
- Series-entry anchoring: any Book 1–2 name (Pike, Wren, Gus, Ralston, Harlan Beech, the keystone) gets a one-clause anchor on first use — coldread showed Pike dangling for readers who start mid-series.

## D. Refrain registrations (stop the linters flagging deliberate voice)

Register as motifs so mechanical checks report them as voice, not findings: *of a man / of a woman*, *the back room*, *the bell rang*, *did not say*, *the almost-right tea*, the hands-read motif. (Pairs with decision-sheet row F022, which does the same for Book 2.)

## E. Pre-publication checklist for The Challenger

- [ ] Rhythm pass on the emotional-peak chapters (B1) — σ ≥ 9, em-dash signature re-entered at peaks only
- [ ] fragment-hunter pass ch4–8 (B2) — kill or confirm SPARE against the decode-beat license
- [ ] Hyphenation rule applied (F021 rule: compound modifiers before nouns only; "almost right" open; "the not-X" always hyphenated)
- [ ] Re-run drift-check + burstiness-check after revisions: negation rise ≤3/1k front→back; σ not declining monotonically
- [ ] coldread with a **series-entry claim** (does ch1 land for a reader who hasn't read Books 1–2?)
- [ ] Create `books/book-03/promises.yaml` (new convention: ledger lives in the book folder) and pass `--final` before export
- [ ] Kill-passes at line edit: kill-the-whole, kill-crutch `just`, kill-soft (15 uses, currently literal — re-sample after the rhythm pass)
- [ ] Panel re-run only if major revisions land (per the triage loop rule)

## F. Provenance

Book 2 audit 2026-10-12 (convergent drift finding + coldread) · reverse/book-02/findings.yaml F021–F031 · panel carry-forwards (fairly-clued red herring, pivotal Mae/Cross beats on-page, varied endings from the start — already honored in this outline's midpoint-inversion structure; keep them honored in draft).
