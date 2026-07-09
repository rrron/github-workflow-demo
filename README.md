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

## Current Demo Flow

1. Create a Jira work item, for example `SCRUM-1`.
2. Create a feature branch with the Jira key:

   ```text
   SCRUM-1-auto-merge-demo
   ```

3. Commit with the same Jira key:

   ```text
   SCRUM-1 support Jira keys in prefixed branch names
   ```

4. Open a pull request with the Jira key in the title:

   ```text
   SCRUM-1 Support Jira keys in prefixed branch names
   ```

5. Put the Jira key in the PR description:

   ```text
   Jira issue: SCRUM-1
   ```

6. CI runs lint, static analysis, tests, build, label automation, and label gate.
7. GitHub blocks merge until one approving review is submitted by another user.
8. Enable auto-merge while the PR is waiting for review.
9. After approval, GitHub automatically squash-merges the PR.
10. Jira shows linked GitHub development data for the work item: branch, commits,
    pull request, builds, and merged state.

## Jira Linking Rules

For the Jira integration to link GitHub activity to the correct work item, always
include the Jira key in these places:

- Branch name: `SCRUM-1-short-description`
- Commit message: `SCRUM-1 short change summary`
- Pull request title: `SCRUM-1 Short change summary`
- Pull request description: `Jira issue: SCRUM-1`

The most important fields are branch name, commit message, and PR title. PR
description is a useful extra signal and makes the demo easier to read.

GitHub-side autolinks from `SCRUM-1` to Jira are not available on the current
GitHub free plan. Traceability is visible from Jira through GitHub for Atlassian.

## Merge Rules

- Direct updates to `main` are blocked.
- Changes go through pull requests.
- One approving review is required.
- The approval must come from someone other than the last pusher.
- CI checks run automatically on pull requests.
- Auto-merge can be enabled on a PR and will merge after review and checks pass.

## Labels

The PR automation updates status labels:

- `status: needs-review`
- `status: approved`
- `status: changes-requested`
- `status: ready-to-merge`

The label gate is informational in this demo so it does not block merge while the
flow is being demonstrated.

See [docs/setup-guide.md](docs/setup-guide.md) for full setup steps.
