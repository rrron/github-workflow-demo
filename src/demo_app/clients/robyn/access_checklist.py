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

    @property
    def ready_for_onboarding(self) -> bool:
        return self.owner_assigned and self.escalation_ready and self.sandbox_ready


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


def access_readiness_blockers(checklist: RobynAccessChecklist) -> list[str]:
    blockers: list[str] = []
    if not checklist.owner_assigned:
        blockers.append("Onboarding owner is not assigned.")
    if not checklist.escalation_ready:
        blockers.append("Escalation contact must be an email address.")
    if not checklist.sandbox_ready:
        blockers.append("Robyn sandbox access is not ready.")
    return blockers
