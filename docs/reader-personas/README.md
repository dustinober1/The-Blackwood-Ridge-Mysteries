# Fiction Persona Review Framework — Blackwood Ridge Mysteries

Review scope: **Books 2–5 now** (Book 1 is the baseline; Books 6–8 as they reach draft). Persona library: [personas.md](personas.md) (123 personas, 21 groups).

## How to run a review

1. **Pick a panel.** Use a preset below, or pick any IDs. For a full pass, run one persona from every group.
2. **Feed the persona only what a real person would have.** Reader/critic personas get the reader-facing export (`books/book-NN/export/manuscript-combined.md`), plus the listing copy and cover if relevant. Do **not** hand them bibles, mission locks, or `story-memory.md`. Only the *Craft & Continuity* and *Industry* groups (D, E, F) may also read bibles.
3. **Spoiler discipline.** Each persona declares which earlier books they've read (see "Entry point"). A persona reviewing Book 4 as a cold start must be judged on whether the book works standalone.
4. **Stay in voice.** The reviewer writes as the persona: their vocabulary, patience, and biases. A hostile persona is hostile in the way that person truly would be, not a strawman.
5. **Use the report template** below. Each report is saved as `books/book-NN/reviews/<persona-id>.md`.
6. **Synthesize.** After the panel, tally in `books/book-NN/reviews/_synthesis.md`: consensus issues (3+ personas), polarizing issues (love/hate splits), and single-persona flags worth a look.

## Report template

```markdown
# <Persona name> (<ID>) — Book N: <Title>
**Entry point:** (cold / read books X–Y)  **Format read:** (ebook / print / audio-proxy)
**Stars:** ★☆☆☆☆–★★★★★  **Would read next book?** yes / maybe / no  **Would recommend?** yes / maybe / no
**DNF point (if any):** chapter + why

## Gut reaction (3–5 sentences, in persona's voice)
## What worked (specific, cite chapters/lines)
## What didn't (specific, cite chapters/lines)
## Persona-specific checklist results (from personas.md)
## Public review draft (the review this person would actually post, 80–250 words)
## One change that would flip my rating
```

## Scoring (applied across the panel)

| Dimension | 1 | 5 |
|---|---|---|
| Hook / opening | skimmable | can't stop |
| Mystery fairness | cheats / unguessable | fair, rewarding rereads |
| Character & arc | flat / static | specific, changing |
| Prose texture | generic, patterned | distinct, human |
| Setting / voice authenticity | caricature | lived-in |
| Pacing | drags / rushes | earned |
| Series value | repeats Book 1 | advances arc and stands alone |
| Ending payoff | deflates | lands, sets up next |

Flag any dimension where panel scores differ by **3+ points** as polarizing.

## Preset panels

- **Quick (8):** R01, R05, M01, M02, A01, L01, I02, H01
- **Standard (20):** Quick + R03, R10, M05, M08, C01, C03, S02, U01, X01, V01, B02, T01
- **Launch Readiness (30):** Standard + A02, R14, S05, G03, K02, P01, N02, O03, Q01, W01
- **Full Gauntlet (all 123):** run in 4 waves of ~30; synthesize between waves.
- **Pre-Release Cover/Blurb Test:** G01–G08 + R01, R05, R12, T01
- **Anti-AI Authenticity Sweep:** A01–A06 (run on every book)
- **Series Continuity Audit (Books 2–5 together):** M01, K01–K06, F01–F03

## Known series risk areas (point panels at these)

- **Repetition of structure:** each book = body found → Callie reads a document → Cross constraint → Eli lesson → arrest. Do readers feel a formula by Book 4/5?
- **Callie's gift as deus ex machina:** is handwriting analysis ever too convenient?
- **Pariah arc pacing:** is Book 2's "unwelcome" status sustained or repeated in Book 3?
- **Short novella length (~22–35k words):** value perception vs. price.
- **Eli Townsend slow-burn:** do careful readers notice and resent, or enjoy, the hidden placement?
- **Cross/Callie "bounded partnership":** satisfying restraint or frustrating stasis?
- **Southern/regional voice:** authentic vs. caricature (see `series-bible/voice-dna.md` banned patterns).
- **AI-prose tells:** rhythm of threes, "not X but Y", em-dash density, tidy-aphorism chapter endings, repeated sensory objects (brass glass, floorboard creak), over-explained emotion.
- **Mystery fairness in Book 5's forged-note:** does the reader get the same evidence Callie gets?
