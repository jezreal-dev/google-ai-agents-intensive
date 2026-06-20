"""
capstone/mcp_client.py
======================
Unified MCP server interface for all SRE Triage Agent tool calls.
Agent files must import from here — never make direct HTTP calls.

Servers:
  - google-developer-knowledge (configured in mcp_config.json)
  - github (simulated for demo)
  - sentry (simulated for demo)
"""

# --- Google Developer Knowledge MCP ---

def _call_gdkn_mcp(query: str) -> str:
    """In production: delegated to the ADK agent's MCP tool call at runtime."""
    return f"[GDK MCP] Query: {query}"

def query_developer_knowledge(query: str) -> str:
    """Query Google Developer Knowledge MCP for runbook/docs content."""
    return _call_gdkn_mcp(query)


# --- GitHub MCP (simulated) ---

def _call_github_mcp(repo: str, keywords: list[str]) -> list[dict]:
    """Simulate GitHub issue search. Replace with real github MCP in production."""
    return [{
        "title": f"[SIMULATED] Past incident: {keywords[0]} in {repo}",
        "url": f"https://github.com/{repo}/issues/999",
        "body": f"Resolved by restarting the {keywords[0]} service. Root cause: memory leak.",
    }]

def search_github_issues(repo: str, keywords: list[str]) -> list[dict]:
    """Search GitHub issues for past incidents matching keywords."""
    return _call_github_mcp(repo, keywords)


# --- Sentry MCP (simulated) ---

_SIMULATED_EVENTS: dict[str, dict] = {
    "FAKE-EVENT-ID-001": {
        "title": "MemoryError: OOM kill in payment-service pod",
        "level": "fatal",
        "stacktrace": "File 'payment_processor.py', line 142, in process_batch\n"
                      "  result = [transform(r) for r in records]  # 500k records",
        "timestamp": "2026-06-20T02:14:33Z",
        "environment": "production",
        "service": "payment-service",
    }
}

def get_sentry_event(event_id: str) -> dict:
    """Retrieve a Sentry error event by ID (simulated for demo)."""
    return _SIMULATED_EVENTS.get(event_id, {
        "title": f"Unknown event: {event_id}",
        "level": "unknown",
        "stacktrace": "No stacktrace available.",
        "timestamp": "N/A",
        "environment": "unknown",
        "service": "unknown",
    })
