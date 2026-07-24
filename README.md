# 📖 GDD Toolkit

A plugin/skill for AI agents that helps you write a Game Design Document through conversation. It won't make decisions for you — it will ask questions, challenge your ideas, and remember your reasoning so you can focus on designing.

---

## 📖 What it does

Most AI game design tools treat GDDs as a documentation of what's already implemented. This one treats the GDD as a **living database of everything your game is** — planned, built, or just imagined.

You have a conversation about your project. The AI asks you questions, helps you structure the answers, and writes everything to a `.md` file you own. If you have existing code, it reads what's there and extracts features to discuss. If you don't, it helps you build from scratch.

The output is a markdown GDD you can open in Obsidian, view on GitHub, or keep anywhere you like.

---

## 📖 Why it exists

Because "make me Minecraft in one prompt" is not game development. Real game design needs:

- A clear vision that guides every decision
- Features that are challenged, not just listed
- Mechanics that are tested against each other
- Designers who make the calls, not AI that decides

This tool is thorough on purpose. You will have to think.

---

## 📖 How it works

You start by saying you want to write a GDD. The AI walks you through:

**1. Vision Lock** — define your pillars, audience, genre, scope. These become the filter for every decision.

**2. Core Loop** — find the minimum fun unit. What's the simplest thing the player does that they keep wanting to do?

**3. Features & Systems** — add features one at a time. Each is checked against your pillars. The AI will ask "why" when something doesn't align. It won't block you — but it will make you think about it.

**4. GDD Output** — a structured markdown document, written wherever you decide.

Along the way, you can call on challenge tools to test what you've built:

| Say this | It does |
|---|---|
| `pillar gate wall-running` | Checks one feature against your pillars |
| `run the matrix` | Tests every feature against every other — pairwise |
| `MDA this combat system` | Analyzes Mechanics → Dynamics → Aesthetics |
| `balance this weapon set` | Captures the relationships between values |
| `audit the code` | Compares GDD features against project code |
| `judge this design` | Full review: pillars, scope, pairs, tuning |
| `pillar judge this` | Deep trace through every pillar |
| `brainstorm enemy types` | Generates ideas, evaluates against pillars |

You always decide. The AI challenges, recommends, and remembers — but never changes your GDD without you saying so.

---

## 📖 The second brain

The AI maintains a `.design-context/` folder next to your project — separate from the GDD. This is where it stores decisions, rationale, tensions, rejected ideas, and open questions.

The GDD is the formal deliverable. The context file is the AI's memory. You can keep changing your mind, discussing options, and exploring dead ends — the GDD only gets the final decisions.

---

## 📖 Install

### Claude Code (plugin)
```
/plugin marketplace add mamoru-miyagawa/gdd-toolkit
/plugin install gdd@game-design-assistant
```

### OpenCode / Codex CLI
Copy `AGENTS.md` to your project root. Both auto-detect it on startup.

### Pi / ChatGPT / Claude Web / Gemini
Open `QUICKSTART.md` and paste the contents as your first message.

### Hermes
```bash
git clone https://github.com/mamoru-miyagawa/gdd-toolkit
bash gdd_toolkit/install.sh
```
Then `/reload-skills` and `/skill game-design-assistant`.

### Anywhere with Python
```bash
python gdd.py init                          # create .design-context/
python gdd.py template GDD-skeleton         # print a template
python gdd.py pillar "Players explore by experimenting"  # test a pillar
python gdd.py matrix Jump,Run,Attack        # generate pairwise pairs
python gdd.py status                        # check project health
```

---

## 📖 What it's not

- Not a GDD generator. You have to think.
- Not a "make me a game" tool. It asks more questions than it answers.
- Not a documentation of what exists. It's a database of what your game is, planned and built.

---

## 📖 License

MIT
