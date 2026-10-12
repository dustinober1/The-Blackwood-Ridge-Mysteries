# Pass: kill unexplained initialisms and acronyms

Targets initialisms/acronyms that appear bare on their first use in a file without
a prior spelling-out. The canonical candidate list (non-exhaustive): `AI`, `ML`,
`NLP`, `GDP`, `UNESCO`, `DNA`, `MRI`, `FBI`, `NASA`, `API`, `CLI`, `HTML`, `CSS`,
`JSON`, `XML`, `YAML`, `SQL`, `URL`, `URI`, `HTTP`, `HTTPS`, `ISO`, `PDF`, `RGB`,
`RGBA`, `UTF`, `CPU`, `GPU`, `RAM`, `ROM`, `I/O` (slash-bearing forms), `FAQ`,
`PDF`, `ISO`, `IEEE`, `ANSI`, `ACLU`, `EPA`, `FDA`, `CDC`, `WHO`, `UN`, `EU`, `NAFTA`,
`GOP`, `IRS`, `SEC`, `DOJ`, `POV`, `Q&A`, `R&D`, `NDA`, `SLA`, `KPIs`.

A candidate is in scope only at its **first bare occurrence** in a file where no
expansion has preceded it. A "bare" occurrence is one not immediately followed or
preceded (on the same or prior line) by `Term (ACRONYM)` or `ACRONYM — Term` or
`ACRONYM (Term)`.

**The flag-first rule:** an acronym is a reader-trip when its meaning is
undeclared. Flag the first bare occurrence of each acronym; expand in place **only**
when the expansion is unambiguous (a quoted source, a project term list, or a
discipline-standard spelling the style guide already endorses). Never guess.

**KEEP (do not touch):**
- Initialisms/acronyms universally known to the book's audience and already
  endorsed bare by the project style guide / audience profile.
- Acronyms established earlier in the same file (or in an earlier chapter the
  reader has seen) — only the first bare use per reader-path is in scope.
- Quoted / cited material where the source uses the bare form and expanding would
  mis-quote or alter the citation.
- Standard units and discipline-owned short forms (`DNA`, `pH`, `MRI`) when the
  field and style guide treat them as bare-safe — confirm by eye.

**FIX:**
- First bare occurrence of an acronym with no prior expansion and an unambiguous
  expansion available → rewrite to `Term (ACRONYM)`.
- An acronym **re-declared** later in the file (`GDP — gross domestic product` on
  line 2 and again on line 412) → DELETE the later redundant re-declaration; keep
  the first expansion only.
- An acronym that **collides** with another meaning in the same file
  (`AI` for "Artificial Intelligence" and "Application Interface") → FLAG as a
  collision; do not edit without the author.
- A second bare "first use" of an already-expanded acronym in the same file →
  DELETE the redundant expansion; the first one stands.

Triage grep (candidate initials; then classify each by eye for bare vs. established
and for ambiguity):
`grep -rnoiE "\b[A-Z][A-Za-z\.]*(?:[A-Z][A-Za-z\.]*)*\b" <files> | grep -E "\b[A-Z]{2,}(?:\.[A-Z]){0,}\b"`

Simpler first-pass scan for the high-signal set:
`grep -rnoiE "\b(AI|ML|NLP|GDP|UNESCO|API|CLI|HTML|CSS|JSON|XML|YAML|SQL|URL|URI|HTTP|HTTPS|ISO|PDF|UTF|CPU|GPU|RAM|ROM|FAQ|IEEE|ANSI|ACLU|EPA|FDA|CDC|WHO|GOP|IRS|SEC|DOJ|POV)\b" <files>`

Confirm bare-vs-established and ambiguity by reading a full sentence of context
around each first-use hit.
