"""
capstone/pipeline.py
=====================
Entry point for the SRE Incident Triage Agent demo.

Usage:
    python -m capstone.pipeline
    python -m capstone.pipeline FAKE-EVENT-ID-001
"""
import sys
from capstone.mcp_client import get_sentry_event
from capstone.coordinator import orchestrate


def run_pipeline(sentry_event_id: str) -> dict:
    """Fetch a Sentry event and run the full triage pipeline."""
    return orchestrate(get_sentry_event(sentry_event_id))


if __name__ == "__main__":
    event_id = sys.argv[1] if len(sys.argv) > 1 else "FAKE-EVENT-ID-001"
    result = run_pipeline(event_id)
    print("\n=== FINAL INCIDENT CARD ===")
    for k, v in result.items():
        if k not in ("rca_draft", "slack_message", "past_incidents"):
            print(f"  {k}: {v}")
