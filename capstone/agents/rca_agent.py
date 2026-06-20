"""
capstone/agents/rca_agent.py
=============================
RCA Agent: synthesises triage + correlation data into a structured
Root Cause Analysis draft for SRE engineer review.
"""
import time
from capstone.telemetry import log_span

_TEMPLATE = """## Incident Root Cause Analysis

**Service:** {service}
**Severity:** {severity}
**Alert:** {title}

### Root Cause
{root_cause}

### Evidence
{evidence}

### Recommended Action
{recommended_action}

### Prevention
Monitor memory with `kubectl top pods`. Set resource limits and implement
circuit breakers for high-throughput batch operations.
"""


def draft_rca(correlation_result: dict, triage_result: dict) -> dict:
    """Draft an RCA from correlation + triage data. Returns {rca_draft: str}."""
    start = time.monotonic()
    triage_result = triage_result or {}
    service = triage_result.get("affected_service", "unknown-service")
    severity = triage_result.get("severity", "SEV2")
    title = triage_result.get("title", "Unknown alert")
    summary = triage_result.get("summary", "No summary available")

    runbook = correlation_result.get("runbook_summary", "No runbook found.")
    incidents = correlation_result.get("past_incidents", [])
    evidence = "\n".join(f"- [{i.get('title', 'Past incident')}]({i.get('url', '#')}): {i.get('body', '')[:100]}" for i in incidents) \
               or "No past incidents found."
    rca = _TEMPLATE.format(
        service=service, severity=severity,
        title=title,
        root_cause=f"{summary}. {runbook}",
        evidence=evidence, recommended_action=runbook,
    )
    result = {"rca_draft": rca.strip()}
    log_span("rca_agent.draft_rca", {"service": service},
             {"rca_length": len(rca)}, (time.monotonic() - start) * 1000)
    return result
