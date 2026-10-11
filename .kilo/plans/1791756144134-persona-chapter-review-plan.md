# Plan: Run personas.md through manuscript chapter-by-chapter

## Goal
Run each persona from `docs/reader-personas/personas.md` through the manuscript(s) chapter-by-chapter, producing persona review outputs per chapter/persona as specified, without overloading context. 

## Constraints / Requirements
- Follow protocol from `docs/reader-personas/README.md` exactly: report template, entry point, spoiler discipline, save to `books/book-NN/reviews/<persona-id>.md` (create reviews dirs as needed), synthesize with `_synthesis.md`.
- Use reader-facing exports: `books/book-NN/export/manuscript-combined.md`. Do not give personas bibles/mission locks/story-memory except where explicitly allowed (Craft & Continuity/Industry groups D,E,F may read bibles). 
- Persona library: 123 personas in 21 groups (per personas.md). 
- Manuscripts: Books 1-5 have exports; chapter structure varies (Book 2 uses `##` chapter headings, Books 3-5 use `# Chapter N — ...`). 
- Must process chapter by chapter per persona to avoid context overflow. 
- Run for each persona chapter by chapter (as requested). 

## Affected boundaries
- Inputs: `docs/reader-personas/personas.md`, `docs/reader-personas/README.md`, `books/book-NN/export/manuscript-combined.md` for target books (start with Books 2-5 per "Review scope: Books 2–5 now"), chapter boundaries parsed per book.
- Outputs: `books/book-NN/reviews/<persona-id>-ch-XX.md` or per-chapter review files, plus final per-persona consolidated review and `_synthesis.md`. Need to decide structure - "break it up so it is getting a good solid review and not overburding the context window. This should be done for each persona chapter by chapter." So write chapter-specific review notes per (persona, chapter), then aggregate.

## Approach
1. **Parse chapter boundaries** for each book's export (extract line ranges for each chapter). Build index: for Book 2 (## headings), Books 3-5 (# Chapter headings), Book 1 similar. 
2. **Parse personas.md** into structured entries: group, ID (R01 etc), name, entry, loves/hates/checks/rates, full text. Also know the 21 groups. 
3. **Design chunked review process**: for each selected persona, feed chapter chunk + persona spec + prior chapter summary (minimal) to produce chapter review using the required template fields. Keep context small by only passing current chunk + running summary.
4. **Orchestration**: implement as a script/command sequence (Python) to split manuscripts by chapter ranges, iterate personas × chapters. Write outputs under `books/book-NN/reviews/chapter-reviews/<persona-id>/ch-<nn>.md` and/or also produce the final per-persona `<persona-id>.md` as specified by README. The README says "save as `books/book-NN/reviews/<persona-id>.md`" - that’s the full review. So do chapter-wise analysis but consolidate to final persona review per book.
5. **Safety/constraints**: respect entry points (cold vs series). Don’t leak bibles to reader personas. Include evidence citations (chapter/lines). Track running context (what’s been read before). 
6. **Execution plan**: start with a small panel first (e.g. Quick panel R01,R05,M01,M02,A01,L01,I02,H01) on Book 2 to validate format, then scale. 
7. **Synthesis**: generate `_synthesis.md` after panel with consensus/polarizing/singletons.

## Implementation details
- Create script at repo root or under tools, e.g. `.kilo/scripts/run_persona_reviews.py` (or `tools/run_persona_reviews.py`). Need to write files - script is fine.
- Chapter splitting: extract ranges by line numbers. For each chunk, include header context (title, chapter name). 
- Output structure: `books/book-NN/reviews/` must exist. Maybe `books/book-NN/reviews/chunks/` or just write chapter notes then merge.
- For each persona, track state across chapters (summary, ratings, evidence). 
- Respect the exact report template from README.

## Validation
- Spot-check a single persona’s chapter output matches template. 
- Verify files written to correct paths. 
- Ensure no bible content passed to non-allowed personas. 

## Open questions (minimal)
1. Which book(s) to run first? README says "Books 2–5 now" - start with Book 2 as smallest. 
2. Which panel? Quick panel (8) is manageable to start; confirm size. 
3. Aggregation: produce both per-chapter notes and final consolidated `<persona-id>.md`? README requires final saved as `<persona-id>.md` - so consolidation is required. 
4. Do we need to run for all 123? User says "run the personas.md through the entire manuscript..." - probably full set, but chunked. Maybe start with Quick panel, then expand as validated.

## Recommended next steps
- Create script to parse chapters and personas.
- Run Quick panel on Book 2, chapter by chapter, produce outputs.
- Verify format against README template.
- Expand to other books/panels if correct.

## Task list (implementation-ready)
1. Parse personas.md into structured data (group, id, name, body with loves/hates/checks/rates). 
2. Parse chapter boundaries for books 2-5. 
3. Create reviews dirs. 
4. Implement chunked reviewer script that takes (book, chapter_range, persona, prior_summary) and outputs chapter review + updated summary.
5. Run Quick panel on Book 2 end-to-end. 
6. Generate synthesis. 
7. Report results and saved files. 

Saved plan: /Users/dustinober/Projects/Books/The-Blackwood-Ridge-Mysteries/.kilo/plans/1791756144134-persona-chapter-review-plan.md
