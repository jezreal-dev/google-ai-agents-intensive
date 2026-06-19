---
name: hello-world-skill
description: Logs a timestamped greeting message to the workspace to demonstrate local declarative skill discovery and execution.
---

# Hello World Agent Skill

> **Day 3 Deliverable** — Demonstrates that the Antigravity TUI successfully discovers and triggers local declarative skills defined in `.agents/skills/`.

---

## Overview

This skill executes a minimal workspace greeting workflow, proving that:

1. The `.agents/skills/` directory is auto-discovered by Antigravity.
2. A `SKILL.md` frontmatter `description` is used for trigger matching.
3. Skills can write structured output to files without bloating the context window.

---

## Trigger

Ask the agent:

> *"Run the hello world skill and output a greeting."*

---

## Workflow

1. **Check workspace state** — Verify the current working directory and confirm the workspace root.
2. **Generate greeting** — Compose a localized hello message that includes the current system timestamp.
3. **Write to file** — Save the greeting to `greetings.txt` in the workspace root (avoids printing long output to stdout).
4. **Report** — Inform the user of the file path where the greeting was written.

---

## Expected Output

```
greetings.txt written at: <workspace_root>/greetings.txt
Content: Hello from the hello-world-skill! Timestamp: 2026-06-17T14:32:05Z
```
