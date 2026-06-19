# Day 3 Study Notes — Agent Skills & Memory Management

> **Unit 3 · June 17, 2026**
> Podcast: [YouTube](https://www.youtube.com/watch?v=uYURYHhpmKc) · Whitepaper: [Agent Skills](https://www.kaggle.com/whitepaper-agent-skills)

---

## Overview

Day 3 focuses on managing dynamic context and combating "context rot" by equipping agents with portable, modular **Agent Skills** — directories structured around a central `SKILL.md` file. The framework uses **progressive disclosure** to keep system prompts lightweight and load specialist tools only on demand.

---

## 📄 Whitepaper Summary — *"Agent Skills"*

### 1. The Threat of "Context Rot"

When all possible tools, files, and documentation are exposed to an agent at once, its context window floods. This leads to **context rot**:

- Reasoning quality degrades
- Token cost increases
- Critical instructions get buried (the "needle-in-a-haystack" problem)
- The agent hallucinates or ignores key constraints

**Solution:** Organize capabilities into modular Agent Skills that are loaded only when triggered.

### 2. Progressive Disclosure & Portable Skills

**Progressive Disclosure** is a design pattern where tool details and execution procedures are hidden until explicitly needed. The main agent's system prompt stays lightweight.

A skill is packaged as a local directory:

```
.agents/skills/<skill-name>/
├── SKILL.md          # Frontmatter metadata + workflow instructions
├── scripts/          # Executable helper code
└── examples/         # Reference implementations
```

**`SKILL.md` structure:**

```yaml
---
name: skill-name
description: One-line description (used for trigger matching)
---

# Skill Title
## Overview
## Workflow
## Steps
```

**Dynamic loading:** When the agent detects a user request matching a skill's `description`, the host loads that skill's tools and files into context on demand. A single generalist agent can flex into hundreds of specialist roles efficiently.

### 3. Best Practices in Skill Engineering

| Practice | Rationale |
|----------|-----------|
| Redirect large outputs to scratch files | Preserves context window space |
| Use granular CLI subcommands with explicit parameters | Forces the agent to make deliberate choices, not silent defaults |
| Declare skill dependencies instead of copy-pasting code | Promotes reuse and maintainability |
| Keep `SKILL.md` under 500 lines | Prevents loading too much context at once |

---

## 🎙️ Podcast Summary — Unit 3

### Key Discussion Points

- **The Shift to Multi-Tooling**: AI workflows are evolving from simple script execution to agent fleets executing complex, multi-stage plans with dozens of specialist skills.
- **Keeping Prompts Lightweight**: Storing instruction sets in local Markdown files instead of stuffing them into the system instruction enables scalable, composable architectures.
- **Skills as APIs**: Standardizing skill design makes them shareable across teams and publishable to a global registry (e.g., `~/.gemini/config/skills/`).

---

## 🛠️ Implementation — Hello World Skill

A local demonstration skill was created at [`.agents/skills/hello-world-skill/SKILL.md`](../.agents/skills/hello-world-skill/SKILL.md).

**Purpose:** Proves that the Antigravity TUI successfully discovers and triggers local declarative skills from the workspace `.agents/skills/` directory.

**Trigger phrase:** *"Run the hello world skill and output a greeting."*

**Behavior:**
1. Checks the current workspace state.
2. Logs a timestamped greeting message to `greetings.txt` in the workspace.
3. Reports the output file location to the user.
