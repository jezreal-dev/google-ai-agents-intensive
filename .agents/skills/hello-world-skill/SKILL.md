---
name: hello-world-skill
description: A local demonstration skill that logs greeting messages in the workspace.
---

# Hello World Agent Skill

## Overview
This skill allows the agent to execute a standardized workspace greetings protocol, showing how declarative skills hook into the Antigravity system.

## Quick Start
To trigger this skill, ask: *"Run the hello world skill and output a greeting"*

## Workflow
1. Check the workspace state.
2. Log a localized hello message containing the current system time to a file named `greetings.txt`.
3. Inform the user of the location where the greetings were written.
