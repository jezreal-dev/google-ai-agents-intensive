"""Tests for capstone configuration loader."""
from capstone.config import settings

def test_settings_has_required_keys():
    assert "gemini_model" in settings
    assert "hitl_threshold_severity" in settings
    assert "log_level" in settings

def test_gemini_model_is_string():
    assert isinstance(settings["gemini_model"], str)
    assert len(settings["gemini_model"]) > 0

def test_hitl_threshold_severity_is_valid():
    assert settings["hitl_threshold_severity"] in ("SEV1", "SEV2", "SEV3")
