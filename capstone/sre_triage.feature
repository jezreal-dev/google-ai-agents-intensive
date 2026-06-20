# capstone/sre_triage.feature
# SRE Incident Triage Agent — Behavioral Specification
# Source of truth: agents must satisfy these scenarios, not the other way around.

Feature: SRE Incident Triage Multi-Agent Pipeline

  Background:
    Given the SRE triage system is initialised

  Scenario: Triage Agent classifies a fatal alert as SEV1
    Given an alert with level "fatal" and title "OOM kill in payment-service"
    When the Triage Agent processes the alert
    Then the severity should be "SEV1"
    And the affected_service should be "payment-service"
    And the summary should contain "OOM"

  Scenario: Triage Agent classifies a warning alert as SEV3
    Given an alert with level "warning" and title "Slow DB queries on reporting-service"
    When the Triage Agent processes the alert
    Then the severity should be "SEV3"

  Scenario: Correlation Agent retrieves runbook and past incidents
    Given a triage result with severity "SEV1" and service "payment-service"
    When the Correlation Agent processes the triage result
    Then the runbook_summary should be a non-empty string
    And the past_incidents should be a list with at least 1 item
    And each past incident should have a "title" and "url" key

  Scenario: RCA Agent drafts a root cause analysis
    Given a correlation result with runbook_summary and past_incidents
    When the RCA Agent processes the correlation result
    Then the rca_draft should be a non-empty string
    And the rca_draft should contain "Root Cause"
    And the rca_draft should contain "Recommended Action"

  Scenario: Notifier Agent formats a Slack-ready message
    Given an RCA draft and a SEV1 triage result
    When the Notifier Agent processes the data
    Then the slack_message should contain the severity "SEV1"
    And the slack_message should contain the service name
    And the slack_message should contain "Human approval required"

  Scenario: HITL gate blocks remediation for SEV1 incidents
    Given a SEV1 incident and a proposed remediation command
    When the HITL gate evaluates the incident
    Then human_required should be True
    And the gate should not execute without approval

  Scenario: HITL gate auto-approves for SEV3 incidents
    Given a SEV3 incident with a low-risk proposed action
    When the HITL gate evaluates the incident
    Then human_required should be False
    And approved should be True

  Scenario: Full pipeline processes a fatal alert end-to-end
    Given a Sentry event ID "FAKE-EVENT-ID-001"
    When the Coordinator Agent runs the full triage pipeline
    Then the final output should contain keys: severity, rca_draft, slack_message, human_required
