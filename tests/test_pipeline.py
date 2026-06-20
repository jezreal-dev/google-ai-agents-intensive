"""End-to-end pipeline test — Gherkin scenario 8."""
from unittest.mock import patch
from capstone.pipeline import run_pipeline

def test_full_pipeline_returns_complete_incident_card():
    with patch("capstone.agents.correlation_agent.query_developer_knowledge",
               return_value="Restart the pod and review memory limits."), \
         patch("capstone.agents.correlation_agent.search_github_issues",
               return_value=[{"title": "Past OOM", "url": "https://x", "body": "Fixed by restart"}]), \
         patch("builtins.input", return_value="y"):
        result = run_pipeline("FAKE-EVENT-ID-001")
    for key in ("severity", "rca_draft", "slack_message", "human_required"):
        assert key in result

def test_full_pipeline_sev1_requires_human():
    with patch("capstone.agents.correlation_agent.query_developer_knowledge", return_value="Fix."), \
         patch("capstone.agents.correlation_agent.search_github_issues", return_value=[]), \
         patch("builtins.input", return_value="n"):
        result = run_pipeline("FAKE-EVENT-ID-001")
    assert result["human_required"] is True
    assert result["remediation_approved"] is False
