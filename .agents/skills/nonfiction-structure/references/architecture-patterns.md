# Nonfiction Architecture Patterns

## The Four Primary Architectures

Every nonfiction book has an argument architecture — the logical skeleton that holds the thesis up. Choose the one that makes your thesis *easiest to prove* for *this* audience.

---

### 1. Problem-Solution
**Logic:** Diagnose → Prescribe
**Reader Journey:** "I have this problem" → "Here's why it happens" → "Here's the solution" → "Here's how to implement it"

**Structure:**
```
Part I: The Problem (Diagnosis)
  Ch 1: The Symptom — What the reader sees/feels
  Ch 2: The Root Cause — Why common fixes fail
  Ch 3: The Cost — What happens if unsolved

Part II: The Solution (The Thesis)
  Ch 4: The Core Insight — The big idea
  Ch 5: The Framework — Mental model / method
  Ch 6: The Evidence — Why it works

Part III: Implementation (Application)
  Ch 7: Getting Started — Quick win
  Ch 8: Scaling / Adapting — Real-world complexity
  Ch 9: Troubleshooting — Failure modes
  Ch 10: Mastery — Beyond the basics
```

**Best For:**
- Prescriptive thesis ("How to do X better")
- Practitioner audience (wants solution *now*)
- Decision-Maker audience (needs decision framework)
- Thesis with clear "before/after" transformation

**Variants:**
- **Decision-Framework**: Part I = Decision Context, Part II = Evaluation Criteria, Part III = Pilot Design
- **Diagnostic**: Heavy Part I (problem space), lighter Part II (solution is "it depends")

---

### 2. Chronological / Process
**Logic:** Sequence → Mastery
**Reader Journey:** "I'm at the start" → "Step 1" → "Step 2" → ... → "I've arrived"

**Structure:**
```
Part I: Foundation (Before You Begin)
  Ch 1: The Landscape — What you're entering
  Ch 2: The Mindset — How to think about this
  Ch 3: The Setup — Prerequisites, tools, environment

Part II: The Process (Sequential Steps)
  Ch 4: Phase 1 — [First major milestone]
  Ch 5: Phase 1 Deep Dive — Common pitfalls
  Ch 6: Phase 2 — [Second milestone]
  Ch 7: Phase 2 Deep Dive — Integration
  Ch 8: Phase 3 — [Third milestone]
  Ch 9: Phase 3 Deep Dive — Edge cases

Part III: Beyond the Process
  Ch 10: Graduation — You can do this independently
  Ch 11: Teaching Others — Scaling your impact
  Ch 12: What's Next — Advanced paths
```

**Best For:**
- Developmental thesis ("How to become X")
- Aspirant audience (needs scaffolded path)
- Any thesis where sequence *matters* (you can't do step 3 before step 1)
- Skill acquisition, career transitions, project-based outcomes

**Variants:**
- **Project-Based**: Each chapter = one project deliverable
- **Sprint-Based**: Time-boxed cycles (Week 1, Week 2, Month 1, Month 3)

---

### 3. Conceptual / Principle-Based
**Logic:** Principles → Synthesis
**Reader Journey:** "Here's a principle" → "Here's another" → "See how they connect" → "Now you have a lens"

**Structure:**
```
Part I: Foundational Principles (The Lens)
  Ch 1: Principle 1 — [Core concept]
  Ch 2: Principle 2 — [Core concept]
  Ch 3: Principle 3 — [Core concept]

Part II: Principles in Action (Application)
  Ch 4: Domain A — Principles applied to [context]
  Ch 5: Domain B — Principles applied to [context]
  Ch 6: Domain C — Principles applied to [context]

Part III: Synthesis (The Unified Model)
  Ch 7: The Integrated Framework — How principles interact
  Ch 8: Boundary Conditions — Where this breaks
  Ch 9: Implications — What this means for [broader field]
  Ch 10: The Big Idea Restated — Now with full weight
```

**Best For:**
- Explanatory thesis ("Why X works / The truth about X")
- Generalist audience (building mental models)
- Skeptic audience (evidence-ordered principles)
- Framework books, theory books, synthesis books
- Thesis with multiple independent but related claims

**Variants:**
- **Evidence-Ordered**: Principles ordered by evidence strength (strongest first)
- **Counter-Intuitive**: Principles ordered by surprise factor (most surprising first)
- **Historical/Intellectual History**: Principles ordered by discovery/evolution

---

### 4. Hybrid
**Logic:** Combined — serves thesis with multiple logics
**Reader Journey:** Depends on combination

**Common Hybrids:**

| Primary + Secondary | When to Use | Structure |
|---------------------|-------------|-----------|
| Problem-Solution + Chronological | Solution *is* a process | Part I: Problem, Part II: Solution Process (chronological), Part III: Mastery |
| Problem-Solution + Conceptual | Solution requires new mental model | Part I: Problem, Part II: Principles (conceptual), Part III: Application |
| Chronological + Conceptual | Process teaches principles | Each phase teaches a principle; synthesis at end |
| Conceptual + Problem-Solution | Principles solve specific problems | Part I: Principles, Part II: Problem-Solution case studies |

**Hybrid Rules:**
- One architecture *leads* (primary); the other *supports* (secondary)
- The reader must always know "where am I in the argument?"
- Transitions between logics must be explicit: "Now that we have the principles, let's apply them..."
- Don't mix more than two — cognitive overload

---

## Architecture Selection Decision Tree

```
START: What is the thesis TYPE?
│
├─ Prescriptive ("Do X") → Problem-Solution
│   └─ Is the "how" a sequence? → Hybrid: Problem-Solution + Chronological
│
├─ Developmental ("Become X") → Chronological
│   └─ Does each step teach a principle? → Hybrid: Chronological + Conceptual
│
├─ Explanatory ("Why X / Truth about X") → Conceptual
│   ├─ For Generalist → Conceptual (narrative-ordered)
│   └─ For Skeptic → Conceptual (evidence-ordered)
│
├─ Evaluative ("Evidence for/against X") → Conceptual (evidence-ordered)
│
├─ Decision ("How to choose X") → Problem-Solution (Decision-Framework variant)
│
└─ Multi-clause thesis → Hybrid
    ├─ Map clauses to architectures
    └─ Choose primary = architecture serving most clauses
```

## Architecture × Audience Cognitive Load

| Architecture | Practitioner | Aspirant | Decision-Maker | Generalist | Skeptic |
|--------------|--------------|----------|----------------|------------|---------|
| Problem-Solution | ★★★ (native) | ★★ (needs scaffolding) | ★★★ (decision variant) | ★★ (if problem relatable) | ★ (wants evidence first) |
| Chronological | ★★ (if process is the work) | ★★★ (native) | ★ (too slow) | ★★ (if journey compelling) | ★ (wants principles) |
| Conceptual | ★ (too abstract) | ★★ (needs concrete anchors) | ★ (decision variant) | ★★★ (native) | ★★★ (evidence-ordered) |
| Hybrid | ★★★ (flexible) | ★★★ (can scaffold) | ★★★ (tailorable) | ★★ (if primary=conceptual) | ★★ (if primary=conceptual) |

★★★ = Native fit | ★★ = Works with adaptation | ★ = Significant friction

---

## Thesis Clause → Architecture Mapping

Decompose your thesis into clauses. Each clause wants an architecture:

| Clause Type | Native Architecture |
|-------------|---------------------|
| "X causes Y" (causal) | Conceptual (evidence-ordered) |
| "To achieve X, do Y" (prescriptive) | Problem-Solution |
| "X develops through stages A→B→C" (developmental) | Chronological |
| "X works *because* of mechanisms A, B, C" (mechanistic) | Conceptual |
| "Choose X when condition Y; choose Z when condition W" (contingent) | Problem-Solution (decision variant) |
| "The history of X reveals pattern Y" (historical) | Chronological (intellectual history) |

**If clauses pull different ways → Hybrid.** Map each clause to its native architecture, then design a structure that serves the *primary* thesis while giving each clause its due.
