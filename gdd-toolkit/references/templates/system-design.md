# System Design Template

Use this template for every system in the game. One file per system.

---

## System: <name>

**Classification:** Core System / Secondary System / Content Feature
**Scope Cost:** <complexity points>

### Purpose
<One paragraph: what this system does for the player, why it exists, what experience it enables.>

### Core Loop Connection
<Which phase of the core loop this system touches, and how. If it doesn't touch the core loop, explain why it exists anyway.>

### Pillars Served
- <Pillar 1>: <how>
- <Pillar 2>: <how>

---

### Inputs

What data, state, or player action feeds into this system:

| Input | Source | Type | Required? |
|---|---|---|---|
| <name> | <player / system / game state> | <boolean / float / trigger> | Yes / No |
| <name> | <player / system / game state> | <boolean / float / trigger> | Yes / No |

### Process

The rules, formulas, and logic that transform inputs into outputs:

```
<Formula or pseudocode>
```

**State Machine:** (if applicable)

```
States: Idle → Active → Resolving → Cooldown → Idle
Transitions:
  Idle → Active: player input received
  Active → Resolving: conditions met
  Resolving → Cooldown: output delivered
  Cooldown → Idle: timer expires
```

### Outputs

What this system produces:

| Output | Consumer | Type | Range |
|---|---|---|---|
| <name> | <player feedback / other system / game state> | <number / event / state change> | <min-max> |

---

### System Interactions

Every system this touches. "None" is not valid — even UI and audio count.

| System | Interaction Type | Effect |
|---|---|---|
| <system A> | Reads from / Writes to / Controls / Is controlled by | <what happens at the boundary> |
| <system B> | Reads from / Writes to / Controls / Is controlled by | <what happens at the boundary> |

### Tuning Levers

| Lever | Min | Max | Default | Effect |
|---|---|---|---|---|
| <name> | <value> | <value> | <value> | <what changing this does to the experience> |

---

### Edge Cases

| Condition | Expected Behavior |
|---|---|
| <edge case scenario> | <what should happen> |
| <edge case scenario> | <what should happen> |

### Failure States

| What can go wrong | Symptom | Recovery |
|---|---|---|
| <failure scenario> | <observable effect> | <how the system or player recovers> |

---

### Pairwise Status

*Updated after each design session.*

| Feature A | Feature B | Status | Interaction |
|---|---|---|---|
| <this system> | <other feature> | ✅ / ⚠ / ❌ | <brief description> |
| <this system> | <other feature> | ✅ / ⚠ / ❌ | <brief description> |
