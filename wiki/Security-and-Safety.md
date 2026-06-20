# Security & Safety Guardrails

Security is a primary pillar when building agentic software. This page outlines the security protocols, pre-commit scanners, and human-in-the-loop policies implemented in the repository.

---

## 1. Human-in-the-Loop (HITL) & The Trust Ladder

Autonomous agents should not have direct, unmitigated access to write to production environments. We enforce a **Trust Ladder**:

*   **Configurable Threshold:** The gate reads `hitl_threshold_severity` from configuration (defaulting to `SEV2`).
*   **SEV1 & SEV2 Alerts (High Risk):** The pipeline halts, displays the diagnostic summaries, proposed actions, and blocks for console input (`y/n`). No actions can execute without human verification.
*   **SEV3 Alerts (Low Risk):** The proposed changes are auto-approved and logged without blocking, keeping standard maintenance smooth.

---

## 2. Automated Credential Security Scanner

To prevent accidental leakage of Cloud API credentials or GitHub personal access tokens, we enforce a two-stage scan:

1.  **Scanner Script:** `scripts/security_scan.py` parses all files in the workspace searching for strings matching common credential patterns (e.g. Google Cloud API keys, AWS secret tokens, generic auth headers).
2.  **Git Pre-commit Hook:** The scanner script is bound to the repository's `.git/hooks/pre-commit` hook. If any raw credentials are found in staged changes, the commit is automatically blocked and rejected.

---

## 3. Sandboxing & Safe Telemetry

*   **API Isolation:** Credentials and API keys are read from environment variables or local central configuration folders (like `~/.gemini/antigravity/mcp_config.json`) which are excluded from source control.
*   **Isolated Telemetry:** Telemetry logs do not contain raw tracebacks, user payloads, or authentication headers, avoiding leak risks in monitoring logs.
*   **Safe Code Execution:** Agents only generate proposals; execution commands are strictly gated by the HITL gate console wrapper.
