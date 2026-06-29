#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = [
    ROOT / "skills" / "academic-paper-strategist",
    ROOT / "skills" / "academic-paper-composer",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def ensure_exists(path: Path, label: str) -> None:
    if not path.exists():
        fail(f"missing {label}: {path.relative_to(ROOT)}")


def extract_paths(text: str, prefix: str) -> set[str]:
    paths: set[str] = set()
    for line in text.splitlines():
        line = line.strip()
        if line.startswith(prefix):
            for raw in re.findall(r"`([^`]+)`", line):
                if raw.startswith(("references/", "scripts/", "agents/")):
                    paths.add(raw)
    return paths


def validate_skill(skill_dir: Path) -> None:
    ensure_exists(skill_dir / "SKILL.md", f"{skill_dir.name} SKILL.md")

    skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    referenced_rels: set[str] = set()
    for prefix in ("-", "*"):
        referenced_rels |= extract_paths(skill_text, prefix)

    for rel in sorted(referenced_rels):
        candidate = skill_dir / rel
        if not candidate.exists():
            fail(f"{skill_dir.name} references missing path: {rel}")

    ensure_exists(skill_dir / "agents" / "openai.yaml", f"{skill_dir.name} agents/openai.yaml")


def validate_readme() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    required_links = [
        "docs/evidence/video-analytics-overview.png",
        "docs/evidence/video-traffic-sources.png",
        "docs/evidence/video-post-summary.png",
        "docs/evidence/user-feedback-01.png",
        "docs/evidence/user-feedback-02.png",
    ]
    for rel in required_links:
        if rel not in readme:
            fail(f"README.md missing evidence link: {rel}")
        ensure_exists(ROOT / rel, f"evidence asset {rel}")


def main() -> None:
    ensure_exists(ROOT / "README.md", "README.md")
    ensure_exists(ROOT / "CONTRIBUTING.md", "CONTRIBUTING.md")
    ensure_exists(ROOT / "SECURITY.md", "SECURITY.md")

    for skill_dir in SKILLS:
        validate_skill(skill_dir)

    validate_readme()
    print("Repository validation passed.")


if __name__ == "__main__":
    main()
