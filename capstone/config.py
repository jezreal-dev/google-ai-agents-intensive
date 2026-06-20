"""
capstone/config.py
==================
Central configuration loader. All values read from environment
variables with safe defaults for local development.
"""
import os
from dotenv import load_dotenv

load_dotenv()

settings: dict = {
    "gemini_model": os.getenv("GEMINI_MODEL", "gemini-2.0-flash"),
    "hitl_threshold_severity": os.getenv("HITL_THRESHOLD_SEVERITY", "SEV2"),
    "log_level": os.getenv("LOG_LEVEL", "INFO"),
    "google_api_key": os.getenv("GOOGLE_API_KEY", ""),
}
