# Game Design Assistant

A game design co-pilot for AI coding agents. Write a GDD, then challenge it against your own pillars, cross-reference mechanics, apply MDA — without the "make me a whole game in one prompt" nonsense.

---

## Quick install

### Claude Code (plugin — recommended)

Inside any Claude Code session:

```
/plugin marketplace add mamoru-miyagawa/gdd-toolkit
/plugin install gdd@game-design-assistant
```

Then type `/gdd` or `/game-design` to load the methodology. Or just start with "I want to write a GDD."

### OpenCode / Codex CLI

Copy `AGENTS.md` to your project root — both auto-detect it on startup.

```bash
# from the repo
cp AGENTS.md /path/to/your/game/project/AGENTS.md

# or clone and cd in
git clone https://github.com/mamoru-miyagawa/gdd-toolkit
cd gdd-toolkit
opencode
```

### Pi / ChatGPT / Claude Web / Gemini

Open `QUICKSTART.md` and paste the contents as your first message or system prompt. No install needed.

### Hermes

```bash
git clone https://github.com/mamoru-miyagawa/gdd-toolkit
bash gdd_toolkit/install.sh
```

Then `/reload-skills` and `/skill game-design-assistant`.

---

## How to use

### Write a GDD

```
Let's write a GDD for my game.    # starts with Vision Lock
```

The assistant walks you through each section. You define the pillars, the core loop, and the features. The GDD is your document — you own it.

### Challenge what you have

Once you have a GDD (or a draft), test it:

| Say this | It does |
|---|---|
| `pillar gate wall-running` | Check one feature against your pillars, core loop, systems, scope |
| `run the matrix` | Test every feature against every other — pairwise |
| `MDA this combat system` | Mechanics → Dynamics → Aesthetics analysis |
| `balance this weapon set` | Capture intent and relationships between values |
| `audit the code` | Compare GDD features against what's implemented |
| `judge this design` | Full adversarial review: pillars, scope, pairs, tuning |
| `pillar judge this stealth mechanic` | Deep trace through every pillar |
| `brainstorm enemy types` | Generate ideas, evaluate against pillars |

You always decide. The assistant challenges, recommends, and logs to `.design-context/` — but never changes your GDD without you saying so.

### Use the CLI directly

```bash
python gdd.py init                          # create .design-context/
python gdd.py template GDD-skeleton         # print a template
python gdd.py pillar "Players explore by experimenting, not reading"  # evaluate a pillar
python gdd.py matrix Jump,Run,Attack,Shoot  # generate pairwise pairs
python gdd.py status                        # scan project health
```

Works anywhere Python 3 is installed. No dependencies.

---

## What's in the repo

| File | What it is |
|---|---|
| `AGENTS.md` | Portable methodology — auto-loaded by Claude Code, OpenCode, Codex |
| `.claude-plugin/plugin.json` | Claude Code plugin manifest |
| `QUICKSTART.md` | Condensed version — paste into any chat LLM |
| `gdd.py` | CLI tool — `init`, `template`, `pillar`, `matrix`, `status` |
| `hermes-skill/` | Full Hermes skill with SKILL.md + references + templates |
| `install.sh` / `install.ps1` | Installers for Hermes |

Templates live in `hermes-skill/references/templates/`:
- GDD skeleton, system design, core loop canvas, balance table, MDA reference, project context init

---

## The second brain (`.design-context/`)

The assistant maintains a sidecar folder alongside your project — separate from the formal GDD. This is where decisions, rationale, tensions, rejected ideas, and open questions live. The GDD is the deliverable. `.design-context/` is the memory.

Run `python gdd.py init` to create it, or the assistant sets it up automatically in Hermes.

---

## License

MIT
