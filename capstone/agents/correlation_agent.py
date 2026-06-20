"""
capstone/agents/correlation_agent.py
=====================================
Correlation Agent: fetches Google Cloud runbook via GDK MCP
and searches GitHub for similar past incidents.
"""
import time
from capstone.mcp_client import query_developer_knowledge, search_github_issues
from capstone.telemetry import log_span


def correlate(triage_result: dict) -> dict:
    """Fetch runbook and past incidents for a triaged alert."""
    start = time.monotonic()
    triage_result = triage_result or {}
    service = triage_result.get("affected_service", "unknown-service")
    severity = triage_result.get("severity", "SEV2")
    summary = triage_result.get("summary", "")
    query = (f"Recommended procedure for a {severity} incident "
             f"on {service}. Context: {summary}")
    runbook = query_developer_knowledge(query) or ""
    incidents = search_github_issues("my-org/sre-runbooks", [service, severity]) or []
    result = {"runbook_summary": runbook, "past_incidents": incidents,
              "service": service, "severity": severity}
    log_span("correlation_agent.correlate", {"service": service},
             {"runbook_chars": len(runbook), "incidents": len(incidents)},
             (time.monotonic() - start) * 1000)
    return result
