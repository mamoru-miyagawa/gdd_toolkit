# GDD Toolkit

**The primary goal is helping you write a Game Design Document.** Everything below is a tool you can choose to run against what you already have.

This does NOT generate placeholder content, write story for you, or make decisions. It writes, reads, challenges, and leaves decisions to the user.

---

## Two modes

### Mode 1 — Write the GDD

**1. Vision Lock** — define pillars, audience, genre, scope.
Done when pillars are defined, scope budget is set, and the user confirms.

**2. Core Loop** — find the minimum fun unit. What's the simplest repeatable thing the player does that they keep wanting to do? Keep it tight — the user defines the length. Show as ASCII in chat, save as Mermaid in the doc.
Done when an ASCII loop is drawn, user approves, Mermaid saved.

**3. Feature & System Design** — add features one at a time, each checked against the pillars. Each system gets its own file under `.design-context/systems/NN-name.md`. Always start with a plain-language summary.

The Pillar Gate produces a verdict:
- **PASS** — serves pillars, connects to loop, scope justified, no contradictions.
- **PASS with N flags** — each flag is `RESOLVED <date>`, `DEFERRED`, or `open` (spawns an OQ).
- **BLOCK** — contradiction unresolved, cannot proceed until the user decides.

Done when every proposed feature has a system file with a verdict.

**4. GDD Output** — wherever the user decides: `GDD.md`, `/gdd/` folder, or whatever works. The GDD is a wiki — summaries with links to deeper docs, grouped by system or subject.

### Mode 2 — Challenge tools (on demand)

| Trigger | What happens |
|---|---|
| "audit the code" | Read GDD + scan project code. Compare feature sets. Surface deltas. User decides which is truth. |
| "pillar gate <feature>" | Check one feature against pillars, core loop, systems, scope, contradictions. |
| "run the matrix" | Test every feature against every other. One pair at a time. |
| "MDA this" | Apply Mechanics-Dynamics-Aesthetics to a feature or scenario. Flags mismatches between pillars and predicted player experience. |
| "balance this" | Document the intent and relationships between values for a system. Hard numbers are placeholders. |
| "judge this design" | Full adversarial review: pillars, scope, pairs, tuning, code drift. Verdict is a recommendation. User decides. |
| "pillar judge this" | Deep trace of one thing through every pillar. Traces support, tension, and trade-offs. |
| "brainstorm <topic>" | Generate ideas. Evaluate each against the pillars. User decides. |

The skill never modifies the GDD without asking. Reference material is at `references/failure-modes.md` (design frauds) and `references/flowcharts.md` (methodology as charts).

---

## The second brain (`.design-context/`)

A sidecar folder alongside the project — the GDD is the deliverable, `.design-context/` is the memory. Stores decisions, rationale, tensions, rejected ideas, open questions.

```
.design-context/
├── design-log.md           # Every decision + rationale
├── pillars.md              # Pillars + evolution history
├── tensions.md             # Known conflicts
├── open-questions.md       # Unresolved questions (resolved goes to bottom)
├── code-change-queue.md    # Decisions awaiting implementation
├── rejected-ideas.md       # What was considered and why it was cut
├── mda-analyses/           # MDA results
├── code-audits/            # GDD-vs-code comparisons
├── design-reviews/         # Design Judge verdicts
├── brainstorming/          # Raw notes
└── systems/                # One file per feature/system
```

---

## Design Pillars

Pillars are the **conceptual and contextual rules** that guide every design decision. They capture what the game is about and what it pushes against.

**Central rule:** every design decision traces to at least one pillar. If it doesn't, it's either an unstated pillar, scope creep, or decoration. The assistant surfaces this. The user decides.

Examples and full anatomy are in the repo at `hermes-skill/references/pillars-reference.md`.

---

## How to communicate

Use plain language. Summarize the feature in one sentence before discussing it. No code snippets, formulas, or engine terminology. Write for the least technical person in the room.

---

## Pillar Gate

Before adding any feature, lead with a brief summary. Then run the checks:

```
FEATURE: Wall-running
SUMMARY: The player can sprint along walls for a short distance.

Does it support the pillars?         → yes/tension
How does it connect to the core loop? → which phase
Which systems does it touch?          → list every system
What's the scope cost?                → trade-off named
Does it contradict anything?          → check existing features
```

The verdict goes into the system file. Always start with the summary — the user needs context before evaluation.

---

## Flowcharts in chat

Show flowcharts as ASCII in conversation. Save the Mermaid version to the GDD file for rendered viewing.

---

## Pairwise Interaction Matrix

Every feature against every other. Run on demand.

```
PAIR: Jump + Attack
  Simultaneous? YES
  Result: Aerial attack. One swing per jump. Resets on landing.
  Status: ✅ Documented

PAIR: Run + Shoot
  Simultaneous? YES
  Result: Speed -30%, spread +50%. Sprint cancels on first shot.
  Status: ⚠ Not yet documented
```

Pairs with undocumented interactions get flagged. The user decides.

---

## Code Audit

Compare GDD features against project code:

```
F_gdd ∩ F_code  = Implemented + documented → verify match
F_gdd \ F_code  = Documented but unimplemented → WIP or removed?
F_code \ F_gdd  = Implemented but undocumented → new features to add?
```

The audit surfaces deltas. The user decides which is truth.

---

## CLI Tool: `gdd.py`

Standalone Python tool, no dependencies.

| Command | What it does |
|---|---|
| `python gdd.py init` | Create `.design-context/` |
| `python gdd.py template GDD-skeleton` | Print a template |
| `python gdd.py pillar "phrase"` | Evaluate a pillar |
| `python gdd.py matrix Jump,Run,Attack` | Generate pairwise pairs |
| `python gdd.py status` | Check project health |
