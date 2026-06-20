# Capstone Project Submission: SRE Incident Triage Agent

**Track:** Track 2 — Agents for Business  
**Author:** Jezreal Momoh  
**GitHub Repository:** [google-ai-agents-intensive](https://github.com/jezreal-dev/google-ai-agents-intensive)  
**Demo Video (YouTube):** *[Insert your YouTube Link here]*  

---

## 1. Problem Statement & Business Value

Production downtime is extremely costly. According to industry surveys, the average cost of IT downtime is **$5,600 per minute**, translating to over **$300,000 per hour** in lost revenue, SLA penalties, and operational overhead. 

When a critical production alert fires at 2:00 AM, SRE (Site Reliability Engineering) teams face a high-stress, manual workflow:
1.  Acknowledging the alert in monitoring portals.
2.  Manually querying documentation for corresponding runbooks.
3.  Searching historical databases or GitHub issues to see if the issue is a known regression.
4.  Investigating stack traces to draft a Root Cause Analysis (RCA) report.
5.  Alerting the engineering team on Slack.
6.  Proposing and executing remediation commands (e.g. restarting a Kubernetes deployment).

This manual triage process typically takes **15 to 20 minutes** of critical coordination time. 

The **SRE Incident Triage Agent** solves this enterprise pain point by automating the entire investigative workflow in **under 30 seconds**. By coordinating a fleet of specialized sub-agents and grounding their inputs in live documentation using the Model Context Protocol (MCP), it reduces operational overhead and TTR (Time to Resolution) while strictly enforcing human gatekeeping for high-severity changes.

---

## 2. Why AI Agents?

Traditional runbook automation relies on rigid, static scripts (e.g., if CPU > 90%, restart). These scripts fail to handle non-deterministic failure modes (like database locking, microservice memory leaks, or dependency drift) and have no capacity to understand context, write human-readable diagnostics, or look up unstructured historic documentation.

AI agents—specifically orchestrated multi-agent systems—bridge this gap:
*   **Reasoning Capability:** They analyze unstructured raw traceback data to extract meaning and targets.
*   **Dynamic Tool Calling:** They query developer documentation and search issues dynamically based on search terms they generate.
*   **Synthesis:** They summarize complex debugging contexts to draft cohesive, human-readable RCA reports and team slack notifications.

---

## 3. System Architecture & Agent Topology

The system uses the **ADK 2.0 Collaborative Teams** pattern. A central coordinator agent manages state and sequences data through five specialized sub-agents:

```
[Sentry Alert Event]
        │
        ▼
[Coordinator Agent] (Orchestrates State & Telemetry)
        │
        ├──► 1. Triage Agent ───────► (Extracts affected service & log severity)
        │
        ├──► 2. Correlation Agent ──► (MCP queries: Google Cloud Runbooks & GitHub Issues)
        │
        ├──► 3. RCA Agent ──────────► (Drafts markdown Root Cause Analysis)
        │
        ├──► 4. Notifier Agent ─────► (Formats structured team Slack alert)
        │
        └──► 5. HITL Gate Agent ────► (Blocks SEV1/SEV2 actions for human y/n approval)
        │
        ▼
[Final Action Execution] (e.g., kubectl rollout restart)
```

### Specialist Sub-Agent Directory
1.  **Triage Agent (capstone/agents/triage_agent.py):** Parses raw Sentry payloads. It extracts metadata, maps log levels (`error`, `warning`) to standard severities (`SEV1`-`SEV3`), and identifies target service keywords.
2.  **Correlation Agent (capstone/agents/correlation_agent.py):** Connects to external systems via MCP. It pulls Google Cloud troubleshooting documentation and scans past closed issues in GitHub to find matching historic incident data.
3.  **RCA Agent (capstone/agents/rca_agent.py):** Merges the traceback facts with the correlation context to write a structured, markdown-formatted Root Cause Analysis report.
4.  **Notifier Agent (capstone/agents/notifier_agent.py):** Formats the diagnostic results into a Slack notification template for direct team consumption.
5.  **HITL Gate Agent (capstone/agents/hitl_gate.py):** Enforces security guardrails. Evaluates settings and halts execution to prompt the console operator (`y/n`) for approval on any SEV1/SEV2 remediation.

---

## 4. Key Course Concepts Demonstrated

To fulfill the capstone requirements, this project demonstrates five key concepts from the Google AI Agents course:

### A. Multi-Agent Collaborative System (ADK)
The system is built entirely on the **Google Agent Development Kit (ADK) 2.0** framework, utilizing isolated agent classes overseen by a central [coordinator.py](capstone/coordinator.py) orchestrator.

### B. Model Context Protocol (MCP) Integration
To prevent hallucinated debugging steps, the Correlation Agent utilizes two active MCP servers:
*   `google-developer-knowledge` (`search_documents`): Queries Google's official developer documentation corpus for runbook verification.
*   `github` (`search_github_issues`): Searches historic logs in the organization repository (`my-org/sre-runbooks`).

### C. Human-in-the-Loop (HITL) Security Gate
The agent is prohibited from executing high-severity changes automatically. The [hitl_gate.py](capstone/agents/hitl_gate.py) checks configuration levels (`hitl_threshold_severity`) and blocks for user confirmation, ensuring a human remains in the loop for critical systems.

### E. Automated Credential Security Hook
A pre-commit script ([security_scan.py](scripts/security_scan.py)) scans all files for leaked API keys or access tokens before commits, protecting the codebase against credential leakage in public repositories.

### F. Telemetry & Observability
A custom telemetry logging adapter ([telemetry.py](capstone/telemetry.py)) tracks execution spans and latencies, mirroring production OpenTelemetry standards.

---

## 5. Setup & Execution Instructions

To reproduce the project and run the automated test suite locally, follow these steps:

### Setup Environment
```bash
git clone https://github.com/jezreal-dev/google-ai-agents-intensive.git
cd google-ai-agents-intensive
```

### Run the Incident Pipeline
```bash
python -m capstone.pipeline FAKE-EVENT-ID-001
```

### Run all Unit and E2E Tests
```bash
python -m pytest -v
```
*(All 25 tests pass successfully, covering individual agent logic, MCP clients, telemetry, and pipeline integrations).*
