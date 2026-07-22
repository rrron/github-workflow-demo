from demo_app.clients.robyn import access_readiness_blockers, build_access_checklist


def test_robyn_access_checklist_is_ready_when_required_fields_are_present() -> None:
    checklist = build_access_checklist(
        onboarding_owner="Robyn Product Owner",
        escalation_contact="robyn-escalation@example.com",
        access_request_id="ROB-ACCESS-42",
        sandbox_ready=True,
    )

    assert checklist.client == "Robyn"
    assert checklist.ready_for_onboarding is True
    assert access_readiness_blockers(checklist) == []


def test_robyn_access_checklist_reports_missing_readiness_items() -> None:
    checklist = build_access_checklist(
        onboarding_owner=" ",
        escalation_contact="robyn-escalation",
        access_request_id="ROB-ACCESS-43",
        sandbox_ready=False,
    )

    assert checklist.ready_for_onboarding is False
    assert access_readiness_blockers(checklist) == [
        "Onboarding owner is not assigned.",
        "Escalation contact must be an email address.",
        "Robyn sandbox access is not ready.",
    ]
