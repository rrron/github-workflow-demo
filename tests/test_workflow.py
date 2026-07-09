from demo_app.workflow import extract_jira_key, summarize_pull_request


def test_extracts_jira_key_from_branch_name() -> None:
    assert extract_jira_key("PROJ-123-demo-change") == "PROJ-123"


def test_extracts_jira_key_from_pull_request_title() -> None:
    assert extract_jira_key("PROJ-456 Add workflow labels") == "PROJ-456"


def test_extracts_jira_key_case_insensitively() -> None:
    assert extract_jira_key("proj-321-demo-change") == "PROJ-321"


def test_extracts_jira_key_from_prefixed_branch_name() -> None:
    assert extract_jira_key("feature/SCRUM-1-auto-merge-demo") == "SCRUM-1"


def test_summary_requires_review_by_default() -> None:
    summary = summarize_pull_request("PROJ-789 Add build step", ["status: needs-review"])

    assert summary.jira_key == "PROJ-789"
    assert summary.needs_review is True
    assert summary.ready_to_merge is False


def test_summary_is_ready_when_ready_label_exists() -> None:
    summary = summarize_pull_request("PROJ-789 Add build step", ["status: ready-to-merge"])

    assert summary.needs_review is False
    assert summary.ready_to_merge is True
