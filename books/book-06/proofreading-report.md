# Book 6 Controlled Proofreading Report

## Scope and verdict

Book 6 — *The Pattern* completed a controlled proofreading pass from the verified final-prose-polish baseline. The pass corrected four objective mechanical errors across Chapters 2, 7, and 8. Chapters 1, 3, 4, 5, and 6 were intentionally retained without manuscript change.

No developmental revision, structural revision, clue redesign, prose polishing, line editing, scene work, export assembly, package work, cover work, listing work, upload work, or publication work occurred.

**Verdict:** controlled proofreading complete.

**Starting manuscript-prose total:** 25,645 words.  
**Final manuscript-prose total:** 25,646 words.  
**Net change:** +1 word.  
**Exact chapter-final lines:** all eight unchanged.

## Repository and dependency verification

- **Repository:** `dustinober1/The-Blackwood-Ridge-Mysteries`
- **Default branch:** `main`
- **Required dependency:** PR #30 — `Polish Book 6 prose`
- **PR #30 target:** `main`
- **PR #30 source:** `agent/book-06-final-prose-polish`
- **PR #30 source head:** `87109304cb0e0f434d203247467e8b37491f1b2c`
- **PR #30 pre-merge base:** `9a09c16e7ce523615aec297cd6ce8f7d92273022`
- **PR #30 merge commit:** `105634b1dbf41a9c15ab6d2ea3df7d9945c8b264`
- **Starting post-PR-#30 `main` HEAD:** `105634b1dbf41a9c15ab6d2ea3df7d9945c8b264`
- **Proofreading branch:** `agent/book-06-controlled-proofreading`
- **Proofreading branch base:** `105634b1dbf41a9c15ab6d2ea3df7d9945c8b264`

PR #30 was confirmed merged before proofreading began. It contained exactly these six changed files:

- `books/book-06/README.md`
- `books/book-06/final-prose-polish-report.md`
- `books/book-06/manuscript/README.md`
- `books/book-06/outline.md`
- `books/book-06/progress.yaml`
- `series-outline.md`

A direct comparison of PR #30's merge commit to `main` returned no intervening commits. Searches found no later Book 6 proofreading, export, package, cover, listing, upload, or publication branch or pull request and no pre-existing `agent/book-06-controlled-proofreading` branch.

## Complete source-file list

### Manuscript read continuously and in full

- `books/book-06/manuscript/ch-01.md`
- `books/book-06/manuscript/ch-02.md`
- `books/book-06/manuscript/ch-03.md`
- `books/book-06/manuscript/ch-04.md`
- `books/book-06/manuscript/ch-05.md`
- `books/book-06/manuscript/ch-06.md`
- `books/book-06/manuscript/ch-07.md`
- `books/book-06/manuscript/ch-08.md`

### Book 6 controlling production records

- `books/book-06/final-prose-polish-report.md`
- `books/book-06/line-edit-report.md`
- `books/book-06/revision-plan.md`
- `books/book-06/README.md`
- `books/book-06/content-notes.md`
- `books/book-06/outline.md`
- `books/book-06/progress.yaml`
- `books/book-06/manuscript/README.md`

### Chapter mission locks

- `books/book-06/control/chapter-01-mission-lock.md`
- `books/book-06/control/chapter-02-mission-lock.md`
- `books/book-06/control/chapter-03-mission-lock.md`
- `books/book-06/control/chapter-04-mission-lock.md`
- `books/book-06/control/chapter-05-mission-lock.md`
- `books/book-06/control/chapter-06-mission-lock.md`
- `books/book-06/control/chapter-07-mission-lock.md`
- `books/book-06/control/chapter-08-mission-lock.md`

### Present Book 6 bible files

- `books/book-06/bible/mystery-solution.md`
- `books/book-06/bible/suspect-matrix.md`
- `books/book-06/bible/clue-ladder.md`
- `books/book-06/bible/story-memory.md`
- `books/book-06/bible/timeline.md`
- `books/book-06/bible/continuity-locks.md`
- `books/book-06/bible/character-arcs.md`
- `books/book-06/bible/carry-forward.md`
- `books/book-06/bible/book-05-to-06-handoff.md`

### Series and recurring-character controls

- `series-bible/voice-dna.md`
- `series-bible/story-memory.md`
- `series-bible/recurring-characters/callie-thorne.md`
- `series-bible/recurring-characters/dalton-cross.md`
- `series-bible/recurring-characters/mae-hartwell.md`
- `series-bible/recurring-characters/eli-townsend.md`
- `series-outline.md`

### Targeted Book 5 continuity and lifecycle sources

- `books/book-05/progress.yaml`
- `books/book-05/bible/story-memory.md`
- `books/book-06/bible/book-05-to-06-handoff.md`

## Source-list discrepancy result

The two paths documented as absent during final prose polish remain absent:

- `books/book-06/bible/premise.md`
- `books/book-06/bible/eli-hidden-chronology.md`

Neither file was recreated. All nine Book 6 bible files actually present on the verified baseline were read. The absent paths do not create a proofreading blocker because the controlling premise, solution, timeline, continuity, long-arc, and Book 5 handoff information is present in the existing files.

## Starting manuscript baseline

| Chapter | Title | Starting blob | Starting words |
|---:|---|---|---:|
| 1 | The Box at Closing | `c9a12f2305b08b1cf81ea88c1ef49e94e7a453c6` | 3,266 |
| 2 | A Fall That Did Not Fit | `31a438514b5d528bac16b99df5e43c713079737f` | 3,135 |
| 3 | The Surveyor's Missing Line | `59575d837b6c51d22d57ff4033e6a09bc218a409` | 3,130 |
| 4 | Marks Made Later | `401d46dad388ddb6ca7df6041c464465a19a48c5` | 3,150 |
| 5 | The Road Through Bellweather | `81fad0335b3781712b38d4d3139d92ffe94b3476` | 3,100 |
| 6 | What the Ledger Withheld | `6b43203b07287771b99ef87240955ec31206e996` | 3,279 |
| 7 | The Weight of the Map | `a38ab3a572b013fcdec34e3bd77aa8e8ed4331c5` | 3,105 |
| 8 | The Pattern | `349a95c237c97039de30fae07c46753a5c7eef15` | 3,480 |
|  | **Total** |  | **25,645** |

Every title, front-matter count, blob, and locked final line matched the required final-polish baseline before proofreading began.

## Proofreading ledger summary

### Corrected

Four objective mechanical errors were corrected:

1. one incorrect honorific/title;
2. one malformed negative construction;
3. one missing article;
4. one inconsistent straight apostrophe in otherwise curly-apostrophe prose.

### Valid house style

Retained without change:

- spelled-out narrative times such as `seven thirty-nine` and `twelve oh six`;
- repository-standard plain ASCII apostrophes inside YAML front matter where already established;
- em-dash use, ellipses, code-formatted record text, and uppercase documentary labels;
- repeated procedural phrases when each carries a distinct evidentiary or authority limit.

### Intentional fragments

Short fragments such as `Not interpreted. Described.`, `No.`, and other clipped documentary or emotional beats were retained because they are grammatically intentional, voice-consistent, and structurally functional.

### Intentional dialogue grammar

Character-specific dialogue remained untouched unless objectively malformed. Cross's clipped phrasing, Mae's warm cadence, Eli's increasingly steady speech, and Dana's controlled non-confessional speech remain intact.

### Exact canon wording

The following were treated as locked, not normalized or rewritten:

- all eight chapter-final lines;
- the exact Halbrook corrected status;
- `older documented grime`;
- `Found in returned Mercer volume by M. Hartwell; prior loose-paper location not established.`
- the unresolved-provenance conclusion;
- item identifiers and record labels.

### Deferred to export formatting

No manuscript defect was deferred. Page layout, ebook typography, front/back matter assembly, section-break rendering, navigation, and retailer-format concerns remain properly deferred to controlled export assembly.

### Rejected as line editing or prose polishing

- `A brighter handled area beside an unchanged body.` was retained. `Handled area` is a valid noun phrase meaning the area normally touched or used; changing it would be preference editing.
- Repeated negative formulations were retained when they mark separate evidentiary limits rather than accidental repetition.
- Procedural recaps were not shortened where they preserve location, seal, transport, intake, scientific limitation, authority, or chronology.
- Sentence fragments and short paragraph beats were not expanded for smoothness.
- No metaphor, rhythm, imagery, emotional explanation, dialogue voice, paragraph order, or scene texture was altered.

## Chapter-by-chapter proofreading result

### Chapter 1 — The Box at Closing

- **Disposition:** proofread; intentionally unchanged.
- **Result:** spelling, grammar, punctuation, dialogue punctuation, agreement, tense, names, identifiers, Markdown, front matter, and final line verified.
- **Words:** 3,266 → 3,266.
- **Blob:** unchanged.

### Chapter 2 — A Fall That Did Not Fit

- **Correction:** `Sheriff Bell called at seven twenty-six.` → `Deputy Bell called at seven twenty-six.`
- **Objective basis:** Dalton Cross is the sheriff; Bell is the deputy. The original honorific contradicted the recurring-character controls, mission locks, and the chapter's own established roles.
- **Canon effect:** none. Authority remains with Cross; Bell's evidence and photography role remains unchanged.
- **Words:** 3,135 → 3,135.
- **Final blob:** `6404737d8d0610908608f7d8ab45c02cd75158fd`.

### Chapter 3 — The Surveyor's Missing Line

- **Disposition:** proofread; intentionally unchanged.
- **Result:** cold-case setup, field-book gap, Miriam triangle separation, lawful access, names, dates, and final line verified.
- **Words:** 3,130 → 3,130.
- **Blob:** unchanged.

### Chapter 4 — Marks Made Later

- **Disposition:** proofread; intentionally unchanged.
- **Result:** quotation pairing, apostrophes, modern-mark chronology, `older documented grime`, no-sampling limits, and final line verified.
- **Words:** 3,150 → 3,150.
- **Blob:** unchanged.

### Chapter 5 — The Road Through Bellweather

- **Disposition:** proofread; intentionally unchanged.
- **Result:** monetary values, October chronology, key/time sequence, names, identifiers, dialogue punctuation, and final line verified.
- **Words:** 3,100 → 3,100.
- **Blob:** unchanged.

### Chapter 6 — What the Ledger Withheld

- **Disposition:** proofread; intentionally unchanged.
- **Result:** audio identifier, travel calculations, alibi wording, third routing mark, Mercer seam, warrant threshold, Markdown, and final line verified.
- **Words:** 3,279 → 3,279.
- **Blob:** unchanged.

### Chapter 7 — The Weight of the Map

- **Correction:** `Bell recorded every transport seal before opening none of them.` → `Bell recorded every transport seal without opening any of them.`
- **Objective basis:** the original negative construction was malformed and reversed the intended relationship between recording seals and preserving unopened packages.
- **Canon effect:** none. The correction clarifies the already locked custody sequence and does not change an act, time, item, custodian, or inference.
- **Words:** 3,105 → 3,105.
- **Final blob:** `9ffbb201458d822bafcdf24ffe3b28df283b635a`.

### Chapter 8 — The Pattern

- **Correction 1:** `treated as inconvenience` → `treated as an inconvenience`.
- **Objective basis:** missing indefinite article before a singular count noun.
- **Correction 2:** `Alton's case` → `Alton’s case`.
- **Objective basis:** one straight apostrophe appeared inside prose otherwise consistently using curly apostrophes; YAML/front-matter ASCII conventions were not changed.
- **Canon effect:** none. The Mercer case reference, exact provenance wording, Halbrook correction, three-mark synthesis, and ending remain unchanged.
- **Words:** 3,480 → 3,481.
- **Final blob:** `be9f1a5531c3a6d61430483b76ed01472d0a03e4`.

## Whole-draft mechanical review

### Spelling

No misspelled word remained. Proper nouns, place names, institutions, surnames, and document terms were checked against controlling records.

### Grammar and agreement

One malformed negative construction and one missing article were corrected. No remaining subject-verb, pronoun, number, or tense agreement error required change.

### Punctuation and dialogue punctuation

One prose apostrophe was normalized. Quotation marks, dialogue commas, terminal punctuation, em dashes, parentheses, brackets, emphasis markers, and backticks were paired and functional. No dialogue-punctuation correction beyond the apostrophe normalization was required.

### Capitalization and honorifics

One honorific was corrected from `Sheriff Bell` to `Deputy Bell`. Proper names, titles, institutions, rooms, locations, and official terms remain consistent.

### Hyphenation and compounds

No objectively inconsistent hyphenation or compound-word error required change. Functional forms including `right-of-way`, `single-vehicle`, `medical-examiner`, `river-access`, `map-weight`, and `repair-ticket` remain contextually consistent.

### Dates, times, numbers, money, and identifiers

Verified without substantive change:

- October 3 / October 6 / October 8 / October 9–12 chronology;
- Gate Three 1:24 departure, 1:52 arrival, 1:55 staging intake, 3:56 release, and 4:24 return;
- death and interview times;
- `$4,860.00`, `$600,000`, and other locked values;
- `WH-07-01`, `VW-07-01`, `VW-07-02`, `T-2`, `MV_0415_06`, and related labels.

### Markdown and front matter

All eight chapter front-matter blocks retain valid delimiters, chapter number, title, POV, date, target, status, and count fields. Heading hierarchy, section breaks, italics, inline code, block quotations, and backticks remain parseable. Chapter 8's front-matter count changed from 3,480 to 3,481 because of the restored article.

### Whitespace and artifacts

No accidental tab, trailing-space dependency, merge marker, placeholder, duplicated line, duplicated paragraph, or malformed blank-line sequence was introduced. No changed file contains export residue or package markup.

### Duplicate or missing-word result

No accidental duplicate sentence, paragraph, adjacent word, or repeated line required correction. The only missing word was Chapter 8's article `an`. Intentional repeated legal, scientific, custody, and provenance formulations remain.

## POV, voice, and story preservation

- Single third-person limited through Callie remains intact.
- No private interiority was added for Dana, Cross, Mae, Eli, Tara, Nadia, Leo, Owen, Bell, custodians, examiners, or historical actors.
- Callie's precise, restrained documentary voice remains intact.
- Cross remains clipped and authority-bearing.
- Mae remains grounding rather than solving.
- Eli remains visibly careful and useful without suspicious knowledge.
- Dana remains non-confessional and non-caricatured.

## Mystery, evidence, authority, custody, and long-arc verification

- Dana Wren remains Miriam Vale's murderer.
- Map weight six remains the cumulative weapon.
- Probable cause remains complete before arrest.
- Dana does not confess.
- Questioning stops immediately after counsel invocation.
- Silence, refusal, anger, grief, invocation, and demeanor supply no evidence.
- Murder proof remains independent of curator identity.
- Halbrook's October 8 death remains accidental.
- Later concealment remains a separate historical wrong.
- The official correction remains exact and evidence-limited.
- Historical actors remain attributed only at supported role and act levels.
- Tara's choir alibi remains independently authenticated.
- Tara's custody, restriction, recount, privacy, and trustee consequences remain separate.
- Callie remains outside the ravine.
- Beyond-perimeter information reaches Callie only through authorized channels.
- The three modern routing marks remain separate from Miriam's triangle.
- No graphite sampling occurred.
- No binder, polymer, particle, composition, grade, brand, owner, buyer, writer, pencil, or instrument identification was added.
- `older documented grime` remains exact.
- The Mercer provenance wording remains exact.
- Deliberate steering remains supported without identity.
- Actor, writer, mover, instrument, common physical hand, drawing occasion, and curator remain unresolved.
- Eli remains unidentified, non-suspicious, non-POV, and outside original evidence, warrants, searches, laboratories, recovery, remains, and suspect access.
- Book 7 retains controlled testing and Eli exposure.
- No prior solved murder is invalidated.
- Callie remains a bounded consultant.
- Cross retains legal and procedural authority.
- Bell and lawful custodians retain custody authority.

## Final manuscript result

| Chapter | Final blob | Before | After | Delta | Disposition |
|---:|---|---:|---:|---:|---|
| 1 | `c9a12f2305b08b1cf81ea88c1ef49e94e7a453c6` | 3,266 | 3,266 | 0 | unchanged |
| 2 | `6404737d8d0610908608f7d8ab45c02cd75158fd` | 3,135 | 3,135 | 0 | honorific corrected |
| 3 | `59575d837b6c51d22d57ff4033e6a09bc218a409` | 3,130 | 3,130 | 0 | unchanged |
| 4 | `401d46dad388ddb6ca7df6041c464465a19a48c5` | 3,150 | 3,150 | 0 | unchanged |
| 5 | `81fad0335b3781712b38d4d3139d92ffe94b3476` | 3,100 | 3,100 | 0 | unchanged |
| 6 | `6b43203b07287771b99ef87240955ec31206e996` | 3,279 | 3,279 | 0 | unchanged |
| 7 | `9ffbb201458d822bafcdf24ffe3b28df283b635a` | 3,105 | 3,105 | 0 | malformed negative corrected |
| 8 | `be9f1a5531c3a6d61430483b76ed01472d0a03e4` | 3,480 | 3,481 | +1 | article restored; apostrophe normalized |
|  | **Total** | **25,645** | **25,646** | **+1** |  |

## Exact chapter-final-line verification

1. `The ladder had not rolled.`
2. `One had been cleaned.`
3. `Sheet 47 had described a public right-of-way through Bellweather river land.`
4. `` `South line retrieval.` ``
5. `The road through Bellweather did not contain the missing thirty-nine minutes.`
6. `It was enough to ask where Dana had put the rest.`
7. `The route field remained blank.`
8. `Who knew which page she would open next?`

All eight remain byte-for-byte unchanged. Chapters 1, 3, 4, 5, and 6 retain their starting blobs. The changed Chapters 2, 7, and 8 were fetched again from the proofreading branch and their final lines reverified directly.

## Files created

- `books/book-06/proofreading-report.md`

## Files modified

- `books/book-06/README.md`
- `books/book-06/manuscript/README.md`
- `books/book-06/manuscript/ch-02.md`
- `books/book-06/manuscript/ch-07.md`
- `books/book-06/manuscript/ch-08.md`
- `books/book-06/outline.md`
- `books/book-06/progress.yaml`
- `series-outline.md`

## Controls inspected and intentionally unchanged

- `books/book-06/final-prose-polish-report.md`
- `books/book-06/line-edit-report.md`
- `books/book-06/revision-plan.md`
- `books/book-06/content-notes.md`
- all eight chapter mission locks;
- all nine present Book 6 bible files;
- series voice, story-memory, and recurring-character controls;
- targeted Book 5 lifecycle and Mercer continuity records.

No mystery-control rewrite was needed because the four manuscript corrections are mechanical and canon-neutral.

## Validation commands and results

### Connector verification

- Repository metadata query: exact repository and default branch — **PASS**.
- PR #30 metadata query: merged state, base, source branch, source SHA, and merge commit — **PASS**.
- PR #30 changed-file listing: exact six-file dependency scope — **PASS**.
- Compare PR #30 merge commit to `main`: identical, no intervening commit — **PASS**.
- Search Book 6 branches and PRs before branch creation: no duplicate proofreading or later production pass — **PASS**.

### Manuscript and control verification

- Read all eight chapters continuously and perform three proofreading passes per chapter — **PASS**.
- Fetch starting and final chapter headers/blobs/counts — **PASS**.
- Re-fetch corrected Chapter 2, 7, and 8 endings — **PASS**.
- Verify unchanged-chapter blob equality — **PASS**.
- Parse the updated `progress.yaml` with `yaml.safe_load` — **PASS**.
- Sum all eight parsed chapter counts and compare to `actual_words` — **25,646 = 25,646; PASS**.
- Verify chapter sequence 1–8 and unchanged titles — **PASS**.
- Verify exact final lines — **PASS**.
- Verify Book 6 lifecycle flags: proofreading complete; export/package/cover/listing/upload/publication pending; upload ready false — **PASS**.

### Whole-draft focused checks

- spelling and word-form review — **PASS**;
- grammar, agreement, article, and tense review — **PASS after two grammar corrections**;
- punctuation, quotation, apostrophe, dialogue, and pairing review — **PASS after one apostrophe normalization**;
- capitalization, honorific, proper-name, place-name, and title review — **PASS after one honorific correction**;
- date, time, number, money, item-identifier, and chronology review — **PASS**;
- Markdown, front matter, headings, code spans, italics, and section-break review — **PASS**;
- duplicate sentence, paragraph, adjacent-word, and missing-word review — **PASS after restoring one missing article**;
- whitespace, merge marker, placeholder, and accidental-artifact review — **PASS**;
- complete changed-file scope review — **PASS**.

No repository-specific Book 6 validator script exists. The preceding final-prose-polish audit documents that focused connector, blob, count, YAML-structure, lifecycle, source-control, and complete-diff checks are the applicable repository validation method.

## Neighboring-book verification

### Book 5

No Book 5 file changed. Book 5 remains:

- manuscript proofreading complete;
- export complete;
- package `in_progress`;
- publication `pending`;
- canonical ebook cover missing or unapproved;
- `cover_ready: false`;
- package completion blocked by the approved-cover requirement;
- not upload ready.

### Book 7

No `books/book-07/manuscript` directory or Book 7 prose exists. Book 7 remains planned only. Controlled testing and Eli exposure remain reserved for Book 7.

## Final Book 6 lifecycle state

- controlled whole-draft revision — complete;
- controlled line edit — complete;
- controlled final prose polish — complete;
- controlled proofreading — complete;
- proofread chapters — 8 of 8;
- proofread manuscript-prose words — 25,646;
- exact chapter-final lines — unchanged;
- export — pending;
- package — pending;
- cover — pending;
- listing — pending;
- upload — pending;
- publication — pending;
- upload ready — no.

## Unresolved blockers

No proofreading blocker remains. The only immediate production dependency is completion and validation of controlled export assembly. Package, cover, listing, upload, and publication must remain deferred.

## Recommended next production stage

Run **Book 6 controlled export assembly** from the merged proofreading result. Do not proceed directly to package, cover, listing, upload, distribution, or publication.
