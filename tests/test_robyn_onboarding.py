from demo_app.clients.robyn import build_onboarding_plan


def test_robyn_onboarding_requires_access_and_escalation_contact() -> None:
    plan = build_onboarding_plan(
        owner="Robyn Product Owner",
        environment="demo",
        access_ready=True,
        escalation_contact="robyn-security@example.com",
    )

    assert plan.client == "Robyn"
    assert plan.ready_for_demo is True


def test_robyn_onboarding_is_not_ready_without_escalation_contact() -> None:
    plan = build_onboarding_plan(
        owner="Robyn Product Owner",
        environment="demo",
        access_ready=True,
        escalation_contact="",
    )

    assert plan.ready_for_demo is False
