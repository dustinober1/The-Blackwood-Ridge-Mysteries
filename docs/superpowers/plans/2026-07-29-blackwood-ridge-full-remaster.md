# Blackwood Ridge Full Series Remaster Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remaster all eight Blackwood Ridge Mysteries ebook editions, complete Books 7–8, create one coordinated cover set, and produce validated upload packages without external publishing.

**Architecture:** Work title-by-title inside the existing gated book pipeline, preserving every pre-remaster baseline and recording each substantive prose or design decision. Finish Books 7–8 only after their canon and mission-lock gates are complete; standardize all eight ebook packages and validate them through a final series matrix.

**Tech Stack:** Markdown prose and YAML ledgers; repository Python export/validation tools; EPUB/DOCX/HTML/TXT generation already used by each book; raster cover assets; Git provenance and reports.

## Global Constraints

- Deliverable scope is eight ebook editions only; no print interiors, retailer uploads, distribution, or publication.
- The series bible, book bibles, mission locks, timelines, story memory, continuity locks, and voice DNA are authoritative.
- All accepted pre-remaster manuscripts and covers must remain recoverable as legacy baselines.
- No locked killer, motive, method, evidence boundary, character arc, relationship boundary, or Book 8 reservation may change without a written continuity decision.
- Book 7 must complete Chapter 5–8 mission locks and drafts before whole-draft editing.
- Book 8 must be architected from the series bible and the final Book 7 ending state before drafting.
- All eight remastered covers share typography, hierarchy, series branding, palette family, dimensions, and thumbnail legibility.
- Every finished title needs a validated EPUB, cover, metadata, listing copy, upload worksheet, manifest, and readiness report.

---

### Task 1: Freeze baselines and create the remaster control ledger

**Files:**
- Create: `docs/remaster/series-remaster-ledger.yaml`
- Create: `docs/remaster/legacy-baselines.md`
- Create: `docs/remaster/change-log.md`
- Modify: `.gitignore` to ignore `.superpowers/` only if it is not already ignored

**Interfaces:**
- Consumes: `series.yaml`, root `progress.yaml`, all `books/book-*/progress.yaml`, Git blob history, existing cover/package artifacts.
- Produces: immutable baseline hashes, title-level status fields, and a change-log format used by every later task.

- [ ] **Step 1: Record current repository state**

  Capture the current commit, branch, dirty files, and all eight title directories in `docs/remaster/legacy-baselines.md`. Treat the pre-existing `.DS_Store` modification as unrelated user work and do not stage it.

- [ ] **Step 2: Record manuscript and cover baselines**

  For each existing manuscript chapter and cover, record path, Git blob/object identity, byte size, pixel dimensions where applicable, and current progress stage. Record Book 8 as an unscaffolded planned title.

- [ ] **Step 3: Define the ledger schema**

  Add one YAML entry per book with fields `book`, `title`, `baseline_commit`, `baseline_paths`, `editorial_status`, `cover_status`, `export_status`, `package_status`, `upload_ready`, and `blocking_findings`. Add a `series_audit` section with eight required passing rows.

- [ ] **Step 4: Verify baseline capture**

  Run a script or shell audit that confirms every existing manuscript and cover path in the ledger exists and that no legacy path is scheduled for destructive replacement.

- [ ] **Step 5: Commit the control ledger**

  Commit only the new remaster control documents and the narrowly scoped `.gitignore` rule, leaving unrelated user changes unstaged.

### Task 2: Establish the unified editorial and ebook specification

**Files:**
- Create: `docs/remaster/editorial-standard.md`
- Create: `docs/remaster/ebook-standard.yaml`
- Modify: `series-bible/voice-dna.md` only if the audit finds a real contradiction; otherwise record no change

**Interfaces:**
- Consumes: approved design spec and all series-bible documents.
- Produces: exact prose-audit rubric, metadata fields, EPUB requirements, spoiler rules, and cover handoff fields.

- [ ] **Step 1: Translate voice and continuity rules into a checklist**

  Include POV, sentence texture, sensory palette, banned-pattern scan, cozy-mystery promise, evidence limits, Cross boundary, Eli chronology, Mae relationship progression, and Book 8 reservations.

- [ ] **Step 2: Define ebook metadata and package fields**

  Specify exact title, series name, book number, author, language, description, identifiers where present, cover filename, EPUB filename, manifest keys, and upload worksheet fields.

- [ ] **Step 3: Define validation thresholds**

  Specify EPUB structural checks, navigation checks, internal-link checks, image constraints, metadata equality checks, filename checks, thumbnail cover checks, and no-reader-facing-spoiler checks.

- [ ] **Step 4: Review for contradictions**

  Compare the new standard against the repository’s existing export scripts and reports; record any required adapter work in `docs/remaster/change-log.md`.

- [ ] **Step 5: Commit the standards**

  Commit the editorial and ebook standards with a message identifying the remaster contract.

### Task 3: Audit and remaster Books 1–2

**Files:**
- Modify: `books/book-01/**` only within existing manuscript, export, package, listing, and metadata conventions
- Modify: `books/book-02/**` only within existing manuscript, export, package, listing, and metadata conventions
- Create: `books/book-01/remaster/` reports and baselines
- Create: `books/book-02/remaster/` reports and baselines

**Interfaces:**
- Consumes: Tasks 1–2 and existing published EPUB/package artifacts.
- Produces: remastered manuscripts or documented unchanged decisions, remastered covers, rebuilt ebook packages, and passing title readiness reports.

- [ ] **Step 1: Run title-level editorial audits**

  Review every chapter against the editorial standard, compare against the series bible, and record each finding with severity, exact location, proposed correction, and continuity impact.

- [ ] **Step 2: Apply only approved evidence-based corrections**

  Preserve the published plot and locked solution; make documented changes for objective continuity, mechanical, clarity, or ebook defects. Record unchanged chapters explicitly.

- [ ] **Step 3: Create standardized covers**

  Produce one cover per title using the unified eight-book cover specification and title-specific archival imagery. Preserve the existing published covers in the legacy location or baseline record.

- [ ] **Step 4: Rebuild and validate each EPUB**

  Use each book’s existing controlled export tool, adapt metadata/front/back matter to the ebook standard, inspect the rendered result, and save a title-level readiness report.

- [ ] **Step 5: Update ledgers and commit**

  Mark Books 1–2 remaster, cover, export, package, and upload fields only after all checks pass; commit title-scoped changes.

### Task 4: Audit and remaster Books 3–6

**Files:**
- Modify: `books/book-03/**`, `books/book-04/**`, `books/book-05/**`, `books/book-06/**` within their existing scoped pipelines
- Create: `books/book-03/remaster/` through `books/book-06/remaster/` audit and provenance reports

**Interfaces:**
- Consumes: Tasks 1–2 and the four existing manuscripts, release artifacts, cover approvals, and export validators.
- Produces: four remastered title packages and reports satisfying the same standard as Books 1–2.

- [ ] **Step 1: Audit existing release artifacts before editing prose**

  Verify each manuscript-to-export mapping, current word counts, cover provenance, metadata, series links, package manifests, and existing validation reports. List objective failures first.

- [ ] **Step 2: Perform controlled editorial remaster passes**

  Run developmental, continuity, mystery-fairness, prose, mechanical, and spoiler audits. Revise only supported findings, preserving accepted baselines and recording all changes.

- [ ] **Step 3: Rebuild the four covers**

  Create standardized covers for *The Challenger*, *The Archive Fire*, *The Planted Page*, and *The Pattern*, with title-specific objects and consistent series treatment. Preserve approved legacy sources.

- [ ] **Step 4: Rebuild each ebook package**

  Run the book-scoped export and release tools, resolve validation failures, inspect rendered EPUB/HTML/DOCX outputs where the pipeline provides them, and write readiness reports.

- [ ] **Step 5: Commit in title-scoped groups**

  Commit each title only after its package and cover checks pass, then update the series remaster ledger.

### Task 5: Complete Book 7 — The Reckoning

**Files:**
- Modify: `books/book-07/control/`, `books/book-07/manuscript/`, `books/book-07/progress.yaml`, `books/book-07/README.md`
- Create: Book 7 revision, line-edit, polish, proofreading, export, package, listing, and cover artifacts following the Book 6+ conventions

**Interfaces:**
- Consumes: Book 7 premise, bibles, Chapters 1–4, and the series-bible constraints.
- Produces: an accepted eight-chapter manuscript, complete editorial ledger, standardized cover, validated EPUB, and upload package.

- [ ] **Step 1: Write and lock Chapter 5 mission lock**

  Use the existing Book 7 outline, ending state, evidence limits, and `next_task` entry to create the dedicated mission lock for **A Catalog for No One**. Include exact opening state, objectives, forbidden knowledge, scene architecture, and success/failure conditions.

- [ ] **Step 2: Draft and accept Chapter 5**

  Draft to its ledger target, run the chapter evaluator and continuity checks, correct only supported findings, and record formal acceptance.

- [ ] **Step 3: Repeat mission-lock and draft gates for Chapters 6–8**

  Create each lock before its prose. Preserve the locked separation between Vivienne’s homicide and Eli’s curation, end with Eli alive and the Book 8 warning available, and update the ledger after each accepted chapter.

- [ ] **Step 4: Run Book 7 whole-draft editorial passes**

  Audit continuity, mystery fairness, suspect balance, procedure, evidence limits, POV, pacing, repetition, voice, mechanics, and reader-facing spoilers. Apply controlled revisions with chapter-level dispositions and blob/count evidence.

- [ ] **Step 5: Export and package Book 7**

  Create standardized front/back matter, listing copy, EPUB, manifest, upload worksheet, readiness report, and remastered cover. Validate rendered output and update `progress.yaml` only after passing checks.

### Task 6: Architect and complete Book 8 — The Last Margin

**Files:**
- Create: `books/book-08/` with premise, README, progress ledger, bibles, outline, mission locks, manuscripts, export, package, listing, and remaster reports
- Modify: series-bible handoff/timeline/story-memory files only for approved Book 8 continuity facts

**Interfaces:**
- Consumes: final accepted Book 7 ending state, series outline, series bible, and Book 7 carry-forward documents.
- Produces: a complete eight-chapter Book 8 manuscript and upload-ready ebook package.

- [ ] **Step 1: Write the Book 8 premise and continuity handoff**

  Lock the final warning, the future murder, Callie’s final trust decision, shared-reading resolution, and the non-negotiable ending target: Callie stays, keeps the shop and glass, and reads differently.

- [ ] **Step 2: Build the Book 8 mystery architecture**

  Create the mystery solution, suspect matrix, clue ladder, timeline, character arcs, continuity locks, and eight-chapter outline. Keep Eli alive, preserve Callie’s agency, and reserve no unresolved requirement outside the designed ending.

- [ ] **Step 3: Draft and accept Chapters 1–8 through mission locks**

  Create each mission lock before drafting; evaluate each chapter for evidence boundaries, fair clues, voice, pacing, and chapter-target compliance; record acceptance and exact word counts.

- [ ] **Step 4: Run the full Book 8 editorial pipeline**

  Perform controlled whole-draft revision, line edit, prose polish, proofreading, and reader-facing-spoiler review with dispositions and provenance records.

- [ ] **Step 5: Export and package Book 8**

  Produce standardized cover, metadata, front/back matter, EPUB, listing copy, upload worksheet, manifest, rendered inspection, and title readiness report.

### Task 7: Create and approve the coordinated eight-cover set

**Files:**
- Create: `docs/remaster/cover-system.md`
- Create: `docs/remaster/cover-contact-sheet.*`
- Create/modify: one approved cover asset and provenance record per `books/book-01/` through `books/book-08/`

**Interfaces:**
- Consumes: title imagery requirements from each completed manuscript and the ebook standard.
- Produces: eight technically valid, visually unified ebook covers and a cover QA report.

- [ ] **Step 1: Define the cover system**

  Record exact canvas dimensions, safe margins, series mark, title/author hierarchy, font choices, palette, border treatment, image treatment, file format, and thumbnail test procedure.

- [ ] **Step 2: Create title-specific compositions**

  Produce covers for all eight titles with no plot spoilers beyond retailer-safe premise cues. Ensure each title’s object/setting is distinct and text is readable against the image.

- [ ] **Step 3: Run visual and technical QA**

  Check pixel dimensions, color mode, file integrity, legibility at thumbnail size, title/author spelling, book number, series name, and match to package metadata.

- [ ] **Step 4: Preserve provenance and approve**

  Record source/editing provenance, final hashes, and approval status; keep legacy covers recoverable and link each final asset from the remaster ledger.

### Task 8: Standardize and rebuild all eight ebook packages

**Files:**
- Modify: each `books/book-*/export/`, `front-matter/`, `back-matter/`, `listing/`, `package/`, and `publication/` area as required by the existing title pipeline
- Create: `docs/remaster/series-metadata.yaml`
- Create: `docs/remaster/package-schema.yaml`

**Interfaces:**
- Consumes: completed manuscripts, covers, editorial reports, and title metadata.
- Produces: eight reproducible, consistently named upload packages.

- [ ] **Step 1: Define canonical metadata once**

  Record the eight exact titles, book numbers, series name, author, language, descriptions, file names, cover hashes, and series sequencing in `series-metadata.yaml`.

- [ ] **Step 2: Normalize package structure and front/back matter**

  Apply the same reader-facing structure and series links while keeping title-specific content and avoiding internal spoilers.

- [ ] **Step 3: Run title-scoped controlled exports**

  Execute each existing export pipeline, adapt only within its declared scope, and regenerate reader-facing Markdown/TXT/HTML/DOCX/EPUB artifacts where supported.

- [ ] **Step 4: Build upload manifests**

  Generate one manifest and upload worksheet per title listing exact file names, hashes, metadata, cover, EPUB, and validation results.

### Task 9: Run final validation and series audit

**Files:**
- Create: `docs/remaster/validate_series_remaster.py`
- Create: `docs/remaster/final-series-audit.md`
- Modify: `docs/remaster/series-remaster-ledger.yaml`

**Interfaces:**
- Consumes: all eight title packages, reports, manifests, covers, metadata, and progress ledgers.
- Produces: a machine-checkable and human-readable proof that all eight titles are upload-ready.

- [ ] **Step 1: Implement the series matrix checks**

  Check exactly eight titles, unique book numbers 1–8, exact title/author/series consistency, required package files, cover dimensions, EPUB existence, manifest hashes, and readiness-report presence.

- [ ] **Step 2: Run every book’s repository validator**

  Execute each available export scope test, package validator, EPUB check, and rendered-output inspection. Record command, date, result, and artifact path.

- [ ] **Step 3: Run spoiler and continuity checks**

  Confirm retailer copy/front matter contains no internal-series spoilers and that final Book 7/8 facts do not contradict the series bible or earlier locked solutions.

- [ ] **Step 4: Complete the final audit report**

  Fill one passing row per book with manuscript, cover, EPUB, metadata, package, and validation evidence. Any failed row blocks completion.

- [ ] **Step 5: Commit the completed remaster**

  Commit only after all eight rows pass and `git diff --check` is clean. Leave unrelated user changes untouched.

---

## Plan self-review

- **Spec coverage:** Editorial rules are covered by Tasks 2–6; coordinated covers by Task 7; ebook/package requirements by Task 8; completion evidence by Task 9; legacy preservation by Task 1.
- **Placeholder scan:** No `TBD`, `TODO`, “implement later,” or undefined cross-task function names are used.
- **Type and path consistency:** All tasks use the repository’s existing `books/book-01` through `books/book-08` structure and the shared remaster documents under `docs/remaster/`.
- **Scope check:** The plan is intentionally sequential at the title-gate level; Books 7 and 8 are separate creative subsystems but share the same editorial and package contracts, so each has its own independently testable task.

