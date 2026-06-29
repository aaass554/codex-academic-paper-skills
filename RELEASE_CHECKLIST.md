# Release Checklist

Use this checklist before publishing a new GitHub release.

## Pre-release

- Run repository validation:

```bash
python3 scripts/validate_repo.py
```

- Review README installation instructions.
- Check that both example prompts still match the current skill behavior.
- Confirm `CONTRIBUTING.md` and `SECURITY.md` still reflect the current maintainer process.
- Review open issues and decide whether any should be mentioned in release notes.

## Versioning

- Use `v0.x.y` while the skill workflows are still evolving.
- Increment the patch version for documentation, examples, and small prompt fixes.
- Increment the minor version when workflow behavior, required inputs, or output expectations change.

## Release Notes

Each release should include:

- Highlights
- Installation notes
- Breaking changes, if any
- Known follow-up work

## Publish

```bash
git tag v0.x.y
git push origin v0.x.y
gh release create v0.x.y --title "v0.x.y" --notes-file RELEASE_NOTES.md
```
