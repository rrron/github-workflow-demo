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
