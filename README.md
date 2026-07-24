# GDD Skills — Game Design Assistant

A disciplined game design co-pilot that helps you write a Game Design Document — then challenges it.

**Not a GDD generator.** Not a "make me a game in one prompt" tool. This is a design methodology that:
- Guides you through writing a proper GDD section by section
- Validates every feature against your own design pillars
- Cross-references every mechanic against every other mechanic
- Applies MDA analysis (Mechanics → Dynamics → Aesthetics) to predict what players actually experience
- Audits your project code against your GDD to find drift
- Leaves every decision to you — it challenges and recommends, never overrides

---

## Contents

| File | What it is | Who uses it |
|---|---|---|
| `AGENTS.md` | Full methodology — no frontmatter, portable | Hermes, Claude Code, OpenCode, Codex — auto-loaded from project root |
| `gdd.py` | Standalone Python tool with `init`, `template`, `pillar`, `matrix`, `status` — works in any agent, any OS | All — no dependencies |
| `QUICKSTART.md` | Condensed 2-page version | Any chat LLM (ChatGPT, Claude Web, Pi, Gemini) — paste as system prompt |
| `hermes-skill/` | Full Hermes skill with SKILL.md + references + templates | Hermes — `hermes -s game-design-assistant` |
| `.claude-plugin/plugin.json` | Claude Code plugin manifest | Claude Code — `/plugin install gdd@game-design-assistant` |
| `install.sh` | POSIX installer | macOS / Linux / Git Bash |
| `install.ps1` | Windows installer | PowerShell |

---

## Quick install

### Hermes
```bash
hermes skills install https://raw.githubusercontent.com/YOUR_USERNAME/GDD_skills/main/hermes-skill/SKILL.md
# or manually:
git clone https://github.com/YOUR_USERNAME/GDD_skills
bash GDD_skills/install.sh
```
Then: `/reload-skills` then `/skill game-design-assistant`

### Claude Code
```bash
# As a plugin (recommended):
/plugin marketplace add YOUR_USERNAME/GDD_skills
/plugin install gdd@game-design-assistant

# Or just copy AGENTS.md to your project root:
cp GDD_skills/AGENTS.md ./AGENTS.md
```

### OpenCode / Codex
Copy `AGENTS.md` to your project root — both auto-detect it.

### Any chat LLM (ChatGPT, Claude Web, Pi, Gemini)
Open `QUICKSTART.md` and paste its contents as your first message or system prompt.

---

## How to use

### Write a GDD
```
/skill game-design-assistant    # (Hermes) load the skill
Let's write a GDD for my game.  # Start with Vision Lock
```

### Challenge what you have
```
audit the code                  # Compare GDD vs project code
run the matrix                  # Test every feature against every other
MDA this combat system          # Analyze Mechanics → Dynamics → Aesthetics
pillar judge this wall-running  # Deep trace through every pillar
judge this design               # Full adversarial review
brainstorm monetization ideas   # Generate + evaluate against pillars
```

### Set up the second brain
The skill auto-creates `.design-context/` in your project folder. This is where decisions, rationale, tensions, and open questions live — separate from the formal GDD.

---

## Templates

The `hermes-skill/references/templates/` folder contains:
- **GDD-skeleton.md** — full 11-section GDD template
- **system-design.md** — per-system documentation template
- **core-loop-canvas.md** — one-page core loop worksheet
- **balance-table.md** — tuning tables with curves and goals
- **mda-reference.md** — MDA framework quick reference
- **project-context.md** — `.design-context/` initialization guide

The `hermes-skill/templates/` folder contains:
- **obsidian-vault-layout.md** — recommended Obsidian vault structure

---

## Design philosophy

This tool exists because most AI game design content is cargo-cult garbage — "make me a whole game in one prompt" treating game development as a vibe, not a discipline.

**This skill does the opposite:**
- It demands pillars before features
- It cross-references every mechanic against every other
- It applies the MDA framework to predict what players actually experience
- It audits your code against your GDD to catch drift
- It challenges you when something doesn't add up
- It never makes a decision for you

The most important line in every pillar definition is **"what it pushes against."** A pillar that can't be challenged filters nothing.

---

## License

MIT — do whatever you want with it. Credit appreciated but not required.
