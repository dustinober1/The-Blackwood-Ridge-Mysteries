---
name: kill-acronym
description: Hunt unexplained initialisms and acronyms on first use across a chapter, flag them, and expand on first occurrence so every reader can follow (flag-first; edits in place when the expansion is unambiguous). Targets first-use of tokens like AI, ML, NLP, GDP, UNESCO without a prior spelling-out. Use when user says "kill-acronym", "flag acronyms", "spell out first use", or "explain initialisms".
metadata:
  author: Nonfiction Toolkit
  version: "1.0.1"
  category: nonfiction-editing
---

# Kill the unexplained acronym — spell it out, then let it ride

A first use that assumes the abbreviation is already known is a reader-trip: the
term appears bare, the reader either stumbles or silently fills a wrong expansion,
and every use after it compounds the ambiguity. The pass is flag-first — it reports
every initialism/acronym and marks the first bare occurrence of each — and it edits
in place only when the expansion is unambiguous (a quoted source, a project term
list, or a discipline-standard spelling that the style guide already endorses).

The request arguments = the chapter file(s): a path, a file pattern, or several
paths. Resolve it to a concrete file list before doing anything.

## What to keep vs. fix

**KEEP (do not touch):**
- Initialisms/acronyms that are **universally known to the book's audience** and that
  the project style guide or audience profile already treats as safe to use bare —
  check `Wiki/Style/style_guide.md` (and `Wiki/Style/audience.md` for the bracket's
  assumptions) before treating a common one as a violation.
- Acronyms whose expansion is **already established earlier** in the file (or an
  earlier chapter the reader has seen) — only the *first* bare use in a reader's
  path is in scope.
- **Quoted / cited material** where the source uses the bare acronym and changing it
  would mis-quote or alter the citation.
- Standard units and symbols that are not really abbreviations: "DNA," "pH," "MRI"
  (where the discipline owns the short form) — confirm against the style guide; when
  in doubt, KEEP and flag for the author.

**FIX (flag, then expand on first use when unambiguous):**
- The **first bare occurrence** of an initialism/acronym in a file that has no prior
  spelling-out — flag it; if the expansion is recoverable from context or a quoted
  source, rewrite to `Term (ACRONYM)` and let later uses stand bare.
- An acronym **re-declared** later in the same file ("GDP — gross domestic
  product" on line 2, then again on line 412) — delete the later re-declaration;
  keep the first expansion only.
- An acronym that **collides** with another meaning in the same file (e.g., "AI"
  used for both "Artificial Intelligence" and "Application Interface") — flag as a
  collision; do not edit without the author's word.
- **Repetition of bare first-uses** across the run: each acronym should be expanded
  at its first occurrence and nowhere else; a second bare "first use" in the same
  file is a FIX (delete the redundant expansion).

The fix is expansion to `Term (ACRONYM)` at first occurrence, not substitution —
and never guess an expansion. When the meaning is not recoverable with certainty,
flag only and leave the text untouched for the author.

## Procedure

1. **Resolve the request arguments to files.** Build the candidate acronym list by
   scanning for capitalized initialism tokens (2+ consecutive uppercase letters,
   optionally with periods). The canonical target set lives in
   `references/acronym.md`.
2. **Triage:** for each candidate, find its **first bare occurrence** per file (an
   occurrence is "bare" if it is not immediately preceded by an expansion on the
   same line or the prior line, and not preceded by any already-recorded expansion
   for that acronym earlier in the file). If the run is small, scan inline. If many
   files, split into up to 6 roughly equal groups and use one focused worker per
   group in parallel when the host supports workers; otherwise process sequentially.
   Each worker must read a full sentence of context around each first-use hit to tell
   a bare occurrence from a legitimately established one.
3. **Each worker gets:** its exact file list; the KEEP/FIX rules verbatim (from
   `references/acronym.md`); the keep-safe acronym set from the style guide (if any);
   instruction to read a full sentence of context around every candidate and to
   respect previously established expansions within the same file. It reports a
   per-file verdict list: each hit tagged (KEPT-universal / KEPT-established /
   KEPT-quoted / KEPT-discipline / FLAGGED-ambiguous / EXPANDED / DELETED-redundant)
   with before→after for changes and the acronym + its location.
4. **Verify when all workers return:** cross-check that each surviving bare acronym
   has exactly one EXPANDED first use and zero KEPT/undefined conflicts; confirm no
   worker guessed an expansion (every EXPANDED must cite its source: context, quote,
   or style guide). Worker edits make your in-context file state stale; reread before
   any follow-up edit. Produce the consolidated flag list and the before/after
   first-use count.
5. Offer to apply expansions or leave flagged. Do not commit unless asked.

## Notes

- This pass is detection-heavy and flag-first by design: guessing an acronym's
  expansion is worse than leaving it for the author. An expansion is only safe when
  it is recoverable from a quoted source, a project term list, or a
  discipline-standard spelling the style guide already endorses.
- "First use" is reader-path-sensitive across the whole book, not just the file.
  When running over a single chapter in isolation, treat an acronym as established
  only if it was spelled out earlier in the same file.
