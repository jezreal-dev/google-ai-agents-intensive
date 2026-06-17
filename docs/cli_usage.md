# Antigravity CLI (agy) & agentapi Usage Guidelines

The Antigravity CLI (`agy`) provides a powerful, keyboard-first Terminal User Interface (TUI) for interacting with Antigravity AI agents, running local commands, and managing code workflows.

---

## 🚀 Launching & Getting Started
To start an interactive session, navigate to your project workspace directory and run:
```bash
agy
```
*   **First-Time Setup**: The CLI will walk you through a brief onboarding to choose a color theme (Dark, Solarized, Solarized Light), select a rendering mode (Alt-Screen full-buffer or Inline scrolling), and verify workspace trust.

---

## 🛠️ Key Command Reference (Slash Commands)
Type these commands directly in the prompt bar to control the CLI state:

| Command | Action / Purpose |
| :--- | :--- |
| `?` | Get help and list all available slash commands |
| `/config` or `/settings` | Open the full-screen configuration and settings overlay |
| `/permissions` | Open the permissions manager to control file/command approvals |
| `/rewind` or `/undo` | Go back in the conversation history (reverts the last agent turn) |
| `/fork` | Spin up a separate branched conversation and workspace |
| `/clear` | Clear the current prompt and start a fresh session |
| `/resume` | List and resume previous conversation logs |
| `/exit` or `ctrl+d` | Terminate the CLI TUI session |

---

## ⌨️ Essential Keyboard Shortcuts & Tips

*   **Path Auto-Complete (`@`)**: Type `@` in the prompt bar to trigger absolute/relative file path suggestions.
*   **Command Line Execution (`!`)**: Prefix your prompt with `!` to run a shell command directly (e.g., `!git status` or `!npm run dev`).
*   **Artifact Review (`ctrl+r`)**: Open the side-by-side code review and diff inspection panel to approve or decline file changes proposed by the agent.
*   **Prompt Clear (`esc esc`)**: Clear the current prompt box instantly when no streaming is active.
*   **Multi-line Input (`alt+enter` / `shift+enter`)**: Insert a new line in the prompt box without submitting.
*   **Approve / Decline Action (`y` / `n`)**: Confirm or decline a proposed terminal command or file change.
*   **Edit Action (`e`)**: Open your terminal's default text editor to modify a proposed command before execution.

---

## 🤖 Programmable API Command Line (`agentapi`)
For headless script integration and conversation management, you can invoke the lower-level `agentapi` utility:

```bash
# Start a new agent session
agentapi new-conversation [--model=<flash_lite|flash|pro>] "<your prompt>"

# Fetch the status and messages of a conversation
agentapi get-conversation-metadata <conversation_id>

# Send a message to an active conversation
agentapi send-message <recipient_id> "<message content>"
```
