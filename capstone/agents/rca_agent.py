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
    runbook = correlation_result.get("runbook_summary", "No runbook found.")
    incidents = correlation_result.get("past_incidents", [])
    evidence = "\n".join(f"- [{i['title']}]({i['url']}): {i['body'][:100]}" for i in incidents) \
               or "No past incidents found."
    rca = _TEMPLATE.format(
        service=triage_result["affected_service"], severity=triage_result["severity"],
        title=triage_result["title"],
        root_cause=f"{triage_result['summary']}. {runbook}",
        evidence=evidence, recommended_action=runbook,
    )
    result = {"rca_draft": rca.strip()}
    log_span("rca_agent.draft_rca", {"service": triage_result["affected_service"]},
             {"rca_length": len(rca)}, (time.monotonic() - start) * 1000)
    return result
