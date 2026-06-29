# Security Policy

## Supported Versions

This repository currently ships Codex skill instructions and helper materials rather than a packaged runtime. Security fixes are applied to the default branch and included in the next tagged release.

| Version | Supported |
| --- | --- |
| `main` | Yes |
| Tagged releases | Best effort |

## Reporting a Vulnerability

Please report security concerns by emailing the maintainer:

- 1412800823@qq.com

If the issue can be safely discussed in public, you may also open a GitHub issue. Do not publish exploit details, private documents, API keys, school account data, or user-identifying materials in a public issue.

## Scope

Security-relevant reports include:

- Instructions that could cause Codex to expose secrets, credentials, private drafts, or local files unnecessarily.
- Prompt patterns that encourage fabrication of academic evidence, screenshots, SQL, references, or project claims.
- Helper scripts that read, write, or delete files outside the intended workspace.
- Documentation that could lead users to paste sensitive materials into public issues or logs.

## Maintainer Response

The maintainer will try to acknowledge valid reports within 7 days. Fixes may include documentation updates, prompt hardening, script changes, or a new release tag.

## Safe Usage Notes

- Review generated thesis content against real code, SQL, configuration, screenshots, and drafts.
- Keep private papers, school templates, detection reports, and project credentials out of public issues.
- Back up working drafts before using composer-style rewriting workflows.
