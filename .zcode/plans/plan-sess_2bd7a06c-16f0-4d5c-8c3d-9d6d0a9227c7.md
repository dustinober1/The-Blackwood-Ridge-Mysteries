# Book 1 Audiobook Fixes — Round 2 (Highlighted Production PDF for Annette)

Annette (narrator) flagged 4 continuity issues while recording from the July 2026 narration PDF. Deliverable: **an updated narration manuscript PDF with the edited paragraphs highlighted**, so she can see exactly what to re-record. Prose fixes follow the July 10 precedent (prose-only edits to chapter files on main).

## The 4 edits (source of truth: `books/book-01/manuscript/`)

**1. "Threads" beat lands too late** — `ch-02.md` lines 68–76 (her p10)
Mae says "not pulling at certain *threads*" (line 68), but "On the word *threads*, her hands stopped moving" (line 74) sits two paragraphs later — after the "too specific question" narration and Callie's "At the archives" reply — so in audio it reacts to nothing.
Fix: resequence — line 68 ends at "...She paused, her hand resting on a spine."; the line-74 hands-stop paragraph moves up directly after it (text unchanged); Mae's "His notes, though. Wendell's. He keep all that at the archives, or did he have copies floating around? Papers somewhere else?" becomes its own paragraph after the beat; the three following paragraphs stay in order.

**2. "Long drive home" — she walked** — `ch-02.md` line 18 (her p8)
Chapter 1 establishes Callie walks everywhere ("She crossed the square on the diagonal"); no car exists in the book.
Replace "the long drive home with the heater on and her hands steady on the wheel and her mind somewhere very far from the road" → "the long walk home with the mist on her coat and her hands deep in her pockets and her mind somewhere very far from the square".

**3. "She sold nothing" vs. the gift she wraps** — `ch-02.md` line 20 (her p8)
"She sold nothing." → "She sold almost nothing." (the birthday-gift customer did buy; stays consistent with Chapter 8's "eleven books, which was normal").

**4. The coat she never put on** — `ch-07.md` line 50 (her p34)
Callie is indoors all evening, answers the knock, then later "took it off and hung it on the hook" — the listener never saw her put it on.
Replace "Callie came out of the back room and stopped just before the floorboard creaked." → "Callie pulled on her coat against the evening chill and came out of the back room, stopping just before the floorboard creaked."

## Main deliverable: highlighted narration PDF

New `books/book-01/audiobook/` folder containing:
- **`The-Annotated-Murder-Audiobook-Narration-Manuscript-2026-10.pdf`** — full narration manuscript matching her July copy's structure: title page (updated to "Final corrected production copy — October 2026"), the Narrator Notes page (pronunciations, Latin guide, performance guidance — recreated verbatim from the July PDF since no source for it exists in the repo), then Chapters 1–8.
- **Every edited paragraph highlighted** (yellow, paragraph-level): the four passages above — for fix 1 that means the whole resequenced block from ""No." Mae smiled..." through "...eat the rest of that soup." so she re-records it as one clean passage.
- A short **"October 2026 revision" block on the notes page (not for recording)** listing the 4 changes with chapter + opening words of each highlighted passage, and the instruction: highlighted paragraphs = re-record; all other text unchanged. References are by chapter/first-words, not July page numbers, since pagination will shift.
- The **build source stays in the repo** (assembled markdown + highlight manifest + the exact command used) so round 3 can regenerate in minutes.
- Also drop a copy in `~/Downloads` next to her July PDF for easy attaching to WhatsApp.

Build approach: chapter markdown → HTML with `<mark>` highlighting → PDF (pandoc/weasyprint or headless Chrome; exact tool confirmed at implementation, pdf skill as fallback). Styled to match the July copy (serif, running header, page numbers).

## Still doing

- Prose fixes committed on branch `agent/book-01-audiobook-round2`, PR to main: one commit for ch-02.md + ch-07.md, one for the audiobook folder.
- Verify after editing: re-read the four passages in context; grep book-01 to confirm no other car/drive/wheel references remain; open the generated PDF and confirm the highlights land on the right paragraphs and the notes page is complete.
- A short suggested WhatsApp message summarizing the 4 changes for Annette.

## Explicitly out of scope

- No epub/dist rebuild on main (July precedent is prose-only; published-edition updates ride the remaster).
- Remaster worktree untouched (it deliberately left Book 1 prose unchanged — no conflict).
- No additional audit pass (just the 4 flagged items, per your choice).