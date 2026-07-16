from demo_app.clients.amber import evaluate_release_gate


def test_amber_release_gate_requires_https_regression_evidence() -> None:
    gate = evaluate_release_gate(
        release_owner="Amber Release Manager",
        regression_evidence_url="https://example.com/amber/regression",
        release_window_confirmed=True,
    )

    assert gate.client == "Amber"
    assert gate.ready_for_approval is True


def test_amber_release_gate_blocks_unconfirmed_release_window() -> None:
    gate = evaluate_release_gate(
        release_owner="Amber Release Manager",
        regression_evidence_url="https://example.com/amber/regression",
        release_window_confirmed=False,
    )

    assert gate.ready_for_approval is False
