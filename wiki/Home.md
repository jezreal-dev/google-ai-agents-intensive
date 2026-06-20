# Welcome to the SRE Incident Triage Agent Wiki!

This wiki acts as the central developer portal for the **SRE Incident Triage Agent** and the 5-Day Google AI Agents Intensive course portfolio. Here you will find architectural specifications, setup guides, tool integrations, and safety standards.

---

## 🗺️ Navigation

*   **[Home](Home)** (This page)
*   **[Getting Started](Getting-Started)** - Setup environment, run pipeline, and execute tests
*   **[Architecture & Agent Topology](Architecture)** - Conductor coordination and specialist roles
*   **[MCP Integrations](MCP-Integrations)** - Connecting GDK, GitHub, and Sentry
*   **[Security & Safety Guardrails](Security-and-Safety)** - HITL gating, pre-commit scanners, and sandboxing

---

## 🏆 Project Spotlight: Capstone SRE Agent

The SRE Incident Triage Agent is an autonomous 5-agent pipeline orchestrated using the Google Agent Development Kit (ADK) 2.0. When a production alert fires, the system:
1.  Classifies severity and service targets.
2.  Fetches reference Google Cloud runbooks and searches historical GitHub issues.
3.  Drafts a markdown Root Cause Analysis (RCA) report.
4.  Previews a formatted team notification for Slack.
5.  Halts execution on a Human-in-the-Loop (HITL) gate for safety checks on SEV1/SEV2 actions.

---

## 📅 Course Roadmap Index

Access daily assignments, learning logs, and whitepaper study notes from the intensive:

*   **Day 1:** [Introduction to Agents & Vibe Coding](https://github.com/jezreal-dev/google-ai-agents-intensive/blob/main/notes/day1_notes.md) (Atmosphere Control Panel web app)
*   **Day 2:** [Agent Tools & Interoperability](https://github.com/jezreal-dev/google-ai-agents-intensive/blob/main/notes/day2_notes.md) (MCP Architecture & CLI configuration)
*   **Day 3:** [Agent Skills & Memory](https://github.com/jezreal-dev/google-ai-agents-intensive/blob/main/notes/day3_notes.md) (Modular skills & progressive disclosure)
*   **Day 4:** [Security & Evaluation Harnesses](https://github.com/jezreal-dev/google-ai-agents-intensive/blob/main/notes/day4_notes.md) (Threat scanning & effective trust models)
*   **Day 5:** [Spec-Driven Production Development](https://github.com/jezreal-dev/google-ai-agents-intensive/blob/main/notes/day5_notes.md) (Serverless Cloud Run & OpenTelemetry-style logs)
