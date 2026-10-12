# Pass: kill the "opinion" personification tic

Targets the tic where non-sentient things (pain, wounds, ribs, walls, pilings, furniture,
weather) are given "opinions" as a stand-in for sensory/physical description ("it had an
opinion about X", "sent up its opinion", "said its piece").

**Pattern:** non-sentient subject + `have an opinion` / `voice or send up its opinion` / `say its piece` / `have something to say about`.

**The fix rule:** replace with concrete physical/sensory detail of what the body or object
actually does (pain spikes/drags, wound pulls at stitches, wall groans/lists). Do not
substitute another cute personification frame.

Examples:
- "The pain sent up its opinion, which I noted and did not act on" → name the actual physical sensation and response.
- "it had opinions about the walk up the hill and I was choosing not to have opinions back" → cut to a concrete beat about the climb (breath, legs, ribs).

**KEEP:**
- The **founding use** — the earliest 1 or 2 uses in a chapter range that intentionally set up the voice choice.
- At most one additional use later in the range if fresh and well-separated.

**FIX:**
- All other instances across the chapter range to prevent the voice choice from becoming a predictable crutch.

Triage grep: `grep -rniE "\b(opinion|said (its|their) piece|had something to say)\b" <files>`
