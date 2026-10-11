# Cross-Book Continuity — Book 1 ↔ Book 2 ↔ series-bible

Produced 2026-10-11 from the two reverse-engineered scaffolds
(`reverse/book-01/`, `reverse/book-02/`), the production bibles, and
`series-bible/`. Method: both books' canon files compared fact by fact —
recurring characters, timeline adjacency, world rules, voice, threads.

**Verdict: with the four approved must-fix items applied, no cross-book
contradiction remains that a reader of both books would hit.** Three of the
four findings are cross-book in nature (they only exist because Book 1 is
frozen canon); one is Book 2-internal.

## Must-fix before publishing Book 2 (details in reverse/book-02/canon-decisions.md)

1. **Callie drives (B2 ch7)** — contradicts Book 1's established no-car canon
   (audiobook continuity fix + "the long walk home"). Cross-book, reader-visible.
2. **"as the bible had said" (B2 ch7)** — production-bible meta-leak in narration.
3. **Mae's diaper line (B2 ch6)** — age-impossible against Book 1's pinned
   arithmetic (Mae ~59–60, Cross mid-fifties).
4. **Yellow rose: "Betrayal" (ch2) vs "Infidelity" (ch8)** — cipher-object
   meaning drift.

## Verified continuity (no action)

- **The hook chain**: Book 1 ch8's botanical (found in an estate lot, "eighth
  day" ≈ mid-December 2025) → Book 2 ch1 ("Since December — the night she'd
  found it"; the rest of the lot released late May 2026 once "the paperwork
  finally cleared"). Timeline adjacency holds: Book 1 present late 2025,
  Book 2 late May–June 2026 (series-bible).
- **The rituals**: bergamot "almost right, one register short" (B2) continues
  Book 1 ch8's "for the first time since the auction it tasted like tea" —
  the register deliberately still incomplete; the glass "hers by choice and
  not by ghost" continues ch8's reclaiming; the floorboard rests in B2 (the
  series renews it in Book 4 per series-bible).
- **Recurring arcs**: Mae (fracture → three-knock grammar, "Earlier than
  Marguerite"); Cross (Book 1's handshake explicitly NOT repeated — "the
  shape of a door that existed but was not opened"; hat-withholding signal
  consistent); Eli (flinch → buttons → provenance catch → apprenticeship).
- **Town state**: Society closed since the Ralston money dried up ✓; "a
  murder trial six months ago" fills Book 1's legal-process blank; the
  pariah state matches carry-forward exactly ("useful, not welcome").
- **World facts**: The Foxed Page, the square, the archive log grammar, the
  council mechanism (rekeying = deliberate rhyme of Book 1's lockout), Cedar
  Lake/Blackwater Cove (new, no conflict), Pippin Street (new).
- **Voice**: same spine — single POV, documents-only past, verdict fragments,
  hands as tells. Gus's over-control tell (B1) and Wells's open-palm tell
  (B2) are a deliberate series pattern (kindred mechanisms, different men) —
  not self-plagiarism; both are motif-registered.
- **Plants honored**: Harlan Beech (Book 3's accused) present but unpaid;
  the rekeying left open for Book 3's records dispute; no founding-fraud
  re-exposure; Eli stays background until the final chapter.

## Open series doors formally ledgered (from both scaffolds)

Eleanor's death revisitable · Jacob Wren's fate · J. Fenn's identity · the
Book 1 knock · land-restitution aftermath · the rekeying's end · Wells's
legal outcome · Helen Carmody's availability · Harlan Beech (Book 3) · the
apprenticeship long-arc · the vow *not like this*. All tracked in the two
`promises.yaml` ledgers with `deferred_to_series: true`.

## Series-bible enrichment proposals (from Book 1 reconciliation — still staged)

See `reverse/book-01/reconciliation.md`: Mae's age correction in the
recurring-character file, Callie's birth-year correction in the series
timeline, adding Wendell Pike + historical figures to the series-bible, and
recording the open doors. **Not applied — awaiting approval** (fold into the
same approval as the must-fix list if desired).

## Recommendation

Approve the four must-fix items; apply them as surgical edits to
`books/book-02/manuscript/` (ch6 one clause, ch7 two passages, ch8 one
word); re-run `books/book-02`'s export with the heading-level fix (the
legacy `build.sh` produces level-two chapter headings — port the remaster's
fix); correct the status ledger (Book 2 marked `published` in progress.yaml
though never uploaded). The remaster worktree's validated upload package
remains the recommended release vehicle.
