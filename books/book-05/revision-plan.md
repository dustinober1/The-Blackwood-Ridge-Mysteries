---
doc: revision-plan
stage: revise
status: approved_for_implementation
book: 5
title: The Planted Page
base_commit: 8c54b0a90826ed1118bef1a630dfd4ce7bcc1118
manuscript_scope: books/book-05/manuscript/ch-01.md through ch-08.md
starting_manuscript_words: 25182
---

# Book 5 Whole-Draft Revision Plan

## Executive summary

The accepted eight-chapter draft is structurally sound, fair-play solvable, procedurally disciplined, and consistent with the locked mystery and Book 4 handoff. The solution already rests on cumulative proof rather than a hidden late fact. No mystery redesign, new decisive evidence, new confession, suspect substitution, authority expansion, or ending change is warranted.

This revision pass will make four substantive repair groups:

1. correct one Chapter 1 day-transition ambiguity;
2. correct one Chapter 6 transition that can imply the erased ledger time was recovered when it was not;
3. synchronize internal pressure-image controls with the accepted reader-visible evidence limit;
4. synchronize the suspect matrix and selected character files with the accepted manuscript rather than older planning shorthand.

Production trackers will then be updated to the actual revised state and word counts. Broad sentence-level compression, motif variation, and voice polish are deferred to the dedicated line-editing stage because they are low urgency, higher touch, and not required for continuity or fairness.

## Controlling baseline

- Repository: `dustinober1/The-Blackwood-Ridge-Mysteries`
- Verified base: current `main` at `8c54b0a90826ed1118bef1a630dfd4ce7bcc1118`
- Chapter 8 prerequisite: merged through PR #13, with the accepted Chapter 8 manuscript blob present on `main`
- Accepted manuscript: Chapters 1–8, totaling 25,182 manuscript-prose words before revision
- Governing rule: accepted reader-visible manuscript truth overrides older planning shorthand where they conflict
- Locked mystery, legal structure, evidence limits, character endpoints, provenance wording, and final line remain unchanged
- Protected internal continuity was checked only to prevent contradiction. No protected content is reproduced, explained, dramatized, or foreshadowed here.

## Audit method

The review used:

- full sequential reading of accepted Chapters 1–8;
- full reading of Book 5 progress, outline, content notes, premise, carry-forward, story memory, timeline, clue ladder, suspect matrix, world, relevant character files, and relevant location files;
- protected-continuity contradiction check without reader-facing use;
- full reading of series outline, root progress, voice DNA, series world, series timeline, series story memory, and recurring Callie, Cross, Mae, and Eli files;
- full reading of the final accepted Book 4 manuscript, with special attention to its ending and the case-by-case consultant handoff;
- inspection of Book 4 revision-plan, tracker, branch-history, commit-history, and production conventions;
- chapter-to-chapter chronology and knowledge-state mapping;
- material-clue fair-play review;
- five-suspect balance review;
- legal/procedural and evidence-custody review;
- proof-stream limit review;
- Callie-only POV review;
- mechanical searches for repeated evidence-limit language, recurring gestures, and high-frequency series vocabulary;
- close reading for repeated explanation, sentence patterns, chapter movement, atmosphere, and technical intelligibility.

# A. Required continuity and mystery-fairness repairs

## R-01 — Chapter 1 day-transition clarification

- **Category:** Chronology / chapter handoff
- **Severity:** Medium
- **Affected chapter:** Chapter 1
- **Precise location:** Final scene, after Callie closes the shop, eats, goes upstairs, and sets the brass magnifying glass on her desk
- **Current wording / function:** `That morning, the telephone below began to ring.` The sentence is meant to open Tuesday morning and deliver Tess's death call.
- **Risk:** `That morning` can read as a return to Monday morning, compressing the close-of-day and next-day death discovery into an unclear transition.
- **Proposed repair:** Change to `The next morning, the telephone below began to ring.`
- **Locked facts to preserve:** Monday, January 25 catalog visit; Monday evening close; Tuesday, January 26 call; Tess discovers Alton at 8:05 a.m.; Chapter 2 remains the Tuesday scene response.
- **Disposition:** Required
- **Expected effect:** No clue-timing or suspect-balance change; approximately +1 manuscript word in Chapter 1.

## R-02 — Chapter 6 erased-time / electronic-event separation

- **Category:** Evidence limit / causal clarity / chronology
- **Severity:** High
- **Affected chapter:** Chapter 6
- **Precise location:** Transition between the altered `8:05` access-ledger analysis and Bell's presentation of the authenticated 9:14 side-door event
- **Current wording / function:** `The earlier time came into the room through a different door.` The intended function is to shift from the handwritten ledger to an independent electronic record.
- **Risk:** The phrase can imply that the erased earlier ledger time has been recovered. The accepted evidence limit is that the ledger does not reveal the erased time; the electronic system separately records a 9:14 assigned-code event.
- **Proposed repair:** Change to `A separate time record came into the room through a different door.`
- **Locked facts to preserve:** The erased underlying time remains unrecovered; no altering hand is identified; the 9:14 event proves use of Nora's assigned code but not visual identity, duration, or conduct inside the house.
- **Disposition:** Required
- **Expected effect:** Clarifies two proof streams without changing clue order or weight; approximately +1 manuscript word in Chapter 6.

## R-03 — Pressure-image evidence-limit synchronization

- **Category:** Clue-order consistency / evidence-limit control
- **Severity:** Medium
- **Affected files:** `books/book-05/outline.md`, `books/book-05/bible/timeline.md`, `books/book-05/bible/clue-ladder.md`
- **Precise locations:** Chapter 7 pressure-image scene in the outline; January 31 entry in the timeline; pressure-image row in the clue ladder
- **Current wording / function:** Older shorthand says the pressure image reconstructs a removed heading, gives `RESTATEMENT / REMOVE N.M.S. / IND. TRUSTEE / AUDIT`, or gives the removed red portfolio a second path.
- **Risk:** The accepted manuscript shows only `REMOVE N.M.S. / IND. TRUSTEE / AUDIT`. It does not independently identify the missing document, locate the red portfolio, or reproduce a `RESTATEMENT` heading. Older shorthand overstates what the impression proves.
- **Proposed repair:**
  - preserve the exact visible text `REMOVE N.M.S. / IND. TRUSTEE / AUDIT`;
  - describe the impression as partial support for the removal / independent-trustee / audit terms;
  - state that Pruitt authenticates those terms against his draft summary;
  - state that the impression does not identify its writer, remover, full source document, or present location.
- **Locked facts to preserve:** Pressure image remains genuine, partial, and non-identifying; missing restatement is recovered only in the warrant search; no new route to the red portfolio is created.
- **Disposition:** Required
- **Expected effect:** No manuscript word-count change; prevents internal controls from encouraging future overstatement.

## R-04 — Suspect-matrix and character-file synchronization

- **Category:** Suspect balance / accepted-continuity control
- **Severity:** Medium
- **Affected files:** `books/book-05/bible/suspect-matrix.md`; selected Book 5 character files for Claire Mercer Duvall, Gideon Shaw, and Caleb Voss
- **Precise locations:** Suspect rows and lie/opportunity summaries
- **Current wording / function:** Several entries retain planning details not present in the accepted manuscript, including a Claire departure-time lie and folio-fiber clue, a Gideon foreman-pressure act and graphite-layout-paper clue, a Caleb 7:55 study time, and other over-specific clearing details.
- **Risk:** Future revision or polish could mistakenly import discarded details, distort suspect balance, or create evidence the reader never saw.
- **Proposed repair:** Align each entry to accepted scenes only:
  - **Nora:** altered departure line; false scarf-return explanation; removal and concealment established by the accepted evidence; no invented denial about current samples.
  - **Claire:** unauthorized removal and evasive non-answer; independently authenticated ride and bookstore alibi; no departure-time lie or folio-fiber clue.
  - **Gideon:** minimization of overruns and revised descriptions; authenticated county-site alibi; no invented foreman instruction or transfer-material clue.
  - **Tess:** incomplete medication handling and later authenticated gate-cottage record; no invented `8:10` entry or unshown side-door-camera detail.
  - **Caleb:** legitimate transfer tools, disputed folio removal, and provenance substitution; authenticated 8:23 courier/shop-camera alibi; no invented 7:55 study departure.
- **Locked facts to preserve:** Nora remains murderer; all four alternate suspects retain meaningful separate misconduct and independently supported critical-window alibis; no new secret, alibi problem, or decisive clue.
- **Disposition:** Required
- **Expected effect:** No reader-facing word-count change; improves future suspect-balance control.

## R-05 — Revision-state and count synchronization

- **Category:** Production continuity / tracker accuracy
- **Severity:** Medium
- **Affected files:** `books/book-05/progress.yaml`, `books/book-05/manuscript/README.md`, and the Book 5 production-status line in `series-outline.md`
- **Precise location:** Revision stage, chapter statuses, actual word counts, total, and Book 5 lifecycle label
- **Current wording / function:** First-draft state is correctly recorded before this pass, while the root series outline still labels Book 5 as initialized with drafting pending.
- **Risk:** Repository controls would disagree after implementation.
- **Proposed repair:** After manuscript validation, mark revision complete, set all eight chapters to `revised`, record actual per-chapter and cumulative manuscript-prose counts, leave polish/export/package/publication pending, and synchronize the Book 5 series-outline status. Root `progress.yaml` remains unchanged because Book 5 correctly remains overall `in_progress` until later production stages.
- **Locked facts to preserve:** No release, upload-ready, package, export, or publication claim.
- **Disposition:** Required after validation
- **Expected effect:** Accurate production state only.

# B. Optional prose and presentation polish

## O-01 — Repeated evidence-limit formulations

- **Category:** Repetition / procedural exposition
- **Severity:** Low
- **Affected chapters:** Primarily Chapters 3–8
- **Current function:** Cross repeatedly asks what a record proves and what it does not prove; Callie repeatedly separates handwriting, medical, motive, access, and custody streams.
- **Risk:** A later line-edit could find some local compression, but broad compression here could weaken legal clarity, fair-play orientation, or Cross's authority.
- **Proposed repair:** Defer broad changes to the line-editing stage. Preserve every distinct evidentiary limit. At polish, vary only genuinely redundant local wording where no proof distinction is lost.
- **Disposition:** Deferred
- **Expected effect:** None in this revision pass.

## O-02 — Repeated procedural objects and gestures

- **Category:** Motif / line-level variety
- **Severity:** Low
- **Affected chapters:** All, especially Chapters 3, 4, 6, 7, and 8
- **Current function:** Folders, photographs, seals, hands held back, Cross's hat, Bell's camera, and Mae's labels externalize authority, restraint, and shared work.
- **Risk:** Mechanical removal would flatten the book's atmosphere and procedural grammar. A few sentence-level variations may be available later.
- **Proposed repair:** Preserve motif recurrence in revision. Reassess density during line polish, scene by scene.
- **Disposition:** Deferred
- **Expected effect:** None in this revision pass.

## O-03 — Repeated series vocabulary and three-part lists

- **Category:** Voice / rhythm
- **Severity:** Low
- **Affected chapters:** Whole draft
- **Current function:** `exact`, `separate`, `ordinary`, `controlled`, `remained`, three-part evidentiary lists, and negative-definition sequences are part of the established series voice.
- **Risk:** Some clusters are visible on close reading, but they do not materially obscure clue hierarchy or slow the mystery at revision-level severity.
- **Proposed repair:** Defer to line editing. Replace only local accidental echoes while preserving voice DNA and technical clarity.
- **Disposition:** Deferred
- **Expected effect:** None in this revision pass.

## O-04 — Chapter-opening and chapter-ending tightening

- **Category:** Pacing / presentation
- **Severity:** Low
- **Affected chapters:** All
- **Current function:** Each chapter opens with a physical object or controlled procedural image and ends on a clue, boundary, or emotional movement.
- **Risk:** No opening or ending fails its locked function. Revision now would be preference rather than necessity.
- **Proposed repair:** No change in this pass. Revisit only for cadence during prose polish.
- **Disposition:** Deferred
- **Expected effect:** None.

## O-05 — Technical-intelligibility micro-polish

- **Category:** Clarity
- **Severity:** Low
- **Affected chapters:** Chapters 3, 4, 6, and 7
- **Current function:** Explains handwriting construction, source authentication, custody, medical limits, access records, and warrant synthesis in nonexpert language.
- **Risk:** Technical passages are already intelligible. Broad simplification could erase distinctions that make the mystery fair.
- **Proposed repair:** No broad revision. The two required transitions above supply the only needed clarity repairs at this stage.
- **Disposition:** Deferred
- **Expected effect:** None beyond R-01 and R-02.

# Whole-draft chronology matrix

| Date | Chapter | Reader-visible movement | Knowledge / authority state | Audit result |
|---|---:|---|---|---|
| Mon. Jan. 25 | 1 | Shop requests; Mercer catalog session; current natural hand; red portfolio; private Tuesday appointment | Callie observes only; no case authority | Sound after R-01 clarifies the next morning |
| Tue. Jan. 26 | 2 | 8:05 discovery; apparent suicide; controlled scene; note and bottle; first handwriting anomaly | Cross preserves scene; Callie receives narrow written scope | Sound |
| Wed. Jan. 27 | 3 | Authenticated comparison lanes; suspect secrets; current repair record enters comparison with a route limitation | Bell controls custody; Cross authorizes; Callie compares; Eli and Mae remain bounded | Sound |
| Thu. Jan. 28 | 4 | Simulation method demonstrated; examiner submission; homicide turn from medical findings | Handwriting and medical streams remain independent | Sound |
| Fri. Jan. 29 | 5 | Voicemail, operative trust, unsigned restatement, exact financial path, altered-access preview | Pruitt and records authenticate; Cross limits motive overreach | Sound |
| Sat. Jan. 30 | 6 | Altered `8:05`; 9:14 assigned-code event; scarf contradiction; medication route; four alibis; warrant threshold | Cross owns re-interview and affidavit; Callie supplies narrow observations | Sound after R-02 separates the time records |
| Sun. Jan. 31 | 7 | Partial pressure image; examiner report; warrant recoveries F-17–F-21; arrest warrant | Cross and Bell own search, seizure, intake, affidavit, and warrant | Sound; internal controls need R-03 |
| Mon. Feb. 1 | 8 | Recorded interview; premature phrase; counsel invocation; immediate stop; arrest; interim aftermath; consultant closure | Arrest warrant already exists; Cross executes it; no confession | Sound |

Time-of-day, winter light, opening/closing, travel, and evidence-availability transitions are otherwise coherent. No character possesses a fact before its authenticated reader-visible introduction.

# Mystery-fairness and clue-planting audit

| Material clue | First appearance / initial meaning | Later reinterpretation and source | Reader timing / expertise / explanation | Alternate fit and proportionality | Result |
|---|---|---|---|---|---|
| Alton's current natural hand | Ch. 1 catalog writing; ordinary age/pain variation | Chs. 3–4 verified current rhythm contrasts with constructed note | Reader sees before death; expert concept explained through Callie | Fits no suspect by itself; proportionate foundation | Fair |
| Older formal/public hand | Ch. 1 bench/public sample knowledge; looks like Alton | Ch. 3 explains why the note persuades and why old shape cannot prove current writer | Reader sees source set early; Callie explains currentness | Multiple suspects have access | Fair |
| Repeated lowercase `g` | Ch. 2 suspicious identical form | Ch. 4 repeated construction; Ch. 7 practice evidence | Reader sees before homicide turn; expert point made portable | Could initially fit Caleb or any skilled copier | Fair |
| Internal stops / ink concentrations | Ch. 4 magnified line behavior | Simulation assembled stroke by stroke; examiner corroborates Ch. 7 | Reader sees before warrant; clearly explained | Does not identify Nora alone | Fair |
| Anticipatory spacing | Ch. 4 next-letter spacing before stops | Planning rather than natural movement; later practice materials fit | Expert-dependent but explained | Could fit any practiced simulator | Fair |
| Selective tremor / pressure inconsistency | Ch. 4 artificial decline pattern | Examiner corroborates; contrasts with authentic fatigue | Reader-visible and explained | No sole identity value | Fair |
| Erased baseline guides | Ch. 4 faint guide residue | Ch. 7 practice preparation | Reader-visible before resolution | Could initially implicate Caleb's tools | Fair |
| Graphite and signature transfer | Ch. 4 signature-area traces | Ch. 7 transfer sheet and reversed signature recovery | Explained before search; examiner limit retained | Caleb remains a fair false solution until alibi/negative search | Fair |
| Exact note language | Ch. 2 vague fund naming and trust phrase | Ch. 8 premature reuse creates supporting guilty knowledge | Reader has full phrase chronology | Supporting, not confession or sole basis | Fair |
| Missing red portfolio | Ch. 1 guarded object; Ch. 2 absent | Ch. 5 unsigned restatement explained; Ch. 7 recovered by warrant | Reader sees absence and terms before arrest | Multiple family/estate motives remain possible | Fair |
| 8:47 p.m. voicemail | Ch. 5 authenticated future plan | Counters staged finality; supports timeline/motive | Reader sees before access narrowing | Does not identify killer | Fair |
| Unsigned restatement | Ch. 5 attorney-authenticated draft | Threat to Nora and audit plan; recovered Ch. 7 | Reader sees terms before search | Motive, not presence | Fair |
| Operative 2021 trust | Ch. 5 controlling estate instrument | Death preserves Nora's immediate authority and residue | Nonexpert explanation is clear | Motive applies strongly but not exclusively enough to solve alone | Fair |
| Removal / outside trustee / audit / redirected residue | Ch. 5 draft terms | Ch. 6 partial pressure support; Ch. 7 recovery | Reader sees full terms before pressure image | Motive, not authorship | Fair after R-03 control sync |
| Exact $286,400 path | Ch. 5 authenticated transfers | Chs. 6–8 cumulative motive/audit pressure | Exact amount repeated only where operationally useful | Gideon remains a fair financial suspect | Fair |
| Altered `8:05` | Ch. 5 preview; Ch. 6 controlled original examination | Backdated departure indication without erased time or altering hand | Limits stated explicitly | Could initially involve any hall-access person | Fair after R-02 |
| 9:14 assigned-code event | Ch. 6 authenticated electronic return | Contradicts departure narrative and narrows access | Reader sees limits: assigned code, not face | Innocent/borrowed-code alternatives remain possible at introduction | Fair |
| Scarf notation | Ch. 6 Tess's authenticated 7:50 household note | Contradicts Nora's stated reason for return | Simple, reader-visible contradiction | Does not prove study entry or murder | Fair |
| Medication-return ledger | Ch. 3 incomplete old-bottle path | Ch. 6 label match and proxy access clarify route | Reader sees long before warrant; limits repeated | Tess remains plausible until alibi; access is not administration | Fair |
| Scene bottle | Ch. 2 apparent overdose prop | Chs. 4 and 6 staging container, not fatal mechanism | Medical distinction is explicit | Does not identify placer | Fair |
| Pressure image | Ch. 6 ending / Ch. 7 handling | Partial support for removal / trustee / audit terms | Reader sees before warrant; source and limits explained | Does not identify writer/remover or locate missing document | Fair after R-03 |
| F-17 through F-21 | Ch. 7 warrant recoveries | Practice, transfer, models, restatement, medication envelope converge | Reader sees before interview/arrest | Cumulative, not magical; each has custody and location | Fair |
| Guilty-knowledge phrase chronology | Ch. 8 at 9:37:14 before Cross's 9:38 quotation | Supporting knowledge inconsistent with disclosed sequence | Reader hears exact order | Not confession; warrant already exists | Fair |
| Repair record and provenance limitation | Ch. 3 authenticated current sample with location limit | Ch. 8 exact provenance statement and non-dispositive endpoint | Reader sees limitation throughout | Not sole proof and not arrest basis | Fair |

**Fair-play conclusion:** A careful first-time reader can identify Nora before arrest by combining motive, late access, false return reason, medication route, simulation method, and warrant recoveries. The final solution does not depend on information withheld from Callie, a magical expert leap, or a late-added fact.

# Suspect-balance audit

| Suspect | Credibility / pressure | Access and capability | Separate wrongdoing | Alibi timing | Balance result |
|---|---|---|---|---|---|
| Nora | Highly credible preservation leader; exact competence reads as real work before it reads as control | Family/administrative access, handwriting models, medication and side-door routes | Financial manipulation, evidence removal, staging preparation | Not cleared; cumulative field narrows late | Properly concealed without being arbitrary |
| Claire | Estranged daughter with inheritance and family-paper grievance | Family routes and decades of correspondence | Unauthorized removal of her mother's letters | Independently cleared for critical window in Ch. 6 | Suspicion meaningful, innocence not signaled too early |
| Gideon | Contractor under audit and debt pressure; real work visible | Site familiarity and current correction records | Overruns and manipulated/revised descriptions | Independently cleared in Ch. 6 by timecards, fuel record, and witnesses | Financial red herring remains consequential |
| Tess | Longtime house manager with home/place at stake | Household keys, medicine records, tray routine | Incomplete medication handling and concealed minor lapses | Independently cleared by preserved gate-cottage movement record | Strong early access suspicion, humane reframing |
| Caleb | Skilled curator with copying tools and proprietary habits | Formal-hand images, tracing tissue, graphite transfer | Folio removal and provenance substitution | Independently cleared by 8:23 courier scan and shop camera | Strongest false-forger path remains fair |

**Balance conclusion:** No suspect needs a new secret, alibi weakness, suspicious beat, or exculpatory fact. R-04 only removes unsupported planning residue.

# Legal and procedural audit

| Area | Finding | Repair needed |
|---|---|---|
| Scene access | Cross preserves the apparent-suicide scene and controls Callie's entry | No |
| Consultant authorization | Written, case-specific, amended only for narrow tasks, closed at end | No |
| Consent / production | House, foundation, shop, medication, and work-material productions are distinguished | No |
| Original vs. working/display copies | Originals, images, copies, scales, sleeves, and movement logs remain distinct | No |
| Evidence handling | Bell owns photography, logs, packaging, display lanes, intake, and search returns | No |
| Electronic authentication | Provider certification, synchronized clock, code-assignment list, and stated limits are present | R-02 wording only |
| Medical reporting | Incapacitation and smothering are independent of handwriting identification | No |
| Estate materials | Pruitt controls privilege and authenticates legally available terms | No |
| Examiner submission | State examiner corroborates simulation but does not identify Nora | No |
| Search warrant | Scope is targeted to missing estate materials, writing preparation/transfer, and medication-route evidence | No |
| Warrant recoveries | Locations and F-17–F-21 intake are recorded; Callie does not search or seize | No |
| Arrest warrant | Cumulative probable cause exists before the Chapter 8 interview | No |
| Recorded interview / rights | Recording and rights precede substantive questioning | No |
| Counsel invocation | Clear invocation; questioning stops immediately | No |
| Arrest execution | Cross executes the preexisting warrant; no confession, struggle, or inference from silence | No |
| Interim civil consequences | Trust, probate, and foundation measures remain temporary/interim | No |

**Authority conclusion:** Cross owns official decisions, questions, warrants, synthesis, arrest, and charging language. Bell owns custody and intake. Callie supplies narrow documentary observations only.

# Evidence-stream audit

| Proof stream | What it proves / supports | What it does not prove | Limit placement | Result |
|---|---|---|---|---|
| Medical cause and manner | Nonfatal incapacitation followed by smothering; homicide | Killer identity or note authorship | Chs. 4, 6, 8 | Sound |
| Medication access and staging route | Old bottle remained available; label/number and proxy route connect the container path | Who administered tablets, when bottle left, or who staged it | Chs. 3, 6, 8 | Sound |
| Document simulation method | Constructed forms, stops, spacing, tremor/pressure mismatch, guides, graphite, transferred signature | Writer identity by handwriting alone | Chs. 4, 6, 7, 8 | Sound |
| Estate and trust motive | Nora's benefit and threatened removal / independent control / audit / redirected residue | Presence, authorship, or murder | Chs. 5, 6, 8 | Sound |
| Financial and audit pressure | Exact $286,400 path and Nora authorizations; Gideon exposure | Physical presence or killing act | Chs. 5, 6, 8 | Sound |
| Timeline and access | Altered displayed exit; 9:14 assigned-code event; false return reason; other alibis | Erased time, visual identity, duration, or acts inside | Ch. 6 | R-02 clarifies |
| Pressure image | Partial removal / independent-trustee / audit terms | Full source document, writer, remover, portfolio route, or location | Chs. 6–7 | R-03 syncs controls |
| Search-warrant recoveries | Preparation, transfer, source models, removed restatement, and medication-return evidence in specified locations | Confession or scientific shortcut | Ch. 7 | Sound |
| Guilty knowledge | Premature knowledge of an exact phrase supports the cumulative case | Confession or independent arrest basis | Ch. 8 | Sound |
| Repair-record authentication and provenance | Genuine recent natural sample; exact finding record and real location limit | Complete prior location, writer identity, or necessary arrest proof | Chs. 3, 4, 7, 8 | Sound |

# POV and character-continuity audit

## Callie-only POV

- No scene enters another character's unexpressed thoughts.
- Demeanor is repeatedly treated as observable but not proof.
- Legal, medical, and scientific conclusions remain with Cross, Bell, Pruitt, Arledge, the examiner, or authenticated records.
- Narration stays inside Callie's perception, memory, inference, and self-correction.
- No required POV repair is identified.

## Callie's Book 5 movement

The complete arc is present and sequential:

1. public requests initially feel flattering;
2. expertise is confident but does not become premature certainty;
3. Bell, Cross, Mae, Eli, Pruitt, and the examiner hold distinct parts of proof;
4. procedure becomes protection rather than obstruction;
5. usefulness is recognized as a substitute for belonging and rest;
6. `NOT TODAY` becomes an accepted practical limit;
7. the route limitation is accepted without enlarging it into a new mystery;
8. Callie closes the case file.

## Recurring cast

- **Cross:** restrained, procedural, non-romantic, and fully responsible for official action.
- **Mae:** practical care, permission, work, and boundary; no coercive reconciliation.
- **Eli:** ordinary competence, bounded work, no over-solving, no reader-facing disclosure.
- **Result:** No reader-facing character-continuity repair is required.

# Repetition review

## Mechanical findings

Mechanical searches and full-draft review identified recurring clusters around:

- `exact`, `separate`, `ordinary`, `controlled`, and `remained`;
- proof-limit formulations such as `does not prove`, `did not establish`, and `not [X]` sequences;
- folders, seals, photographs, scales, blank fields, and movement logs;
- hands held back, folded, or placed outside a marked boundary;
- Cross's hat and Bell's camera;
- three-part lists and parallel negative definitions;
- usefulness, belonging, proof, route, ownership, and portable record language.

## Close-reading classification

- **Necessary legal/evidentiary restatement:** frequent but functional in Chapters 4, 6, 7, and 8.
- **Useful thematic echo:** hands, routes, labels, empty spaces, and ownership.
- **Reader-orientation recap:** strongest at the openings of Chapters 4, 6, 7, and 8; proportionate for a procedural mystery.
- **Accidental redundancy:** present at line-polish scale, not at continuity-revision scale.
- **Over-explanation materially harming suspense:** not found.

No repeated paragraph, duplicated scene, or contradictory evidence recap was identified. Broad repetition reduction is therefore deferred rather than forced into this pass.

# Pacing audit

- **Chapter 1:** Efficient social and documentary setup; death arrives after enough current-hand and suspect planting. R-01 improves the overnight handoff.
- **Chapter 2:** Apparent-suicide problem turns on one precise anomaly without solving too soon.
- **Chapter 3:** Deliberately methodical comparison architecture; multiple suspects and custody rules justify the length.
- **Chapter 4:** Technical demonstration earns the homicide turn; no acceleration needed.
- **Chapter 5:** Trust and financial exposition remains active through authenticated documents and Cross's limits.
- **Chapter 6:** Strong narrowing chapter; R-02 prevents a false causal shortcut.
- **Chapter 7:** Warrant synthesis is cumulative and calm; no thriller escalation.
- **Chapter 8:** Interview, invocation, arrest, aftermath, and emotional closure are proportionate; no confession or villain speech.

The book maintains quiet procedural pressure. No scene needs relocation, new action, or chapter restructuring.

# Atmosphere and prose audit

- Winter light, old snow, shop wood, folders, graphite, seals, labels, tea, and hands create a coherent sensory system.
- Emotional meaning arrives through work, objects, and restrained physical action rather than speechifying.
- Technical explanation is intelligible to a nonexpert reader without reducing the evidence to magic.
- Dialogue voices remain differentiated: Cross clipped and procedural; Mae practical; Nora controlled; Tess dry; Caleb technical; Gideon blunt; Claire possessive; Eli careful.
- Metaphor density is controlled and consistent with the established series voice.
- No Gothic excess, cutesy banter, supernatural certainty, or living-author imitation is present.
- The ending is earned and must remain exactly intact.

# Locked elements preserved by this plan

The revision will not change:

- Nora Mercer Shaw as murderer;
- motive, murder method, staged bottle, or simulated-note method;
- older formal/public models, erased guides, constructed forms, difficult joins, or transferred signature;
- operative 2021 trust versus unsigned/unexecuted restatement;
- approximate $2.4 million residue, immediate successor authority, outside trustee, audit, redirected residue, or $286,400 path;
- 8:47 voicemail, altered `8:05`, 9:14 assigned-code event, scarf contradiction, medication route, pressure image, or F-17–F-21 recoveries;
- examiner non-identification limit;
- cumulative arrest basis established before interview;
- guilty-knowledge order, counsel invocation, immediate stop, arrest execution, or no-confession structure;
- interim trust/foundation consequences and separate outcomes for Claire, Tess, Gideon, and Caleb;
- consultant closure, Mae's `NOT TODAY` boundary, or bounded visible Eli conduct;
- exact provenance statement;
- non-dispositive provenance limitation;
- final image and final line, `She closed the file.`

No DNA, fingerprints, residue testing, surveillance, phone-record shortcut, new witness, new confession, villain monologue, chase, struggle, threat, hostage event, escape attempt, decisive new document, or overt later-series hook will be added.

# Implementation batches

## Batch 1 — Reader-facing required repairs

1. Revise Chapter 1 transition per R-01.
2. Revise Chapter 6 transition per R-02.
3. Update both chapter frontmatter statuses and actual manuscript-prose word counts.

## Batch 2 — Internal continuity controls

1. Apply R-03 to outline, timeline, and clue ladder.
2. Apply R-04 to suspect matrix and selected character files.
3. Do not modify story memory unless a reader-visible continuity fact changes materially; these repairs do not require such a change.

## Batch 3 — Trackers

1. Recount all eight chapters.
2. Mark all chapters revised and revision complete in Book 5 progress.
3. Update manuscript README with revised counts and remaining pending stages.
4. Synchronize the Book 5 status line in the series outline.
5. Leave root progress unchanged unless validation reveals a repository convention requiring otherwise.

## Batch 4 — Full reread and validation

Reread Chapters 1–8 in order after all edits, then validate:

- all eight files and frontmatter fields;
- YAML parseability and arithmetic;
- Monday Jan. 25 through Monday Feb. 1 chronology;
- Callie-only POV;
- clue order and fair-play solvability;
- five-suspect balance;
- authority division and custody;
- all ten proof-stream limits;
- trust/restatement distinction;
- medical method and medication route;
- exact financial total;
- access sequence and pressure-image limit;
- F-17 through F-21 locations;
- guilty-knowledge ordering;
- rights, counsel invocation, immediate stop, warrant authority, and no confession;
- aftermath scope, consultant closure, public-overdependence endpoint, Mae's boundary, and bounded visible Eli conduct;
- exact provenance statement and non-dispositive status;
- protected-information exclusion;
- exact ending;
- repeated paragraphs, phrase clusters, placeholders, and merge markers;
- changed-file scope, blob hashes, and final diff.

# Acceptance criteria

The revision is complete only when:

- R-01 through R-05 are implemented;
- no optional item is silently expanded into a plot or architecture change;
- every changed chapter matches this plan;
- chapter and total counts are exact;
- revision trackers are accurate;
- full-manuscript reread finds no new contradiction;
- final diff contains no Books 1–4 production, export, package, release, or listing changes;
- the branch is committed and an unmerged pull request is opened against `main`.

# Deferred next-stage scope

After this revision pull request is reviewed and merged, the appropriate next stage is **Book 5 — Complete Line Editing, Voice Consistency, and Prose Polish**. That pass may address low-risk rhythm, local repetition, dialogue cadence, transition smoothness, paragraph movement, atmosphere density, and technical intelligibility, but it must not alter plot, clue order, legal structure, evidence limits, protected continuity, or the ending.
