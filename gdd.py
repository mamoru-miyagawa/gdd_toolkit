#!/usr/bin/env python3
"""gdd-toolkit — game design assistant for any agent. No dependencies, stdlib only.

Commands:
  init                    Create .design-context/ in the current directory
  template <name>         Print a template to stdout (GDD-skeleton, system-design,
                            core-loop-canvas, balance-table, mda-reference, project-context)
  pillar <statement>      Validate a pillar statement (is it specific, observable,
                            contradictable, opinionated?)
  matrix <features>       Generate pairwise interaction pairs from a comma-separated list
                            e.g. "matrix Jump,Run,Attack,Shoot"
  status                  Scan the current project for GDD + .design-context/ health
"""

import argparse
import itertools
import os
import sys
import textwrap
from pathlib import Path


# ── Template paths ──────────────────────────────────────────────────

def _tool_dir() -> Path:
    return Path(__file__).resolve().parent


def _template_path(name: str) -> Path:
    tpl = _tool_dir() / "hermes-skill" / "references" / "templates"
    candidates = [
        tpl / f"{name}.md",
        tpl / f"{name}.txt",
        tpl / name,
    ]
    for c in candidates:
        if c.exists():
            return c
    # Also check without extension
    for f in tpl.iterdir():
        if f.stem.lower() == name.lower():
            return f
    raise FileNotFoundError(
        f"Template '{name}' not found. Available: "
        + ", ".join(sorted(f.stem for f in tpl.iterdir() if f.suffix in (".md", ".txt")))
    )


AVAILABLE_TEMPLATES = [
    "GDD-skeleton", "system-design", "core-loop-canvas",
    "balance-table", "mda-reference", "project-context",
]


# ── Commands ─────────────────────────────────────────────────────────

def cmd_init(args):
    """Create .design-context/ structure in current directory."""
    base = Path.cwd() / ".design-context"
    subdirs = [
        "mda-analyses",
        "code-audits",
        "design-reviews",
        "brainstorming",
    ]
    files = {
        "index.md": textwrap.dedent(f"""\
            # Project: <name>
            **Current phase:** <pre-production / production / live-ops>
            **Pillars:** <N defined>
            **GDD status:** <N sections complete>
            **Last code audit:** <none>
            **Last design review:** <none>
        """),
        "design-log.md": "# Design Log\n\n## {}\n**Decision:** <what>\n**Rationale:** <why>\n".format(
            __import__("datetime").date.today().isoformat()
        ),
        "pillars.md": "# Design Pillars\n\n## Current Pillars\n\n(Define 2-5 pillars below)\n\n## Pillar Evolution\n\n",
        "rejected-ideas.md": "# Rejected Ideas\n\n| Idea | Why Rejected | Date |\n|-----|-------------|------|\n",
        "open-questions.md": "# Open Questions\n\n| Question | Raised | Status |\n|---------|--------|--------|\n",
        "tensions.md": "# Design Tensions\n\n## Active Tensions\n\n| Pillar A | Pillar B | Nature |\n|---------|---------|--------|\n\n## Resolved Tensions\n\n",
    }
    created = 0
    base.mkdir(parents=True, exist_ok=True)
    for sd in subdirs:
        (base / sd).mkdir(parents=True, exist_ok=True)
        created += 1
    for name, content in files.items():
        fp = base / name
        if not fp.exists():
            fp.write_text(content)
            created += 1
    print(f"✓ .design-context/ initialised at {base}")
    print(f"  {created} items created (existing ones preserved)")


def cmd_template(args):
    """Print a template to stdout."""
    try:
        path = _template_path(args.name)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        return 1
    print(path.read_text(encoding="utf-8"))


def cmd_pillar(args):
    """Evaluate a pillar for clarity and usefulness."""
    statement = args.statement
    issues = []

    if len(statement) < 10:
        issues.append("Very short. A pillar should describe a guiding principle, not just a label.")

    vague_words = ["fun", "engaging", "nice", "cool", "interesting"]
    found_vague = [w for w in vague_words if w in statement.lower()]
    if found_vague:
        issues.append(f"Uses vague word(s): {', '.join(found_vague)}. "
                       "Try describing what the player actually does or experiences.")

    # Check direction: does it have a clear "this way, not that way" feel?
    direction_words = ["not", "never", "without", "instead", "rather than", "avoid", "rejects", "pushes against"]
    if not any(w in statement.lower() for w in direction_words):
        issues.append("No clear direction. What does this pillar push against? "
                      "A pillar that doesn't exclude anything doesn't guide decisions.")

    # Check if it describes a principle vs just a feature
    if len(statement.split()) < 5:
        issues.append("Try expanding: what's the core idea, and what does it mean for the player experience?")

    if not issues:
        print("✓ This pillar has a clear direction and guiding principle.")
        return 0
    else:
        print("⚠ This pillar could be sharper:")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
        return 1


def cmd_matrix(args):
    """Generate pairwise interaction pairs from a comma-separated feature list."""
    features = [f.strip() for f in args.features.split(",") if f.strip()]
    if len(features) < 2:
        print("Need at least 2 features.", file=sys.stderr)
        return 1

    n = len(features)
    pairs = list(itertools.combinations(features, 2))

    print(f"Pairwise Interaction Matrix ({n} features → {len(pairs)} pairs)")
    print("=" * 60)
    print()

    # Matrix table
    col_w = max(len(f) + 2 for f in features) + 2
    header = " " * col_w + "".join(f"{f:>{col_w}}" for f in features)
    print(header)
    for f1 in features:
        row = f"{f1:>{col_w}}"
        for f2 in features:
            if f1 == f2:
                row += f"{'—':>{col_w}}"
            else:
                pair = tuple(sorted([f1, f2]))
                row += f"{'⬜':>{col_w}}"
        print(row)

    print()
    print("⬜ = undocumented — analyse each pair:")
    print()

    for a, b in pairs:
        print(f"  PAIR: {a} + {b}")
        print(f"    Simultaneous?  [YES / NO / SEQUENCE-ONLY / CONTEXT-DEPENDENT]")
        print(f"    Result:        <what actually happens when both are active>")
        print(f"    Edge cases:    <boundary conditions, timing dependencies>")
        print(f"    Status:        ⬜ Not yet analysed")
        print()

    print(f"  Total: {len(pairs)} pairs to document.")
    return 0


def cmd_status(args):
    """Scan current directory for GDD + .design-context/ health."""
    cwd = Path.cwd()
    report = []
    issues = 0

    # GDD check
    gdd_candidates = list(cwd.glob("*.md")) + list(cwd.glob("docs/*.md"))
    gdd_found = [p for p in gdd_candidates if "gdd" in p.stem.lower() or "design" in p.stem.lower()]
    if gdd_found:
        for p in gdd_found:
            size = len(p.read_text(encoding="utf-8", errors="replace").splitlines())
            report.append(f"✓ GDD found: {p.name} ({size} lines)")
    else:
        report.append("⚠ No GDD file detected (looking for *gdd*.md or *design*.md)")
        issues += 1

    # .design-context/ check
    dc = cwd / ".design-context"
    if dc.exists():
        items = list(dc.rglob("*"))
        report.append(f"✓ .design-context/ exists ({len([i for i in items if i.is_file()])} files)")
        for key_file in ["design-log.md", "pillars.md", "tensions.md", "open-questions.md"]:
            kp = dc / key_file
            if kp.exists():
                lines = len(kp.read_text(encoding="utf-8", errors="replace").splitlines())
                report.append(f"  ✓ {key_file} ({lines} lines)")
            else:
                report.append(f"  ⚠ {key_file} missing")
                issues += 1
    else:
        report.append("⚠ No .design-context/ directory — run 'gdd.py init'")
        issues += 1

    # Pillars check
    pillars_file = dc / "pillars.md" if dc.exists() else Path("pillars.md")
    if pillars_file.exists():
        content = pillars_file.read_text(encoding="utf-8", errors="replace")
        pillar_count = content.count("PILLAR:")
        if pillar_count == 0:
            report.append("⚠ pillars.md exists but no pillars defined (no 'PILLAR:' lines)")
            issues += 1
        else:
            report.append(f"✓ {pillar_count} pillar(s) defined")
    else:
        if not dc.exists():
            pass  # already flagged
        else:
            report.append("⚠ No pillars defined yet")
            issues += 1

    print(f"Project Design Status — {cwd.name}")
    print("=" * 50)
    for line in report:
        print(f"  {line}")
    if issues:
        print(f"\n  {issues} issue(s) found. Run 'gdd.py init' or 'gdd.py pillar <statement>' to resolve.")
    else:
        print(f"\n  ✓ All checks passed.")
    return 0


# ── CLI ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog="gdd.py",
        description="Game Design Assistant — write GDDs, validate pillars, run pairwise matrices.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              gdd.py init
              gdd.py template GDD-skeleton
              gdd.py pillar "The player can complete any level without attacking"
              gdd.py matrix Jump,Run,Attack,Shoot
              gdd.py status
        """),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="Create .design-context/ in current directory")

    p_tpl = sub.add_parser("template", help="Print a template to stdout")
    p_tpl.add_argument("name", help=f"One of: {', '.join(AVAILABLE_TEMPLATES)}")

    p_pil = sub.add_parser("pillar", help="Validate a pillar statement")
    p_pil.add_argument("statement", nargs="+", help="The pillar statement, e.g. 'The player can beat any level without attacking'")
    # join the statement back with spaces in the handler

    p_mat = sub.add_parser("matrix", help="Generate pairwise pairs from comma-separated features")
    p_mat.add_argument("features", help="Comma-separated list, e.g. Jump,Run,Attack,Shoot")

    p_st = sub.add_parser("status", help="Scan project for GDD + .design-context/ health")

    args = parser.parse_args()

    if args.command == "init":
        return cmd_init(args)
    elif args.command == "template":
        return cmd_template(args)
    elif args.command == "pillar":
        args.statement = " ".join(args.statement)
        return cmd_pillar(args)
    elif args.command == "matrix":
        return cmd_matrix(args)
    elif args.command == "status":
        return cmd_status(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
