# Antigravity CLI (`agy`) & agentapi — Usage Guide

> **Day 2 Deliverable** — Documenting the Antigravity CLI environment as configured and used throughout the Google AI Agents Intensive Course.

The Antigravity CLI (`agy`) provides a powerful, keyboard-first Terminal User Interface (TUI) for interacting with Antigravity AI agents, running local commands, and managing code workflows.

---

## 🚀 Getting Started

Navigate to your project workspace directory and launch the TUI:

```bash
agy
```

**First-time setup:** The CLI walks through a brief onboarding to configure:
- Colour theme (`Dark`, `Solarized`, `Solarized Light`)
- Rendering mode (`Alt-Screen` full-buffer or `Inline` scrolling)
- Workspace trust verification

---

## 🛠️ Slash Command Reference

Type these commands directly in the prompt bar to control the session:

| Command | Purpose |
|---------|---------|
| `?` | List all available slash commands and get help |
| `/config` · `/settings` | Open the full-screen configuration overlay |
| `/permissions` | Manage file and command approval rules |
| `/rewind` · `/undo` | Revert the last agent turn |
| `/fork` | Spin up an isolated branched conversation and workspace |
| `/clear` | Clear the prompt and start a fresh session |
| `/resume` | List and resume previous conversation logs |
| `/exit` · `Ctrl+D` | Terminate the CLI TUI session |

---

## ⌨️ Essential Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `@` | Trigger file path auto-complete (absolute & relative paths) |
| `!<command>` | Execute a shell command directly (e.g., `!git status`) |
| `Ctrl+R` | Open the side-by-side diff review panel to approve or decline changes |
| `Esc Esc` | Clear the current prompt box instantly |
| `Alt+Enter` · `Shift+Enter` | Insert a new line without submitting |
| `Y` / `N` | Confirm or decline a proposed terminal command or file change |
| `E` | Open your terminal's default editor to modify a proposed command |

---

## 🤖 Programmable API — `agentapi`

For headless script integration and programmatic conversation management, use the `agentapi` CLI utility:

```bash
# Start a new agent session
agentapi new-conversation [--model=<flash_lite|flash|pro>] "<your prompt>"

# Fetch the status and messages of an active conversation
agentapi get-conversation-metadata <conversation_id>

# Send a message to a running conversation
agentapi send-message <recipient_id> "<message content>"
```

---

## 📝 Notes & Tips

- **Windows PowerShell**: Use `;` to chain commands instead of `&&` (e.g., `git add .; git commit -m "msg"`).
- **MCP Server Config**: Store your `mcp_config.json` in `~/.gemini/antigravity/` — outside the repo — to prevent API keys from being committed.
- **Skills Path**: Local agent skills are discovered from `.agents/skills/<skill-name>/SKILL.md` relative to the workspace root.
