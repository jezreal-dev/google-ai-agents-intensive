"""
capstone/agents/notifier_agent.py
===================================
Notifier Agent: formats incident data as a Slack-ready message string.
In production this calls the Slack MCP server.
"""
import time
from capstone.telemetry import log_span

_TEMPLATE = """🚨 *{severity} INCIDENT — {service}*

*Summary:* {summary}

*Root Cause Analysis:*
{rca_snippet}

Pause *Human approval required* before any remediation is executed.
"""


def format_slack_message(rca_result: dict, triage_result: dict) -> dict:
    """Format incident data as a Slack notification. Returns {slack_message: str}."""
    start = time.monotonic()
    rca = rca_result.get("rca_draft", "RCA pending.")
    snippet = rca[:400] + "..." if len(rca) > 400 else rca
    message = _TEMPLATE.format(
        severity=triage_result["severity"], service=triage_result["affected_service"],
        summary=triage_result["summary"], rca_snippet=snippet,
    )
    result = {"slack_message": message.strip()}
    log_span("notifier_agent.format_slack_message", {"severity": triage_result["severity"]},
             {"message_length": len(message)}, (time.monotonic() - start) * 1000)
    return result
