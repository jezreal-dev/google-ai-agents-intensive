"""
capstone/coordinator.py
========================
Coordinator Agent: orchestrates the 5 specialist sub-agents
using the ADK 2.0 Collaborative Teams pattern.
"""
import time
from capstone.agents.triage_agent import classify_alert
from capstone.agents.correlation_agent import correlate
from capstone.agents.rca_agent import draft_rca
from capstone.agents.notifier_agent import format_slack_message
from capstone.agents.hitl_gate import evaluate
from capstone.telemetry import log_span

_REMEDIATION_TEMPLATE = "kubectl rollout restart deployment/{service}"


def orchestrate(sentry_event: dict) -> dict:
    """Run the full 5-agent triage pipeline for a single Sentry event."""
    start = time.monotonic()
    print(f"\n{'='*60}\n[*] Coordinator: Starting triage pipeline")
    print(f"[*] Alert: {sentry_event.get('title', 'Unknown')}\n{'='*60}\n")

    print("[1/5] Triage Agent - classifying severity...")
    triage = classify_alert(sentry_event)
    print(f"      -> {triage['severity']} | {triage['affected_service']}\n")

    print("[2/5] Correlation Agent - fetching runbook + past incidents...")
    correlation = correlate(triage)
    print(f"      -> Runbook: {len(correlation['runbook_summary'])} chars | "
          f"Incidents: {len(correlation['past_incidents'])}\n")

    print("[3/5] RCA Agent - drafting root cause analysis...")
    rca = draft_rca(correlation, triage)
    print(f"      -> RCA drafted ({len(rca['rca_draft'])} chars)\n")

    print("[4/5] Notifier Agent - formatting Slack message...")
    notification = format_slack_message(rca, triage)
    print(f"\n--- SLACK NOTIFICATION PREVIEW ---\n{notification['slack_message']}\n{'--'*18}\n")

    print("[5/5] HITL Gate - evaluating remediation approval...")
    action = _REMEDIATION_TEMPLATE.format(service=triage["affected_service"])
    gate = evaluate(triage, action)

    incident_card = {
        "severity": triage["severity"],
        "affected_service": triage["affected_service"],
        "summary": triage["summary"],
        "runbook_summary": correlation["runbook_summary"],
        "past_incidents": correlation["past_incidents"],
        "rca_draft": rca["rca_draft"],
        "slack_message": notification["slack_message"],
        "human_required": gate["human_required"],
        "remediation_approved": gate["approved"],
        "proposed_action": action,
    }
    log_span("coordinator.orchestrate", {"event": sentry_event.get("title", "")},
             {"severity": triage["severity"], "approved": gate["approved"]},
             (time.monotonic() - start) * 1000)
    print(f"\n[+] Pipeline complete. Severity: {triage['severity']} | "
          f"Remediation: {'APPROVED' if gate['approved'] else 'REJECTED/PENDING'}")
    return incident_card

