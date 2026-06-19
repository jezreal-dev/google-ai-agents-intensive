Feature: Expense Approval Gating
  As a company administrator
  I want to automatically triage expense claims
  So that minor claims are auto-approved and high-value claims require human verification

  Scenario: Small expense claims are automatically approved
    Given the expense approval limit is $100
    When an employee submits an expense of $45 for "Client Lunch"
    Then the expense agent should auto-approve the claim
    And log the status as "APPROVED" in the results registry

  Scenario: Large expense claims block for human-in-the-loop triage
    Given the expense approval limit is $100
    When an employee submits an expense of $250 for "External Monitor"
    Then the expense agent should block the transaction
    And request manual Human-in-the-Loop verification
    And log the status as "PENDING_VERIFICATION" in the results registry
