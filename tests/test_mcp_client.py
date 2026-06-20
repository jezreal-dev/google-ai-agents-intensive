"""Tests for the MCP client wrapper — uses mocks to avoid live API calls."""
from unittest.mock import patch
from capstone.mcp_client import query_developer_knowledge, search_github_issues, get_sentry_event

def test_query_developer_knowledge_returns_string():
    with patch("capstone.mcp_client._call_gdkn_mcp", return_value="Cloud Run scales to zero by default."):
        result = query_developer_knowledge("How does Cloud Run scaling work?")
    assert isinstance(result, str) and len(result) > 0

def test_search_github_issues_returns_list():
    with patch("capstone.mcp_client._call_github_mcp",
               return_value=[{"title": "OOM", "url": "https://github.com/x", "body": "Fixed by restart"}]):
        result = search_github_issues("my-org/my-repo", ["OOM", "memory"])
    assert isinstance(result, list)
    assert all("title" in i and "url" in i for i in result)

def test_get_sentry_event_returns_required_keys():
    result = get_sentry_event("FAKE-EVENT-ID-001")
    for key in ("title", "level", "stacktrace"):
        assert key in result
