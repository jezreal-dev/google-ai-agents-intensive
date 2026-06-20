"""
capstone/agents/triage_agent.py
================================
Triage Agent: classifies incoming alerts into SEV1-SEV3
and extracts service name and incident summary.
"""
import time
from capstone.telemetry import log_span

_LEVEL_TO_SEVERITY = {"fatal": "SEV1", "error": "SEV2", "warning": "SEV3", "info": "SEV3"}
_KNOWN_SERVICES = ["payment-service", "reporting-service", "api", "auth-service", "worker"]


def classify_alert(alert: dict) -> dict:
    """Classify alert severity and extract key metadata."""
    start = time.monotonic()
    level = (alert.get("level") or "error").lower()
    severity = _LEVEL_TO_SEVERITY.get(level, "SEV2")
    service = alert.get("service") or _extract_service(alert.get("title") or "")
    summary = _build_summary(alert)
    result = {"severity": severity, "affected_service": service, "summary": summary,
              "title": alert.get("title") or "", "original_level": level}
    log_span("triage_agent.classify_alert",
             {"level": level, "title": alert.get("title") or ""},
             {"severity": severity, "service": service},
             (time.monotonic() - start) * 1000)
    return result


def _extract_service(title: str) -> str:
    for svc in _KNOWN_SERVICES:
        if svc in title.lower():
            return svc
    return "unknown-service"


def _build_summary(alert: dict) -> str:
    title = alert.get("title") or "Unknown alert"
    stacktrace = alert.get("stacktrace") or ""
    first_line = stacktrace.split("\n")[0] if stacktrace else ""
    return f"{title}. {first_line}".strip(". ")

