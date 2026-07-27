---
name: gdd-toolkit
description: Helps you write a GDD and challenges it against your pillars. Reads project code, cross-references mechanics pairwise, applies MDA. Never decides for you.
version: 2.3.0
author: Mamoru Miyagawa
license: MIT
metadata:
  hermes:
    tags: [game-design, gdd, mda-framework, code-analysis, design-pillars, pairwise-analysis, second-brain]
    related_skills: [fable-method, fable-judge, writing-plans]
---

# GDD Toolkit

**The primary goal is helping you write a Game Design Document.** Everything below is a tool you can choose to run against what you already have.

This skill writes, reads, challenges, and leaves decisions to you. It does not generate placeholder content, write story, or make choices.

---

## Two modes

### Mode 1 — Write the GDD

You say "let's write the GDD." The skill guides you through:

**Step 1: Vision Lock** — define pillars, audience, genre, scope.
Done when pillars.md has entries, scope budget is set, and you confirm.

**Step 2: Core Loop** — find the minimum fun unit. What's the simplest repeatable thing the player does that they keep wanting to do? Keep it tight — you define the length.
Show it as ASCII in chat, save as Mermaid in the doc.
Done when an ASCII loop is drawn, you approve, and the Mermaid version is saved.

**Step 3: Feature & System Design** — add features one at a time. Each goes through the Pillar Gate. Always start with a plain-language summary so you know what you're evaluating.

Each system gets its own file at `.design-context/systems/NN-name.md`. The GDD links to these — it's a wiki, not a monolith.

The Pillar Gate produces a verdict recorded in the system file:
- **PASS** — serves pillars, connects to loop, scope justified, no contradictions.
- **PASS with N flags** — passes with tracked issues. Each flag is `RESOLVED <date>`, `DEFERRED`, or `open` (spawns an Open Question).
- **BLOCK** — contradiction unresolved, cannot proceed until you decide.

Resolved flags often spawn code change queue items or new open questions. Both are tracked.

If the skill spots a tension, it surfaces it: "This feature supports Pillar A but creates tension with Pillar B because reason. How do you want to handle this?"

Done when every proposed feature has a system file with a verdict.

**Step 4: Flowcharts** — show ASCII in chat, save Mermaid in the doc.
Show flowcharts as ASCII in conversation. Save the Mermaid version to the GDD file for rendered viewing.

**Step 5: GDD Output** — written wherever you decide: a single `GDD.md`, a `/gdd/` folder, or whatever works. The GDD is a wiki — summaries with links to deeper docs, grouped by system or subject.

### Mode 2 — Challenge tools (on demand)

Once you have a GDD, run any tool to test it:

| Say this | It does |
|---|---|
| `"audit the code"` | Read GDD + scan project code. Compare feature sets. Surface deltas. The audit surfaces what's implemented vs documented vs missing. You decide which is truth. |
| `"pillar gate <feature>"` | Check one feature against your pillars, core loop, systems, scope, contradictions. |
| `"run the matrix"` | Test every feature against every other. Jump + Attack? Run + Shoot? Each pair documented with edge cases. |
| `"MDA this"` | Mechanics → Dynamics → Aesthetics for a feature or scenario. Predicts what the player actually experiences, compares against pillars, flags gaps. |
| `"balance this"` | Capture the intent and relationships between values for a system. Hard numbers are placeholders — what matters is the relationship. |
| `"judge this design"` | Full adversarial review: pillars, scope, pairs, tuning, code drift. Delivers a verdict as a recommendation — you decide what to act on. |
| `"pillar judge this"` | Deep trace of one thing through every pillar. Traces support, tension, and trade-offs for each pillar, then states the overall trade-off. |
| `"brainstorm <topic>"` | Generate ideas. Evaluate each against your pillars. You decide what stays. |

The skill never modifies your GDD without you asking. It reads, analyzes, challenges, and writes to `.design-context/`. The GDD changes only when you say so.

Reference material is available in the skill folder: `references/failure-modes.md` lists 20 design frauds the Design Judge hunts, `references/flowcharts.md` has the full methodology as executable mermaid charts, and `references/domains/TEMPLATE.md` is the schema for genre-specific adapters. Templates are listed under `python gdd.py template`.

---

## CLI Tool: `gdd.py`

The repo includes a standalone Python tool that works on any agent, any OS — no dependencies.

| Command | What it does |
|---|---|
| `python gdd.py init` | Create `.design-context/` in current directory |
| `python gdd.py template GDD-skeleton` | Print a template (also: system-design, core-loop-canvas, balance-table, mda-reference, project-context) |
| `python gdd.py pillar "phrase"` | Evaluate a pillar for clarity and direction |
| `python gdd.py matrix Jump,Run,Attack` | Generate a pairwise matrix from comma-separated features |
| `python gdd.py status` | Scan for GDD + `.design-context/` health |

The agent runs these when you ask; you can run them directly.

---

## The second brain (`.design-context/`)

The skill keeps a sidecar folder alongside your project — separate from the GDD. The GDD is the formal deliverable. `.design-context/` is the skill's memory. It stores decisions, rationale, tensions, rejected ideas, and open questions.

```
.design-context/
├── design-log.md           # Every decision + rationale
├── pillars.md              # Current pillars + evolution history
├── tensions.md             # Known conflicts
├── open-questions.md       # Unresolved questions (resolved ones go to bottom, not deleted)
├── code-change-queue.md    # Design decisions made, awaiting code implementation
├── rejected-ideas.md       # What was considered and why it was cut
├── mda-analyses/           # MDA results
├── code-audits/            # GDD-vs-code comparisons
├── design-reviews/         # Design Judge verdicts
├── brainstorming/          # Raw notes
└── systems/                # One file per feature/system
```

The skill reads `.design-context/` at session start and writes to it after every interaction. You can read it too — it's plain markdown.

---

## Design Pillars

Pillars are the **conceptual and contextual rules** that guide every design decision. They capture what the game is about and what it pushes against. See `references/pillars-reference.md` for examples and full anatomy.

The central rule: **every design decision traces to at least one pillar.** If it doesn't, it's either an unstated pillar (name it and log it), scope creep, or decoration. The skill surfaces this. You decide.

---

## How to communicate

Use plain language. Summarize the feature in one sentence before discussing it. No code snippets, formulas, or engine terminology. Write for the least technical person in the room.

---

## Design Pillars reference

Detailed pillar anatomy with examples. See `references/pillars-reference.md`.

---

## Code Audit

Reads your GDD and project code, compares feature sets:

```
F_gdd ∩ F_code  = Implemented + documented → verify match
F_gdd \ F_code  = Documented but unimplemented → WIP or removed?
F_code \ F_gdd  = Implemented but undocumented → new features to add?
```

For each match, it deep-compares: do the tuning values match? Do behaviors match the spec?

**The audit surfaces deltas. You decide which is truth.**

---

## Common Pitfalls

1. **Pillars too vague.** "Fun" filters nothing. Each pillar needs something it pushes against.
2. **Running all tools at once.** The challenge tools are deep. Run one at a time.
3. **Letting GDD and code diverge.** Run the code audit periodically.
4. **Not logging overrides.** Every accepted tension is a decision future-you will need.
5. **GDD as one-time document.** Treat it as living documentation.

---

## Verification Checklist

- [ ] GDD exists or is being written
- [ ] Pillars are defined with clear direction and something they push against
- [ ] `.design-context/` has a design-log entry for the session
- [ ] All tensions surfaced have been addressed or explicitly accepted
- [ ] Designer has made all final decisions — the skill has not silently decided anything
