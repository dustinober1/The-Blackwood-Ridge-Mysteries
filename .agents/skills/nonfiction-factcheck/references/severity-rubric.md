## Severity Rubric

### Status Values
- **verified:** assertion matches the corpus source exactly, with correct calibration.
- **unsupported:** no source in the corpus; the assertion floats free.
- **contradicted:** the corpus source says the opposite or a different value.
- **misattributed:** real fact, wrong name, year, work, or role.
- **imprecise:** true but miscalibrated — wrong hedge, missing denominator, false precision, context stripped.
- **unverifiable:** the corpus does not contain the source at all; the author must supply it or cut the assertion.

### Severity Levels

**Critical** — publish-blockers. Fabricated or contradicted material; a misquote presented verbatim; a superlative that is false; a causal claim its source does not support.
*Rule:* any misquote, any fabricated number, any claim the corpus contradicts.

**High** — materially misleads. Wrong number with right order of magnitude; wrong year or name that misdirects the reader; population swap that changes the claim's meaning; unsupported statistic.

**Medium** — weakens trust. Missing denominator; stale superlative; hedge stronger than evidence; circular sourcing; undefined term of art doing load-bearing work.

**Low** — hygiene. Misspelling that does not mislead; inconsistent citation format; imprecise but harmless rounding.

### Disposition Rules
- Critical and High findings must be fixed before the chapter proceeds to `nonfiction-clarity-edit` — polishing prose around a false fact wastes the edit.
- Unverifiable findings get an explicit author disposition: supply the source or cut the assertion. Never leave them in a "maybe" pile.
- Low findings may be batched into a single cleanup pass.
- When in doubt between two severities, choose the higher one: fact errors compound, style errors don't.
