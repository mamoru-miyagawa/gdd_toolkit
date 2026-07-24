#!/usr/bin/env bash
# GDD Skills Installer — macOS / Linux / Git Bash
set -euo pipefail
src="$(cd "$(dirname "$0")" && pwd)"

echo "━━━ GDD Skills — Installer ━━━"
echo ""

# Detect which agent environments are available
install_hermes() {
    local dst
    if [ -d "$HOME/.hermes/skills" ]; then
        dst="$HOME/.hermes/skills/software-development"
    elif [ -d "$HOME/AppData/Local/hermes/skills" ]; then
        dst="$HOME/AppData/Local/hermes/skills/software-development"
    else
        echo "  ⚠ Hermes not found (no skills directory)"
        return 1
    fi
    mkdir -p "$dst"
    cp -r "$src/hermes-skill" "$dst/game-design-assistant"
    echo "  ✓ Hermes: $dst/game-design-assistant"
}

install_claude() {
    local dst="$HOME/.claude/skills"
    if [ ! -d "$HOME/.claude" ]; then
        echo "  ⚠ Claude Code not found (no ~/.claude directory)"
        return 1
    fi
    mkdir -p "$dst"
    # Claude Code uses AGENTS.md from project root, but we can also
    # install as a skill via the plugin system
    cp "$src/AGENTS.md" "$dst/game-design-assistant.md"
    echo "  ✓ Claude Code: $dst/game-design-assistant.md"
    echo "  ℹ  Claude Code can also use AGENTS.md from the project root"
}

install_opencode() {
    # OpenCode reads AGENTS.md from project root — no global install needed
    echo "  ℹ  OpenCode: place AGENTS.md in your project root (or copy manually)"
}

echo "Installing..."
install_hermes
install_claude
install_opencode

echo ""
echo "━━━ Done ━━━"
echo "Hermes:   /skill game-design-assistant"
echo "Claude:   copy AGENTS.md to your project root"
echo "OpenCode: copy AGENTS.md to your project root"
echo "Any LLM:  paste QUICKSTART.md as system prompt"
echo ""
echo "See README.md for full documentation."
