# Pass: kill hedge words and qualifiers

Targets the hedge tokens the model overuses to pad, soften, and back a claim off
its own edge: `somewhat`, `tends to`, `in a sense`, `arguably`, `essentially`,
`basically`, `virtually`, `practically`, `kind of`, `sort of`, `rather`, `fairly`,
`quite`, `relatively`, `comparatively`, `in some ways`, `to some extent`,
`more or less`.

**The deletion-first rule:** in most cases the hedge can simply be **deleted** without
changing the meaning. Prefer outright deletion over swapping in another qualifier.
Never replace one hedge with another ("essentially" → "basically" is not a fix).

Examples:
- "the theory essentially explains X" → "the theory explains X"
- "results virtually confirm the finding" → "results confirm the finding"
- "this approach is quite effective" → "this approach is effective"
- "arguably the strongest predictor" → "the strongest predictor" (commit; if the
  argument needs the caveat, place it deliberately, not smeared into the noun)
- "somewhat effective" → "effective" (if the degree matters, add a concrete
  comparison; do not trade "somewhat" for "slightly")

**KEEP:**
- Genuine epistemic uncertainty that is the point the sentence makes (measured
  claims about limits of knowledge: "evidence suggests," "with X still unresolved").
- Quoted speech and direct discussion of hedging (the hedge is the subject).
- Idiomatic / field-standard phrasing where the qualifier carries meaning, not
  padding.
- Comparative qualifiers with an explicit referent when the comparison is the work
  ("relatively low, compared to Y").

**FIX:**
- "essentially/basically/virtually/practically X" padding — DELETE, commit the claim.
- "somewhat/rather/fairly/quite X" volume knobs — DELETE; reword only with a
  concrete grounding if the degree matters.
- "arguably/in a sense/to some extent/in some ways/more or less/tends to" that
  softens a claim the sentence should own — DELETE, or rewrite so the claim
  commits and any caveat sits deliberately at the point.
- "kind of/sort of" filler hesitation — DELETE.
- The same hedge twice within a few lines — cut at least that one.

Verify grep (remaining hits should be only KEEP-classified, by eye):
`grep -rniE "\b(somewhat|tends to|in a sense|arguably|essentially|basically|virtually|practically|kind of|sort of|rather|fairly|quite|relatively|comparatively|in some ways|to some extent|more or less)\b" <files>`

For before/after counts: `grep -rioE "\b(somewhat|tends to|in a sense|arguably|essentially|basically|virtually|practically|kind of|sort of|fairly|quite|relatively|comparatively|more or less)\b" <files> | wc -l`.
