"""
capstone/telemetry.py
=====================
Telemetry adapter for capstone agents.
Wraps scripts/observability_logger.py without requiring agents to
import from the scripts/ directory directly.
"""
import sys
import os
import uuid
from datetime import datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

try:
    from observability_logger import log_span as _base_log_span
    _HAS_BASE = True
except ImportError:
    _HAS_BASE = False


def log_span(operation: str, inputs: dict, outputs: dict, duration_ms: float) -> dict:
    """Log a telemetry span. Never raises — telemetry must not crash the agent."""
    span = {
        "span_id": str(uuid.uuid4())[:8],
        "operation": operation,
        "inputs": inputs,
        "outputs": outputs,
        "duration_ms": duration_ms,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    if _HAS_BASE:
        try:
            _base_log_span(operation, inputs, outputs, duration_ms)
        except Exception:
            pass
    return span
