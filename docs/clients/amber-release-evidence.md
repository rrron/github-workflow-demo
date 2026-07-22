# Amber Release Evidence

Amber release approval requires a client-specific evidence packet before the
shared workflow can be merged and released.

## Feature Notes

- Capture the release notes URL for the Amber handoff.
- Track regression evidence separately from the shared CI result.
- Require an Amber approval owner before release review starts.
- Preserve the rollout window selected for the client release.

## Demo Validation

- Client repository: `client-amber-workflow-demo`
- Source branch: `feature/SCRUM-12-amber-release-evidence`
- Jira ticket: `SCRUM-12`
- Pull request title should include `[Amber] SCRUM-12`.
