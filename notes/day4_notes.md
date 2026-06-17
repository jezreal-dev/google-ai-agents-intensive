# Day 4 Study Notes: Vibe Coding Agent Security and Evaluation

## Overview
Day 4 explores security and evaluations in non-deterministic AI agent workflows. To establish "Effective Trust", the system relies on a strict 7-pillar architecture, defenses against package supply-chain attacks (slopsquatting), a Red/Blue/Green security triad, and OpenTelemetry trajectory evaluation.

---

## 📄 Summary: "Vibe Coding Agent Security and Evaluation" (Whitepaper)

### 1. Moving from Static to "Effective Trust"
*   **The Problem**: Unlike traditional deterministic software (where code behaves exactly the same way every run), AI agent workflows are non-deterministic. Traditional security scans (static analysis) are not enough.
*   **The Solution**: We must establish **Effective Trust**—a security posture that assumes the agent's behavior could drift and actively evaluates it during runtime using guardrails and verification.

### 2. The 7-Pillar Security Architecture
To build safe agent workflows, organizations rely on seven design pillars:
1.  **Ephemeral Sandboxing**: Agents must execute commands and run code inside short-lived, isolated environments (e.g., Docker containers or virtual sandboxes) to prevent damage to the host system.
2.  **Human-in-the-Loop (HITL) Triage**: Critical actions (like modifying key system files, making payments, or deleting resources) must require explicit human confirmation.
3.  **Indirect Prompt Injection Defense**: Sanitizing files and URLs read by the agent to prevent malicious prompts embedded in data from hijacking the agent (the "Confused Deputy" problem).
4.  **Credential Scoping**: Limiting token and API key access strictly to the resources required by the active task.
5.  **Slopsquatting Protection**: Verifying package installs. Attackers publish packages with names similar to popular libraries but filled with AI-generated malicious code ("slopsquatting").
6.  **Trajectory Auditing**: Logging every tool call, reasoning step, and state change for post-hoc analysis.
7.  **Dynamic Safety Guardrails**: Hardcoded predicates that block unsafe commands or actions before they reach execution.

### 3. Red/Blue/Green Security Triad
*   **Red Team (Attack)**: Running prompt injections, data poisoning, and bypass strategies against the agent to find vulnerabilities.
*   **Blue Team (Defense)**: Implementing sandboxing, lints, input validation, and logging policies to secure the system.
*   **Green Team (Compliance/Eval)**: Defining the evaluation metrics, auditing trajectories using tools like OpenTelemetry, and running test suites to measure agent accuracy.

---

## 🎙️ Summary: Companion Podcast Episode (Unit 4)

### Key Discussion Points
*   **Securing the Agent Loop**: Recognizing that a compromised agent has access to terminal execution and local file APIs. Sandboxing is non-negotiable.
*   **The Value of Trajectory Logs**: Storing the complete trace of an agent's thoughts and tool calls so security teams can audit what happened when a failure occurs.
*   **Automated Scans in CI/CD**: Running automated threat and credentials scans on every commit to catch leaks before they reach production.

---

## 🛠️ Local Implementation: HITL and Security Scans
1.  **Expense Agent (`expense_agent.py`)**: Demonstrates **Human-in-the-Loop (HITL)** triage. Expenses exceeding $100.00 block execution and prompt the user for input. Auto-approves smaller amounts.
2.  **Automated Scan (`security_scan.py`)**: A local scanner script that parses files recursively, searching for raw API keys (`AIzaSy...`) to prevent credential exposures.
3.  **Tests & Validation**: Both scripts were run and verified locally to ensure correctness.
