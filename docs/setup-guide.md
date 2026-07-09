# GitHub Workflow Demo Setup Guide

This guide configures a small GitHub repository for a customer demo of a
controlled pull request workflow.

## 1. Create Repository

Recommended:

- Repository name: `github-workflow-demo`
- Visibility: public for the easiest free-plan demo
- Add README: off if pushing this local repository
- Add `.gitignore`: off if pushing this local repository
- License: optional

After creating the empty repository, connect this local repo:

```powershell
git remote add origin https://github.com/OWNER/github-workflow-demo.git
git branch -M main
git push -u origin main
```

## 2. Invite Demo Users

Use at least two accounts:

- repository owner/admin: can configure settings and merge
- developer/reviewer: can create branches, open PRs, and review if granted write access

For a stronger demo, use a GitHub Organization:

- `developers`: write access
- `reviewers`: write or maintain access
- `maintainers`: maintain/admin access

Then replace placeholders in `.github/CODEOWNERS`:

```txt
* @OWNER @REVIEWER_USER
/.github/ @OWNER
```

The committed default uses only `@rrron` so the file is valid before the second
demo user is invited. Update it before the customer demo.

## 3. Create Labels

Create these labels in GitHub UI under `Issues > Labels`:

- `status: needs-review`
- `status: changes-requested`
- `status: approved`
- `status: ready-to-merge`
- `jira-linked`
- `ci: failed`
- `ci: passed`

Optional GitHub CLI commands:

```powershell
.\scripts\setup-labels.ps1 -Repository OWNER/github-workflow-demo
```

## 4. Enable Auto-Merge

In GitHub:

1. Open repository `Settings`.
2. Open `General`.
3. Find `Pull Requests`.
4. Enable `Allow auto-merge`.
5. Recommended: enable `Automatically delete head branches`.
6. Recommended: allow only `Squash merging` for a clean history.

## 5. Protect `main`

Use either a branch protection rule or a repository ruleset.

Recommended rule for `main`:

- Require a pull request before merging
- Require approvals: `1`
- Dismiss stale pull request approvals when new commits are pushed
- Require review from Code Owners
- Require approval of the most recent reviewable push
- Require conversation resolution before merging
- Require status checks to pass before merging
- Require branches to be up to date before merging
- Do not allow bypassing the above settings, if available
- Block force pushes
- Block deletions

Required status checks:

- `lint`
- `static-analysis`
- `test`
- `build`
- `ready-to-merge-label`

Optional GitHub CLI command:

```powershell
.\scripts\setup-branch-protection.ps1 -Repository OWNER/github-workflow-demo
```

## 6. Jira Cloud Integration

Fastest option:

1. Install the `GitHub for Atlassian` app in Jira Cloud.
2. Connect the GitHub organization or repository.
3. Use Jira issue keys in branch names, commits, and PR titles.

Naming examples:

```txt
Branch: PROJ-123-demo-change
Commit: PROJ-123 add demo validation
PR:     PROJ-123 Add demo validation
```

Optional direct Jira comments from GitHub Actions:

1. Create GitHub repository variable:
   - `JIRA_ENABLED=true`
2. Create GitHub repository secrets:
   - `JIRA_BASE_URL=https://your-domain.atlassian.net`
   - `JIRA_EMAIL=your-email@example.com`
   - `JIRA_API_TOKEN=<jira-api-token>`

The workflow `.github/workflows/jira-comment.yml` posts a Jira comment when a
PR is opened, reopened, or closed. Keep it disabled until the Jira demo tenant
is ready.

## 7. Demo Script

Developer account:

```powershell
git checkout -b PROJ-123-demo-change
# make a small change
git add .
git commit -m "PROJ-123 add demo change"
git push -u origin PROJ-123-demo-change
```

GitHub UI:

1. Open PR titled `PROJ-123 Add demo change`.
2. Show automatic `status: needs-review` label.
3. Show CI checks: lint, static-analysis, test, build.
4. Show CODEOWNERS review request.
5. Reviewer requests changes.
6. Developer pushes fix.
7. Reviewer approves.
8. Add `status: ready-to-merge`.
9. Enable auto-merge.
10. Show final merge after checks pass.

## 8. What This Demonstrates

- Controlled access to `main`
- Mandatory pull requests
- Reviewer and CODEOWNER governance
- Automated lint, tests, static analysis, and build
- Status labels as visible workflow state
- Auto-merge after all requirements are satisfied
- Jira traceability through issue keys and optional comments
