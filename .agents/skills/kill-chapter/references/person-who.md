# Pass: kill "the [quality] of a [person] who [clause]"

Targets the mechanical subtext shortcut where the prose names an abstract quality,
attaches it to a generic type-cast ("a man who", "a woman who", "men who"), and closes with
a defining relative clause that labels character interiority instead of dramatizing it.

**Pattern:** `the [qualifier]? [abstract-noun or "expression"/"look"/"tone"] of a/the [person/animal] who/deciding/having [clause]`
- Qualifiers: exact, elaborate, specific, particular, steady, careful, practiced, unhurried, deliberate
- Nouns: patience, expression, disinterest, unhurry, calm, ease, look, tone, manner, air

**The fix rule:** rewrite into a concrete beat (physical action, micro-gesture, or line of
subtext dialogue) rather than synonym swaps. If multiple hits occur in one chapter, vary
the fix (do not turn every hit into "he did X with his hands").

Examples:
- "the patience of a woman who is very good at waiting for things she knows are coming" → show her waiting specifically (not looking at the door, letting silence stretch).
- "the exact expression of a man who has priced a thing for someone he expects to accept the price" → show the concrete facial/postural detail or dialogue.

**KEEP:**
- A single, isolated instance in an otherwise clean chapter (density and repetition is the issue, not a blanket phrase ban).
- Genuine dialogue where a character intentionally speaks this way.

**FIX:**
- Any chapter or scene with 2+ instances of the construction.

Triage grep: `grep -rniE "\bthe [a-z]+ (expression|patience|disinterest|unhurry|calm|ease|look|tone|manner|air) of (a|the) [a-z]+ (who|deciding|having)\b" <files>`
