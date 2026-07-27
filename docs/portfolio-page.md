# GDD Toolkit

**A game design document, written through conversation.**

*A plugin/skill for AI agents that helps game designers write a GDD — asking questions, challenging ideas, and remembering reasoning, but never making decisions for the designer.*

---

## The problem

Most AI game design tools treat GDDs as documentation of what's already built. You paste your code, the AI writes a spec sheet, and you're done. That misses the point of a GDD entirely.

A Game Design Document should be a **living database of everything a game is** — planned, built, or just imagined. It should capture intent, not just implementation. It should challenge assumptions, not just list features. And it should be written *through conversation*, not through a single "generate" button.

I was tired of seeing "make me Minecraft in one prompt" treated as game development. So I built something different.

---

## What it does

GDD Toolkit is a set of instruction files (skills/plugins) for AI coding agents that turns them into a game design co-pilot. Instead of generating a document, it has a conversation:

**It asks questions** — about pillars, audience, scope, core loop. It doesn't let you skip the hard parts.

**It challenges your features** — every mechanic is checked against your stated pillars. If something doesn't align, it flags the tension and asks what you want to do about it. It doesn't block you, but it makes you think.

**It remembers your reasoning** — decisions, rejected alternatives, open questions, and tensions are all logged in a separate `.design-context/` folder. The GDD itself stays clean; the second brain holds the full history.

**It cross-references mechanics** — on demand, it runs a pairwise interaction matrix that tests every feature against every other. Jump + Attack? Run + Shoot? Attack + Shoot? Each pair gets documented with edge cases.

**It applies the MDA framework** — analyze any feature or scenario through Mechanics → Dynamics → Aesthetics to predict what players actually experience.

**It audits code against the GDD** — compares what's documented against what's actually in the project, surfacing drift between design and implementation.

And critically: **the designer always decides.** The AI challenges and recommends. The human makes the call.

---

## How it works

The process has four phases:

**1. Vision Lock** — define the pillars, audience, genre, and scope. These become the filter for every decision that follows. A pillar captures what the game is about *and* what it pushes against — every good pillar explicitly names something it excludes.

```
PILLAR: Exploration
  Principle: The player discovers the world through curiosity, not waypoints.
  Pushes against: Map markers, linear paths, hand-holding.
```

**2. Core Loop** — find the minimum fun unit. What's the simplest repeatable thing the player does that they keep wanting to do? Keep it tight — the designer defines the length.

**3. Features & Systems** — add features one at a time. Each gets a plain-language summary, then runs through the pillar gate:

- Does it serve a pillar?
- How does it connect to the core loop?
- Which systems does it touch?
- What's the scope cost?
- Does it contradict anything?

Each system gets its own file in `.design-context/systems/`. The GDD links to these — it's a wiki, not a monolith.

**4. GDD Output** — a structured markdown document, written wherever the designer decides. Output is a `.md` file ready for Obsidian, GitHub, or any markdown renderer.

On top of this, the designer can call challenge tools at any point — pairwise matrix, MDA analysis, balance documentation, design judge, pillar judge, code audit, brainstorming.

---

## Design principles

Several ideas shaped how this tool works:

**The GDD and the second brain are separate.** The GDD is the formal deliverable — clean, structured, decision-based. `.design-context/` is the AI's memory — it stores the full conversation: rejected alternatives, open questions, tensions, rationale. The designer can change their mind freely without cluttering the document.

**Pillars are conceptual, not mechanical.** They don't need to be testable hypotheses or rigid checklists. A pillar just needs to capture a direction — something the game is *about* — so it can guide decisions. The most important part of a pillar is what it pushes against.

**Numbers are placeholders.** Tuning values will change during balancing. What matters is the relationship between values — is this gun faster or slower than that one? By roughly how much? Hard numbers are optional and understood as temporary.

**Conversation over generation.** The tool doesn't produce a final document from a single prompt. It walks through each section interactively, asking the designer to think about each decision. The output is better because the process forces engagement.

---

## Technical approach

The toolkit is distributed as a set of markdown instruction files, a Python CLI tool, and a plugin manifest — no dependencies, no build step, works anywhere.

Three formats cover different use cases:

- **AGENTS.md** — portable methodology file auto-detected by Claude Code, OpenCode, and Codex CLI when placed in a project root. Contains the full methodology without any frontmatter.
- **Hermes skill** — full skill with SKILL.md, references, templates, and flowcharts. Installed via `/skill gdd-toolkit` after a one-line install script.
- **Claude Code plugin** — installable via `/plugin marketplace add mamoru-miyagawa/gdd-toolkit` then `/plugin install gdd@gdd-toolkit`.
- **CLI tool (gdd.py)** — standalone Python script, stdlib only, with five commands: init (creates .design-context/), template (prints GDD templates), pillar (evaluates pillar clarity), matrix (generates pairwise pairs), status (checks project health).
- **QUICKSTART.md** — condensed 2-page version pasteable into any chat LLM (ChatGPT, Claude Web, Pi, Gemini).

---

## What I learned

Building this reinforced a few things I already believed about game design and AI:

**The "make me a game" approach is broken.** A single prompt cannot produce meaningful game design. The value comes from conversation, iteration, and being challenged — not from generation.

**AI works best as a critic, not a creator.** The most useful thing the tool does is ask "why" and surface tensions. That's something AI can do well — hold a consistent frame of reference and compare new ideas against established principles. Letting the AI decide would defeat the purpose.

**Documentation is a byproduct of thinking, not the goal.** The GDD is what comes out of a good design conversation. If you focus on the conversation, the document writes itself. If you focus on the document, you get templates with placeholder text.

**Tools should be honest about their limits.** The code audit works best on small projects with clear structure. The pairwise matrix is overkill for most systems. The balance tables capture intent, not exact numbers — because exact numbers change. Being upfront about what the tool can and can't do makes it more useful, not less.

---

## Links

- **GitHub:** [github.com/mamoru-miyagawa/gdd_toolkit](https://github.com/mamoru-miyagawa/gdd_toolkit)
- **Install:** `/plugin marketplace add mamoru-miyagawa/gdd-toolkit` (Claude Code) or clone from GitHub
- **Quickstart:** open `QUICKSTART.md` and paste into any chat LLM
- **First test output:** [loneliness GDD](https://github.com/mamoru-miyagawa/pico8_prototypes/blob/main/loneliness/GDD.md) — a real GDD produced from a PICO-8 cart

---

*Built with Hermes Agent, tested on OpenCode and Claude Code. Works on any agent with Python 3.*
