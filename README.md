# Google AI Agents Intensive Course Portfolio

Welcome to my portfolio for the **5-Day AI Agents: Intensive Vibe Coding Course With Google** (June 15 - June 19, 2026).

This repository contains all my course notes, daily assignment reflections, progress trackers, and projects developed throughout the intensive program.

---

## 📅 Course Roadmap & Deliverables

*   **Day 1: Introduction to Agents & Vibe Coding**
    *   **Topic**: Transition from manual coding syntax to natural language intent ("vibe coding").
    *   **Deliverables**: [day1_notes.md](notes/day1_notes.md) (Notes), Snowflakes & Balloons Web App prototype ([index.html](index.html) served at root).
*   **Day 2: Agent Tools & Interoperability**
    *   **Topic**: Connecting agents to external APIs, code execution, and multi-agent setups.
    *   **Deliverables**: [day2_notes.md](notes/day2_notes.md) (Notes & central MCP Setup), [cli_usage.md](docs/cli_usage.md) (CLI Guidelines), [SECURITY.md](SECURITY.md) (Security Policy), and [.github/dependabot.yml](.github/dependabot.yml) (Automated Security Updates).
*   **Day 3: Agent Skills**
    *   **Topic**: Implementing memory, handling long-context windows, and building modular agentic skills.
    *   **Deliverables**: [day3_notes.md](notes/day3_notes.md) (Notes), and a local custom declarative skill ([SKILL.md](.agents/skills/hello-world-skill/SKILL.md)).
*   **Day 4: Vibe Coding Agent Security and Evaluation**
    *   **Topic**: Testing, guardrails, security benchmarks, and safety evaluations.
    *   **Deliverables**: [day4_notes.md](notes/day4_notes.md) (Notes), [expense_agent.py](scripts/expense_agent.py) (Human-in-the-Loop simulation), and [security_scan.py](scripts/security_scan.py) (Credentials Scanner).
*   **Day 5: Spec-Driven Production Grade Development**
    *   **Topic**: Cloud deployment (Cloud Run), debugging, fleet orchestration, and Spec-Driven Development (SDD).
    *   **Deliverables**: [day5_notes.md](notes/day5_notes.md) (Notes), [cloud_run_deploy.sh](scripts/cloud_run_deploy.sh) (Cloud Run deployment simulator), [observability_logger.py](scripts/observability_logger.py) (Telemetry logger), and [expense_agent.feature](scripts/expense_agent.feature) (Gherkin specification).
*   **🏆 Capstone Project**
    *   **Topic**: Autonomous AI agent project showcasing key ADK, MCP, and skill capabilities.
    *   **Status**: Under Development (Tracks: Business, Good, Concierge, Freestyle. Deadline: July 6, 2026).

---

## 📂 Project Structure

```text
google-ai-agents-intensive/
│
├── .github/
│   └── dependabot.yml       # Automated dependency security scanning
│
├── .agents/
│   └── skills/
│       └── hello-world-skill/
│           └── SKILL.md     # Day 3: Local declarative agent skill definition
│
├── docs/
│   └── cli_usage.md            # Guidelines for using agy CLI and agentapi
│
├── notes/
│   ├── day1_notes.md           # Unit 1: Podcast and Whitepaper summaries
│   ├── day2_notes.md           # Unit 2: Podcast/Whitepaper notes & local MCP config
│   ├── day3_notes.md           # Unit 3: Podcast/Whitepaper summaries (Agent Skills)
│   ├── day4_notes.md           # Unit 4: Podcast/Whitepaper summaries (Security & Eval)
│   ├── day5_notes.md           # Unit 5: Podcast/Whitepaper summaries (Production SDD)
│   ├── emails.md               # Day 3 & 4 converted raw email announcements
│   └── incoming_emails.md      # Converted raw email announcements (markitdown)
│
├── scripts/
│   ├── cloud_run_deploy.sh     # Day 5: Cloud Run serverless deployment simulation script
│   ├── expense_agent.feature   # Day 5: Behavior-driven Gherkin feature specification
│   ├── expense_agent.py        # Day 4: Expense approval agent featuring HITL
│   ├── expense_results.json    # Log of expense results
│   ├── observability_logger.py # Day 5: Telemetry logger simulating OpenTelemetry spans
│   └── security_scan.py        # Day 4: Local threat credential scanner
│
├── README.md               # Course overview & portfolio index
├── progress.md             # Interactive checklist for course requirements
├── SECURITY.md             # Vulnerability reporting guidelines
│
├── index.html              # Web page dashboard structure (deployed to root)
├── index.css               # Custom snowflakes and balloons animations
└── index.js                # Interactive trigger and cleanup logic
```

---

## 🛠️ Getting Started & Local Setup

### 1. View the Day 1 Animations Web App
To view the interactive prototype locally:
1. Open the repository root.
2. Launch a local web server (e.g., Python `python -m http.server` or VS Code Live Server).
3. Open the root URL in your browser to test the interactive falling snowflakes and rising balloons!

### 2. Configure Google Developer Knowledge MCP (Day 2)
To enable the Google Developer Knowledge MCP server locally in your Antigravity environment:
1. Create a Google Cloud API Key restricted to the Google Developer Knowledge API.
2. Add the configuration to your central configuration file `~/.gemini/antigravity/mcp_config.json`:
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
3. Test your MCP connection using the Antigravity TUI or CLI by querying: *"Does Google Workspace support MCP servers?"*


