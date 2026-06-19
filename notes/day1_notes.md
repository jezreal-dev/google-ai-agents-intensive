# Day 1 Study Notes — Introduction to Agents & Vibe Coding

> **Unit 1 · June 15, 2026**
> Podcast: [YouTube](https://www.youtube.com/watch?v=cbzmr7vt4XA) · Whitepaper: [The New SDLC with Vibe Coding](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding)

---

## Overview

Day 1 introduces the paradigm shift in modern software engineering — from **syntax-based manual coding** to **intent-driven development (vibe coding)** and **agentic engineering**. The core insight: the developer's role is not being replaced; it is being elevated to systems architect.

> [!NOTE]
> **Vibe Coding** is a term popularized by Andrej Karpathy (early 2025). It describes a flow state where developers communicate high-level *intent* using natural language, while AI agents handle the syntax translation and multi-file code compilation.

---

## 📄 Whitepaper Summary — *"The New SDLC with Vibe Coding"*

### 1. Syntax vs. Intent

| Traditional Programming | Vibe Coding |
|-------------------------|-------------|
| Developer acts as a compiler, translating problems into machine syntax | Developer communicates intent, architecture, and goals in natural language |
| Manual bottleneck — prone to bugs and slow iteration | AI agent compiles intent into precise, multi-file code automatically |
| Focus: typing correct syntax | Focus: designing systems, defining tests, reviewing output |

### 2. The "Factory Model" of Software Development

In the new SDLC, the developer shifts from "code writer" to "system orchestrator" — like a factory manager directing a production line. The developer's primary job is designing three harnesses that guide the AI:

1. **Context Harness** — feeding the agent the right files, environment details, and domain knowledge.
2. **Constraint Harness** — establishing guardrails, rules, and limits (coding standards, file structures, library restrictions).
3. **Evaluation Harness** — defining what "correctness" looks like via automated test suites, linting configs, and quality checks.

> [!IMPORTANT]
> Without an active **evaluation harness**, agents cannot verify their results or auto-correct errors. Harness and test design is the new core skill.

### 3. Compression of the SDLC

Traditionally, planning → coding → compiling → testing → deployment are slow, sequential steps. With AI agents, these collapse into a tight autonomous loop:

```
Read Files → Write Code → Run Tests → Observe Errors → Fix Code → Repeat
```

A complete SDLC iteration that once took days can now complete in seconds.

---

## 🎙️ Podcast Summary — Unit 1

### Key Discussion Points

- **AI Chatbots vs. AI Agents**: Chatbots are reactive (one-off text completion). Agents are proactive and autonomous — they operate in a continuous loop of **Perception → Reasoning → Action** to achieve a defined goal.
- **What is "Vibe Coding"?**: A flow state where developers focus on building features, UI design, and testing, while leaving syntax details to the AI.
- **The Paradigm Shift**: Software engineering isn't dying — it is graduating to a higher level of abstraction. Success requires strong system design skills, clear communication, and rigorous verification.
