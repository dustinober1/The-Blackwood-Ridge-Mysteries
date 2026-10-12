# Argument Mapping: Thesis to Chapters

## The Mapping Principle

**Every clause in your thesis must be evidenced in at least one chapter. Every chapter must advance at least one thesis clause.**

If a chapter doesn't advance the thesis → cut or repurpose.
If a thesis clause has no chapter → the argument is incomplete.

---

## Step 1: Decompose the Thesis

Take your thesis sentence and break it into **independent, evidencable clauses**.

**Example Thesis:**
> "For knowledge workers in distributed teams, identity-based habits outperform outcome-based habits because they reduce decision fatigue and survive motivation dips, leading to 3x consistency over 90 days."

**Clauses:**
1. **C1 (Population):** "For knowledge workers in distributed teams" — scope/boundary
2. **C2 (Claim):** "Identity-based habits outperform outcome-based habits" — comparative claim
3. **C3 (Mechanism 1):** "...because they reduce decision fatigue" — causal mechanism
4. **C4 (Mechanism 2):** "...and survive motivation dips" — causal mechanism
5. **C5 (Outcome):** "...leading to 3x consistency over 90 days" — measurable outcome

**Test:** Can each clause be evidenced independently? Yes → good decomposition.

---

## Step 2: Map Clauses to Evidence Types

From `concept.md` evidence_architecture, assign evidence to each clause.

| Clause | Evidence Types Needed |
|--------|----------------------|
| C1 (Population) | Survey data, demographic analysis, definitional framework |
| C2 (Comparative Claim) | RCT/quasi-experiment, longitudinal tracking, case studies |
| C3 (Mechanism 1) | Cognitive load studies, process tracing, self-report + behavioral |
| C4 (Mechanism 2) | Motivation research, habit decay curves, intervention studies |
| C5 (Outcome) | Field study data, 90-day tracking, consistency metrics |

---

## Step 3: Sequence for Your Architecture

### Problem-Solution Sequencing
```
Part I (Problem): C1 → C2 (diagnosis)
Part II (Solution): C3 → C4 (mechanisms = the "why it works")
Part III (Application): C5 (outcome evidence + implementation)
```
*Logic: Prove the problem exists, then prove the solution works via its mechanisms.*

### Chronological Sequencing
```
Foundation: C1 (who this is for) + C3/C4 preview (mental models)
Phase 1: C2 (comparison) + C3 application (decision fatigue reduction)
Phase 2: C4 application (motivation dip survival)
Phase 3: C5 (90-day outcome) + synthesis
```
*Logic: Teach mechanisms *through* the process; outcome validates the journey.*

### Conceptual Sequencing
```
Principle 1: C3 (Decision fatigue as core problem)
Principle 2: C4 (Motivation volatility as core problem)
Principle 3: C2 (Identity vs Outcome as the lever)
Synthesis: C1 + C5 (Scope + Outcome evidence)
Application: C2-C5 in domains A, B, C
```
*Logic: Build the theoretical architecture; evidence supports each principle; synthesis shows integration.*

---

## Step 4: The Three Flows

Every book has three simultaneous flows. Your architecture prioritizes one; the others must not contradict.

### 1. Logical Flow (The Argument)
**Thesis clause order that makes the proof valid.**
- Premises before conclusions
- Mechanisms before outcomes
- Scope before generalization
- *This is your thesis_clause_map*

### 2. Pedagogical Flow (The Learning)
**Concept order that makes the reader understand.**
- Concrete before abstract
- Familiar before novel
- Simple before complex
- Prerequisites before dependents
- *This drives your chapter prerequisites and cognitive_load*

### 3. Narrative Flow (The Experience)
**Emotional/intellectual journey that makes the reader continue.**
- Hook → Tension → Insight → Relief → Tension → ...
- Questions posed → Questions answered → New questions
- Story arcs (case studies, personal narrative, historical threads)
- *This drives your opens_with / closes_with hooks*

---

## Step 5: Mapping Table Template

Create this table *before* writing chapter briefs:

| Ch | Logical Flow (Thesis Clause) | Pedagogical Flow (Concept) | Narrative Flow (Hook/Arc) | Evidence Deployed |
|----|------------------------------|----------------------------|---------------------------|-------------------|
| 1  | C1 (Scope) | "What is a habit?" (concrete) | "Meet Sarah — 47 tabs open" | Survey data (C1) |
| 2  | C2 (Claim) | Identity vs Outcome (contrast) | "Why Sarah's goals failed" | Case study (C2) |
| 3  | C3 (Mech 1) | Decision fatigue (mechanism) | "The 3pm collapse" | Cognitive load study (C3) |
| 4  | C4 (Mech 2) | Motivation waves (mechanism) | "The Monday myth" | Motivation research (C4) |
| 5  | C3+C4 (Synthesis) | Identity architecture (framework) | "Sarah's new system" | Framework + case (C3,C4) |
| 6  | C5 (Outcome) | 90-day protocol (application) | "The 90-day results" | Field study (C5) |
| 7  | Application | Adapting to your context | "Your 90-day plan" | Templates (C5) |

---

## Step 6: Validation Checks

Run these after mapping:

### Coverage Check
- [ ] Every thesis clause appears in thesis_clause_map
- [ ] Every thesis clause has ≥1 chapter with that clause as primary
- [ ] Every evidence type from concept.md appears in ≥1 chapter

### Sequence Check
- [ ] No chapter requires a concept taught *later* (pedagogical flow)
- [ ] No chapter evidences a clause before the clause is introduced (logical flow)
- [ ] Narrative hooks open chapters; narrative bridges close them

### Load Check
- [ ] No 3+ consecutive high-cognitive-load chapters
- [ ] Synthesis/reflection chapters after evidence-dense sections
- [ ] Application chapters spaced for practice intervals

### Audience Check
- [ ] Practitioner: Solution appears by Chapter 3-4
- [ ] Aspirant: First "doable" action by Chapter 2
- [ ] Decision-Maker: Decision framework by Chapter 2
- [ ] Generalist: First "aha" insight by Chapter 2
- [ ] Skeptic: Methods/limitations discussed by Chapter 3

---

## Common Mapping Failures

| Failure | Symptom | Fix |
|---------|---------|-----|
| **Orphan Clause** | Thesis claim never evidenced | Add chapter or merge into existing evidence chapter |
| **Reverse Dependency** | Chapter 4 needs concept from Chapter 7 | Reorder or add bridge chapter |
| **Evidence Cluster** | 5 chapters use case studies; 0 use data | Redistribute evidence types |
| **Cognitive Cliff** | Chapters 3-5 all high-load | Insert synthesis/reflection chapter |
| **Thesis Drift** | Chapters 8-10 address different thesis | Cut or spin off; refocus on core thesis |
| **Audience Abandonment** | Practitioner sees no application until Ch 10 | Front-load quick win; move application up |
