# Model Context Protocol (MCP) Integrations

Hallucination is a major risk when AI agents propose production changes. To ensure diagnostic ground truth, the SRE Incident Triage Agent integrates with multiple external systems using standard **Model Context Protocol (MCP)** specifications.

---

## 1. Unified Client Wrapper (`mcp_client.py`)

All Model Context Protocol calls are consolidated inside `capstone/mcp_client.py` rather than directly in the agent scripts. This design:
- Promotes clean separation of concerns.
- Centralizes authentication configuration.
- Facilitates mock-injection during unit and integration tests.

---

## 2. Connected MCP Servers

```
                ┌──────────────────────────────────┐
                │        Correlation Agent         │
                └────────────────┬─────────────────┘
                                 │
         ┌───────────────────────┼────────────────────────┐
         ▼                       ▼                        ▼
┌──────────────────┐   ┌──────────────────┐    ┌────────────────────┐
│    GDK Server    │   │  GitHub Server   │    │Sentry (Simulated)  │
│ search_documents │   │ github_search... │    │  get_sentry_event  │
└──────────────────┘   └──────────────────┘    └────────────────────┘
```

### 1. Google Developer Knowledge (GDK)
- **Tool used:** `search_documents`
- **Purpose:** Connects to the official Google Workspace documentation corpus. Queries runbooks for the targeted service to extract remediation procedures (e.g. OOM fixes, memory increase parameters).

### 2. GitHub MCP
- **Tool used:** `search_github_issues`
- **Purpose:** Searches the repository `my-org/sre-runbooks` for past issues matching the target service name and severity. This allows the RCA agent to know if the same service failed similarly in the past.

### 3. Sentry (Simulated)
- **Tool used:** `get_sentry_event`
- **Purpose:** Simulates connection to Sentry. Fetches raw stack traces, log levels, messages, and timestamps by incident event ID.

---

## 3. Mock Testing Strategy

To run integration tests reliably in non-connected sandboxed pipelines:
- Tests patch `capstone.mcp_client` functions (`query_developer_knowledge` and `search_github_issues`) using `unittest.mock.patch` to return structured simulation strings and dictionaries.
- Automated tests verify formatting, key presence, and error handling without making real HTTP requests.
