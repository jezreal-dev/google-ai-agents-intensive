"""Tests for the MCP client wrapper - uses real simulations instead of mocks."""
from capstone.mcp_client import query_developer_knowledge, search_github_issues, get_sentry_event

def test_query_developer_knowledge_returns_string():
    result = query_developer_knowledge("How does Cloud Run scaling work?")
    assert isinstance(result, str) and len(result) > 0
    assert "[GDK MCP]" in result

def test_search_github_issues_returns_list():
    result = search_github_issues("my-org/my-repo", ["OOM", "memory"])
    assert isinstance(result, list)
    for issue in result:
        for key in ("title", "url", "body"):
            assert key in issue
            assert isinstance(issue[key], str)

def test_search_github_issues_empty_keywords_does_not_crash():
    # This should verify that empty keywords list doesn't raise IndexError
    result = search_github_issues("my-org/my-repo", [])
    assert isinstance(result, list)
    for issue in result:
        for key in ("title", "url", "body"):
            assert key in issue

def test_get_sentry_event_returns_required_keys():
    result = get_sentry_event("FAKE-EVENT-ID-001")
    for key in ("title", "level", "stacktrace", "timestamp", "environment", "service"):
        assert key in result
        assert isinstance(result[key], str)
