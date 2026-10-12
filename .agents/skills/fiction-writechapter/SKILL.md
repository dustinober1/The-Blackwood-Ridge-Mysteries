---
name: fiction-writechapter
description: "Draft or continue a fiction chapter from an established scene plan, book voice, continuity, and book-specific Wiki canon. Use when the user asks to write a chapter or continue writing; use fiction-scenes when the chapter's causal beats are not yet settled."
metadata:
  author: Fiction Toolkit
  version: "4.1.1"
  category: fiction-writing
  output-format: markdown
---

# Write Chapter

Draft the assigned chapter without redesigning the story or running a full editorial pass. The book's instructions and Wiki are authoritative; the scene plan owns the chapter's causal, emotional, genre, arc, and motif obligations.

## Authority and scope

Use this order of authority:

1. The user's current instructions.
2. The book's `AGENTS.md`, `CLAUDE.md`, and applicable nested instructions.
3. The book's established source and filename conventions.
4. The book's Wiki, scene plan, style guide, and voice prompt.
5. This skill's generic defaults.

Read the book instructions before writing. Do not create a new plot direction, planning artifact, review report, or parallel chapter directory. If the assigned chapter lacks enough causal beats to draft without inventing its purpose, stop and recommend `fiction-scenes` for that chapter.

## Identify the chapter and destination

Use the project or chapter named by the user. Otherwise infer the selected book from the current working context and `Wiki/Story/active-context.md`; if multiple books remain plausible, ask which one.

Resolve the book root, root `Wiki/`, active context, target scene plan, target outline entry, style guide, voice prompt, previous authoritative chapter, optional psych document, and exact output path. Read the outline only when it adds information missing from the scene plan.

Follow neighboring chapter filenames and the book's instructions. When no local convention exists, use `<book-root>/Chapters/Chapter-[NNN].md` and put the title inside the Markdown file. Never create `[WorkingTitle]_Chapters` or another independently editable copy.

If `active-context.md` is missing, use an explicit user assignment or the outline to identify the target. Create a compact active context only when the book's workflow requires one; missing tracking infrastructure must not silently change the story assignment.

## Use a focused writing worker

When isolated workers are supported, use one focused worker for the chapter so its context contains only relevant book material. Give it the resolved paths and the instructions below. If workers are unavailable, follow the same instructions directly.

Pointing a worker at a rules file does not make that file binding: naming only some mechanical rules in the brief turns the unnamed ones into a whitelist the worker is free to violate. In every drafting brief, either quote every binding mechanical rule from the style and review guides verbatim, or state that every rule in those files is binding whether or not the brief quotes it. After the draft returns, search the prose for the rules the brief did not name before accepting the completion check — the worker's own compliance tally will mirror what the brief named.

## Worker instructions

Write the assigned chapter as finished prose.

### Read only drafting context

Read, in this order:

1. Relevant current-status and continuity sections from `active-context.md`.
2. The target scene plan or beats.
3. The target outline entry only when the scene plan does not fully state the required outcome.
4. The style guide and protagonist voice prompt. Treat the stricter book-specific rule as binding.
5. The previous authoritative chapter for immediate continuity.
6. The optional psych document for interior movement, without copying its analytical language.

Do not load the entire synopsis, theme, review guide, character directory, or world directory by default. Retrieve additional Wiki context only when a scene beat, continuity question, or proper noun requires it.

Before drafting, extract a compact working brief:

- POV, tense, and voice constraints;
- opening physical and emotional state;
- required scene outcomes and ending movement;
- facts carried from the previous chapter;
- named participants, places, organizations, systems, objects, events, and other canon terms that the scene expects.

The scene plan has already decided plot architecture. Honor its required outcomes, choices, consequences, and chapter-specific obligations. You may shape connective action, dialogue, sensory detail, and local choreography, but do not replace the plan with a new one.

### Research every proper noun in the book Wiki

Every proper noun used in the chapter title or prose must be researched in this book's own Wiki. This includes people, aliases, honorifics, places, organizations, cultures, species, deities, named objects, events, systems, technologies, demonyms, and specialized capitalized canon terms.

For each planned proper noun:

1. Search the entire book Wiki recursively, not just the expected character or world folder.
2. Read the supporting Wiki context.
3. Confirm exact spelling, capitalization, identity, relationships, and facts relevant to this scene.

The book's own Wiki is the only research authority for proper nouns. A previous chapter, another book's Wiki, general memory, or the draft itself is not sufficient evidence. Do not guess, silently invent, or import a name. If an unsupported proper noun is not essential, use an accurate generic description. If replacing it would materially alter the scene plan or canon, report the missing canon and do not mark the chapter complete.

### Draft the prose

Use the book's requested length; otherwise aim for roughly 2,000–3,000 words. Follow the project's chapter-heading and scene-break conventions.

In a multi-POV chapter, mark every scene break with the POV character of the section that follows, using the book's marker convention, and make sure the chapter's head marker names the POV that actually opens the chapter. An unmarked break or a head marker naming the wrong POV is a defect, not a style choice: continuity maps, narration passes, and audio tooling parse these markers mechanically.

When the book's instructions set a per-chapter word floor, treat a first draft landing under it as under-built: expand with substantive material inside the planned beats — added scene work, texture that earns its place, or a canon-consistent subplot when the plan offers nothing left to deepen — and check the next chapter's scene plan first so the addition does not steal its beats. Never pad, and never cut a planned beat, image, or texture hit as a length measure. In a revision pass, mandated redundancy cuts may take a chapter below the floor; report the honest count and leave it rather than re-adding padding to clear the number.

Keep the prose inside the POV character's perception, judgment, body, and immediate thought. Match established dialogue voices, knowledge limits, relationships, setting rules, time, injuries, possessions, and unresolved promises. End with the forward movement required by the scene plan.

Do not turn planning language into narration. Terms such as beat, arc, motif, reversal, false belief, or chapter function belong in planning documents, not the character's lived experience. Do not force a motif or genre beat into conspicuous prose merely to satisfy a tracker; deliver the planned effect through natural action, choice, image, dialogue, or consequence.

### Verify before saving

Perform a focused completion check, not a full editorial review:

1. Confirm every required scene outcome and consequence is present.
2. Confirm POV, tense, voice, chronology, physical continuity, and knowledge boundaries — including that every scene break carries the correct POV marker per the book's convention.
3. Scan the title and prose for every proper noun, including possessives and aliases. Search the entire book Wiki for each one and correct every unsupported or inconsistent use.
4. Remove analytical drafting language and generic voice drift that clearly violates the style guide or voice prompt.
5. Verify every exact count or duration the prose asserts ("four words," "two syllables," "six days") against the line on the page. Recast any assertion the page disproves; never adjust the page to fit the count. Check durations and dates against the chapter's own stated anchors, and recast any reference to a manuscript or chapter number into in-world terms.
6. Scan for verbatim duplication: a sentence or block rendered twice in near-identical form, especially in adjacent paragraphs or across a scene seam. A deliberate echo varies its continuation; an artifact repeats. Cut the artifact copy.

Leave broader prose diagnosis, AI-pattern auditing, ratings, and revision recommendations to `fiction-reviewchapter` or a specialized editing skill.

## Save and hand off

Save only to the resolved authoritative chapter path. Do not overwrite a different existing chapter or create a parallel manuscript copy.

Update `active-context.md` minimally:

- last written chapter, next chapter, title, and word count;
- concrete continuity created or changed: location and time, injuries, possessions, promises, character knowledge, relationship facts, and open threads;
- unresolved canon questions that affected drafting.

Do not recalculate motif cadence, genre architecture, false-belief stages, or character-arc strategy during the writing pass unless the book's own instructions explicitly require that update. Those are planning and review judgments.

Return the chapter path, title, word count, and any genuine canon blocker. Offer the next appropriate action: review this chapter, plan the next chapter, or continue writing when its scene plan already exists.
