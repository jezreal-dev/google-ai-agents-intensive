# Getting Started

Welcome to the SRE Incident Triage Agent setup guide. Follow these instructions to get your environment configured and run the multi-agent pipeline.

---

## 🛠️ Environment Prerequisites

- **Python:** Python 3.10+
- **Agent SDK:** Google Agent Development Kit (ADK) 2.0
- **Testing framework:** `pytest` (e.g. `pip install pytest pytest-asyncio`)

---

## 🚀 1. Setup & Configuration

### Clone the Repository
```bash
git clone https://github.com/jezreal-dev/google-ai-agents-intensive.git
cd google-ai-agents-intensive
```

### Configure the MCP Settings
Create or update your central model context protocol configuration at `~/.gemini/antigravity/mcp_config.json` to configure the Google Developer Knowledge MCP server. (Note: store this outside the repository to ensure your API keys are kept safe):

```json
{
  "mcpServers": {
    "google-developer-knowledge": {
      "headers": {
        "X-Goog-Api-Key": "<YOUR_API_KEY>"
      },
      "serverUrl": "https://developerknowledge.googleapis.com/mcp"
    }
  }
}
```

---

## ⚙️ 2. Run the Incident Triage Pipeline

To run the pipeline against a mock Sentry event, run the CLI entrypoint:

```bash
python -m capstone.pipeline FAKE-EVENT-ID-001
```

### Interactive HITL Gate
When running a high-severity (SEV1/SEV2) incident, the coordinator will pause and prompt for confirmation in the console:

```
============================================================
[!] HITL GATE - SEV1 incident on payment-service
[!] Proposed action: kubectl rollout restart deployment/payment-service
============================================================
Approve this remediation? (y/n): 
```

- Type `y` to approve and allow execution.
- Type `n` to reject the action and pause the alert.

---

## 🧪 3. Run the Automated Test Suite

We use `pytest` to execute all unit, integration, and end-to-end pipeline tests:

```bash
python -m pytest -v
```

Expected output:
```
tests/test_agents_correlation.py::... PASSED
tests/test_agents_hitl.py::... PASSED
tests/test_agents_rca.py::... PASSED
tests/test_agents_triage.py::... PASSED
tests/test_config.py::... PASSED
tests/test_mcp_client.py::... PASSED
tests/test_pipeline.py::... PASSED
tests/test_telemetry.py::... PASSED
============================= 25 passed in 0.12s ==============================
```
