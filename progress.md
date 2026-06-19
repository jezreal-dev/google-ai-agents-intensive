# Progress Tracker — Google AI Agents Intensive

> **5-Day AI Agents: Intensive Vibe Coding Course with Google**
> June 15–19, 2026 · Deadline for Capstone: **July 6, 2026**

Track the completion status of all daily assignments, codelabs, and the capstone project below.

---

## Day 1 — Introduction to Agents & Vibe Coding

> **Theme:** Transitioning from manual syntax coding to intent-driven development and agentic engineering.

### Onboarding & Setup
- [x] Create Kaggle account
- [x] Create Google AI Studio account & API key
- [x] Install Antigravity 2.0
- [x] Install Antigravity IDE
- [x] Install Antigravity CLI
- [x] Join Kaggle Discord server

### Assignments
- [x] Listen to the Unit 1 podcast — [YouTube](https://www.youtube.com/watch?v=cbzmr7vt4XA)
- [x] Read *"The New SDLC with Vibe Coding"* whitepaper — [Kaggle](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding)

### Codelabs
- [x] Get started with Antigravity 2.0 and IDE
- [x] Build a web application in AI Studio and deploy to Cloud Run (deployed to GitHub Pages)

### Livestream
- [x] Attend Day 1 livestream — Monday, June 15 at 11:00 AM PT

---

## Day 2 — Agent Tools & Interoperability

> **Theme:** Connecting agents to external APIs, code execution environments, and multi-agent setups via MCP.

### Assignments
- [x] Listen to the Unit 2 podcast — [YouTube](https://www.youtube.com/watch?v=GjjKXqxFTOY)
- [x] Read *"Agent Tools & Interoperability"* whitepaper — [Kaggle](https://www.kaggle.com/whitepaper-agent-tools-and-interoperability)

### Codelabs
- [x] Get started with Antigravity CLI — documented in [`docs/cli_usage.md`](docs/cli_usage.md)
- [x] Configure Google Developer Knowledge MCP server — configured in central `mcp_config.json`

### Livestream
- [/] Attend Day 2 livestream — Tuesday, June 16 at 11:00 AM PT

---

## Day 3 — Agent Skills

> **Theme:** Building memory, managing long-context windows, and creating modular agentic skills.

### Assignments
- [x] Listen to the Unit 3 podcast — [YouTube](https://www.youtube.com/watch?v=uYURYHhpmKc)
- [x] Read *"Agent Skills"* whitepaper — [Kaggle](https://www.kaggle.com/whitepaper-agent-skills)

### Codelabs
- [x] Explore how Skills work in Antigravity — created local skill at [`.agents/skills/hello-world-skill/SKILL.md`](.agents/skills/hello-world-skill/SKILL.md)
- [x] Build agents in Antigravity with Agents CLI and ADK

### Livestream
- [x] Attend Day 3 livestream — Wednesday, June 17 at 11:00 AM PT

---

## Day 4 — Vibe Coding Agent Security & Evaluation

> **Theme:** Rigorous testing, security guardrails, and quality evaluations in non-deterministic AI workflows.

### Assignments
- [x] Listen to the Unit 4 podcast — [YouTube](https://www.youtube.com/watch?v=Ddz1b8CYPvg)
- [x] Read *"Vibe Coding Agent Security and Evaluation"* whitepaper — [Kaggle](https://www.kaggle.com/whitepaper-vibe-coding-agent-security-and-evaluation)

### Codelabs
- [x] Build an expense-approval agent with HITL triage — [`scripts/expense_agent.py`](scripts/expense_agent.py)
- [x] Implement automated credential threat scanner — [`scripts/security_scan.py`](scripts/security_scan.py)

### Livestream
- [/] Attend Day 4 livestream — Thursday, June 18 at 11:00 AM PT

---

## Day 5 — Spec-Driven Production Grade Development

> **Theme:** Cloud deployment, fleet orchestration, debugging, observability, and Spec-Driven Development (SDD).

### Assignments
- [x] Listen to the Unit 5 podcast — [YouTube](https://www.youtube.com/watch?v=VSRdL4wlbLY)
- [x] Read *"Spec-Driven Production Grade Development in the Age of Vibe Coding"* whitepaper — [Kaggle](https://www.kaggle.com/whitepaper-spec-driven-production-grade-development-in-the-age-of-vibe-coding)

### Codelabs
- [x] Deploy and host AI agents on Google Cloud — simulated via [`scripts/cloud_run_deploy.sh`](scripts/cloud_run_deploy.sh)
- [x] Build a frontend web app and link to cloud-hosted agent — simulated locally

### Phase 1 SDD Implementation *(bonus)*
- [x] Write Gherkin SDD specification — [`scripts/expense_agent.feature`](scripts/expense_agent.feature)
- [x] Implement Gherkin test runner — [`scripts/run_sdd_tests.py`](scripts/run_sdd_tests.py)
- [x] Configure git pre-commit secret scanner hook — [`.git/hooks/pre-commit`](.git/hooks/pre-commit)

### Livestream
- [x] Attend Day 5 livestream — Friday, June 19 at 11:00 AM PT — [Recording](https://youtube.com/live/Y3HfV4IroCU)

---

## 🏆 Capstone Project

> **Deadline:** July 6, 2026 at 11:59 PM PT
> **Submission:** [Kaggle Capstone Competition](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project)

### Track Selection *(choose one)*
- [ ] **Track 1 — Agents for Good:** Societal challenges (education, healthcare, agriculture, arts)
- [ ] **Track 2 — Agents for Business:** Enterprise problems (expense management, pipeline optimization)
- [ ] **Track 3 — Concierge Agents:** Personal assistants (planning, task management, user data security)
- [ ] **Track 4 — Freestyle:** Niche, creative, or experimental

### Requirements *(demonstrate at least 3)*
- [ ] Multi-agent systems built with Agent Development Kit (ADK)
- [ ] Model Context Protocol (MCP) server integration
- [ ] Agent skills (`SKILL.md` with progressive disclosure)
- [ ] Security features (HITL, automated scans, sandboxing)

### Deliverables
- [ ] Working autonomous agent
- [ ] Video walkthrough and project summary write-up
- [ ] Public GitHub repository with clean documentation
- [ ] Submit on Kaggle
