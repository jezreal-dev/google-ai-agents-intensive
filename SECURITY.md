# Security Policy

## Overview

This repository contains study notes, working code samples, and assignment deliverables for the Google AI Agents Intensive Course. Security is taken seriously — the codebase includes automated credential scanning on every commit via a pre-commit git hook.

---

## Supported Versions

Only the latest state on the `main` branch is actively maintained and reviewed.

| Version | Supported |
|---------|-----------|
| `main` (latest) | ✅ Yes |
| Older commits / branches | ❌ No |

---

## Reporting a Vulnerability

If you discover a security vulnerability in this project — such as exposed credentials, API keys, or security flaws in code samples — please follow responsible disclosure practices:

1. **Do NOT** open a public GitHub issue.
2. Email your report privately to **jezreelglobal@gmail.com**.
3. Include the following in your report:
   - A clear description of the vulnerability
   - Steps to reproduce it
   - Any suggested remediation steps

---

## What to Expect

| Stage | Timeframe |
|-------|-----------|
| Acknowledgement email | Within 48 hours of your report |
| Validation & triage | Within 5 business days |
| Patch & resolution | As soon as possible; commit pushed to `main` |

We appreciate responsible disclosure and will credit reporters where appropriate.

---

## Built-in Security Controls

This project uses the following automated security controls:

- **Pre-commit hook** — [`scripts/security_scan.py`](scripts/security_scan.py) runs before every `git commit`, scanning staged files for raw API keys matching the `AIzaSy...` pattern.
- **Dependabot** — [`.github/dependabot.yml`](.github/dependabot.yml) is configured to flag outdated or vulnerable dependencies.
- **`.gitignore`** — Prevents `.env` files, Python bytecode, and OS artifacts from being tracked.
