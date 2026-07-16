# Client Repository Pull Request Demo

This demo uses one common upstream repository and two client-specific source
repositories.

## Repositories

- `github-workflow-demo`: common upstream repository
- `client-robyn-workflow-demo`: Robyn client repository
- `client-amber-workflow-demo`: Amber client repository

## Client Branches

Client branches can use the normal feature naming pattern:

```txt
feature/SCRUM-12-robyn-demo-change
feature/SCRUM-13-amber-demo-change
```

The automation detects the client from the source repository name, not from the
branch prefix.

## Pull Request Flow

Open pull requests into the common upstream repository:

```txt
base repository: rrron/github-workflow-demo
base branch: main
head repository: rrron/client-robyn-workflow-demo
compare branch: feature/SCRUM-12-robyn-demo-change
```

or:

```txt
base repository: rrron/github-workflow-demo
base branch: main
head repository: rrron/client-amber-workflow-demo
compare branch: feature/SCRUM-13-amber-demo-change
```

## Expected Automation

When a client pull request is opened, reopened, or updated, the upstream
automation normalizes the pull request title and description.

Example title:

```txt
[Robyn] SCRUM-12 Add client workflow change
```

Example managed description section:

```md
## Client

Robyn

## Jira

SCRUM-12

## Source

Repository: rrron/client-robyn-workflow-demo
Branch: feature/SCRUM-12-robyn-demo-change
Target: rrron/github-workflow-demo / main

## Change Summary

- abc1234 Add Robyn client config

## Demo Review Policy

Required approvals: 6

Required reviewers:
- Robyn Product Owner
- Robyn Security
- Robyn QA
- Common Platform
- Release Manager
- Jira Owner
```

The `client-review-policy` check also displays the six required demo reviewer
roles in the GitHub checks area.

## Jira Comments

Jira lifecycle comments include the client, SCRUM ticket, source repository,
source branch, target repository, target branch, and commit summary.
