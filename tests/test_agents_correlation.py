"""Tests for Correlation Agent - Gherkin scenario 3."""
from unittest.mock import patch
from capstone.agents.correlation_agent import correlate

_TRIAGE = {"severity": "SEV1", "affected_service": "payment-service",
           "summary": "OOM kill", "title": "OOM kill"}

def test_correlate_returns_non_empty_runbook_summary():
    with patch("capstone.agents.correlation_agent.query_developer_knowledge",
               return_value="Restart the pod and check memory limits."), \
         patch("capstone.agents.correlation_agent.search_github_issues",
               return_value=[{"title": "Past OOM", "url": "https://x", "body": "Fixed by restart"}]):
        result = correlate(_TRIAGE)
    assert isinstance(result["runbook_summary"], str) and len(result["runbook_summary"]) > 0

def test_correlate_past_incidents_have_required_keys():
    with patch("capstone.agents.correlation_agent.query_developer_knowledge", return_value="Fix: restart."), \
         patch("capstone.agents.correlation_agent.search_github_issues",
               return_value=[{"title": "t", "url": "u", "body": "b"}]):
        result = correlate(_TRIAGE)
    assert isinstance(result["past_incidents"], list) and len(result["past_incidents"]) >= 1
    assert "title" in result["past_incidents"][0] and "url" in result["past_incidents"][0]
