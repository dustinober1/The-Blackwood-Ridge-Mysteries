---
doc: book-06-revision-plan
status: controlled_revision_complete
book: 6
accepted_plan_blob: 5d29ed877110a99e82bf370f8dc88ccbfcbd25e7
accepted_first_draft_words: 25181
revised_words: 25645
net_word_delta: 464
reader_facing: false
---

# Book 6 Controlled Whole-Draft Revision Plan and Implementation Record

## Accepted dependency and baseline

- **Acceptance PR:** #27 — `Accept Book 6 first draft and plan revision`
- **Acceptance branch head:** `145451ad9e3487c1e46be01fc33889ab54228499`
- **Post-merge main / revision base:** `59498c40cbe21c0cab48c85c3668bbf9d181f3b2`
- **Formal verdict:** `ACCEPTED WITH REQUIRED PRE-REVISION CONTROL REPAIRS`
- **Accepted plan blob:** `5d29ed877110a99e82bf370f8dc88ccbfcbd25e7`
- **Accepted structure:** eight chapters
- **Accepted total:** 25,181 whitespace-delimited manuscript-prose words
- **Revision branch:** `agent/book-06-whole-draft-revision`

The accepted first draft and this plan controlled the revision. No plot, murderer, weapon, motive, arrest basis, cold-case outcome, curator endpoint, chapter structure, or exact final line was changed.

## Accepted chapter baseline and revised result

| Ch | Title | Accepted blob | Accepted | Revised | Delta | Revision IDs | Final line |
|---:|---|---|---:|---:|---:|---|---|
| 1 | The Box at Closing | `c9a12f2305b08b1cf81ea88c1ef49e94e7a453c6` | 3,266 | 3,266 | 0 | reviewed; no change | unchanged |
| 2 | A Fall That Did Not Fit | `31a438514b5d528bac16b99df5e43c713079737f` | 3,135 | 3,135 | 0 | reviewed; no change | unchanged |
| 3 | The Surveyor's Missing Line | `59575d837b6c51d22d57ff4033e6a09bc218a409` | 3,130 | 3,130 | 0 | reviewed; no change | unchanged |
| 4 | Marks Made Later | `401d46dad388ddb6ca7df6041c464465a19a48c5` | 3,150 | 3,150 | 0 | reviewed; no change | unchanged |
| 5 | The Road Through Bellweather | `81fad0335b3781712b38d4d3139d92ffe94b3476` | 3,100 | 3,100 | 0 | reviewed; no change | unchanged |
| 6 | What the Ledger Withheld | `8bdc850338411167733de54ba63f7d1de8c097b0` | 3,150 | 3,279 | +129 | R-01, R-04, O-03 | unchanged |
| 7 | The Weight of the Map | `8d2a40e7ae6157c1e3d6271019399b3930a87cb1` | 3,100 | 3,105 | +5 | R-06 | unchanged |
| 8 | The Pattern | `c5d64e5b493152cd31a304d1eb1ad7b3c4d01064` | 3,150 | 3,480 | +330 | R-01, R-02, R-03, R-05, R-07, O-01, O-02, O-10 | unchanged |
|  | **Total** |  | **25,181** | **25,645** | **+464** |  |  |

## Non-negotiable locks preserved

- Dana Wren remains Miriam Vale's murderer.
- Map weight six remains the cumulative weapon.
- Dana does not confess; questioning stops immediately upon counsel invocation.
- Silence, invocation, anger, grief, refusal, and demeanor are not evidence.
- Murder proof remains independent of curator identity.
- Halbrook's October 8 death remains accidental; later concealment remains a separate historical wrong.
- The exact official correction remains unchanged.
- The three modern routing marks remain separate from Miriam's triangle and Dana's murder proof.
- The exact Mercer provenance remains `Found in returned Mercer volume by M. Hartwell; prior loose-paper location not established.`
- Deliberate steering is supported without actor, writer, mover, instrument, common hand, drawing occasion, or curator identity.
- Eli remains unidentified, receives no POV/private confirmation/suspicious knowledge, and has no original-evidence, warrant, search, recovery, or remains access.
- Callie remains a bounded consultant; Cross retains legal authority; Bell and lawful custodians retain custody authority; Mae grounds rather than solves.
- No Book 5 file changed. No Book 7 prose was created.
- No export, package, cover, listing, upload, or publication asset was changed.

# Implementation appendix

## Required revisions

### R-01 — Graphite, binder, composition, and grime controls

**Disposition:** implemented.

**Files changed:**

- `books/book-06/manuscript/ch-06.md`
- `books/book-06/manuscript/ch-08.md`
- `books/book-06/outline.md`
- `books/book-06/bible/mystery-solution.md`
- `books/book-06/bible/suspect-matrix.md`
- `books/book-06/bible/clue-ladder.md`
- `books/book-06/bible/story-memory.md`
- `books/book-06/bible/timeline.md`
- `books/book-06/bible/continuity-locks.md`
- `books/book-06/control/chapter-06-mission-lock.md`
- `books/book-06/control/chapter-08-mission-lock.md`

**Outcome:**

- No graphite sampling is claimed.
- No binder, polymer, particle, or composition result is claimed.
- Miriam's triangle is separated by custody, pressure, placement, construction, and function—not composition.
- Leo is not included or excluded through binder/composition evidence.
- No pencil, grade, brand, owner, buyer, writer, or instrument is identified.
- Non-destructive analysis remains only a hypothetical broad-class capability.
- `later grime` was replaced by `older documented grime` wherever relevant.
- Authenticated image state, repair tissue, and visible surface chronology remain the dating proof.

**Word-count effect:** included in Chapters 6 and 8 deltas.

### R-02 — Correct the historical date sequence

**Disposition:** implemented.

**Primary passage:** Chapter 8 historical synthesis and official-record packet.

**Outcome:** The manuscript and controls state the exact sequence:

1. October 3, 1989 — Halbrook complaint.
2. October 6 — county payment to Wren Grading Company under `south line retrieval`.
3. October 8 — accidental single-vehicle road departure.
4. October 9–12 — post-crash concealment, field-material removal, spoil placement, maintenance, and false-report activity.

The October 6 payment supports the broader suppression path but is not described as payment during the later interval or direct proof of a post-crash service by date alone. The crash is not implied to have been planned.

**Files changed:** Chapter 8; outline; mystery solution; clue ladder; story memory; timeline; continuity locks; Chapter 8 mission lock; lifecycle/status records.

**Word-count effect:** included in Chapter 8's +330.

### R-03 — Narrow historical actor and act attribution

**Disposition:** implemented.

**Outcome:**

- Dana's father is named only through authenticated Wren Grading proprietorship, receipt signature, company, and payment records.
- The company/payment supports the suppression path without placing him personally at the post-crash scene by date alone.
- Maintenance entries, grader identity, two officials' roles/signatures, removed material, spoil, and the false supplement support collective concealment.
- Discovery, grader operation, material removal, spoil movement, drafting, and every specific individual act remain unresolved unless supported.
- No confession, conspiracy agreement, charge, prosecution, adjudication, or complete legal disposition was invented.
- Dana remains responsible for Miriam's murder, not Halbrook's crash.

**Files changed:** Chapter 8; outline; mystery solution; suspect matrix; clue ladder; story memory; timeline; continuity locks; Chapter 8 mission lock.

**Word-count effect:** included in Chapter 8's +330.

### R-04 — Close Tara Bellweather's opportunity loop

**Disposition:** implemented in Chapter 6, the least intrusive approved location.

**Outcome:** St. Orison's choir director authenticates Thursday's rehearsal register; two singers interviewed separately place Tara continuously in the nave from 6:05 through 6:47. She cannot reach the Grange during Miriam's 6:15–6:35 death window. The alibi is reader-visible before warrant synthesis.

Tara's two-folder removal, false inventory statement, privacy breach, two-person recount, lawful restriction process, and trustee consequences remain intact. No magical surveillance, phone tracking, demeanor, wealth, family status, or letter content supplies the alibi.

**Files changed:** Chapter 6; outline; suspect matrix; clue ladder; story memory; timeline; continuity locks; Chapter 6 mission lock.

**Word-count effect:** principal part of Chapter 6's +129.

### R-05 — Gate Three travel control

**Disposition:** implemented after resolving the control before Chapter 8 revision.

**Authoritative table:**

| Event | Time |
|---|---:|
| Sheriff office departure | 1:24 p.m. |
| Physical Gate Three arrival | 1:52 p.m. |
| Reed safety/staging intake logged | 1:55 p.m. |
| Callie released | 3:56 p.m. |
| Sheriff records-room return/opening | 4:24 p.m. |

Physical arrival and staging intake are distinct. Both outbound and return drives use the locked twenty-eight-minute dry-condition travel time. No emergency speeding or safety compression occurs. Callie remains outside the ravine.

**Timestamp adjustment disclosed:** records-room opening moved from 4:22 to 4:24. The 1:55 staging-log entry remains, now correctly separated from 1:52 physical arrival.

**Files changed:** Chapter 8; outline; story memory; timeline; continuity locks; Chapter 8 mission lock.

**Word-count effect:** included in Chapter 8's +330.

### R-06 — Repair the Chapter 7 POV sentence

**Disposition:** implemented.

**Original:** `Dana's mistake had been believing ordinary meant without consequence.`

**Revised:** `To Callie, the concealment carried its own warning: ordinary did not mean without consequence.`

The thematic turn remains within Callie's explicit perception. No Dana interiority, confession, remorse, villain narration, or demeanor evidence was added.

**Files changed:** Chapter 7; outline; story memory; continuity locks.

**Word-count effect:** +5.

### R-07 — Ground Chapter 8 recovery knowledge

**Disposition:** implemented.

**Outcome:** Every beyond-perimeter fact reaches Callie through Cross's direct update, a numbered tablet image, Bell's radio/logged summary, the medical examiner's transport record, or the later authorized packet. Callie never enters the ravine, handles recovery evidence, identifies remains, or determines cause/manner.

The unsupported categorical sentences about a glove-compartment note and pocket accusation were removed. The revised passage states only that the medical examiner's transport inventory lists no recovered note among transferred driver-area effects, while vehicle-compartment examination remains pending. The emotional absence of a convenient final accusation is therefore source-bound.

**Files changed:** Chapter 8; outline; clue ladder; story memory; timeline; continuity locks; Chapter 8 mission lock.

**Word-count effect:** included in Chapter 8's +330.

## Optional revisions

### O-01 — Emotional air for Halbrook identification/correction

**Disposition:** implemented.

Chapter 8 pauses after the lawful correction to distinguish restored evidence from institutional absolution. The old false entry remains visible. The added emotional space does not change facts, authority, or the exact correction.

### O-02 — Provisional same-day odontological comparison

**Disposition:** implemented.

A pre-notified forensic odontologist issues a provisional written comparison consistent with Halbrook's preserved dental records. The formal specialist report remains pending. Identification remains cumulative and no preliminary finding is sole proof.

### O-03 — Ease Chapter 6 density before third-mark scene

**Disposition:** implemented.

A short sensory reset—wall-clock tick, rain at wired glass, and Callie's cramped pencil hand—was added after the Owen interview. It adds no evidence or scene function.

### O-04 — Compress a repeated Chapter 7 custody recap

**Disposition:** skipped.

The apparently repeated material carries distinct location, package, seal, transfer, and intake facts. Compression risked weakening custody clarity.

### O-05 — Vary selected Cross evidence-limit catechisms

**Disposition:** skipped.

The repeated question/limit form is functional procedural characterization and preserves portable evidence boundaries. Broad variation would be preference editing outside this pass.

### O-06 — Thin redundant negation clusters

**Disposition:** skipped.

The reviewed clusters distinguish separate prohibited inferences in legal, scientific, and provenance contexts. No clearly redundant cluster justified change without beginning a broad line edit.

### O-07 — Reduce duplicate Eli blank-field inventories

**Disposition:** skipped.

The inventories occur at different evidentiary stages and are deliberate long-arc behavior. Each reinforces an authorized boundary without suspicious knowledge.

### O-08 — Vary one Mae labeled-food/table beat

**Disposition:** skipped.

The labels serve recurring evidence-boundary and relationship functions. No single beat was expendable enough to justify change in a controlled revision.

### O-09 — Add an ordinary-life detail for Dana

**Disposition:** skipped.

Chapter 5 already supplies Dana's hardware-store, committee, financing, employment, and inherited-record context. Adding another detail was unnecessary and risked shifting characterization weight.

### O-10 — Vary one repeated distinction/separation turn

**Disposition:** implemented.

Chapter 8 uses `Keeping the accident and the later concealment in separate rows kept both facts honest.` The change reinforces the accident/concealment boundary without altering evidence.

### O-11 — Vary a pre-final-line abstraction

**Disposition:** skipped.

The controlled ending already moves through concrete shop action, route-ledger fields, and the exact final question. No abstraction required repair.

### O-12 — Restore one sensory/bodily beat to Chapter 5 or 6 transition

**Disposition:** skipped as a separate change.

O-03 supplies the approved Chapter 6 sensory/bodily reset. A second similar change would duplicate purpose and expand the pass unnecessarily.

## Passage-level manuscript changes

### Chapter 6

- Replaced the stale Leo graphite/binder implication with explicit no-sampling/no-result language.
- Added one brief sensory transition after Owen's interview.
- Added Tara's authenticated choir record and two independent witnesses before warrant synthesis.
- Added Tara to the alternatives reduction.
- Updated the synthesis count from six to seven narrower paths.
- Preserved the exact final line.

### Chapter 7

- Recast the single Dana-interiority sentence as Callie's explicit inference.
- Preserved all evidence, arrest, counsel, custody, murderer/curator, Mae, Eli, and ending content.
- Preserved the exact final line.

### Chapter 8

- Distinguished 1:52 physical arrival from 1:55 staging intake and moved records-room opening to 4:24.
- Routed all recovery facts through authorized channels.
- Reframed the absence of a final note through the medical examiner's transport inventory and pending compartment examination.
- Made the October 3 / October 6 / October 8 / October 9–12 sequence explicit.
- Narrowed Dana's father's and the two officials' supported roles and left specific acts unresolved.
- Added the provisional dental comparison with formal report pending.
- Added proportionate emotional space after the official correction.
- Corrected `older documented grime` and removed all sampling/binder/polymer/composition claims.
- Preserved the exact official correction, Mercer provenance, unresolved-provenance entry, Eli boundaries, and final line.

## Control and lifecycle files synchronized

- `books/book-06/outline.md`
- `books/book-06/bible/mystery-solution.md`
- `books/book-06/bible/suspect-matrix.md`
- `books/book-06/bible/clue-ladder.md`
- `books/book-06/bible/story-memory.md`
- `books/book-06/bible/timeline.md`
- `books/book-06/bible/continuity-locks.md`
- `books/book-06/control/chapter-06-mission-lock.md`
- `books/book-06/control/chapter-08-mission-lock.md`
- `books/book-06/progress.yaml`
- `books/book-06/README.md`
- `books/book-06/manuscript/README.md`
- `series-outline.md`
- `books/book-06/revision-plan.md`

`books/book-06/bible/character-arcs.md`, the Book 5-to-6 handoff, carry-forward file, and Chapters 1–5 mission locks were reviewed and required no change.

## Final production state

- Controlled whole-draft revision: complete.
- All eight chapters reviewed: complete.
- Required control repairs: complete.
- R-01 through R-07: complete.
- Optional changes: O-01, O-02, O-03, O-10 implemented; all others skipped as documented.
- Line editing: pending.
- Final prose polish: pending.
- Proofreading: pending.
- Export: pending.
- Package: pending.
- Cover/listing/upload/publication: pending.
- Book 6 upload ready: no.
- Book 5: unchanged, package in progress, publication pending, cover-blocked, not upload ready.

The recommended next production stage is **Book 6 line editing or controlled prose polish**, not export, package, upload, or publication.
