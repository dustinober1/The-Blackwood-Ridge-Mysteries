---
name: kill-hedge
description: Hunt hedge words and qualifiers that weaken claims across a chapter and cut or commit them so the prose states its point with authority (deletion-first, parallel focused workers, edits in place). Targets somewhat, tends to, in a sense, arguably, essentially, basically, virtually, practically, kind of, sort of, rather, fairly, quite, relatively, comparatively, in some ways, to some extent, more or less. Use when user says "kill-hedge", "kill the hedges", "strip hedging words", or "reduce qualifiers".
metadata:
  author: Nonfiction Toolkit
  version: "1.0.0"
  category: nonfiction-editing
---

# Kill the hedge — strip the qualifier, commit to the claim

Non-fiction earns its authority by stating a claim and defending it. The model
undermines that authority by padding and softening every sentence with a hedge:
"somewhat," "arguably," "essentially," "basically," "sort of," "to some extent,"
and the dozens of other tiny escape hatches that let a claim retreat from its own
edge. A hedge is doing real work only when a measured uncertainty is itself the
point the sentence needs to make; everywhere else it is noise that makes the
argument flinch.

The request arguments = the chapter file(s): a path, a file pattern, or several
paths. Resolve it to a concrete file list before doing anything (skip files that
don't contain a hedge token).

## What to keep vs. fix

**KEEP (do not touch):**
- **Genuine epistemic uncertainty that is the point** — a claim explicitly about the
  limits of knowledge or the tentative state of a field: "the evidence only
  *suggests*," "this effect appears *to some extent*," "we can say *arguably* at
  this stage, with X still unresolved." If removing the hedge would misstate the
  strength of the claim, KEEP and note it.
- **Quoted speech / direct analysis of hedging** where the hedge is the subject
  under discussion ("the author hedges with 'essentially' here").
- **Idiomatic / field-standard phrasing** that carries meaning, not padding ("to a
  large extent," "rather than," "fairly certainly" in the legal sense) — treat by
  eye, not as a mechanical target.
- **Comparative qualifiers that carry a real comparison** ("relatively low,"
  "comparatively stable") when the referent frame is explicit and the comparison
  is doing the work.

**FIX (cut first; reword only if the sentence needs it):**
- "essentially X" / "basically X" / "virtually X" / "practically X" where the
  hedge adds nothing the sentence didn't already state — DELETE, leaving the claim.
- "somewhat," "rather," "fairly," "quite" used as soft volume knobs ("somewhat
  effective," "quite small") — DELETE; if the degree matters, ground it in a
  concrete comparison or figure.
- "arguably," "in a sense," "to some extent," "in some ways," "more or less,"
  "tends to" used to back the sentence off its own edge — DELETE, or rewrite so
  the sentence commits and the qualification (if any) is placed deliberately at
  the point, not smeared into the verb.
- "kind of," "sort of" as filler hesitation — DELETE.
- **Repetition:** the same hedge twice within a few lines — cut at least that one.

Default move is **deletion**, not a swap into another softener. Only do a fuller
rewrite if deletion genuinely loses needed meaning, and commit the claim rather
than replacing one hedge with another.

## Procedure

1. **Resolve the request arguments to files;** use the host's available text search
   to keep only files containing a hedge token.
2. **Triage:** search for the hedge set (the full token list lives in
   `references/hedge.md`) and skim. If rare, fix inline. If spread across many
   files, split into up to 6 roughly equal groups and use one focused worker per
   group in parallel when the host supports workers; otherwise process the groups
   sequentially.
3. **Each worker gets:** its exact file list; the KEEP/FIX and deletion-first rules
   verbatim (from `references/hedge.md`); instruction to read each file in 20-line
   chunks so it judges every hit in full context; the global style rules (no em
   dashes except to interrupt dialogue; complete grounded sentences; no
   metaphorical math/analytical language). It makes the minimal in-place edit,
   touching ONLY the hedge token and nothing else on the line, and reports a
   per-file verdict list: each hit tagged (KEPT-uncertainty / KEPT-voice / KEPT-idiom /
   DELETED / REWRITTEN) with before→after for changes.
4. **Verify when all workers return:** search again for the hedge set — remaining
   hits should be only KEEP-classified ones. Worker edits make your in-context file
   state stale; reread before any follow-up edit. Report the consolidated change
   list and before/after count from the host's available text search.
5. Offer to commit or leave staged.

## Notes

- This pass is deletion-first by design: a claim that survives its own hedge was
  not worth hedging. The few KEEP cases are genuine measured uncertainty, not
  mechanical timidity — flag them explicitly so a future pass can audit the rate.
- Do not confuse "hedging" with "nuance." A claim can be strong and still
  caveated correctly; if the caveat carries the meaning, KEEP it.
