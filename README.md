# GitHub Workflow Demo

Demo repository for showing a controlled GitHub pull request flow:

- feature branch development
- pull requests with required review
- CODEOWNERS-based approval
- required CI checks
- status labels
- auto-merge after approvals and checks
- Jira Cloud linking by issue key

## Demo Application

This repository contains a tiny Python pseudo-application. It is intentionally
small so the demo can focus on the GitHub process instead of business logic.

## Local Commands

```powershell
python -m pip install -e ".[dev]"
python -m pytest
python -m ruff check .
python -m mypy src
python -m demo_app.cli PROJ-123 "demo workflow"
```

## Recommended Demo Flow

1. Create a Jira issue, for example `PROJ-123`.
2. Create a branch named `PROJ-123-demo-change`.
3. Commit with the Jira key in the message.
4. Open a pull request with the Jira key in the title.
5. Wait for CI.
6. Ask a code owner to review.
7. Add `status: ready-to-merge` after approval.
8. Enable auto-merge on the pull request.
9. Watch GitHub merge the PR when all requirements are met.

See [docs/setup-guide.md](docs/setup-guide.md) for full setup steps.
