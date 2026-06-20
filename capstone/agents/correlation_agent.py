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
    service = triage_result["affected_service"]
    query = (f"Recommended procedure for a {triage_result['severity']} incident "
             f"on {service}. Context: {triage_result['summary']}")
    runbook = query_developer_knowledge(query)
    incidents = search_github_issues("my-org/sre-runbooks", [service, triage_result["severity"]])
    result = {"runbook_summary": runbook, "past_incidents": incidents,
              "service": service, "severity": triage_result["severity"]}
    log_span("correlation_agent.correlate", {"service": service},
             {"runbook_chars": len(runbook), "incidents": len(incidents)},
             (time.monotonic() - start) * 1000)
    return result
