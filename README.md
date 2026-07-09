## GitHub Workflow Demo

This repository demonstrates an automated delivery workflow built around GitHub
pull requests, code review, CI checks, auto-merge, and Jira traceability.

## What The Demo Shows

1. A Jira work item is created for the planned change.
2. A developer creates a feature branch and opens a GitHub pull request.
3. GitHub runs automated validation checks for the pull request.
4. The pull request receives status labels that show its review state.
5. Merge is blocked until an authorized reviewer approves the change.
6. Auto-merge waits for all required gates to pass.
7. After approval, GitHub squash-merges the pull request automatically.
8. Jira shows the linked branch, commits, pull request, builds, and merge state.
9. Jira also receives lifecycle comments from GitHub when the pull request is
   opened, reopened, approved, merged, or closed.

## Demo Walkthrough

During the demo, start from a Jira work item and show how the same work item is
visible throughout the GitHub delivery flow.

- Open the Jira work item and show the Development panel.
- Open the linked GitHub pull request.
- Show the automated checks and status labels.
- Show that merge is blocked before approval.
- Enable auto-merge.
- Approve the pull request from a different user.
- Show GitHub merging the pull request after the gates pass.
- Return to Jira and show the updated development status and comments.

## Expected Result

The customer should see a complete trace from planning to merged code:

- Jira tracks the work item.
- GitHub controls code review and merge policy.
- CI validates every pull request.
- Review approval is mandatory.
- Auto-merge reduces manual merge steps.
- Jira remains updated with GitHub development activity.
