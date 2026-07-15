---
doc: revision-plan
stage: acceptance
status: approved_for_controlled_revision
book: 6
title: The Pattern
base_commit: 3130ff6aaf6fcebb778d7b15f3d441566637ae95
manuscript_scope: books/book-06/manuscript/ch-01.md through ch-08.md
starting_manuscript_words: 25181
formal_verdict: ACCEPTED WITH REQUIRED PRE-REVISION CONTROL REPAIRS
required_revision_count: 7
optional_revision_count: 12
manuscript_prose_changed_in_acceptance_pass: false
---

# Book 6 Complete First-Draft Acceptance and Revision Plan

## Audit method and source scope

This review used the repository at `dustinober1/The-Blackwood-Ridge-Mysteries` as the sole source of truth. PR #26, `Draft Book 6 Chapter 8 — The Pattern`, was verified merged before the audit began. The accepted baseline is `main` at `3130ff6aaf6fcebb778d7b15f3d441566637ae95`.

The audit included a continuous full read of Chapters 1–8, a transition reread, clue/suspect/procedural/emotional arc rereads, and full reads of:

- `books/book-06/README.md`
- `books/book-06/content-notes.md`
- `books/book-06/outline.md`
- `books/book-06/progress.yaml`
- `books/book-06/manuscript/README.md`
- `books/book-06/control/chapter-01-mission-lock.md` through `chapter-08-mission-lock.md`
- `books/book-06/bible/book-05-to-06-handoff.md`
- `books/book-06/bible/carry-forward.md`
- `books/book-06/bible/story-memory.md`
- `books/book-06/bible/mystery-solution.md`
- `books/book-06/bible/suspect-matrix.md`
- `books/book-06/bible/clue-ladder.md`
- `books/book-06/bible/timeline.md`
- `books/book-06/bible/character-arcs.md`
- `books/book-06/bible/continuity-locks.md`
- `series-outline.md`
- `series-bible/premise.md`
- `series-bible/voice-dna.md`
- `series-bible/world.md`
- `series-bible/timeline.md`
- `series-bible/story-memory.md`
- `series-bible/recurring-characters/callie-thorne.md`
- `series-bible/recurring-characters/dalton-cross.md`
- `series-bible/recurring-characters/mae-hartwell.md`
- `series-bible/recurring-characters/eli-townsend.md`
- the relevant Book 5 ending and Book 5 production tracker needed to verify the Mercer wording and protected lifecycle state.

Mechanical review covered exact and normalized recurring constructions, distinctive seven- and eight-word phrase families, evidence-limit restatements, Cross authority formulations, Mae food/tea/table beats, Eli blank-field beats, body-language recurrence, chapter-ending abstractions, and high-frequency negative-definition language. Necessary legal, scientific, custody, and canon repetitions were not treated as defects merely because they recur.

# A. Formal verdict

## **ACCEPTED WITH REQUIRED PRE-REVISION CONTROL REPAIRS**

The complete eight-chapter manuscript is accepted as the controlling Book 6 first draft. It contains a complete beginning, middle, climax, aftermath, historical recovery, official correction, and controlled series hook. Dana Wren's murder of Miriam Vale is fair-play solvable before arrest through cumulative documentary, opportunity, staging, transfer, warrant-recovery, and physical proof. The arrest does not require confession, handwriting identity, curator identity, Dana's silence, or any Chapter 8-only present-murder clue. June Halbrook's accidental death remains distinct from later concealment. Eli remains unidentified and receives no POV or private confirmation.

No fatal architecture, fair-play, custody, authority, POV, or series-lock failure requires rejection or manuscript reconciliation.

Formal acceptance is qualified because several repository controls overstate graphite-composition findings that do not appear in the accepted manuscript, and because the controlled revision must repair six additional manuscript or continuity issues: one historical date-sequence error, one historical actor-attribution overreach, Tara Bellweather's unclosed alibi loop, one Sunday travel-time control conflict, one Dana-knowledge POV sentence, and one staging-only knowledge-grounding gap. These are repairable without redesigning the mystery, changing the eight-chapter structure, weakening the arrest, or exposing the curator.

No Chapter 1–8 prose changed during this acceptance pass.

# B. Accepted manuscript baseline

## Repository and lifecycle baseline

- **Accepted `main` HEAD:** `3130ff6aaf6fcebb778d7b15f3d441566637ae95`
- **PR #26 head accepted onto `main`:** `69629026857c9a1209768c7c83ed228820a1c34c`
- **Structure:** eight chapters in intended order
- **Exact manuscript-prose total:** 25,181 whitespace-delimited words
- **Opening chronology:** Thursday, April 15, 2027, approximately 4:30 p.m., The Foxed Page
- **Closing chronology:** Sunday, April 18, 2027, 7:16 p.m., The Foxed Page
- **Exact final line:** `Who knew which page she would open next?`
- **Lifecycle:** first draft accepted; pre-revision control repairs and controlled revision pending; polish, export, package, upload, and publication pending; not upload ready

## Accepted chapter blobs, counts, chronology, geography, and final lines

| Ch. | Title | Accepted blob SHA | Words | Date | Opening | Closing | Exact final line |
|---:|---|---|---:|---|---|---|---|
| 1 | The Box at Closing | `c9a12f2305b08b1cf81ea88c1ef49e94e7a453c6` | 3,266 | Thu. Apr. 15 | approximately 4:30 p.m., The Foxed Page | 7:39 p.m., Bellweather Grange map-room threshold | `The ladder had not rolled.` |
| 2 | A Fall That Did Not Fit | `31a438514b5d528bac16b99df5e43c713079737f` | 3,135 | Thu.–Fri. Apr. 15–16 | 7:39 p.m., Bellweather Grange | 9:27 a.m., sheriff's records room | `One had been cleaned.` |
| 3 | The Surveyor's Missing Line | `59575d837b6c51d22d57ff4033e6a09bc218a409` | 3,130 | Fri. Apr. 16 | 9:32 a.m., sheriff's records room | 3:28 p.m., The Foxed Page | `Sheet 47 had described a public right-of-way through Bellweather river land.` |
| 4 | Marks Made Later | `401d46dad388ddb6ca7df6041c464465a19a48c5` | 3,150 | Fri. Apr. 16 | 3:36 p.m., sheriff's records room | 8:12 p.m., The Foxed Page | `South line retrieval.` |
| 5 | The Road Through Bellweather | `81fad0335b3781712b38d4d3139d92ffe94b3476` | 3,100 | Sat. Apr. 17 | 8:18 a.m., sheriff's records room | 5:36 p.m., The Foxed Page | `The road through Bellweather did not contain the missing thirty-nine minutes.` |
| 6 | What the Ledger Withheld | `8bdc850338411167733de54ba63f7d1de8c097b0` | 3,150 | Sat. Apr. 17 | 5:52 p.m., sheriff's evidence room | 10:46 p.m., sheriff's records room | `It was enough to ask where Dana had put the rest.` |
| 7 | The Weight of the Map | `8d2a40e7ae6157c1e3d6271019399b3930a87cb1` | 3,100 | Sun. Apr. 18 | 6:41 a.m., sheriff's records room | 11:38 a.m., The Foxed Page | `The route field remained blank.` |
| 8 | The Pattern | `c5d64e5b493152cd31a304d1eb1ad7b3c4d01064` | 3,150 | Sun. Apr. 18 | 12:06 p.m., sheriff's evidence room | 7:16 p.m., The Foxed Page | `Who knew which page she would open next?` |
|  | **Total** |  | **25,181** |  |  |  |  |

## Accepted Chapter 1–8 mission-lock blobs

| Lock | Accepted blob SHA |
|---|---|
| Chapter 1 | `96d240fbc89e13eee9017e0a88039df735658293` |
| Chapter 2 | `d71eafcd1dfdf2ed5e8461246afd14b0414184f1` |
| Chapter 3 | `0ea78a86470009407752c844043e031cead76481` |
| Chapter 4 | `2896e6b99384bfd451f14e98c60fe9bae02631e0` |
| Chapter 5 | `3dedd113a66453629178c7b0a617c7f8f1b9df6e` |
| Chapter 6 | `59b388a8013f342de19d8e9b0d0435b69a1f43a7` |
| Chapter 7 | `92f9b809b329e54a67c0308f71592fb17c8cb544` |
| Chapter 8 | `cc7951523118bf5cab9b305be0aaf380f718f3c3` |

## Eight-chapter architecture

1. **Chapter 1 — victim alive, inquiry, first mark, apparent accident.** Miriam is present long enough to establish personality, work, conflict, and the 6:15 appointment before the locked-ladder discovery.
2. **Chapter 2 — accident breaks.** Scene geometry, wound mismatch, brass transfer, and the differently cleaned weight move the case into homicide without naming a weapon or killer.
3. **Chapter 3 — cold-case architecture.** Sheet 47, Halbrook's complaint, Miriam's triangle, Owen's inherited route language, and Nadia's deleted-file path widen the book without replacing the present case.
4. **Chapter 4 — modern-mark chronology and linked routing.** The one-writer assumption is corrected; two modern directional marks are supported without handwriting identity; Tara's real custody breach is separated from murder.
5. **Chapter 5 — historical payment, present financing, Dana opportunity.** The Wren payment, guaranty, admitted appointment, key conflict, fuel record, and unexplained interval make Dana the leading suspect without supplying a warrant yet.
6. **Chapter 6 — warrant threshold.** Pressure shadow and audio are recovered within limits; Nadia, Leo, and Owen false paths close with consequences preserved; the third mark establishes repeatable design; Cross signs two narrow applications.
7. **Chapter 7 — lawful recovery, cumulative weapon proof, arrest.** Valid warrants precede searches; tracing, coat, and cloth enter custody; weight six is established cumulatively; Dana invokes counsel and does not confess.
8. **Chapter 8 — historical recovery, official correction, deliberate-steering synthesis.** Halbrook is recovered and restored to the record; accidental death remains distinct from concealment; three marks plus Mercer support deliberate steering without identifying Eli or any curator.

The chapter functions remain distinct. No structural merge, split, or reorder is approved.

# C. Non-negotiable canon locks

The controlled revision must preserve all of the following:

- Dana Wren murdered Miriam Vale.
- Removable brass map weight six is the cumulatively established weapon.
- Dana does not confess.
- Dana invokes counsel; Cross stops immediately; silence, refusal, grief, anger, and demeanor are not evidence.
- The murder case is complete without identifying the curator or routing-mark writer.
- June Halbrook died in an accidental single-vehicle departure on October 8, 1989.
- Historical concealment occurred after the accident and must not convert the death into murder.
- Halbrook's false voluntary-departure status is superseded through lawful official correction while the old entry remains visible.
- The three modern routing marks are the Grange bracket, St. Orison omitted-line symbol, and returned-pamphlet numeral.
- Miriam's triangle is legitimate research notation and is separate from those three marks.
- The Mercer wording remains exactly: `Found in returned Mercer volume by M. Hartwell; prior loose-paper location not established.`
- Deliberate steering is supported; actor, writer, mover, instrument, common physical hand, drawing occasion, and curator remain unresolved.
- Eli remains unidentified and receives no POV, private confirmation, suspicious knowledge, original evidence, warrant access, recovery access, remains access, or reader-facing curator connection.
- Book 7 retains controlled testing and Eli's exposure. No Book 7 prose is created in the Book 6 revision.
- Callie remains a bounded consultant: she observes and explains documentary relationships only within written scope and never conducts searches, questions suspects, handles unrestricted originals, enters the ravine, identifies remains, decides cause/manner, decides charges, or writes the official correction.
- Cross owns authority, scopes, scenes, interviews, records requests, forensic requests, warrants, searches, probable-cause synthesis, arrest, recovery authority, official language, and unresolved-provenance entry.
- Bell and lawful custodians own originals, photography, movement, supports, item numbers, packages, seals, transfer, transport, intake, and authenticated copies.
- Mae supplies permission, food, tea, table protection, practical history, and emotional grounding without becoming detective, moral switch, custodian, or official author.
- Eli's legitimate visible competence and apprentice role remain intact; protection does not require making him incompetent or absent.
- Book 5 remains unchanged, package `in_progress`, publication `pending`, not upload ready, and cover-blocked.

# D. Required revisions

## R-01 — Synchronize graphite, binder, composition, and grime controls

- **Priority:** High
- **Category:** Evidence-limit control / accepted-manuscript truth
- **Affected files:** `books/book-06/bible/mystery-solution.md`, `books/book-06/bible/suspect-matrix.md`, `books/book-06/bible/clue-ladder.md`, `books/book-06/outline.md`, and any copied shorthand that repeats the same claims
- **Exact issue:** The accepted manuscript reports no graphite sampling and no actual particle, binder, polymer, brand, or composition result. Chapter 4 says non-destructive work might classify those features broadly and explicitly states that no sampling was authorized. Older controls nevertheless say a modern polymer binder was found, that Miriam's triangle differs in pencil composition, that Leo's pencil binder differs, and that the St. Orison mark lies above “later” rather than older documented grime.
- **Accepted evidence:** The marks are dated through authenticated image state, repair tissue, and visible surface sequence. Leo owns pencils, and one is broadly similar in grade to a class description; grade, binder, brand, ownership, and short-stroke shape cannot identify a writer.
- **Why it matters:** A later revision guided by stale controls could import nonexistent laboratory certainty, falsely clear or identify a suspect, or contradict the manuscript's explicit no-sampling limit.
- **Required outcome:** Remove every claim of a reported polymer/binder/composition result or binder difference. Correct `later grime` to `older documented grime`. Preserve only hypothetical class-level capability and the explicit non-identification limits.
- **Prohibited overcorrection:** Do not delete the modern-mark chronology, make graphite useless, invent a new laboratory test, identify any pencil or hand, or remove Leo's ordinary pencil-access context.
- **Likely manuscript word-count effect:** None; control-file repair only.
- **Dependencies:** Must be completed before any prose revision so later editing does not import false forensic facts.

## R-02 — Correct the October 6 / October 8 / October 9–12 historical sequence

- **Priority:** High
- **Category:** Chronology / historical causality
- **Affected chapter and controls:** Chapter 8 concealment synthesis; `books/book-06/outline.md`; `books/book-06/bible/story-memory.md`; `books/book-06/bible/clue-ladder.md`; `books/book-06/bible/timeline.md`; `books/book-06/control/chapter-08-mission-lock.md`; any duplicated summary
- **Exact issue:** Chapter 8 says the county payment to Wren Grading occurred “during the same interval” as the October 9–12 grader and official activity. The authenticated payment is October 6; Halbrook's accidental crash is October 8; discovery and concealment occur October 9–12.
- **Why it matters:** The current sentence makes a pre-crash payment sound like payment for a known post-crash concealment act and blurs the accident-versus-concealment distinction.
- **Required outcome:** State the sequence explicitly: October 3 complaint; October 6 payment under `south line retrieval`; October 8 accidental departure; October 9–12 discovery, field-material removal, spoil placement, and false-report activity. Explain that the payment supports the broader suppression path but does not, by date alone, prove a post-crash service or exact task.
- **Prohibited overcorrection:** Do not move the locked payment date, move the crash date, convert the payment into a payment by Dana's father, make the crash planned, or weaken Dana's present motive.
- **Likely word-count effect:** Approximately +5 to +25 words in Chapter 8.
- **Dependencies:** Coordinate with R-03 so date correction and actor limits use one coherent historical paragraph.

## R-03 — Narrow historical actor and act attribution to the authenticated record

- **Priority:** High
- **Category:** Evidence limit / official-history fairness
- **Affected chapter and controls:** Chapter 8 recovery and correction scenes; `mystery-solution.md`; `story-memory.md`; `clue-ladder.md`; `continuity-locks.md`; `outline.md`; Chapter 8 mission lock
- **Exact issue:** The accepted paragraph moves from an October 6 payment naming Wren Grading, an October 9–12 entry placing “a grader and two officials” on the spur, and signatures on the false supplement to the collective statement that Dana's father and both officials each found the location, removed field material, concealed the descent, and supported the false account. The listed records do not individually allocate all four acts, and the pre-crash payment does not by itself place Dana's father at the post-crash scene.
- **Why it matters:** The book carefully refuses invented confession, charge, agreement, or adjudication. Assigning every act to every historical actor exceeds the same evidence limit and sits uneasily beside the corrected status `RESPONSIBILITY PARTIALLY ESTABLISHED, INDIVIDUAL ACTS ... UNRESOLVED.`
- **Required outcome:** Name Dana's father only through the authenticated Wren Grading proprietor/signatory record and describe the company/payment as part of the suppression path. Attribute post-crash presence and acts only where the maintenance entry, grader identity, signatures, removed material, and false supplement support them. Keep the collective concealment supported while leaving which person found the car, removed which material, pushed spoil, or drafted/signed which false statement unresolved unless an already-authenticated repository source assigns that act.
- **Prohibited overcorrection:** Do not erase Dana's father's supported role, absolve the two officials, invent a confession or prosecution, identify a sheet remover without evidence, or make Dana responsible for Halbrook's crash.
- **Likely word-count effect:** Approximately neutral to +40 words in Chapter 8.
- **Dependencies:** R-02; official corrected wording remains exact.

## R-04 — Close Tara Bellweather's murder-opportunity loop independently

- **Priority:** High
- **Category:** Suspect balance / fair-play closure
- **Affected chapter and controls:** Add a concise authenticated closure in Chapter 5 or Chapter 6; align `suspect-matrix.md`, `timeline.md`, `story-memory.md`, and clue summaries
- **Exact issue:** Chapter 4 states that Tara's choir attendance “still required independent verification.” The letters explain her custody lie but do not place her outside Miriam's death window. No later chapter supplies the promised verification before Tara disappears from the warrant synthesis.
- **Why it matters:** Every alternate suspect should be reduced through an independent reason rather than through the irrelevance of the secret they concealed. Leaving Tara's timing open creates an avoidable fair-play seam and makes her disappearance feel procedural rather than resolved.
- **Required outcome:** Add one concise, authenticated choir-rehearsal timeline using an institutional record and/or multiple independent witnesses sufficient to keep Tara away from the Grange during 6:15–6:35. Preserve her removal of letters, false inventory statement, trustee review, privacy consequences, and lack of authority.
- **Prohibited overcorrection:** Do not use phone tracking, magical video coverage, the letters themselves, demeanor, or family status as clearing proof. Do not erase custody consequences or turn Tara into a cooperative detective.
- **Likely word-count effect:** Approximately +20 to +60 words in Chapter 5 or 6.
- **Dependencies:** Update the final suspect-reduction synthesis after the placement is chosen.

## R-05 — Reconcile Gate Three travel and the 3:56-to-4:22 transition

- **Priority:** Medium
- **Category:** Geography / travel continuity / control-file precision
- **Affected chapter and controls:** Chapter 8; `bible/timeline.md`; Chapter 8 mission lock; any geography summary
- **Exact issue:** The control says Blackwood Ridge to Gate Three is 28 minutes in dry conditions. Chapter 8 departs at 1:24 and logs Callie at 1:55, which can read as 31 minutes without distinguishing arrival from staging intake. More importantly, Callie is released at 3:56 and the sheriff's records-room scene opens at 4:22, only 26 minutes later.
- **Why it matters:** The rest of the book treats minute-specific travel and evidence chronology as meaningful. A small contradiction in the recovery chapter is visible because every time is otherwise exact.
- **Required outcome:** Before prose revision, establish one authoritative point-to-point travel lock for sheriff's office ↔ Gate Three and distinguish road arrival from Reed's staging log. Then align departure, arrival/log, release, and records-room opening in Chapter 8 and all controls. Preserve the 2:31 vehicle location, 3:56 release unless the final reconciled travel table requires a disclosed adjustment, and the 5:07 correction endpoint.
- **Prohibited overcorrection:** Do not use emergency speeding, unexplained teleportation, or a new location for the sheriff's records room. Do not compress safety checks or let Callie enter the ravine.
- **Likely word-count effect:** Approximately +5 to +20 words or a two-to-four-minute timestamp adjustment.
- **Dependencies:** Resolve the control value before touching Chapter 8 prose.

## R-06 — Recast the Chapter 7 Dana-belief sentence within Callie's POV

- **Priority:** Medium
- **Category:** POV / knowledge boundary
- **Affected chapter:** Chapter 7, immediately after Cross states the cumulative weight-six conclusion
- **Exact issue:** `Dana's mistake had been believing ordinary meant without consequence.` presents Dana's private belief as narrator-known fact although Dana has not expressed that thought and the manuscript is single third-person limited through Callie.
- **Why it matters:** The sentence is isolated but breaches the otherwise disciplined knowledge boundary and gives a small omniscient statement of hidden intent.
- **Required outcome:** Recast as Callie's inference, as a statement about the concealment strategy supported by the scene, or as neutral thematic observation.
- **Prohibited overcorrection:** Do not add Dana interiority, confession, villain monologue, remorse, or demeanor-as-evidence. Preserve the ordinary-object thematic turn.
- **Likely word-count effect:** Neutral.
- **Dependencies:** None.

## R-07 — Ground Chapter 8 recovery facts in an authorized channel

- **Priority:** Medium
- **Category:** POV / recovery authority / knowledge provenance
- **Affected chapter:** Chapter 8 staging and recovery-summary passage
- **Exact issue:** Callie remains outside Reed's perimeter, yet the narrative states detailed recovery facts after the 3:12 Cross update without always identifying a later radio, tablet, or official-summary channel. `No note waited in the glove compartment. No last accusation survived in a pocket.` is especially categorical despite the manuscript also saying Bell did not open the recovered field case at roadside.
- **Why it matters:** The recovery design depends on Callie not seeing or controlling the ravine scene. Ungrounded omniscient facts weaken that boundary even though the custody sequence itself is sound.
- **Required outcome:** Attribute all post-perimeter details to Cross's update, Bell's logged summary, the medical examiner's transport record, or the later authorized records-room packet. Remove or reframe facts that no authorized source could yet establish, including the glove-compartment/pocket claim if it has not been lawfully reported.
- **Prohibited overcorrection:** Do not bring Callie into the ravine, show graphic remains detail, turn the recovery into a live procedural transcript, or eliminate the restrained emotional absence of a convenient final message.
- **Likely word-count effect:** Neutral to +25 words.
- **Dependencies:** Coordinate with R-02 and R-03 in the same Chapter 8 section.

# E. Recommended optional revisions

These revisions are not required for acceptance. The existing prose is publishable at the first-draft level in each cited respect; the following changes would materially improve clarity, pace, emotional weight, or rhythm if implemented without weakening evidence limits.

## O-01 — Give the Chapter 8 restoration sequence slightly more emotional air

- **Priority:** High optional
- **Affected chapter:** Chapter 8
- **Why existing prose is acceptable:** Vehicle identification, remains custody, correction, and pattern synthesis are all present and clearly separated.
- **Available improvement:** Add or redistribute roughly 80–150 words of Callie-centered stillness between cumulative identification, Ruthie's correction, and the pattern session so Halbrook's restoration lands before the series mechanism resumes.
- **Do not:** add graphic remains detail, a recovered farewell, a speech, or a new murder clue.

## O-02 — Reinforce the provisional same-day identification procedure once

- **Priority:** High optional
- **Affected chapter:** Chapter 8
- **Why existing prose is acceptable:** The text says the odontological comparison is cumulative and formal reporting will follow.
- **Available improvement:** Add one concise line establishing that the preserved dental file and pre-notified examiner/odontologist supported a provisional written comparison before the supplement, while final specialist reporting remains pending.
- **Do not:** claim instant final laboratory certainty or let Callie make the identification.

## O-03 — Ease Chapter 6's false-path density before the third-mark scene

- **Priority:** Medium optional
- **Affected chapter:** Chapter 6
- **Why existing prose is acceptable:** Nadia, Leo, and Owen each receive a fair, independent disposition with misconduct preserved.
- **Available improvement:** Strengthen one transition or add a brief sensory reset between the Owen disposition and returned-pamphlet intake so three interview closures do not read as one uninterrupted report block.
- **Do not:** delay the warrant threshold, reopen a cleared murder path, or expand subplots.

## O-04 — Compress one repeated custody recap in Chapter 7

- **Priority:** Medium optional
- **Affected chapter:** Chapter 7
- **Why existing prose is acceptable:** The warrant and custody paths are rigorous and comprehensible.
- **Available improvement:** Once each item has received location photograph, number, package, seal, transport, and intake, compress one later restatement and spend the recovered space on the arrest turn.
- **Do not:** remove any unique custody fact or let Callie see evidence before intake.

## O-05 — Vary selected Cross evidence-limit catechisms

- **Priority:** Medium optional
- **Affected chapters:** Primarily 3–8
- **Why existing prose is acceptable:** Cross's clipped question-and-limit method is character-true and makes the mystery portable.
- **Available improvement:** Preserve the strongest `What does it establish? / What does it not?` sequence in each major proof stream, but convert a few later repetitions into action, a logged sentence, or Callie's internal correction.
- **Do not:** blur authority or remove distinct legal/scientific limits.

## O-06 — Thin local negation clusters where the limit is already secure

- **Priority:** Medium optional
- **Affected chapters:** Primarily 4, 6, 7, and 8
- **Why existing prose is acceptable:** Repeated `not`, `did not`, `remained`, `supported`, and `established` formulations protect fair play.
- **Available improvement:** Where two adjacent paragraphs repeat the same exclusion, keep the clearest version and let the surrounding material image carry the second beat.
- **Do not:** compress separate propositions into one vague disclaimer.

## O-07 — Reduce one or two duplicate Eli blank-grid beats

- **Priority:** Medium optional
- **Affected chapters:** 4–8
- **Why existing prose is acceptable:** Honest blanks are an important apprentice skill and the correct long-arc protection.
- **Available improvement:** Keep the first, third-mark, arrest-endpoint, and final provenance-ledger blanks; vary or shorten one intermediate inventory of blank fields.
- **Do not:** make Eli suspicious, remove his visible competence, or give him original evidence access.

## O-08 — Vary Mae's repeated labeled-food/table care motif

- **Priority:** Medium optional
- **Affected chapters:** 3–8
- **Why existing prose is acceptable:** Labels such as `NOT CASE MATERIAL`, `AFTER THE SEARCH`, and `NOT EVIDENCE` embody permission and boundary-aware care.
- **Available improvement:** Preserve the strongest labels, but allow one later care beat to arrive through placement, timing, or unasked permission rather than another card-and-kettle construction.
- **Do not:** restore easy intimacy, make Mae the moral authority, or let food enter evidence space.

## O-09 — Add one non-evidentiary human texture beat for Dana before arrest

- **Priority:** Medium optional
- **Affected chapters:** 5 or 7
- **Why existing prose is acceptable:** Dana is credible, controlled, motivated, and not caricatured.
- **Available improvement:** Add a brief ordinary-business or community responsibility detail that complicates her financial-survival posture without inviting sympathy as exculpation.
- **Do not:** add confession, secret POV, melodramatic grief, villain signaling, or demeanor evidence.

## O-10 — Vary repeated abstract-turn constructions

- **Priority:** Low optional
- **Affected chapters:** Whole draft, especially 2–4, 7–8
- **Why existing prose is acceptable:** Short turns such as `The difference offered no comfort`, `The separation mattered`, and related distinction statements efficiently mark analytical boundaries.
- **Available improvement:** Replace one or two with the concrete consequence that follows, especially where `difference`, `distinction`, or `separation` appears near another abstract noun turn.
- **Do not:** remove the accident/concealment distinction or any evidence-limit statement.

## O-11 — Vary one pre-final-line abstraction without changing locked endings

- **Priority:** Low optional
- **Affected chapters:** 3, 5, 7, and 8
- **Why existing prose is acceptable:** Each final line fulfills its chapter hook and should remain locked.
- **Available improvement:** Adjust the sentence immediately before one or two final lines so the sequence does not repeatedly move from abstract record language to a short document/page/blank image.
- **Do not:** alter the exact final lines or weaken chapter hooks.

## O-12 — Restore a little lived texture to the most report-like sheriff-room transitions

- **Priority:** Low optional
- **Affected chapters:** 5 and 6
- **Why existing prose is acceptable:** Procedure remains integrated into scene action and the technical material is understandable.
- **Available improvement:** Add a small body, weather, sound, or object beat at one dense transition so Callie's consciousness remains present while records change hands.
- **Do not:** ornamentalize every document or slow clue delivery with generic dread.

# F. Chapter-by-chapter revision map

| Ch. | Current function | Strengths to preserve | Required changes | Optional changes | Clue / authority / character locks | Expected direction |
|---:|---|---|---|---|---|---|
| 1 | Victim alive; Halbrook inquiry; first modern mark; apparent accident | Miriam's presence; selected-reader temptation; exact appointment card; locked-ladder hook | None | Only local rhythm if needed later | Mark chronology remains limited; Cross controls threshold; Eli ordinary; no killer/curator reveal | Stable |
| 2 | Break accident assumption; open homicide | Scene geometry; wound restraint; no premature weapon claim; Leo pressure | None | Vary one abstract distinction beat if useful | No magical medical certainty; Callie works from photographs; one cleaned handle is not yet weapon proof | Stable or slight compression |
| 3 | Establish sheet 47, Halbrook complaint, triangle, Owen/Nadia paths | Custodian procedure; honest one-writer misread; source grid; cold-case/present-case separation | None | Minor cadence variation only | Triangle remains Miriam's; sheet route incomplete; no audio heard; no Owen conclusion | Stable |
| 4 | Date two modern marks and establish linked routing; resolve Tara's secret | Excellent image-before-original sequence; surface chronology; Tara's custody consequences | R-01 applies to controls, not accepted prose | Vary one `not proved` exchange or abstract turn | No sampling; no binder result; Tara not cleared by letters; Cross/custodians control | Stable |
| 5 | Historical payment, present financing, Dana opportunity, Owen pressure | Exact money; fuel and key limits; Mae context independently checked | Place or prepare R-04 Tara alibi closure if this is the least intrusive location | Add one Dana human texture beat | Fuel is not tracking; motive not presence; no garment/weapon identification; curator separate | Slight expansion |
| 6 | Recover pressure/audio; close false paths; third mark; warrant threshold | Fair independent reductions; third-mark chronology; exact Mercer comparison; warrant restraint | Complete R-04 here if not in Ch. 5 | O-03, O-05, O-06, O-07 | Only quoted audio `Dana at six fifteen`; only pressure fragment; no search/arrest; consequences preserved | Stable to slight expansion |
| 7 | Execute warrants; recover items; establish weapon; arrest without confession | Narrow warrants; full custody; preliminary DNA limit; cumulative proof; immediate counsel stop | R-06 POV recast | O-04, O-05, O-09 | Map weight six cumulative; no confession; no silence evidence; murder independent of curator | Stable or slight compression |
| 8 | Complete tracing; recover Halbrook; correct record; synthesize pattern | Recovery section rather than magical point; respectful staging; exact correction; Mercer wording; final ledger image | R-02, R-03, R-05, R-07 | O-01, O-02, O-05–O-08, O-10–O-12 as applicable | Accident remains accident; individual acts limited; Callie staging-only; deliberate steering without identity; Eli unidentified | Moderate targeted expansion after chronology repair |

# G. Whole-book consistency repairs and audit matrices

## Control-file corrections required before prose revision

1. **`books/book-06/bible/mystery-solution.md`** — remove the unperformed polymer-binder finding; preserve no-sampling/class-only limits; correct historical attribution and sequence.
2. **`books/book-06/bible/suspect-matrix.md`** — remove Leo binder-difference language; replace “helps locate Halbrook car” with his actual hazard/road-information role; add the independently verified Tara alibi only after it is placed on-page; preserve separate consequences.
3. **`books/book-06/bible/clue-ladder.md`** — remove the claim that Miriam's triangle differs in pencil composition; align historical chronology and actor limits.
4. **`books/book-06/bible/story-memory.md`** — align Chapter 8's October sequence, supported-role language, Tara closure, and any revised travel time.
5. **`books/book-06/bible/timeline.md`** — distinguish departure, physical arrival, staging log, release, and return travel; preserve all evidence/warrant/arrest times that remain consistent.
6. **`books/book-06/bible/continuity-locks.md`** — replace collective all-acts attribution with evidence-limited role/act language while preserving partial responsibility and accident/concealment separation.
7. **`books/book-06/outline.md`** — correct `later grime` to `older documented grime`; align Tara, historical chronology, actor limits, and travel timing.
8. **`books/book-06/control/chapter-08-mission-lock.md`** — correct the October 6 payment relationship, historical attribution, and the final reconciled travel table.
9. **Status files** — this acceptance pass records the verdict and plan but leaves every chapter `drafted`, revision pending, and Book 6 not upload ready.

Planning shorthand is subordinate to accepted manuscript truth except where this plan identifies a genuine manuscript repair.

## Chronology and geography audit

| Sequence | Audit finding | Classification |
|---|---|---|
| Thu. Apr. 15, Miriam alive through 6:07; death window 6:15–6:35; discovery 7:12 | Coherent | No issue |
| Dana `T-2` 5:43 issue, 6:03 out, 6:32 in, 6:42 fuel; six-to-eight-minute route | Coherent and properly limited; at least 39 minutes unexplained | No issue |
| Nadia at café through 6:22; earliest Grange arrival 6:38 | Independently excludes murder window while preserving misconduct | No issue |
| Leo 6:10–7:05 program; images/video place him continuously by 6:12–7:03 | Independently excludes murder window | No issue |
| Owen Wednesday mud versus Thursday depot/truck records | Correctly dates false path and preserves discipline | No issue |
| Tara choir timing | Promised but not independently shown after Chapter 4 | Minor manuscript continuity / fair-play repair (R-04) |
| Sat. evidence review 5:52–10:46 and warrant applications | Evidence precedes application; no search or arrest | No issue |
| Sun. 6:37 issuance; 6:41 verification; 7:30 execution; 10:14 probable cause; 10:20 arrest | Correct authority order | No issue |
| Ch. 7 endpoint 11:38; Ch. 8 opening 12:06 | Exact 28-minute chapter handoff | No issue |
| 12:06–12:47 tracing review; 12:55–1:18 briefing; 1:24 departure; 1:55 staging log | Arrival/log distinction not explicit against 28-minute geography lock | Control/manuscript clarity repair (R-05) |
| 2:31 vehicle location; 3:38 active recovery end; 3:56 release | Coherent internally | No issue |
| 3:56 release; 4:22 records-room opening | Two minutes shorter than the existing 28-minute general travel lock | Control-file conflict requiring reconciliation (R-05) |
| 4:22–5:07 correction; 5:34–6:48 pattern; 7:16 closing | Coherent after return-time repair | No issue |
| Oct. 3 complaint; Oct. 6 payment; Oct. 8 accident; Oct. 9–12 concealment | Manuscript incorrectly calls payment part of later interval | Minor manuscript chronology repair, high importance (R-02) |

No character otherwise appears in incompatible locations. No warrant, search, arrest, recovery, or record correction occurs before its necessary authority or evidence.

## Mystery-fairness and clue-order audit

- **Documentary/motive:** `D.W. — title line / six fifteen`, sheet 47, Halbrook complaint, Wren payment, `south line retrieval`, Bellweather Landing financing, Dana's guaranty, and title/right-of-way risk are reader-visible before the arrest. Motive is never treated as presence.
- **Opportunity:** Dana admits the appointment. The key conflict, 5:55 claim, 6:42 fuel record, six-to-eight-minute route, and 39-minute unexplained interval are all available before arrest. Fuel is not treated as continuous tracking.
- **Staging/physical proof:** Locked ladder, no-rotation floor sequence, wound geometry, weight six, cuff transfer, green wool, recovered coat, recovered cloth, preliminary Miriam association, polish/metal residue, and differently wiped handle form a cumulative chain.
- **Corroboration:** `...ROW 14 / RIVER ACCESS`, `Dana at six fifteen`, original tracing possession, and false-path exclusions strengthen the warrant and arrest without becoming individual dispositive clues.
- **Chapter 8:** Adds no fact required to solve Miriam's murder. It resolves Halbrook and provenance.
- **Fatal fair-play failure:** None.
- **Clue arriving too late:** None for the murder solution.
- **Under-closed false path:** Tara's opportunity only; R-04 repairs it.
- **Over-repeated limit:** Some Cross catechisms and negative-definition clusters; optional only because each proof stream remains intelligible and accurate.

## Suspect-balance audit

| Person | Reader-visible suspicion | Independent reduction / disposition | Audit result |
|---|---|---|---|
| Dana Wren | Exact appointment, present financing pressure, inherited suppression path, key conflict, false departure, unexplained interval, possession, transfer | Arrested on cumulative evidence; no confession; not curator | Sound |
| Owen Pike | Route knowledge, copy, mud, unauthorized use | Wednesday mud; Thursday depot records; no Grange access; discipline and possible legal review remain | Sound |
| Nadia Reese | Deleted recording, ownership/commercial pressure | Café witnesses/records and travel exclusion; privacy, consent, ownership, copyright, and commercialization consequences remain | Sound |
| Leo March | Public quarrel, plagiarism, payment offer, retained copy, pencils | Continuous library program; professional/civil consequences remain; pencils non-identifying | Sound |
| Tara Bellweather | Keys, altered count, removed letters, family pressure | Secret explains custody breach but choir alibi is not independently closed on-page | Required repair R-04 |
| Institutional historical actors | Payment, maintenance, false supplement | Collective concealment supported; individual acts and legal disposition unresolved | Requires R-02/R-03 precision |

No alternate suspect should disappear before an independent murder-opportunity resolution. No real misconduct should be erased merely because it is not murder.

## Procedural and authority audit

- **Cross:** Correctly controls scene access, written consultant scopes, records requests, interviews, evidence requests, warrants, execution, probable cause, rights, arrest, recovery authority, official synthesis, record correction process, public/legal wording, and unresolved provenance.
- **Bell/lawful custodians:** Correctly control originals, supports, photography, movement, item numbers, packages, seals, transfer, transport, intake, registered images, and display copies.
- **Callie:** Remains within written observation/explanation scopes; handles no unrestricted original; conducts no search or suspect interview; does not enter the ravine, identify remains, decide cause/manner, decide charges, or write/sign/file the correction. R-07 repairs only knowledge-channel wording, not conduct.
- **Mae:** Protects tables, food, tea, permission, and emotional scale; authenticates nothing and directs no authority.
- **Eli:** Works from approved metadata/copies and honest blanks; no official evidence, warrant, search, recovery, suspect, or private curator access.
- **Weekend process:** On-call magistrate, county access, road crew, fire-rescue, medical examiner, vehicle examiner, and weekend annex custody are all named. Same-day provisional identification would benefit from O-02 but is not a fatal procedural defect because formal reports remain pending.

## Evidence-limit matrix

| Evidence / conclusion | Proves | Supports | Does not prove | Authorized voice | Manuscript limit status |
|---|---|---|---|---|---|
| Short graphite marks | Visible shape and placement | Broad function and relative chronology with images/repairs | Writer, identity, intent by itself | Callie within scope; examiner/Cross for official use | Clear |
| Handwriting identity | Nothing individual from these short marks | At most non-identifying comparison context | Dana, Leo, Eli, or any writer | Examiner/Cross | Clear |
| Graphite particle class | No reported result | Hypothetical broad class if lawfully tested | Person, brand user, owner, purchase | Examiner | Control overstates; R-01 |
| Binder/polymer class | No sampling or reported result | Hypothetical manufacturing-period context only | Writer, pencil, brand, purchase, common hand | Examiner | Control overstates; R-01 |
| Pencil grade/brand | One Leo pencil broadly similar in grade context | Ordinary access to pencils | Writer identity or exclusion | Examiner/Cross | Clear in manuscript |
| Instrument/ownership/purchase | Not established | Investigative question only | Mark maker or curator | Cross | Clear |
| Common physical hand/occasion | Not established | Shared directional design only | Same writer, same pencil, same day | Cross after Callie comparison | Clear |
| Route versus mover | Three directions form a designed route | Non-neutral access and tailored sequence | Who moved or marked any item | Cross | Clear |
| Genuine host versus neutral arrival | Host content remains genuine | Arrival/access may have been deliberately shaped | Fabrication of content or murder guilt | Custodian/Callie/Cross | Clear |
| Preliminary DNA association | Human blood; profile consistent with Miriam at reported loci | Cumulative cloth-to-victim association | Exclusive identity, full final profile, murder by itself | Laboratory/Cross | Clear and properly preliminary |
| Dark green wool | Class characteristics shared | Transfer chain with independently authenticated coat possession | Unique garment or wearer by fiber alone | Trace examiner/Cross | Clear |
| Brass polish / metal residue | Shared class characteristics | Cuff/weight/cloth cumulative relation | Unique tin, cloth, user, or minute | Trace examiner/Cross | Clear |
| Wound geometry | Rounded heavy-object class; inconsistency with ladder/edge | Weight six with all other evidence | Unique object by geometry alone | Dr. Arledge/Cross | Clear |
| Differently wiped handle | Surface differs from other handles | Staging/wiping with residue chain | Exact wipe time or wiper | Examiner/Cross | Clear |
| Vehicle identification | Plate sequence and frame number match registration cumulatively | Halbrook vehicle identity | Driver identity or cause alone | State vehicle examiner/Cross | Clear |
| Human-remains identification | Cumulative vehicle/location/effects/dental comparison | Halbrook identity provisionally pending final report | Identity from effects alone | Medical examiner/odontologist | Clear; O-02 optional reinforcement |
| Accidental-death conclusion | Scene relationships support single-vehicle departure | Official supplemental status with pending specialists | Murder, exact mechanical failure, every final detail | Medical examiner/Cross/lawful custodian | Clear |
| Historical concealment | Spoil, maintenance records, removed material, false supplement | Deliberate post-accident concealment | Every actor's act, confession, agreement, charge, final disposition | Cross/custodian | Actor wording overstates; R-03 |
| Dana's father's role | Wren Grading proprietorship/signature and payment | Company/family connection to suppression path | Personal post-crash presence or every concealment act from payment alone | Treasurer records/Cross | Needs R-02/R-03 precision |
| Two officials | Historical roles/signatures and later road/false-report record | Participation at supported role/act level | Confession, prosecution, every individual act | Cross/custodian | Mostly clear; R-03 precision |
| Mercer ticket | Genuine, recent, useful, independently authenticated, route-incomplete | Earlier access anomaly | Common mover, curator, or invalid Book 5 solution | Book 5 record/Cross | Exact wording preserved |
| Deliberate steering | Three dated marks share directional design tailored to Callie's public method | Designed access/routing concern | Actor, writer, mover, instrument, common hand, occasion, curator | Cross | Clear |

The final unresolved-provenance distinction remains: deliberate routing supported; actor unresolved; writer unresolved; mover unresolved; instrument unresolved; common hand unresolved; curator unresolved.

## POV and knowledge audit

The manuscript remains single third-person limited through Callie except for the isolated R-06 sentence and the R-07 recovery-summary grounding gap. Cross's, Mae's, Eli's, Dana's, Owen's, Nadia's, Leo's, Tara's, Bell's, and custodians' thoughts are otherwise conveyed only through observable behavior, speech, or authenticated report. No reader-only Eli knowledge appears.

## Character-arc audit

- **Callie:** Moves from dangerous satisfaction at being selected through correction of her one-writer assumption to disciplined provenance vigilance. She is not paranoid, omniscient, deputized, romance-led, or emotionally cured.
- **Cross:** Uses written boundaries, specialized expertise, warrants, arrest control, recovery authority, official correction, and an unresolved-provenance entry. He remains procedural, accountable, clipped, and non-romantic.
- **Mae:** Protects permission, table, food, tea, and human scale; distinguishes receipt from intended receipt; does not solve, authenticate, or erase the fracture.
- **Eli:** Shows source-grid, duplicate, chronology, and honest-blank competence. No confession, suspicious knowledge, POV, original evidence, or curator exposure appears.
- **Dana:** Remains credible before arrest, financially and familially pressured rather than caricatured, arrested on cumulative evidence, and non-confessional. O-09 is optional enrichment only.

## Voice, atmosphere, dialogue, exposition, and repetition findings

- **Voice:** Strong match for precise, close-Callie, atmospheric-but-controlled series prose. Material observation usually carries emotion rather than naming it.
- **Atmosphere:** Rain, cold rooms, wet gravel, old wood, glass, graphite, brass, tea, river air, and shop light form a coherent sensory system without trivializing murder or remains recovery.
- **Dialogue:** Cross's clipped procedural dialogue, Mae's restrained care, and Callie's exact distinctions are character-consistent. Cross's repeated catechism becomes locally predictable but remains functional.
- **Exposition:** Technical material is generally integrated into custody, interview, or comparison action. Chapters 5–6 and parts of 8 occasionally read like a polished production summary; optional transitions can restore lived texture.
- **Exact/near-exact repetition:** Recurrent distinction turns (`The difference...`, `The distinction...`, `The separation mattered`) appear across Chapters 2–4, 7, and 8. They are thematically functional but one or two can be varied.
- **Repeated construction:** Cross repeatedly asks what a fact establishes, followed by a sequence of `No`, `Not proved`, or `It does not`. Preserve where each answer protects a different limit; vary only redundant local instances.
- **Repeated body/work beats:** hands held behind table edges, folders opened/closed, Bell changing displays, Cross writing the limit first, Mae placing labeled food/tea, and Eli leaving blanks. Most are intentional authority motifs; O-07/O-08 address density rather than removal.
- **Repeated vocabulary:** `remained`, `supported`, `established`, `controlled`, `authorized`, `genuine`, `blank`, `route`, and `record` are high-frequency. Much is necessary technical language. Accidental clusters are polish targets, not grounds for broad revision.
- **Repeated endings:** Several chapters close on a record, blank, route, page, or absence abstraction. Exact ending lines remain effective and locked; only pre-ending cadence is optional.
- **Distinctive repeated seven/eight-word material:** Repetition is concentrated in required evidence formulations and recurring field labels rather than accidental duplicate narrative sentences. No repeated passage suggests copy error or structural duplication.

## Pacing and emotional-resolution audit

Miriam receives sufficient living-page time before death. The accident-to-homicide turn lands promptly. Halbrook's erasure grows alongside the present case rather than displacing it. Dana's motive and opportunity accumulate over Chapters 5–6; warrant preparation receives a full threshold; Chapter 7 contains the legal/physical climax; Chapter 8 gives aftermath, recovery, correction, and series movement.

Chapter 8's complete-tracing interpretation is appropriately a recovery section, not a magical coordinate. The recovery is respectful, quiet, and non-graphic. Accident and concealment are conceptually separate, though R-02/R-03 must repair their historical wording. The corrected record lands clearly; O-01 would give it more air. The pattern explanation is understandable and preserves identity limits. The final ledger and question provide closure plus controlled Book 7 movement rather than a cliffhanger.

# H. Deferred work

The following remain explicitly outside this acceptance pass and outside the first controlled revision except where separately approved:

- broad line editing;
- final prose polish;
- copyediting and proofreading;
- front matter, back matter, and retail metadata;
- combined-manuscript assembly;
- DOCX, HTML, EPUB, PDF, or other export;
- package validation;
- cover work;
- listing and upload worksheets;
- upload, distribution, submission, or publication.

Book 6 remains unrevised and not upload ready until the required control repairs and approved manuscript revisions are implemented and validated.