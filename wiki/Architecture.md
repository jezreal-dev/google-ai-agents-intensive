# Architecture & Agent Topology

This page describes the multi-agent design patterns, state flow, and execution orchestration details of the SRE Triage Agent.

---

## 1. Conductor Orchestration Pattern

Rather than a loose chain of agent interactions, the system utilizes the **ADK 2.0 Collaborative Teams** pattern. A single central orchestrator class - the **Coordinator Agent** - directs the execution flow, transfers inputs/outputs between specialist agents, constructs the final incident card, and tracks performance telemetry.

```
       Alert payload
             │
             ▼
      [Coordinator]
             │
             ├──► 1. Triage Agent ───────► (Severity, service extracted)
             │
             ├──► 2. Correlation Agent ──► (GDK runbooks, GitHub search)
             │
             ├──► 3. RCA Agent ──────────► (Drafts markdown report)
             │
             ├──► 4. Notifier Agent ─────► (Formats Slack template)
             │
             └──► 5. HITL Gate Agent ────► (Gated approval y/n)
             │
             ▼
    Final Incident Card
```

---

## 2. Specialist Sub-Agent Roles

Each sub-agent in the pipeline has a single, isolated responsibility:

### 1. Severity classification & Service Triage
*   **Module:** `capstone/agents/triage_agent.py`
*   **Role:** Analyzes the raw alert logs to identify which service (e.g. `payment-service`, `reporting-service`) is failing and maps the log levels to standard severities (`SEV1` to `SEV3`).

### 2. Context Correlation
*   **Module:** `capstone/agents/correlation_agent.py`
*   **Role:** Utilizes external Model Context Protocol (MCP) clients to search reference document runbooks and GitHub issues for historic correlation context.

### 3. Root Cause Analysis
*   **Module:** `capstone/agents/rca_agent.py`
*   **Role:** Merges correlation details (e.g., historical OOM errors) with current trace facts to write a markdown-formatted Root Cause Analysis draft.

### 4. Alert Notifier
*   **Module:** `capstone/agents/notifier_agent.py`
*   **Role:** Prepares the team Slack template detailing the diagnostic state, the RCA report, and proposed remediation actions.

### 5. Human-in-the-Loop Safety Gate
*   **Module:** `capstone/agents/hitl_gate.py`
*   **Role:** Checks settings thresholds and holds execution for manual user confirmation before any high-severity remediation actions can execute.

---

## 3. Telemetry Logging & Observation

Observability is maintained via a mock OpenTelemetry-compliant adapter (`capstone/telemetry.py`). The coordinator automatically logs diagnostic trace records in JSON format after each specialist step completes. To ensure reliability, telemetry is fully isolated within safe try-except boundaries to prevent monitoring code from ever crashing the main pipeline.
