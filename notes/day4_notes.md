# Day 4 Study Notes — Vibe Coding Agent Security & Evaluation

> **Unit 4 · June 18, 2026**
> Podcast: [YouTube](https://www.youtube.com/watch?v=Ddz1b8CYPvg) · Whitepaper: [Vibe Coding Agent Security and Evaluation](https://www.kaggle.com/whitepaper-vibe-coding-agent-security-and-evaluation)

---

## Overview

Day 4 explores security and evaluation in non-deterministic AI agent workflows. Traditional static analysis is not sufficient for agentic systems. The answer is establishing **"Effective Trust"** — a continuous, runtime security posture built on a 7-pillar architecture.

---

## 📄 Whitepaper Summary — *"Vibe Coding Agent Security and Evaluation"*

### 1. Moving from Static to "Effective Trust"

| Traditional Security | Effective Trust (AI Agents) |
|---------------------|----------------------------|
| Deterministic — code behaves the same every run | Non-deterministic — agent behavior can drift at runtime |
| Static analysis (linting, SAST) is sufficient | Requires runtime guardrails + continuous evaluation |
| One-time security review | Continuous "Trust Score" monitoring |

### 2. The 7-Pillar Security Architecture

| # | Pillar | Description |
|---|--------|-------------|
| 1 | **Ephemeral Sandboxing** | Agents execute commands inside short-lived, isolated environments (Docker, virtual sandboxes) to prevent host system damage |
| 2 | **Human-in-the-Loop (HITL)** | Critical actions — payments, deletions, key file modifications — require explicit human confirmation before execution |
| 3 | **Indirect Prompt Injection Defense** | Sanitize all files and URLs the agent reads to block malicious prompts embedded in external data |
| 4 | **Credential Scoping** | Limit token and API key access strictly to resources required by the active task |
| 5 | **Slopsquatting Protection** | Verify all package installs; attackers publish AI-generated malicious packages with names mimicking popular libraries |
| 6 | **Trajectory Auditing** | Log every tool call, reasoning step, and state change for post-hoc analysis and forensics |
| 7 | **Dynamic Safety Guardrails** | Hardcoded predicates that block unsafe commands before they reach execution |

### 3. Red / Blue / Green Security Triad

```
Red Team   → Attack:    Prompt injections, data poisoning, bypass strategies
Blue Team  → Defend:    Sandboxing, lints, input validation, logging policies
Green Team → Evaluate:  Metrics, trajectory audits (OpenTelemetry), test suites
```

> [!WARNING]
> **Slopsquatting** is an emerging supply-chain attack where adversaries publish packages with names nearly identical to popular libraries, filled with AI-generated malicious code. Always verify package checksums and pin dependency versions.

---

## 🎙️ Podcast Summary — Unit 4

### Key Discussion Points

- **Securing the Agent Loop**: A compromised agent has access to terminal execution and local file APIs — sandboxing is non-negotiable.
- **The Value of Trajectory Logs**: Storing a complete trace of an agent's thoughts and tool calls gives security teams the full picture when a failure occurs.
- **Automated Scans in CI/CD**: Running credential and threat scans on every commit catches leaks before they reach production.

---

## 🛠️ Implementation — HITL & Security Scans

### 1. Expense Approval Agent — [`scripts/expense_agent.py`](../scripts/expense_agent.py)

Demonstrates **Human-in-the-Loop (HITL)** triage:

| Expense | Behaviour |
|---------|-----------|
| ≤ $100.00 | Auto-approved — no human input required (`hitl=False`) |
| > $100.00 | Execution blocks and prompts the user for explicit approval (`hitl=True`) |

### 2. Credential Leak Scanner — [`scripts/security_scan.py`](../scripts/security_scan.py)

A local scanner that parses all files recursively, flagging any raw API keys matching the `AIzaSy...` pattern. Integrated as a **git pre-commit hook** so every commit is scanned automatically.

### 3. SDD Gherkin Test Runner — [`scripts/run_sdd_tests.py`](../scripts/run_sdd_tests.py)

Validates `expense_agent.py` against the Gherkin specification in [`expense_agent.feature`](../scripts/expense_agent.feature) — both scenarios pass cleanly.

| Scenario | Result |
|----------|--------|
| Small expense ($45) — auto-approved | ✅ PASSED |
| Large expense ($250) — HITL gate triggered | ✅ PASSED |
