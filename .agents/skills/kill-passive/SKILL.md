---
name: kill-passive
description: Hunt avoidable passive voice across a chapter and convert to active voice for clarity and authority (parallel focused workers, edits in place). Targets "is/are/was/were [past participle] by", "has been [past participle]", and "gets [past participle]". Use when user says "kill-passive", "kill passive voice", "make it active", or "convert passive to active".
metadata:
  author: Nonfiction Toolkit
  version: "1.0.0"
  category: nonfiction-editing
---

# Kill the passive — name the actor, own the action

Non-fiction is an argument: the reader wants to know who did what and why. Passive
voice hides the actor, and the model hides actors by the dozen — "the decision was
made," "mistakes were made," "it was determined," "the data were analyzed," "X gets
measured by." Each one is a small retreat from responsibility and clarity. The fix
is not to ban passive but to convert the avoidable ones: promote the actor to the
subject, or state the actor explicitly.

The request arguments = the chapter file(s): a path, a file pattern, or several
paths. Resolve it to a concrete file list before doing anything (skip files whose
passive hit count is zero).

## What to keep vs. fix

**KEEP (do not touch):**
- **Actor genuinely unknown or irrelevant** where passive is the clearer option:
  "the chamber was sealed," "the samples were stored at -80°C," "the model was
  fit with…" — the actor is either not the point or genuinely unavailable.
- **Field-standard / disciplinary convention** where passive is the norm (e.g.,
  methods sections, some social-science writing) — check the project's style guide
  and audience assumptions; when the field owns the passive, keep it.
- **Active "get" that is literal, not a passive disguise** ("he gets paid," "the
  system gets a lot of use") and idiomatic uses of "gets" ("it gets to the heart
  of the matter").
- **Quoted speech / cited material** where the source uses passive and changing it
  would mis-quote.

**FIX (rewrite to active):**
- **Nameless-agent passives** where the actor is suppressible and known: "mistakes
  were made," "the decision was made," "it was agreed," "X was rejected," "the
  change was implemented" — name the actor ("the committee made the decision," "we
  rejected the change").
- "**X gets [past participle]**" as a passive euphemism ("the issue gets
  overlooked," "the data gets cleaned") — convert to active ("reviewers overlook
  the issue," "we clean the data").
- "**has been / have been [past particle]**" used to park the actor at the end or
  hide it: "a mistake has been identified" → "we identified a mistake."
- **Repetition:** the same actor-hidden construction twice within a few lines —
  fix at least that one, preferably both.

The fix is a **rewrite**, not a deletion: the sentence still needs a verb phrase.
Prefer naming the real actor ("we," "the study," "the model," "the evidence"); if
the actor is genuinely unavailable, KEEP and note rather than invent a fake actor.

## Procedure

1. **Resolve the request arguments to files;** use the host's available text search
   to find passive hits (`is/are/was/were + past participle` and `gets/has been +
   past participle`) and keep only files containing them.
2. **Triage:** search the passive pattern across those files and skim. If rare, fix
   inline. If spread across many files, split into up to 6 roughly equal groups and
   use one focused worker per group in parallel when the host supports workers;
   otherwise process the groups sequentially.
3. **Each worker gets:** its exact file list; the KEEP/FIX and active-voice rules
   verbatim (from `references/passive.md`); instruction to read a full sentence of
   context around every hit (passive detection needs whole-sentence scope); the
   global style rules (no em dashes except to interrupt dialogue; complete grounded
   sentences; no metaphorical math/analytical language). It converts each FIX hit to
   active in place, touching ONLY the construction, and reports a per-file verdict
   list: each hit tagged (KEPT-unknown / KEPT-field / KEPT-voice / REWRITTEN-active /
   REWRITTEN-noun-voice) with before→after for changes.
4. **Verify when all workers return:** re-search the passive pattern — remaining hits
   should be only KEEP-classified ones. Confirm no worker invented a fake actor on a
   KEEP candidate. Worker edits make your in-context file state stale; reread before
   any follow-up edit. Report the consolidated change list and before/after count.
5. Offer to commit or leave staged.

## Notes

- Passive is a clarity problem, not a grammar sin. Do not hunt a "get" that is
  idiomatic, or a passive that the discipline and audience actually expect. The pass
  is strongest in argument/exposition prose; methods sections should be tuned down
  or skipped per the style guide.
- "It has been argued that…" is a hedge-and-passive double: convert to name the
  arguer ("Scholars have argued that…") when the arguer is recoverable, otherwise
  flag for the author.
