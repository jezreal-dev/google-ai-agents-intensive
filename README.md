# Google AI Agents Intensive Course Portfolio

Welcome to my portfolio for the **5-Day AI Agents: Intensive Vibe Coding Course With Google** (June 15 - June 19, 2026).

This repository contains all my course notes, daily assignment reflections, progress trackers, and projects developed throughout the intensive program.

---

## 📅 Course Roadmap & Deliverables

*   **Day 1: Introduction to Agents & Vibe Coding**
    *   **Topic**: Transition from manual coding syntax to natural language intent ("vibe coding").
    *   **Deliverables**: [day1_notes.md](file:///C:/Users/USER/.gemini/antigravity/scratch/google-ai-agents-intensive/notes/day1_notes.md) (Notes), Snowflakes & Balloons Web App prototype ([index.html](file:///C:/Users/USER/.gemini/antigravity/scratch/google-ai-agents-intensive/index.html) served at root).
*   **Day 2: Agent Tools & Interoperability**
    *   **Topic**: Connecting agents to external APIs, code execution, and multi-agent setups.
    *   **Deliverables**: [day2_notes.md](file:///C:/Users/USER/.gemini/antigravity/scratch/google-ai-agents-intensive/notes/day2_notes.md) (Notes & central MCP Setup), [cli_usage.md](file:///C:/Users/USER/.gemini/antigravity/scratch/google-ai-agents-intensive/docs/cli_usage.md) (CLI Guidelines), [SECURITY.md](file:///C:/Users/USER/.gemini/antigravity/scratch/google-ai-agents-intensive/SECURITY.md) (Security Policy), and [.github/dependabot.yml](file:///C:/Users/USER/.gemini/antigravity/scratch/google-ai-agents-intensive/.github/dependabot.yml) (Automated Security Updates).
*   **Day 3: Agent Skills**
    *   **Topic**: Implementing memory, handling long-context windows, and building modular agentic skills. *(Upcoming)*
*   **Day 4: Vibe Coding Agent Security and Evaluation**
    *   **Topic**: Testing, guardrails, security benchmarks, and safety evaluations. *(Upcoming)*
*   **Day 5: Spec-Driven Production Grade Development**
    *   **Topic**: Cloud deployment (Cloud Run), debugging, and fleet orchestration. *(Upcoming)*

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
│   └── emails.md               # Converted raw email announcements
│
├── scripts/
│   ├── expense_agent.py        # Day 4: Expense approval agent featuring HITL
│   ├── expense_results.json    # Log of expense results
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


