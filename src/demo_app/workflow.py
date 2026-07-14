from dataclasses import dataclass


@dataclass(frozen=True)
class PullRequestSummary:
    jira_key: str
    title: str
    needs_review: bool
    ready_to_merge: bool


def extract_jira_key(text: str) -> str | None:
    """Return the first Jira-like issue key from a branch, commit, or PR title."""
    compact_text = text.replace("/", "-").replace("_", "-")
    words = compact_text.split()
    tokens = compact_text.split("-")

    for index, token in enumerate(tokens[:-1]):
        next_token = tokens[index + 1]
        if token.isalpha() and next_token.isdigit():
            return f"{token.upper()}-{next_token}"

    for word in words:
        cleaned = word.strip("[]():,;")
        if "-" in cleaned:
            prefix, suffix = cleaned.split("-", maxsplit=1)
            if prefix.isalpha() and suffix.isdigit():
                return f"{prefix.upper()}-{suffix}"

    return None


def summarize_pull_request(title: str, labels: list[str]) -> PullRequestSummary:
    jira_key = extract_jira_key(title) or "NO-JIRA-KEY"
    ready_to_merge = "status: ready-to-merge" in labels
    needs_review = not ready_to_merge and "status: approved" not in labels

    return PullRequestSummary(
        jira_key=jira_key,
        title=title,
        needs_review=needs_review,
        ready_to_merge=ready_to_merge,
    )
