# Day 3 Study Notes: Agent Skills

## Overview
Day 3 focuses on managing dynamic context and avoiding "context rot" by equipping agents with portable "Agent Skills"—directories structured around a central `SKILL.md` file. This framework uses progressive disclosure to keep system prompts lightweight and load tools on demand.

---

## 📄 Summary: "Agent Skills" (Whitepaper)

### 1. The Threat of "Context Rot"
*   **The Problem**: Exposing all possible tools and documentation files to an agent at once floods its context window. This leads to **context rot**, where the model's reasoning capabilities degrade, cost increases, and key instructions are lost (the "needle-in-a-haystack" problem).
*   **The Solution**: Instead of forcing a single agent to carry massive instructions for every task, we organize capabilities into modular **Agent Skills**.

### 2. Progressive Disclosure & Portable Skills
*   **Progressive Disclosure**: A design pattern where details, tools, and execution procedures are hidden until they are explicitly needed. The main agent's system prompt stays extremely lightweight.
*   **Skills Structure**: A skill is packaged as a local directory containing:
    *   `SKILL.md`: A declarative file with frontmatter metadata (`name`, `description`) and detailed workflow instructions or command definitions.
    *   `scripts/` or `examples/`: Associated executable code, tools, or references.
*   **Dynamic Loading**: When the agent detects a user request matching a skill's description, the host loads that specific skill's tools and files into the context window on demand. A single generalist agent can now flex into hundreds of specialist roles efficiently.

### 3. Best Practices in Skill Engineering
*   **Standardize File Outputs**: Avoid printing large logs to stdout. Redirect long data outputs to local scratch files to conserve context space.
*   **Granular Commands**: CLI scripts should use subcommands with mandatory parameters rather than silent defaults (forcing the agent to explicitly choose limits and inputs).
*   **Dependency Reuse**: Instead of copy-pasting code, skills should declare other skills as dependencies (e.g., a "code-lint" skill depending on a "file-reader" skill).

---

## 🎙️ Summary: Companion Podcast Episode (Unit 3)

### Key Discussion Points
*   **The Shift to Multi-Tooling**: AI workflows are evolving from simple script execution to agent fleets executing complex, multi-stage plans.
*   **Keeping Prompts Lightweight**: Storing instruction sets in local Markdown files instead of stuffing them into the system instruction enables scalable agent architectures.
*   **Skills as APIs**: Standardizing how skills are designed makes it easy to share them across teams or publish them to a global registry (e.g., `~/.gemini/config/skills/`).

---

## 🛠️ Local Implementation: Hello World Skill
We created a local demonstration skill at `.agents/skills/hello-world-skill/SKILL.md`. This skill allows the agent to execute a basic greeting workflow, proving that the Antigravity TUI successfully registers and triggers local declarative skills.
