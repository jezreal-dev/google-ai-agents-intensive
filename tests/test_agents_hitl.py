"""Tests for HITL Gate - Gherkin scenarios 6 and 7."""
from unittest.mock import patch
from capstone.agents.hitl_gate import evaluate

def test_sev1_requires_human_and_approves_on_y():
    with patch("builtins.input", return_value="y"):
        result = evaluate({"severity": "SEV1", "affected_service": "payment-service"},
                          "kubectl rollout restart deployment/payment-service")
    assert result["human_required"] is True
    assert result["approved"] is True

def test_sev1_rejection_sets_approved_false():
    with patch("builtins.input", return_value="n"):
        result = evaluate({"severity": "SEV1", "affected_service": "payment-service"},
                          "kubectl rollout restart deployment/payment-service")
    assert result["human_required"] is True
    assert result["approved"] is False

def test_sev3_auto_approves_without_input():
    result = evaluate({"severity": "SEV3", "affected_service": "reporting-service"}, "scale up replicas by 1")
    assert result["human_required"] is False
    assert result["approved"] is True
