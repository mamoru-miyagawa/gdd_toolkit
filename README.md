<p align="center">
  <span style="font-size: 5em;">📖</span>
</p>

<h1 align="center">GDD Toolkit</h1>

<p align="center">
  <strong>a game design document, written through conversation</strong>
</p>

<p align="center">
  A plugin/skill for AI agents that helps you write a GDD. It asks questions, challenges your ideas, and remembers your reasoning — but never makes decisions for you. Works with Claude Code, OpenCode, Hermes, and any chat LLM.
</p>

<p align="center">
  <a href="https://github.com/mamoru-miyagawa/gdd_toolkit/stargazers"><img src="https://img.shields.io/github/stars/mamoru-miyagawa/gdd_toolkit?style=flat&color=yellow" alt="Stars"></a>
  <a href="https://github.com/mamoru-miyagawa/gdd_toolkit"><img src="https://img.shields.io/badge/works_with-Claude%20%7C%20OpenCode%20%7C%20Hermes%20%7C%20any%20LLM-orange?style=flat" alt="Works with"></a>
  <a href="https://github.com/mamoru-miyagawa/gdd_toolkit/commits/main"><img src="https://img.shields.io/github/last-commit/mamoru-miyagawa/gdd_toolkit?style=flat" alt="Last commit"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/mamoru-miyagawa/gdd_toolkit?style=flat" alt="License"></a>
</p>

<p align="center">
  <a href="#what-it-does">What it does</a> ·
  <a href="#quick-install">Install</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#the-second-brain">Second brain</a> ·
  <a href="#license">License</a>
</p>

---

## What it does

Most AI game design tools treat GDDs as documentation of what's already implemented. This one treats the GDD as a **living database of everything your game is** — planned, built, or just imagined.

You have a conversation about your project. The AI asks you questions, helps you structure the answers, and writes everything to a `.md` file you own. If you have existing code, it reads what's there and extracts features to discuss. If you don't, it helps you build from scratch.

The output is a markdown GDD you can open in Obsidian, view on GitHub, or keep anywhere you like.

---

## Why it exists

Because "make me Minecraft in one prompt" is not game development. Real game design needs:

- A clear vision that guides every decision
- Features that are challenged, not just listed
- Mechanics that are tested against each other
- Designers who make the calls, not AI that decides

This tool is thorough on purpose. You will have to think.

---

## Quick install

### Claude Code (plugin)
```
/plugin marketplace add mamoru-miyagawa/gdd-toolkit
/plugin install gdd@gdd-toolkit
```

### OpenCode / Codex
Copy `AGENTS.md` to your project root. Auto-detected on startup.

### Hermes
```bash
git clone https://github.com/mamoru-miyagawa/gdd_toolkit
bash gdd_toolkit/install.sh
```
Then `/reload-skills` and `/skill gdd-toolkit`.

### Any chat LLM
Open `QUICKSTART.md` and paste the contents as your first message.

### CLI (any OS, Python 3)
```bash
python gdd.py init             # create .design-context/
python gdd.py template GDD-skeleton  # print a template
python gdd.py pillar "..."     # evaluate a pillar
python gdd.py matrix Jump,Run,Attack  # pairwise matrix
python gdd.py status           # check project health
```

---

## How it works

You start by saying you want to write a GDD. The AI walks you through the process. Here's what that looks like in practice:

### Before and after

**Without this tool,** asking an AI to write a GDD gives you a generic template filled with placeholder text. It doesn't know your game, your constraints, or your vision. You get a document. You're on your own.

**With this tool,** the AI asks questions, challenges your answers, and builds the GDD around your specific project. You have a conversation — not a document generation.

### What the conversation feels like

```
You: I want to write a GDD for my game.

AI: Let's start with Vision Lock. What's the game about, in one sentence?

You: It's a platformer where you collect flowers to change the world.

AI: What are the core pillars — the principles that guide every decision?

You: Exploration, emotional storytelling, short play sessions.

AI: Let's define those more precisely.

  PILLAR: Exploration
    Principle: The player discovers the world through curiosity, not waypoints.
    Pushes against: Map markers, linear paths, hand-holding.

  PILLAR: Emotional storytelling
    Principle: The narrative lands through atmosphere and gameplay, not cutscenes.
    Pushes against: Text walls, dialogue trees, lore dumps.

  PILLAR: Short sessions
    Principle: A meaningful experience in 10-15 minutes.
    Pushes against: Long levels, save points, grinding.

  Does this capture what you mean?
```

### When you suggest a feature

```
You: I want to add crafting.

AI: FEATURE: Crafting
     SUMMARY: The player combines flowers to create items.

  Pillar check: "Exploration" — crafting encourages foraging, yes.
                "Short sessions" — crafting menus slow things down, tension.
  Core loop check: Does crafting connect to the core loop? Collecting flowers
                   is already part of the loop — crafting adds a decision point
                   between collection and use.
  Systems it touches: Inventory, UI, Progression.

  This creates tension with "Short sessions" — crafting menus can pause the
  action. Options:
  1. Keep it, accept the tension (log to tensions.md)
  2. Make crafting real-time (no menu, combine by touching)
  3. Skip crafting, focus on the existing loop

  Your call.
```

### The output

The result is a structured markdown file that works as a wiki:

```
GDD.md
├── Executive Summary
├── Design Pillars (3 defined)
├── Core Loop (ASCII → Mermaid in doc)
├── Feature Catalog (8 systems, each with own file)
├── Pairwise Matrix (optional, run on demand)
├── Balance & Tuning (relationships, not hard numbers)
└── Risks & Open Questions
```

Each system gets its own file under `.design-context/systems/` — the GDD links to them. It's a wiki, not a monolith.

### Before vs after

| Without this tool | With this tool |
|---|---|
| "Write a GDD for a platformer" → generic template with `[insert mechanic here]` placeholders | "Let's define your pillars. What's the game about?" → conversation that builds your actual game |
| One huge document nobody reads | Wiki-style with summaries, links, and per-system files |
| Lists features without questioning them | Every feature checked against pillars — "why does this belong?" |
| Numbers treated as truth | Relationships captured, hard numbers understood as placeholders |
| AI makes decisions, you approve | AI challenges, you decide |
| No memory of why things were done | Full decision log with rationale and rejected alternatives |

### Challenge tools (on-demand)

Along the way, you can call on these to test what you've built:

| Say this | It does |
|---|---|
| `pillar gate wall-running` | Checks one feature against your pillars |
| `run the matrix` | Tests every feature against every other — pairwise |
| `MDA this combat system` | Analyzes Mechanics → Dynamics → Aesthetics |
| `balance this weapon set` | Captures relationships between values |
| `audit the code` | Compares GDD features against project code |
| `judge this design` | Full review: pillars, scope, pairs, tuning |
| `pillar judge this` | Deep trace through every pillar |
| `brainstorm enemy types` | Generates ideas, evaluates against pillars |

You always decide. The AI challenges, recommends, and remembers — but never changes your GDD without you saying so.

---

## The second brain

The AI maintains a `.design-context/` folder next to your project — separate from the GDD. This is where it stores decisions, rationale, tensions, rejected ideas, and open questions.

The GDD is the formal deliverable. The context file is the AI's memory. You can keep changing your mind, discussing options, and exploring dead ends — the GDD only gets the final decisions.

---

## What it's not

- Not a GDD generator. You have to think.
- Not a "make me a game" tool. It asks more questions than it answers.
- Not a documentation of what exists. It's a database of what your game is, planned and built.

---

## License

MIT
