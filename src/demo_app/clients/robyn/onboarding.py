from dataclasses import dataclass


@dataclass(frozen=True)
class RobynOnboardingPlan:
    client: str
    owner: str
    environment: str
    access_ready: bool
    escalation_contact: str

    @property
    def ready_for_demo(self) -> bool:
        return self.access_ready and bool(self.escalation_contact)


def build_onboarding_plan(
    owner: str,
    environment: str,
    *,
    access_ready: bool,
    escalation_contact: str,
) -> RobynOnboardingPlan:
    return RobynOnboardingPlan(
        client="Robyn",
        owner=owner,
        environment=environment,
        access_ready=access_ready,
        escalation_contact=escalation_contact,
    )
