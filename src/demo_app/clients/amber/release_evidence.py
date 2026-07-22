from dataclasses import dataclass


@dataclass(frozen=True)
class AmberReleaseEvidence:
    client: str
    release_notes_url: str
    regression_evidence_url: str
    approval_owner: str
    rollout_window: str

    @property
    def has_release_notes(self) -> bool:
        return self.release_notes_url.startswith("https://")

    @property
    def has_regression_evidence(self) -> bool:
        return self.regression_evidence_url.startswith("https://")

    @property
    def has_approval_owner(self) -> bool:
        return bool(self.approval_owner.strip())

    @property
    def ready_for_release_review(self) -> bool:
        return self.has_release_notes and self.has_regression_evidence and self.has_approval_owner


def collect_release_evidence(
    release_notes_url: str,
    regression_evidence_url: str,
    approval_owner: str,
    rollout_window: str,
) -> AmberReleaseEvidence:
    return AmberReleaseEvidence(
        client="Amber",
        release_notes_url=release_notes_url,
        regression_evidence_url=regression_evidence_url,
        approval_owner=approval_owner,
        rollout_window=rollout_window,
    )


def release_evidence_blockers(evidence: AmberReleaseEvidence) -> list[str]:
    blockers: list[str] = []
    if not evidence.has_release_notes:
        blockers.append("Release notes must be linked with an HTTPS URL.")
    if not evidence.has_regression_evidence:
        blockers.append("Regression evidence must be linked with an HTTPS URL.")
    if not evidence.has_approval_owner:
        blockers.append("Amber approval owner is not assigned.")
    return blockers
