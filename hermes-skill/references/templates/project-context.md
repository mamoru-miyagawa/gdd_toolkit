# Project Context — `.design-context/`

This is the skill's second brain. Every design decision, rationale, tension, and rejected idea lives here. It is separate from the GDD (which is the formal deliverable).

## Initialize

Run this when starting a new project:

```
.design-context/
├── index.md               # Project overview, current status, pillar snapshot
├── design-log.md           # Chronological log of every design decision + rationale
├── pillars.md              # Current pillars + their full evolution history
├── rejected-ideas.md       # Ideas considered, and why they were rejected
├── open-questions.md       # Design questions not yet resolved
├── tensions.md             # Known pillar-pillar and feature-feature tensions
├── mda-analyses/           # MDA analysis results
├── code-audits/            # GDD-vs-code comparison results
├── design-reviews/         # Design Judge verdicts
└── brainstorming/          # Raw notes, half-formed ideas (less structured)
```

## File templates

### index.md
```markdown
# Project: <name>

**Current phase:** <pre-production / production / live-ops>
**Pillars:** <N defined, N locked, N under review>
**GDD status:** <N sections complete / N total>
**Last code audit:** <date>
**Last design review:** <date> — <verdict>

## Open questions (summary)
- <critical question>
- <open question>

## Current tensions
- <pillar A> × <pillar B>: <what the tension is about>
```

### design-log.md
```markdown
# Design Log

## 2026-07-24
**Decision:** Added wall-running as a movement option
**Rationale:** Playtest showed players wanted more vertical mobility in combat. 
  Pillar check: serves "Fluid acrobatic movement" ✓
  Pairwise matrix: updated (WallRun + Attack, WallRun + Shoot)
**Alternative considered:** Double-jump instead. Rejected because it would 
  make aerial combat too easy (Pillar: "Punishing but fair").
**Tensions:** WallRun + Combat creates camera challenges in tight corridors. 
  Noted in tensions.md.
**Status:** Documented in GDD §4.2, implemented in Movement.cs (branch: feat/wallrun)

## 2026-07-23
...
```

### pillars.md
```markdown
# Design Pillars

## Current Pillars (locked)

### Pillar 1: Fluid Acrobatic Movement
  Statement: The player can chain movement actions without interruption.
  Enables: Wall-running, slide, air-dash combo chains
  Forbids: Animation-locked movement, canned traversal animations
  Verify: Player chains 3+ movement actions without feeling blocked
  Tensions: Combat precision (fast movement makes aiming harder)

### Pillar 2: Punishing But Fair Combat
  Statement: The player knows why they died and feels they could have avoided it.
  Enables: Telegraph-heavy enemy attacks, consistent hitboxes, clear feedback
  Forbids: Random damage, invisible kill zones, inconsistent timing
  Verify: Player's "that's bullshit" rate < 1 per session
  Tensions: Fluid movement (harder to make fair when players move fast)

### Pillar 3: Systemic Discovery
  Statement: The player learns new interactions by experimenting, not reading.
  Enables: Physics interactions, elemental combos, hidden mechanics
  Forbids: Tutorial pop-ups for every system, ability gating
  Verify: Players discover undocumented interactions in playtest
  Tensions: Narrative control (emergent gameplay can break story sequence)

## Pillar Evolution

2026-07-20: Initial pillars drafted
2026-07-24: Split "Fast Combat" into "Fluid Acrobatic Movement" + "Punishing But Fair Combat"
  Why: Playtesting showed two distinct experiences being conflated
```

### tensions.md
```markdown
# Design Tensions

## Active Tensions

### Fluid Movement × Fair Combat
  Nature: The faster the player moves, the harder it is to design fair combat.
  Current approach: Enemy attack telegraphs scale with player velocity.
  Open question: Does this make enemies too predictable at close range?

### Systemic Discovery × Narrative Control
  Nature: Player-driven discovery can bypass story-gated content.
  Current approach: Narrative-critical paths disable physics interactions.
  Risk: Players notice the restriction and feel the "invisible wall."

## Resolved Tensions

### <none yet>
```
