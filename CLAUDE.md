# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not a software project** — it's a fiction production repository for *The Blackwood Ridge Mysteries*, an 8-book cozy mystery series (author pen name: Vesper Blythe). The repo tracks a structured, gated content pipeline for each book: concept → bible → outline → draft → revision → line edit → polish → proofread → export → package → cover → listing → upload → publish. "Code" in this repo consists almost entirely of small Python export/validation scripts that assemble and QA manuscript files for ebook/print release; there is no application logic, server, or user-facing software.

Treat prose files (`.md` manuscripts, bibles, outlines) as the actual deliverable. Treat YAML `progress.yaml`/`novella.yaml` files as authoritative state — always check them before assuming a book's stage.

## Repository layout

- `series.yaml`, `series-outline.md`, `progress.yaml` — series-level metadata and per-book status (`published`, `upload_ready`, `in_progress`, `planned`).
- `series-bible/` — canonical cross-book continuity: `premise.md`, `world.md`, `timeline.md`, `story-memory.md` (recurring motifs/objects), `voice-dna.md` (prose style rules), `recurring-characters/*.md`.
- `books/book-NN/` — one directory per book, numbered `01`–`08`. Each contains a subset of:
  - `novella.yaml` / `progress.yaml` — book-level metadata and the detailed per-chapter production ledger (git blob hashes, word counts, revision dispositions per stage).
  - `bible/` — book-specific continuity docs: `mystery-solution.md`, `suspect-matrix.md`, `clue-ladder.md`, `timeline.md`, `character-arcs.md`, `continuity-locks.md`, `carry-forward.md`, `characters/*.md`, `locations/*.md`.
  - `control/chapter-NN-mission-lock.md` — the authoritative pre-writing spec for a single chapter: dominant function, opening state, objectives, success/failure conditions, a strict knowledge/evidence boundary (what the POV character may/must-not know yet), and locked scene architecture. Newer books (6, 7) use this format instead of a single outline for chapter-level control.
  - `manuscript/ch-NN.md` — the actual chapter prose (source of truth for word counts and content).
  - `outline.md`, `content-notes.md`, `revision-plan.md` — outline-stage and revision-stage planning documents.
  - `export/` — Python scripts and generated artifacts for the reader-facing build (see below).
  - `front-matter/`, `back-matter/`, `package/`, `publication/`, `listing/`, `dist/`, `revision/` — later-pipeline artifacts (varies by book depending on how far it has progressed).
  - `README.md` — per-book status snapshot: production state, current story state, and an explicit **production boundary** stating what work is and isn't authorized next. Read this first when picking up work on a book.

## Working within the pipeline

- **Respect stage gating.** Each book's `README.md` ends with a "Production boundary" section stating exactly what the next authorized action is (e.g., "Chapter 2 may be created only in the dedicated Book 7 Chapter 2 mission lock and drafting task"). Do not skip ahead to later stages (export, package, cover, publish) or draft chapters that haven't had a mission lock written.
- **Mission locks are contracts.** When drafting a chapter, follow its `control/chapter-NN-mission-lock.md` exactly — especially the "Callie must not know" boundary and "failure conditions." These exist to prevent premature reveals and preserve future-book twists (e.g., Eli Townsend's curator role must stay hidden until Book 7).
- **Continuity locks are non-negotiable.** `bible/continuity-locks.md` and the series-bible's `story-memory.md` encode facts that must never contradict earlier books (e.g., "Callie and Cross do not become unrestricted partners"). Cross-check before writing scenes involving established relationships, evidence rules, or character capabilities.
- **Voice DNA governs all prose.** `series-bible/voice-dna.md` defines sentence texture, POV diction per character, sensory palette, and an explicit list of **banned generic patterns** (mystery-thriller clichés, cozy-cuteness overload, info-dumping, over-explained emotion, purple prose, Southern caricature). Any prose written or edited in this repo should be checked against this document.
- **`progress.yaml` files are ledgers, not just status flags.** They record git blob hashes and word counts per chapter per stage (accepted → revised → line-edited → polished → proofread). When a stage completes, the expectation is that most chapters are `reviewed_unchanged` and only chapters with real issues are `changed`/`corrected` — wholesale rewrites at late stages (line edit, polish, proofreading) are against the established pattern here.

## Book-production skills and agents

This repo is normally driven through the specialized book-pipeline skills and agents already available in this environment (do not reimplement their logic manually):

- Skills: `book-genesis` / `book-genesis-full` / `book-genesis-codex` (end-to-end pipeline), `narrative-foundation`, `voice-fingerprint`, `prose-craft`, `prose-de-tell`, `entity-tracker`, `continuity-guardian`, `beta-reader`, `editorial-package`, `production-prep`, `series-architect`, `manuscript-manager` (session state), `reader-persona`.
- Agents: `book-architect` (blueprints/outlines, never final prose), `book-writer` (drafts one chapter at a time from a mission lock), `book-disruptor` (breaks predictability/adds human noise), `book-editor` (surgical revision from evaluator feedback), `book-evaluator` (scores chapters it didn't write), `book-researcher` (market/comps), `book-packager` (editorial package + production prep), `book-orchestrator` (runs the full pipeline autonomously, pausing at human checkpoints).

Prefer invoking these over ad hoc prose generation, since they encode the pipeline's quality gates (Genesis Score, anti-AI pattern scan, 4-reader simulation, adversarial continuity checks).

## Export pipeline (the actual "code" in this repo)

Each book past drafting has a `books/book-NN/export/` directory with a near-identical Python toolchain:

- `assemble-manuscript.py` — concatenates `manuscript/ch-NN.md` files into a single reader-facing Markdown source without retyping prose.
- `finalize-package.py` — verifies the accepted git blob/word-count baseline, generates front/back matter, renders DOCX/EPUB/TXT/HTML, runs EPUBCheck, enforces scope (no unrelated files touched), and writes reports.
- `run-export.py` — the full controlled build entry point; applies known sentinel/metadata normalization fixes for byte-stable rebuilds.
- `build.sh` — thin wrapper: `python3 run-export.py`.
- `test_finalize_package_scope.py` (book-06+) — unit test guarding that the export script only touches its declared file scope.

### Common commands

Run a book's controlled export build (from repo root):
```bash
python books/book-06/export/run-export.py
```

Run the export scope-safety test (where present):
```bash
python -m unittest books/book-06/export/test_finalize_package_scope.py
```

Generated outputs land in `export/dist/` (DOCX/EPUB/manifest) and `export/qa/` (DOCX render pages, PDF, contact sheets) — both gitignored locally but uploaded as CI artifacts. Canonical, committed review sources are `export/manuscript-combined.{md,txt,html}` plus `export-readiness.md`, `word-count-report.md`, `validation-report.md`, and `../export-report.md`.

Required system dependencies for a full export build (installed in CI, needed for local runs): `pandoc`, `libreoffice`, `poppler-utils`, `fonts-liberation`, `epubcheck`, and Python packages `PyYAML`, `beautifulsoup4`, `python-docx`, `Pillow`, `pypdf`.

### CI workflows (`.github/workflows/`)

Each book in export/release stages has its own workflow (`book-NN-proof-export.yml`, `book-NN-release-package.yml`), scoped by `paths:` filters to that book's directory. These:
1. Run the export scope test.
2. Run the controlled build script, tee output to `build.log`.
3. Print the generated readiness/validation/word-count/export reports.
4. On push or same-repo PRs, commit the regenerated stable reader-facing artifacts back to the branch.
5. Upload DOCX/EPUB/manifest/QA artifacts (30-day retention) and full diagnostics (7-day retention, `if: always()`).

When editing a book's export scripts, keep them scoped to that book's `books/book-NN/**` path — cross-book export logic is deliberately duplicated per book rather than shared, since each book's workflow and scope validator asserts exclusive ownership of its own directory.
