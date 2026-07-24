# GDD Skills Installer — Windows PowerShell
$ErrorActionPreference = "Stop"
$src = $PSScriptRoot

Write-Host "━━━ GDD Skills — Installer ━━━" -ForegroundColor Cyan
Write-Host ""

# Detect Hermes
$hermesSkills = Join-Path $HOME "AppData\Local\hermes\skills\software-development"
if (Test-Path (Join-Path $HOME "AppData\Local\hermes\skills")) {
    New-Item -ItemType Directory -Force -Path $hermesSkills | Out-Null
    Copy-Item (Join-Path $src "hermes-skill") (Join-Path $hermesSkills "gdd-toolkit") -Recurse -Force
    Write-Host "  ✓ Hermes: $hermesSkills\gdd-toolkit" -ForegroundColor Green
} else {
    Write-Host "  ⚠ Hermes not found (no skills directory)" -ForegroundColor Yellow
}

# Detect Claude Code
$claudeDir = Join-Path $HOME ".claude"
$claudeSkills = Join-Path $claudeDir "skills"
if (Test-Path $claudeDir) {
    New-Item -ItemType Directory -Force -Path $claudeSkills | Out-Null
    Copy-Item (Join-Path $src "AGENTS.md") (Join-Path $claudeSkills "gdd-toolkit.md") -Force
    Write-Host "  ✓ Claude Code: $claudeSkills\gdd-toolkit.md" -ForegroundColor Green
} else {
    Write-Host "  ℹ  Claude Code: place AGENTS.md in your project root" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "━━━ Done ━━━" -ForegroundColor Cyan
Write-Host "Hermes:   /skill gdd-toolkit"
Write-Host "Claude:   copy AGENTS.md to your project root"
Write-Host "OpenCode: copy AGENTS.md to your project root"
Write-Host "Any LLM:  paste QUICKSTART.md as system prompt"
Write-Host ""
Write-Host "See README.md for full documentation."
