# MDA Framework Reference

The MDA framework (Mechanics, Dynamics, Aesthetics) was formalized by Robin Hunicke, Marc LeBlanc, and Robert Zubek in their 2004 paper "MDA: A Formal Approach to Game Design and Game Research."

**Source:** https://en.wikipedia.org/wiki/MDA_framework

---

## The Three Layers

```
┌────────────────────────────────────────────┐
│               AESTHETICS                    │
│        ┌─── What the player feels          │
│        │   (emotional response)            │
│        ▼                                   │
│  ┌────────────────────────────────────┐    │
│  │           DYNAMICS                  │    │
│  │    ┌─── What emerges when           │    │
│  │    │    the player plays            │    │
│  │    ▼                               │    │
│  │  ┌──────────────────────────┐      │    │
│  │  │      MECHANICS            │      │    │
│  │  │  ┌─── The rules,         │      │    │
│  │  │  │    systems, code      │      │    │
│  │  │  ▼                      │      │    │
│  │  │  (designer controls)     │      │    │
│  │  └──────────────────────────┘      │    │
│  └────────────────────────────────────┘    │
└────────────────────────────────────────────┘
```

**Key insight:** Designers create mechanics. Players experience aesthetics. Dynamics bridge the gap — they're what the mechanics produce when a real player engages with them.

---

## The 8 Aesthetic Types (LeBlanc, 2004)

| # | Aesthetic | Description | Example mechanics that produce it |
|---|---|---|---|
| 1 | **Sensation** | Game as sense-pleasure | Visual effects, haptic feedback, sound design, screen shake, particle systems |
| 2 | **Fantasy** | Game as make-believe | Narrative framing, character role, world-building, immersion systems |
| 3 | **Narrative** | Game as drama | Story, character arcs, branching choices, plot twists, cutscenes |
| 4 | **Challenge** | Game as obstacle course | Difficulty scaling, time pressure, skill gates, puzzle complexity, boss fights |
| 5 | **Fellowship** | Game as social framework | Multiplayer, co-op, guilds, leaderboards, shared goals, trading |
| 6 | **Discovery** | Game as uncharted territory | Exploration, secrets, hidden mechanics, emergent systems, player-driven goals |
| 7 | **Expression** | Game as self-discovery | Customization, build variety, creative tools, player choices with consequences |
| 8 | **Submission** | Game as pastime | Grind, collection, routine tasks, idle play, mindless repetition (can be positive: flow, negative: drudgery) |

---

## Common MDA Mismatches

| Designer says | Player experiences | Problem |
|---|---|---|
| "Deep tactical combat" | Sensation (flashy effects) + Submission (button mashing) | Aesthetics are Challenge, but mechanics reward speed not thought |
| "Open world discovery" | Submission (map icon checklist) | Pillars say Discovery, mechanics produce grind |
| "Player expression" | Fellowship (one build is optimal, everyone uses it) | Expression requires viable alternatives; dominant strategy kills it |
| "Narrative-driven" | Challenge (hard combat gates story progress) | Narrative aesthetic blocked by skill requirement |
| "Social experience" | Submission (grinding alone to unlock social features) | Fellowship locked behind solo play |

---

## Debugging with MDA

When a game isn't delivering the intended experience:

1. **Check the mechanics** — are the rules producing the dynamics you expect?
2. **Check the dynamics** — what are players actually doing? (not what you intended)
3. **Check the aesthetics** — what do players say they feel?
4. **Identify the gap** — is it a mechanics→dynamics problem (rules produce wrong behavior) or dynamics→aesthetics problem (behavior produces wrong feeling)?
5. **Fix the lower layer** — change mechanics to shift dynamics, which shifts aesthetics.

---

## How to Use MDA in Design

**Before building:** Predict the MDA profile. "If I have these mechanics, what dynamics will emerge, and what aesthetics will the player feel?" If the predicted aesthetics don't match the pillars, change the mechanics before building.

**After prototyping:** Verify the MDA profile. "The player is doing X (dynamics) and reporting Y feeling (aesthetics). Does this match the prediction?"

**During iteration:** Use MDA to identify which layer is broken. Don't add mechanics when the problem is dynamics (players know what to do but aren't enjoying it). Don't change aesthetics targets when the problem is mechanics (rules don't produce the intended behavior).
