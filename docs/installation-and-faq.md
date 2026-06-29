# Installation and FAQ

This guide answers the common setup and usage questions for Codex Academic Paper Skills.

## Do I need Codex Desktop or Codex CLI?

You can use these skills with any Codex environment that supports local skills.

- Codex Desktop is convenient when your thesis materials include screenshots, Word documents, PDFs, or multiple local files.
- Codex CLI is convenient when your work is mainly inside a project repository and terminal workflow.

The skills themselves are plain directories under `skills/`, so the installation step is the same idea: copy each skill directory into your Codex skills directory.

## Install the skills

Clone or download this repository, then copy both skill directories:

```bash
mkdir -p ~/.codex/skills
cp -R skills/academic-paper-strategist ~/.codex/skills/
cp -R skills/academic-paper-composer ~/.codex/skills/
```

After copying, start a new Codex conversation or reload your Codex environment so the skills list is refreshed.

## Which skill should I use?

Use `academic-paper-strategist` first when you need planning:

- analyze a real project repository
- map code, SQL, config, and docs to thesis chapters
- decide what to keep, rewrite, or delete from an existing draft
- plan diagrams, screenshots, and composer handoff

Use `academic-paper-composer` after the plan is clear:

- continue editing a working draft
- rewrite selected sections
- restore supported old figures and database tables
- apply final thesis-writing rules
- prepare content for final DOCX formatting

For a full thesis workflow, use strategist first, then composer.

## How should I handle private thesis files?

Keep private materials local unless you intentionally choose to share them.

Do not upload these to public GitHub issues:

- thesis drafts
- school templates
- detection reports
- private project source code
- screenshots with personal or school account data
- API keys, database passwords, or cookies

When asking for help, prefer a minimal public example, a redacted screenshot, or a short description of the problem.

## Why are there two skills instead of one?

The split keeps responsibilities clear.

- Strategist decides the plan and evidence boundary.
- Composer edits or assembles the manuscript from that plan.

This reduces the risk of rewriting a whole thesis blindly, losing manual edits, or inventing unsupported project claims.

## The skills do not appear in Codex

Check these items:

1. Confirm both directories exist under `~/.codex/skills/`.
2. Confirm each directory contains `SKILL.md`.
3. Restart or reload the Codex environment.
4. Make sure you copied the skill directories themselves, not only the repository root.

Expected structure:

```text
~/.codex/skills/
  academic-paper-strategist/
    SKILL.md
  academic-paper-composer/
    SKILL.md
```

## Can I use only one skill?

Yes, but the full workflow is safer when both are used together.

- Use only strategist if you just need a plan, outline, or evidence map.
- Use only composer if you already have a reliable plan and a clear working draft.

## Can the skills guarantee a plagiarism or AIGC score?

No. The skills can help rewrite high-risk sections while preserving project truth, but they should not promise a score. Similarity and AIGC tools vary by vendor, database, settings, and report date.

The safe workflow is:

1. read the report
2. map hotspots to thesis sections
3. rewrite supported content
4. rerun the external report
5. repeat only on remaining hotspots

## Maintainer checks

Run this before release or after changing skill references:

```bash
python3 scripts/validate_repo.py
```

The script checks skill folders, referenced files, and README evidence links.
