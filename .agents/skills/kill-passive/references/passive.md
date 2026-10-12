# Pass: kill avoidable passive voice

Targets the passive constructions the model produces to hide the actor and weaken
authority: `[is|are|was|were] + past-participle (+ by …)`, `has/have been +
past-participle`, and `gets + past-participle` used as a passive disguise.

**The active-voice rule:** convert to active. The sentence still needs a verb
phrase, so the fix is a rewrite that promotes the actor to the subject — never a
mechanical swap into another passive ("is thought" → "has been suggested" is not a
fix). If the actor is genuinely unavailable, KEEP and note rather than invent one.

Examples:
- "the decision was made" → "the committee made the decision"
- "mistakes were made" → "we made the mistakes"
- "the data gets cleaned by the pipeline" → "the pipeline cleans the data"
- "a mistake has been identified" → "we identified a mistake"
- "X was rejected by reviewers" → "reviewers rejected X"

**KEEP (do not touch):**
- Actor genuinely unknown or irrelevant: "the chamber was sealed," "the samples were
  stored at -80°C," "the model was fit with…".
- Field-standard / disciplinary convention (e.g., methods sections) per the project
  style guide and audience assumptions.
- Active, idiomatic "gets": "he gets paid," "the model gets a lot of use."
- Quoted speech / cited material where changing it would mis-quote.

**FIX (rewrite to active — name the actor):**
- Nameless-agent passives where the actor is suppressible and known: "mistakes were
  made," "the decision was made," "it was agreed," "X was rejected," "the change was
  implemented."
- `gets + past-participle` used as a passive euphemism: "the issue gets overlooked,"
  "the data gets cleaned."
- `has/have been + past-participle` parking the actor at the end or hiding it: "a
  mistake has been identified" → "we identified a mistake."
- The same actor-hidden construction twice within a few lines — fix at least that one.

Triage grep:
`grep -rniE "\b(is|are|was|were|has been|have been|gets) \w+ed\b" <files>`

Note this over-matches ("was red," "gets better," "have been kind") — confirm the past
participle reading by eye before classifying.
