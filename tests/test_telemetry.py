# tests/test_telemetry.py
"""Tests for the telemetry adapter."""
from capstone.telemetry import log_span

def test_log_span_returns_dict_with_required_keys():
    result = log_span("triage_agent.classify", {"alert": "OOM"}, {"severity": "SEV1"}, 142.3)
    for key in ("span_id", "operation", "inputs", "outputs", "duration_ms", "timestamp"):
        assert key in result

def test_log_span_values_are_correct():
    result = log_span("test.op", {"k": "v"}, {"out": 1}, 10.0)
    assert result["operation"] == "test.op"
    assert result["duration_ms"] == 10.0
    assert result["inputs"] == {"k": "v"}
