"""Tests for RCA and Notifier agents - Gherkin scenarios 4 and 5."""
from capstone.agents.rca_agent import draft_rca
from capstone.agents.notifier_agent import format_slack_message

_TRIAGE = {"severity": "SEV1", "affected_service": "payment-service", "summary": "OOM kill", "title": "OOM kill"}
_CORRELATION = {"runbook_summary": "Restart pod and check limits.",
                "past_incidents": [{"title": "Past OOM", "url": "https://x", "body": "Fixed by restart"}],
                "service": "payment-service", "severity": "SEV1"}

def test_draft_rca_returns_non_empty_string():
    result = draft_rca(_CORRELATION, _TRIAGE)
    assert isinstance(result["rca_draft"], str) and len(result["rca_draft"]) > 50

def test_draft_rca_contains_required_sections():
    result = draft_rca(_CORRELATION, _TRIAGE)
    assert "Root Cause" in result["rca_draft"]
    assert "Recommended Action" in result["rca_draft"]

def test_slack_message_contains_severity_and_service():
    result = format_slack_message({"rca_draft": "Root Cause: OOM. Recommended Action: Restart."}, _TRIAGE)
    assert "SEV1" in result["slack_message"]
    assert "payment-service" in result["slack_message"]
    assert "Human approval required" in result["slack_message"]

def test_rca_and_notifier_with_missing_keys():
    # Test draft_rca with empty inputs
    result_rca = draft_rca({}, {})
    assert "rca_draft" in result_rca
    assert "unknown-service" in result_rca["rca_draft"]

    # Test format_slack_message with empty inputs
    result_slack = format_slack_message({}, {})
    assert "slack_message" in result_slack
    assert "unknown-service" in result_slack["slack_message"]
