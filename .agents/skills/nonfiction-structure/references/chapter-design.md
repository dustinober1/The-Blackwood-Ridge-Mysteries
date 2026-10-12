# Chapter Design Patterns

## The Five Chapter Archetypes

Every chapter in a nonfiction book serves one primary *argument function*. Design to the archetype.

---

### 1. Frame Chapter
**Argument Function:** *Poses* — Sets up the problem, question, or paradigm shift.
**Reader State Change:** "I see the territory differently now."

**Structure:**
```
OPEN: Hook — Question, paradox, story, data point, or scene that creates tension
CONTEXT: Why this matters now (urgency, stakes, reader's pain)
FRAME: The lens/definition/reframe — "Here's what we're actually looking at"
PREVIEW: What's coming — "In this part we'll..."
CLOSE: Bridge — "But first, we need to understand [next chapter's concept]..."
```

**Cognitive Load:** Low–Medium (orientation, not density)
**Evidence:** Minimal — illustrative only
**Artifacts:** Mental model diagram, "before" self-assessment
**Typical Position:** Chapter 1, Part openers, major transitions

**Frame Chapter Checklist:**
- [ ] Opens with genuine tension (not throat-clearing)
- [ ] Defines key terms *in the reader's language*
- [ ] States the question this part answers
- [ ] Promises a specific payoff
- [ ] Closes with a *need* for the next chapter

---

### 2. Evidence Chapter
**Argument Function:** *Evidences* — Proves a thesis clause with deployed evidence.
**Reader State Change:** "I believe this claim because..."

**Structure:**
```
OPEN: The Claim — "Here's what we're proving: [thesis clause]"
EVIDENCE 1: [Primary evidence type] — Data, case study, study, framework
  → What it shows
  → Why it's credible (methods, source, replication)
  → Limitations acknowledged
EVIDENCE 2: [Supporting evidence type] — Different angle, same claim
  → Triangulation
SYNTHESIS: "Taken together, this means [thesis clause] is supported."
CAVEATS: Boundary conditions, where this doesn't apply, counter-evidence
CLOSE: Bridge — "But knowing this isn't enough. We need to [apply/extend]..."
```

**Cognitive Load:** Medium–High (densest chapters)
**Evidence:** Primary — this is where evidence_architecture deploys
**Artifacts:** Evidence summary table, "trust this because" checklist
**Typical Position:** Core of each part (2-3 per part)

**Evidence Chapter Checklist:**
- [ ] Lead with the claim, not the evidence
- [ ] One primary evidence type per chapter (don't kitchen-sink)
- [ ] Explicitly address: methods, sample, limitations
- [ ] Steel-man the strongest counter-argument
- [ ] End with *so what* for the thesis, not just data summary

---

### 3. Application Chapter
**Argument Function:** *Applies* — Shows the reader how to use the idea.
**Reader State Change:** "I can do this now."

**Structure:**
```
OPEN: The Situation — "You're facing [specific context from audience.prerequisites]"
FRAMEWORK: The Tool — Named framework/model with visual
STEP-BY-STEP: Numbered, concrete, with decision points
  → Decision: "If X, do Y. If Z, do W."
  → Example: "Here's how [persona] did it"
  → Trap: "Common mistake: [X]. Fix: [Y]."
WORKED EXAMPLE: Full walkthrough with artifacts
YOUR TURN: Exercise with rubric/checklist
CLOSE: Bridge — "This works for [this context]. But what about [next context]?"
```

**Cognitive Load:** Medium (procedural, not conceptual)
**Evidence:** Worked examples, templates, decision trees
**Artifacts:** **MUST HAVE** — Template, checklist, script, calculator, rubric
**Typical Position:** Part III (Problem-Solution), every phase (Chronological), Application section (Conceptual)

**Application Chapter Checklist:**
- [ ] Opens with *reader's* context (from audience.md)
- [ ] Framework is named, visual, and memorable
- [ ] Steps are executable without author present
- [ ] Decision points handle "it depends"
- [ ] Worked example uses audience's language/context
- [ ] Exercise produces portfolio-ready / usable artifact
- [ ] Rubric defines "good" for self-assessment

---

### 4. Synthesis Chapter
**Argument Function:** *Synthesizes* — Connects multiple threads; shows integration.
**Reader State Change:** "I see how it all fits together."

**Structure:**
```
OPEN: The Tension — "We've seen X, Y, Z. They seem separate. They're not."
INTEGRATION: The Unified Model — Visual/framework showing connections
  → How Principle A enables Principle B
  → How Mechanism 1 solves Problem 2
  → The emergent property
IMPLICATIONS: What this means for [broader context / reader's work / field]
BOUNDARY MAP: Where this works / where it breaks / what's unknown
CLOSE: Bridge — "Now we have the model. Next: [mastery / edge cases / teaching others]..."
```

**Cognitive Load:** High (integration is hard cognitive work)
**Evidence:** Cross-references to prior chapters; no new primary evidence
**Artifacts:** Integrated framework diagram, "complete picture" one-pager
**Typical Position:** End of Part II (Conceptual), before Application (Hybrid), Part III opener

**Synthesis Chapter Checklist:**
- [ ] Explicitly names what's being synthesized
- [ ] Visual integration (not just list)
- [ ] Shows *emergent* insight (not just summary)
- [ ] Honest boundary map (builds skeptic trust)
- [ ] Closes with forward momentum, not just "ta-da"

---

### 5. Transition Chapter
**Argument Function:** *Bridges* — Manages cognitive load; prepares for shift.
**Reader State Change:** "I'm ready for what's next."

**Structure:**
```
OPEN: Reflection — "Here's where we are. Here's what we've proven."
RECAP: 3-bullet synthesis of prior section
PREVIEW: "Next, we [shift gears / go deeper / zoom out / apply]."
PREP: Prerequisite check — "Before the next chapter, make sure you..."
MINDSET: "The next section requires [different thinking / more rigor / hands-on]."
CLOSE: "Turn the page when you're ready."
```

**Cognitive Load:** Low (recovery, orientation)
**Evidence:** None (meta-commentary)
**Artifacts:** Progress tracker, "am I ready?" checklist
**Typical Position:** Between high-load sections; architecture shifts; Part boundaries

**Transition Chapter Checklist:**
- [ ] Honest about difficulty shift
- [ ] Concrete readiness criteria
- [ ] No new content — pure meta
- [ ] Short (500-1500 words max)
- [ ] Feels like a *breath*, not a lecture

---

## Chapter Type Distribution by Architecture

| Architecture | Frame | Evidence | Application | Synthesis | Transition |
|--------------|-------|----------|-------------|-----------|------------|
| Problem-Solution | 2-3 (Ch1, PtII, PtIII) | 3-5 (PtI, PtII) | 4-6 (PtIII) | 1-2 (PtII end) | 1-2 (Pt boundaries) |
| Chronological | 2-3 (Ch1, PtII, PtIII) | 2-3 (PtI, woven) | 6-8 (PtII - every phase) | 1 (PtIII) | 2-3 (phase boundaries) |
| Conceptual | 3-4 (Ch1, each Principle) | 4-6 (each Principle) | 3-4 (Application section) | 2-3 (Synthesis section) | 1-2 (Principle boundaries) |
| Hybrid | Follows primary | Follows primary | Follows primary | Follows primary | At logic shifts |

---

## Cognitive Load Management

### Load Levels Defined

| Level | Reader Effort | Max Consecutive | Recovery Needed |
|-------|---------------|-----------------|-----------------|
| **Low** | Orientation, recognition, skimmable | 3-4 | None |
| **Medium** | Comprehension, comparison, application | 2-3 | 1 Low or Transition |
| **High** | Synthesis, abstraction, novel framework | 1 | 1 Transition + 1 Low |

### Load Signals in Chapter Design

**High Load Markers:**
- New framework/model introduction
- Multiple interacting concepts
- Counter-intuitive claims requiring belief revision
- Dense evidence evaluation (methods, stats)
- Synthesis across 3+ prior chapters

**Medium Load Markers:**
- Single new framework applied
- Evidence evaluation (one study type)
- Procedure with decision points
- Case study analysis

**Low Load Markers:**
- Narrative / story
- Recap / synthesis (familiar material)
- Application with template (follow steps)
- Orientation / framing

### Pacing Rules

1. **Never 3 High in a row** — Insert Transition or Low
2. **High must be followed by Low/Transition** — Cognitive recovery
3. **Front-load Medium, back-load High** — Build capacity
4. **Application = Medium (not High)** — If High, split into Frame + Application
5. **Synthesis = High** — Always precede with Transition, follow with Low

---

## Chapter Design Template (Writer's Brief)

Use this for every chapter in `structure.md`:

```markdown
## Chapter NN: [Title]

- **chapter_type:** frame | evidence | application | synthesis | transition
- **thesis_clause:** [Primary clause from thesis_clause_map]
- **evidence_types:** [From concept.md — what deploys here]
- **reader_milestone:** [Micro-transformation: "Reader can now X"]
- **key_frameworks:** [Named frameworks introduced, max 2]
- **exercises_or_artifacts:** [Templates, checklists, outputs — specific names]
- **opens_with:** [Hook type: question / story / paradox / data / scene — 1 sentence]
- **closes_with:** [Bridge to next chapter — 1 sentence]
- **cognitive_load:** low | medium | high
- **prerequisites_required:** [From audience.prerequisites — specific items]
- **what_must_happen:** [Directive for writer: 3-5 sentences, imperative]
- **argument_function:** poses | evidences | complicates | synthesizes | applies
- **audience_service:** quick_win | mental_model | decision_tool | narrative_payoff | rigor
```

### what_must_happen Examples

**Frame:** "Open with the '47 tabs' scene. Define 'identity-based' vs 'outcome-based' in reader's language. Pose the central question: 'Why do smart people fail at habits?' Close with: 'The answer isn't willpower — it's architecture.'"

**Evidence:** "Present the 90-day field study (n=240) showing 3x consistency. Walk through the design: randomization, measures, attrition. Show the decision-fatigue mediation analysis. Acknowledge: self-selection bias, WEIRD sample. Close: 'The mechanism holds. But does it work in *your* chaos?'"

**Application:** "Walk through the Identity Architecture canvas step by step. Show Maya (distributed PM) filling it out. Highlight decision point: 'If your identity claim feels fake, use the 'aspirational but believable' test.' Provide the canvas template. Exercise: Reader drafts their identity claim. Close: 'You have your claim. Now we build the system that makes it inevitable.'"

**Synthesis:** "Reveal the Integrated Habit Architecture: Identity → Environment → Feedback → Identity. Show how decision fatigue (Ch3) and motivation dips (Ch4) are both solved by the same loop. Map boundary conditions: works for knowledge work; untested for physical rehab; fails without weekly review. Close: 'The model is complete. Now: your 90-day protocol.'"

**Transition:** "Recap: We've proven identity beats outcomes (Ch2), via decision fatigue (Ch3) and motivation (Ch4), synthesized in the Architecture (Ch5). Next: the 90-day protocol. Before you continue: complete the Identity Canvas (Ch6 exercise). You need it for Chapter 7."
