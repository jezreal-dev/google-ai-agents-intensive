"""Tests for Triage Agent — Gherkin scenarios 1 and 2."""
from capstone.agents.triage_agent import classify_alert

def test_fatal_alert_classified_as_sev1():
    result = classify_alert({"level": "fatal", "title": "OOM kill in payment-service",
                              "stacktrace": "MemoryError at line 142", "service": "payment-service"})
    assert result["severity"] == "SEV1"
    assert result["affected_service"] == "payment-service"
    assert "OOM" in result["summary"]

def test_warning_alert_classified_as_sev3():
    result = classify_alert({"level": "warning", "title": "Slow DB queries on reporting-service",
                              "stacktrace": "", "service": "reporting-service"})
    assert result["severity"] == "SEV3"

def test_classify_alert_returns_required_keys():
    result = classify_alert({"level": "error", "title": "Unknown error", "stacktrace": "", "service": "api"})
    for key in ("severity", "affected_service", "summary"):
        assert key in result
