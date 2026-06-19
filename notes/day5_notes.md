# Day 5 Study Notes — Spec-Driven Production Grade Development

> **Unit 5 · June 19, 2026**
> Podcast: [YouTube](https://www.youtube.com/watch?v=VSRdL4wlbLY) · Whitepaper: [Spec-Driven Production Grade Development in the Age of Vibe Coding](https://www.kaggle.com/whitepaper-spec-driven-production-grade-development-in-the-age-of-vibe-coding)

---

## Overview

Day 5 bridges the gap between fragile vibe-coded prototypes and production-grade enterprise software. The answer is **Spec-Driven Development (SDD)** — where behavior specifications (written in Gherkin) become the source of truth that drives all code generation, testing, and deployment decisions.

---

## 📄 Whitepaper Summary — *"Spec-Driven Production Grade Development in the Age of Vibe Coding"*

### 1. Spec-Driven Development (SDD)

> [!IMPORTANT]
> In SDD, **code is disposable**. The source of truth is the specification, not the implementation. The agent is instructed to write and modify code *only* to satisfy the defined specs.

**Core principle:** Write the spec first. Generate code to match it. If they diverge, fix the code — never the spec.

**Gherkin syntax** (Given/When/Then) makes behavior-driven specifications human-readable and machine-parseable:

```gherkin
Feature: Expense approval workflow
  Scenario: Small expense claims are automatically approved
    Given an expense of $45.00 is submitted
    When the agent processes the claim
    Then the status should be "Approved"
    And the HITL flag should be False
```

### 2. The Production Grade Gap

| Prototype (Vibe Code) | Production Grade (SDD) |
|-----------------------|------------------------|
| Works locally, flaky in production | Deterministic, spec-verified behavior |
| No formal test coverage | Gherkin scenarios act as executable contracts |
| Manual deployment | Automated CI/CD with pre-commit gates |
| Unstructured logs | OpenTelemetry-structured telemetry traces |

### 3. Zero-Trust Development Pipelines

- **Automated code-review agents**: Audit generated code changes before staging or deploying.
- **Hybrid Policy Servers**: Dynamically govern what actions agents can take and restrict access to backend infrastructure.
- **Pre-commit gates**: Security and SDD tests run automatically before every commit reaches the remote.

---

## 🎙️ Podcast Summary — Unit 5

### Key Discussion Points

- **The Paradigm of SDD**: Shift from capability testing ("can it do X?") to specification verification ("does it satisfy the contract?").
- **Disposable Code**: In vibe coding, implementations are temporary. Regenerate code freely as long as specs are preserved.
- **Fleet Governance**: When deploying multiple agents across cloud environments, policy servers and observability pipelines become critical for maintaining consistency.

---

## 🛠️ Implementation — Local SDD Simulation

### 1. Cloud Run Deployment — [`scripts/cloud_run_deploy.sh`](../scripts/cloud_run_deploy.sh)

Simulates the full scaffolding, build, and deployment workflow for pushing the expense agent to **Google Cloud Run** via Agent Runtime:

```bash
bash scripts/cloud_run_deploy.sh
```

### 2. Telemetry Observability — [`scripts/observability_logger.py`](../scripts/observability_logger.py)

Implements structured JSON logging and trajectory tracing in an **OpenTelemetry-compatible format**. Records:

| Field | Description |
|-------|-------------|
| `span_id` | Unique identifier for each tool call |
| `operation` | Name of the tool/function called |
| `duration_ms` | Measured latency |
| `inputs` / `outputs` | Captured inputs and results |
| `timestamp` | ISO 8601 timestamp |

### 3. Gherkin Specification — [`scripts/expense_agent.feature`](../scripts/expense_agent.feature)

Defines the behavioral contracts for the expense approval agent using BDD syntax. This file is the **source of truth** — the implementation in `expense_agent.py` must satisfy it.

### 4. SDD Test Runner — [`scripts/run_sdd_tests.py`](../scripts/run_sdd_tests.py)

Parses the `.feature` file and validates `expense_agent.py` against each Gherkin scenario. Uses `unittest.mock` to simulate HITL human input for headless test execution.

**Run the full suite:**

```bash
python scripts/run_sdd_tests.py
```

**Verified results:**

| Scenario | Outcome |
|----------|---------|
| Small expense ($45) — auto-approve | ✅ PASSED |
| Large expense ($250) — HITL gate | ✅ PASSED |
