---
name: game-design-assistant
description: Helps you write a GDD — then challenges it. Reads your code, knows your pillars, cross-references every mechanic against every other, and applies MDA analysis. Always leaves decisions to you.
version: 2.2.0
author: Mamoru Miyagawa
license: MIT
metadata:
  hermes:
    tags: [game-design, gdd, mda-framework, code-analysis, design-pillars, pairwise-analysis, second-brain]
    related_skills: [fable-method, fable-judge, writing-plans]
---

# Game Design Assistant

**The primary goal is helping you write a Game Design Document.** Everything below is a tool you can choose to run against what you already have.

This skill does NOT generate placeholder content, write story for you, or make decisions. It:
- **Writes** — helps you structure and populate a GDD section by section
- **Reads** — loads your existing GDD, project code, and `.design-context/` to understand where you are
- **Challenges** — when you ask, it checks your design against your own pillars, runs the pairwise matrix, applies MDA, and audits code-vs-GDD alignment
- **Leaves decisions to you** — it recommends, flags tensions, and surfaces contradictions. You decide what to do. Every override is logged so future-you knows why.

---

## How it works: two modes

### Mode 1 — Write the GDD (the primary path)

You say "let's write the GDD" or start a new project. The skill guides you through:

1. **Vision Lock** — define pillars, audience, genre, scope. These become the filter for every decision.
2. **Core Loop** — find the minimum fun unit. What's the simplest repeatable thing the player does that they keep wanting to do? 3-5 nodes max. Show it as ASCII in chat, save as Mermaid in the doc.
3. **Feature & System Design** — add features one at a time. Each goes through the Pillar Gate.
4. **Pairwise Matrix** — every feature tested against every other. You choose when to run it.
5. **Balance & Tuning** — capture the intent and relationships between values. Hard numbers are placeholders that will change during balancing. What matters is: is this gun faster or slower than that one? Does it deal more or less damage? By how much (roughly)?
6. **Documentation** — structured GDD output you own.

At any point you can say "I want to add a feature" and the skill will help you write it, then surface what it might conflict with — and ask you what you want to do.

### Mode 2 — Challenge what you have (on-demand tools)

You have a GDD (or a draft, or code) and want to test it. Run any tool:

| Say this | And the skill will |
|---|---|
| "audit the code" | Read your GDD, scan your project, compare feature sets. Surface deltas. |
| "pillar gate this feature" | Check one feature against your pillars, core loop, systems, scope, contradictions. |
| "run the matrix" | Test every feature against every other. One pair at a time. |
| "MDA this" | Apply Mechanics-Dynamics-Aesthetics to a feature or scenario. Predict what the player actually experiences. |
| "judge this design" | Full adversarial review: pillars, scope, pairs, tuning, code drift. |
| "pillar judge this" | Deep trace of one thing through every pillar. Tensions, trade-offs, recommendation. |
| "brainstorm <topic>" | Generate ideas. Then help you evaluate each against your pillars. You decide what stays. |

**The skill never modifies your GDD without you asking.** It reads, analyzes, challenges, and writes to `.design-context/` — your GDD only changes when you say so.

---

## The Project Context File (`.design-context/`)

The skill maintains a separate folder — the second brain — alongside your project. This is where it stores:

- **Design log** — every decision and its rationale
- **Pillar evolution** — how pillars changed over time and why
- **Tensions** — known conflicts between pillars, features, systems
- **Rejected ideas** — what was considered and why it was cut
- **Open questions** — things not yet resolved
- **MDA analyses** — analysis results
- **Code audits** — GDD-vs-code comparison snapshots
- **Design reviews** — Design Judge verdicts
- **Brainstorming** — raw notes and half-formed ideas

**The GDD is the formal deliverable. `.design-context/` is the skill's memory.** They are separate. The skill reads `.design-context/` at session start and writes to it after every interaction. You can read it too — it's plain markdown.

### Initialize

```
<project-root>/.design-context/
├── index.md               # Project overview, current status
├── design-log.md           # Chronological log of every decision + rationale
├── pillars.md              # Current pillars + evolution history
├── rejected-ideas.md       # What was considered and why it was rejected
├── open-questions.md       # Questions not yet resolved
├── tensions.md             # Known tensions
├── mda-analyses/           # MDA results
├── code-audits/            # Code audit snapshots
├── design-reviews/         # Design Judge verdicts
└── brainstorming/          # Raw notes
```

---

## Design Pillars

Pillars are the **conceptual and contextual rules** that guide every design decision. They are not rigid checklists — they're principles that tell you whether a feature *belongs* in this game.

A good pillar captures the game's identity in a way that helps you answer "does this belong here?" when you're unsure. It should have a clear direction — it pushes toward some things and pushes against others.

### Examples

```
PILLAR: Emergent Chaos
  Principle: The game creates interesting situations through system interactions, not scripted events.
  Guides decisions: Features that enable player-driven stories get priority.
  Pushes against: Scripted set-pieces, linear progression, dialogue trees.

PILLAR: Learn by Doing
  Principle: The player figures out mechanics through experimentation, not reading.
  Guides decisions: Tutorials are environmental, systems are intuitive, failure is informative.
  Pushes against: Text pop-ups, ability gating, modal tutorial levels.
```

### What to define per pillar

- **Principle** — the core idea, one sentence. What is this game about?
- **How it guides decisions** — how you'd use this pillar when evaluating a feature. A lens, not a rule.
- **What it pushes against** — the kinds of features this pillar resists. A pillar that never conflicts filters nothing.

Pillars can evolve. Log changes to `.design-context/pillars.md`.

### The central rule

**Every design decision traces to at least one pillar.** If it doesn't, it's either an unstated pillar (name it and log it), scope creep, or decoration. The skill surfaces this. You decide.

---

## How to communicate

Use simple, plain language. No code snippets, no numbers, no technical jargon — unless the conversation specifically calls for it.

**When discussing a feature, system, or mechanic:**
1. **Summarize it first** — one or two sentences explaining what it is, in plain language, so the designer knows what you're talking about.
   - Good: "Wall-running lets the player sprint along vertical surfaces for a short distance."
   - Bad: "WallRunStateMachine activates on surface normal check with velocity threshold ≥ 5m/s."
2. **Then discuss it** — ask questions, run checks, surface tensions.
3. **Then let the designer decide.**

**Avoid:** code blocks, formulas, state machine diagrams, technical specs, engine terminology, or anything that assumes engineering knowledge. Save that for the Technical Requirements section of the GDD.

The person writing the GDD might be a designer, a producer, an artist, or someone learning game dev. Write for the least technical person in the room.

---

## Writing the GDD (Mode 1)

### Step 1: Vision Lock

Define pillars, audience, genre, platform, scope. No feature work until this exists.

### Step 2: Core Loop

The 5-15 second cycle the player repeats. Mermaid flowchart + annotated phases.

### Step 3: Feature & System Design

Add features one at a time. **Always start with a plain-language summary of the feature** so the designer knows what they're evaluating. Then run the Pillar Gate questions:

```
FEATURE: Wall-running
SUMMARY: The player can sprint along walls for a short distance, opening new paths and combat angles.

Does it support the pillars?         → <your answer>
How does it connect to the core loop? → <your answer>
Which systems does it touch?          → <your answer>
What's the scope cost?                → <your estimate>
Does it contradict anything?          → <the skill checks>
```

**Never jump straight into checks.** The summary is mandatory — without it the designer doesn't have context for the discussion.

If the skill spots a tension, it surfaces it: "This feature supports <Pillar A> but creates tension with <Pillar B> because <reason>. How do you want to handle this?"

**You decide.** The skill logs the decision and rationale to `.design-context/design-log.md` and continues.

### Step 4: Flowcharts — ASCII in chat, Mermaid in docs

Mermaid is great for rendered docs (Obsidian, GitHub) but **unreadable as raw text in a terminal**. When showing flowcharts in conversation, use ASCII diagrams:

```
  [Observe] ──→ [Decide] ──→ [Act] ──→ [Feedback]
                   ↑                        │
                   └────────────────────────┘
```

Vertical for complex flows:

```
  Player sees enemy
         ↓
  Choose weapon
    ↙      ↘
 Attack   Sneak
    ↓        ↓
 Deal DMG  Bypass
    ↓        ↓
  Enemy    Loot
  reacts   room
```

Save the Mermaid version to the GDD doc file for when it's viewed in a renderer. Never paste raw Mermaid code in a conversation.

### Step 5: Pairwise Interaction Matrix (optional, run on demand)

When you say "run the matrix," the skill tests every feature against every other:

```
PAIR: Jump + Attack
  Can the player do both simultaneously? YES
  Result: Aerial attack. One swing per jump. Resets on landing.
  Edge cases: Timing differs on ascent vs descent.
  Status: ✅ Documented

PAIR: Jump + Shoot
  Can the player do both simultaneously? YES
  Result: Shooting mid-air, momentum preserved.
  Edge cases: Sprint-jump + shoot has accuracy penalty.
  Status: ⚠ Not yet documented — add interaction rules?
```

Pairs with undocumented interactions get flagged. You decide whether to document, change, or accept the gap.

### Step 5: Balance & Tuning

Numbers in a GDD are placeholders — they will change during balancing. Capture the **intent and relationships** between values, not the absolute numbers.

Good:
```
The pistol is the baseline: fast, reliable, low damage.
The rifle is about 2x the pistol's damage but slower.
The shotgun is devastating up close (3-4x pistol) but useless at range.
```

Not useful:
```
Pistol: 10 damage. Rifle: 20 damage. Shotgun: 35 damage.
```
(These numbers will change in the first balancing pass. The relationships are what matter.)

The Design Judge flags "tuning theater" — prose that sounds specific without capturing relationships. "Enemies get harder" is useless. "Enemies scale faster than the player, so fights get shorter and more lethal" captures the intent.

### Step 6: GDD Output

Structured document you own. Written to wherever you want it.

---

## Challenge Tools (Mode 2 — all optional)

### Code Audit

Reads your GDD and project code, compares feature sets:

```
F_gdd ∩ F_code  = Implemented + documented → verify match
F_gdd \ F_code  = Documented but unimplemented → WIP or removed?
F_code \ F_gdd  = Implemented but undocumented → new features to add?
```

For each match, it deep-compares: do the tuning values match? Do behaviors match the spec?

**The audit surfaces deltas. You decide which is truth.** The GDD might be outdated. The code might have drifted. The skill doesn't assume either is right.

### The Design Judge

Full adversarial review. Hunts 20 design frauds including:

- Pillar drift (feature without a pillar)
- Loop orphan (mechanic not connected to core loop)
- Tuning theater (prose that sounds like numbers without capturing relationships — "enemies get harder" vs "enemies scale faster than the player does, so fights get shorter and more lethal")
- GDD-code drift (doc says one thing, code does another)
- MDA mismatch (pillars say X, mechanics produce Y)
- Pillar-pillar denial (active tension ignored)

**Verdict is delivered as a recommendation. You decide what to act on.**

### Pillar Judge (deep trace)

Traces one specific feature, scenario, or question through EVERY pillar, one at a time:

```
Pillar 1: <name> → Supports (intensity 4/5)
Pillar 2: <name> → Tension (intensity 3/5) — fast movement makes fair combat harder
Pillar 3: <name> → Neutral
```

Then states the trade-off: "This strengthens <A> at the cost of <B>. Mitigations available: <...>."

**Recommendation delivered. You decide.**

### MDA Analysis

Applies Mechanics → Dynamics → Aesthetics to a feature or composed scenario.

Predicts what the player will actually experience. Compares against the pillars. Flags gaps:

"Your pillars say this game is about Discovery, but this feature's MDA profile produces Submission. The player will experience grinding, not exploring. Is that intentional?"

**You decide.** Maybe the gap is acceptable. Maybe you want to retune. The skill helps you explore both paths.

### Brainstorming

When you say "brainstorm <topic>," the skill generates ideas and helps you evaluate each against your pillars. It does not add anything to the GDD. It suggests, you filter, you decide.

---

## How the skill behaves

### It challenges — it does not override

When the skill finds a contradiction, tension, or gap, it says:

```
⚠ TENSION DETECTED: <what the tension is>
  → <Feature X> contradicts <Pillar Y> because <reason>
  → Options:
    1. Modify the feature to align with the pillar
    2. Accept the tension (log to .design-context/tensions.md)
    3. Reconsider the pillar (log change to .design-context/pillars.md)
  Your call.
```

It does not proceed silently. It does not make the choice. It presents options and asks.

### It learns your context — it does not assume

At the start of every session, the skill loads:
- The GDD (if it exists)
- `.design-context/` (the evolving memory)
- The project code (if accessible)

It does not start from scratch. It knows what you decided last time and why.

### It logs everything — so you can look back

Every interaction that produces a decision gets logged: what was decided, why, what alternatives were considered, what tensions were accepted. This is how the skill works as a second brain — it remembers what you'd forget.

### It leaves decisions to you — always

The skill recommends. It challenges. It brainstorms. It surfaces tensions and trade-offs.

**It never modifies your GDD without you asking. It never overrides a decision. It never proceeds as if your silence is consent.**

The designer decides. Always.

---

## Common Pitfalls

1. **Pillars too vague.** "Fun" is not a pillar. If you can't name what it pushes against, it's not filtering anything.
2. **Running all tools at once.** The challenge tools are deep. Run one at a time. Let each result inform the next.
3. **Letting the GDD and code diverge.** Run the code audit periodically. A GDD that describes a different game than the code implements is a liability.
4. **Not logging overrides.** Every time you accept a tension or override a recommendation, log it. Future-you will need the context. The skill prompts you to log.
5. **Treating the GDD as a one-time document.** A GDD that isn't updated when the design changes is a historical artifact, not a design tool.
6. **Using the skill to make decisions for you.** The skill challenges and recommends. You decide. If you find yourself accepting every recommendation without thinking, you're not designing anymore.
7. **Designing for an undefined audience.** Every mechanic serves someone. If you don't know who, you're designing for yourself. The skill will ask.

---

## Verification Checklist

- [ ] GDD exists or is being written — this is the primary objective
- [ ] Pillars are defined with a clear direction and something they push against
- [ ] `.design-context/` is initialized and has a design-log entry for the session
- [ ] At least one challenge tool has been run (optional but recommended)
- [ ] All tensions surfaced by the skill have been addressed or explicitly accepted
- [ ] Designer has made all final decisions — the skill has not silently decided anything
- [ ] Design log is current (every decision + rationale recorded)
