from dataclasses import dataclass


@dataclass(frozen=True)
class RobynAccessChecklist:
    client: str
    onboarding_owner: str
    escalation_contact: str
    access_request_id: str
    sandbox_ready: bool

    @property
    def owner_assigned(self) -> bool:
        return bool(self.onboarding_owner.strip())

    @property
    def escalation_ready(self) -> bool:
        return "@" in self.escalation_contact


def build_access_checklist(
    onboarding_owner: str,
    escalation_contact: str,
    access_request_id: str,
    *,
    sandbox_ready: bool,
) -> RobynAccessChecklist:
    return RobynAccessChecklist(
        client="Robyn",
        onboarding_owner=onboarding_owner,
        escalation_contact=escalation_contact,
        access_request_id=access_request_id,
        sandbox_ready=sandbox_ready,
    )
