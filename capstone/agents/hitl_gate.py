"""
capstone/agents/hitl_gate.py
==============================
HITL Gate: blocks any remediation action for SEV1/SEV2 incidents
until a human explicitly approves via stdin.

RULE: This gate must NEVER be bypassed or auto-approved in production.
      Only patch builtins.input in automated tests.
"""
import time
from capstone.telemetry import log_span

_AUTO_APPROVE = {"SEV3"}


def evaluate(triage_result: dict, proposed_action: str) -> dict:
    """
    Evaluate whether a remediation requires human approval.
    SEV1/SEV2 → blocks on input(). SEV3 → auto-approves.
    Returns {human_required: bool, approved: bool, action: str, severity: str}
    """
    start = time.monotonic()
    severity = triage_result.get("severity", "SEV2")
    service = triage_result.get("affected_service", "unknown")
    human_required = severity not in _AUTO_APPROVE
    approved = False

    if human_required:
        print(f"\n{'='*60}")
        print(f"[!] HITL GATE — {severity} incident on {service}")
        print(f"[!] Proposed action: {proposed_action}")
        print(f"{'='*60}")
        response = input("Approve this remediation? (y/n): ").strip().lower()
        approved = response == "y"
        print(f"[{'+'if approved else '!'}] Remediation {'APPROVED' if approved else 'REJECTED'}.")
    else:
        approved = True
        print(f"[*] {severity} — auto-approved: {proposed_action}")

    result = {"human_required": human_required, "approved": approved,
              "action": proposed_action, "severity": severity}
    log_span("hitl_gate.evaluate", {"severity": severity, "action": proposed_action[:50]},
             {"human_required": human_required, "approved": approved},
             (time.monotonic() - start) * 1000)
    return result
