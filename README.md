# Google AI Agents Intensive — Portfolio

> **5-Day AI Agents: Intensive Vibe Coding Course with Google**
> June 15–19, 2026 · Kaggle × Google DeepMind

A hands-on portfolio documenting all study notes, daily assignments, working code deliverables, and capstone project development from the 5-day intensive program.

---

## 📅 Course Roadmap

| Day | Topic | Key Deliverables |
|-----|-------|-----------------|
| **Day 1** | Introduction to Agents & Vibe Coding | [`day1_notes.md`](notes/day1_notes.md) · [`index.html`](index.html) Web App |
| **Day 2** | Agent Tools & Interoperability (MCP) | [`day2_notes.md`](notes/day2_notes.md) · [`cli_usage.md`](docs/cli_usage.md) · [`SECURITY.md`](SECURITY.md) |
| **Day 3** | Agent Skills & Memory | [`day3_notes.md`](notes/day3_notes.md) · [`SKILL.md`](.agents/skills/hello-world-skill/SKILL.md) |
| **Day 4** | Security & Evaluation | [`day4_notes.md`](notes/day4_notes.md) · [`expense_agent.py`](scripts/expense_agent.py) · [`security_scan.py`](scripts/security_scan.py) |
| **Day 5** | Spec-Driven Production Development | [`day5_notes.md`](notes/day5_notes.md) · [`cloud_run_deploy.sh`](scripts/cloud_run_deploy.sh) · [`expense_agent.feature`](scripts/expense_agent.feature) |
| **🏆 Capstone** | SRE Incident Triage Agent | [`capstone/`](capstone/) · [`capstone/ARCHITECTURE.md`](capstone/ARCHITECTURE.md) |

---

## 📂 Repository Structure

```text
google-ai-agents-intensive/
│
├── .github/
│   └── dependabot.yml              # Automated dependency security scanning
│
├── .agents/
│   └── skills/
│       └── hello-world-skill/
│           └── SKILL.md            # Day 3: Local declarative agent skill definition
│
├── capstone/                       # 🏆 Capstone Project: Multi-Agent Triage System
│   ├── agents/                     # Specialist sub-agents
│   │   ├── triage_agent.py         # 1. Classification & service extraction
│   │   ├── correlation_agent.py    # 2. Runbook & incident search
│   │   ├── rca_agent.py            # 3. Root Cause Analysis documentation
│   │   ├── notifier_agent.py       # 4. Slack notification template formatter
│   │   └── hitl_gate.py            # 5. Human-in-the-loop validation gate
│   ├── ARCHITECTURE.md             # Technical design & agent topology
│   ├── config.py                   # Central settings loader (API models, thresholds)
│   ├── coordinator.py              # Orchestration layer
│   ├── mcp_client.py               # Google Dev Knowledge, GitHub, Sentry wrapper
│   ├── pipeline.py                 # Pipeline entrypoint execution runner
│   └── telemetry.py                # Mock OpenTelemetry observability span logger
│
├── docs/
│   └── cli_usage.md                # Antigravity CLI (agy) & agentapi usage guide
│
├── notes/
│   ├── day1_notes.md               # Unit 1: Introduction to Agents & Vibe Coding
│   ├── day2_notes.md               # Unit 2: Agent Tools & Interoperability (MCP)
│   ├── day3_notes.md               # Unit 3: Agent Skills & Memory Management
│   ├── day4_notes.md               # Unit 4: Security & Evaluation
│   └── day5_notes.md               # Unit 5: Spec-Driven Production Development
│
├── scripts/
│   ├── cloud_run_deploy.sh         # Day 5: Cloud Run deployment simulation
│   ├── expense_agent.feature       # Day 5: Gherkin BDD specification
│   ├── expense_agent.py            # Day 4: Expense approval agent with HITL
│   ├── expense_results.json        # Persisted expense approval log
│   ├── observability_logger.py     # Day 5: OpenTelemetry-style telemetry logger
│   ├── run_sdd_tests.py            # Day 5: Gherkin SDD test runner
│   ├── security_scan.py            # Day 4: Credential leak pre-commit scanner
│   └── sre_triage_agent.py         # Study exercises: SRE incident triage skeleton
│
├── tests/                          # 🧪 Automated Test Suite (25 passing tests)
│   ├── test_agents_correlation.py  # Unit tests for Correlation specialist
│   ├── test_agents_hitl.py         # Unit tests for HITL safety gate
│   ├── test_agents_rca.py          # Unit tests for RCA & Slack notification formats
│   ├── test_agents_triage.py       # Unit tests for Severity Triage
│   ├── test_config.py              # Settings validation test cases
│   ├── test_mcp_client.py          # Simulated MCP server client test cases
│   ├── test_pipeline.py            # E2E pipeline integration scenarios
│   └── test_telemetry.py           # Telemetry span safety validation
│
├── .gitignore                      # Python, OS, and IDE artifact exclusions
├── README.md                       # Course overview & portfolio index (this file)
├── SECURITY.md                     # Vulnerability reporting policy
├── progress.md                     # Interactive daily progress checklist
│
├── index.html                      # Day 1: Snowflakes & Balloons web app
├── index.css                       # Day 1: Animation styles
└── index.js                        # Day 1: Interactive trigger logic
```

---

## 🛠️ Local Setup

### Prerequisites

- Python 3.10+
- [Antigravity 2.0](https://antigravity.dev) with CLI (`agy`) installed
- A Google Cloud API Key (for MCP server configuration)

### 1. View the Day 1 Web App

```bash
python -m http.server 8080
# Open http://localhost:8080 in your browser
```

### 2. Configure the Google Developer Knowledge MCP Server

> **Security note:** The API key is stored in `~/.gemini/antigravity/mcp_config.json`, which lives **outside** this repo to prevent committing secrets.

Add the following to your central `mcp_config.json`:

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

Verify the connection in the Antigravity TUI by querying: *"Does Google Workspace support MCP servers?"*

### 3. Run the SDD Gherkin Test Suite

```bash
python scripts/run_sdd_tests.py
```

Expected output:

```
[*] Running SDD Gherkin validation tests...
>> Scenario: Small expense claims are automatically approved
   [+] PASSED: Auto-approved with hitl=False
>> Scenario: Large expense claims block for human-in-the-loop triage
   [+] PASSED: HITL gate triggered with hitl=True
[+] ALL GHERKIN SCENARIOS PASSED
```

### 4. Run the Credential Security Scanner

```bash
python scripts/security_scan.py
# Also runs automatically as a git pre-commit hook
```

### 5. Run the Capstone SRE Incident Triage Agent

Start the multi-agent incident orchestration pipeline runner:

```bash
python -m capstone.pipeline FAKE-EVENT-ID-001
```

*   When prompted `Approve this remediation? (y/n):` — type `y` to approve or `n` to reject.
*   To bypass the interactive HITL prompt for testing, you can modify `hitl_threshold_severity` in environment settings or pipe a simulated response: `echo "y" | python -m capstone.pipeline FAKE-EVENT-ID-001`

### 6. Run the Full Automated Test Suite

To run all 25 unit and integration tests across config, MCP wrapper, and agents:

```bash
python -m pytest -v
```

---

## 🔗 Course Resources

| Resource | Link |
|----------|------|
| Course Home | [Kaggle — 5-Day AI Agents Intensive](https://www.kaggle.com/learn-guide/5-day-genai) |
| Capstone Submission | [Kaggle Competition Page](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project) |
| ADK Documentation | [Google Agent Development Kit](https://google.github.io/adk-docs/) |
| MCP Specification | [modelcontextprotocol.io](https://modelcontextprotocol.io) |

---

## 📄 License

This repository is a personal learning portfolio. All course materials, whitepapers, and codelabs are the property of Google and Kaggle.
