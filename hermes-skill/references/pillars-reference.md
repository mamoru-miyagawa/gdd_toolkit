# Design Pillars — Reference

Pillars are the **conceptual and contextual rules** that guide every design decision. They are not rigid checklists.

## Anatomy

A well-defined pillar has three parts:

- **Principle** — the core idea, one sentence. What is this game about?
- **How it guides decisions** — how you use this pillar to evaluate features. A lens, not a rule.
- **What it pushes against** — the kinds of features this pillar resists. A pillar that never conflicts filters nothing.

## Examples

```
PILLAR: Emergent Chaos
  Principle: The game creates interesting situations through system interactions, not scripted events.
  Guides decisions: Features that enable player-driven stories get priority.
  Pushes against: Scripted set-pieces, linear progression, dialogue trees.

PILLAR: Learn by Doing
  Principle: The player figures out mechanics through experimentation, not reading.
  Guides decisions: Tutorials are environmental, systems are intuitive, failure is informative.
  Pushes against: Text pop-ups, ability gating, modal tutorial levels.

PILLAR: Short Sessions
  Principle: A meaningful experience in 10-15 minutes.
  Guides decisions: Levels are designed for short play windows, save states are generous.
  Pushes against: Long levels, save points, grinding, story cutscenes.
```

## Good tests

A well-defined pillar passes these checks:
- **You can name what it pushes against.** If no feature could ever conflict with it, it's not filtering anything.
- **You can see it in a playtest.** Not as a testable hypothesis, but as a direction you'd recognise if it was missing.
- **It makes some decisions easy.** "Does this fit?" should have a clear answer for most features.

## Evolution

Pillars can change — refined, split, merged. Log every change to `.design-context/pillars.md` with the rationale. The evolution history is as important as the current pillars.
