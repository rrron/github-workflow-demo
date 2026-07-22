from demo_app.clients.amber import collect_release_evidence, release_evidence_blockers


def test_amber_release_evidence_is_ready_when_links_and_owner_are_present() -> None:
    evidence = collect_release_evidence(
        release_notes_url="https://example.com/amber/release-notes",
        regression_evidence_url="https://example.com/amber/regression",
        approval_owner="Amber Release Manager",
        rollout_window="2026-07-24 10:00 CET",
    )

    assert evidence.client == "Amber"
    assert evidence.ready_for_release_review is True
    assert release_evidence_blockers(evidence) == []


def test_amber_release_evidence_reports_missing_review_inputs() -> None:
    evidence = collect_release_evidence(
        release_notes_url="http://example.com/amber/release-notes",
        regression_evidence_url="",
        approval_owner=" ",
        rollout_window="2026-07-24 10:00 CET",
    )

    assert evidence.ready_for_release_review is False
    assert release_evidence_blockers(evidence) == [
        "Release notes must be linked with an HTTPS URL.",
        "Regression evidence must be linked with an HTTPS URL.",
        "Amber approval owner is not assigned.",
    ]
