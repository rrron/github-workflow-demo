from dataclasses import dataclass


@dataclass(frozen=True)
class AmberReleaseGate:
    client: str
    release_owner: str
    regression_evidence_url: str
    release_window_confirmed: bool

    @property
    def ready_for_approval(self) -> bool:
        return self.release_window_confirmed and self.regression_evidence_url.startswith("https://")


def evaluate_release_gate(
    release_owner: str,
    regression_evidence_url: str,
    *,
    release_window_confirmed: bool,
) -> AmberReleaseGate:
    return AmberReleaseGate(
        client="Amber",
        release_owner=release_owner,
        regression_evidence_url=regression_evidence_url,
        release_window_confirmed=release_window_confirmed,
    )
