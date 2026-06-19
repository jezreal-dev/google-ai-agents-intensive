"""
scripts/run_sdd_tests.py
========================
Spec-Driven Development (SDD) Gherkin Test Runner.

Parses `scripts/expense_agent.feature` and validates the `expense_agent.py`
implementation against each Gherkin scenario, confirming that:
  - Small expenses ($45) are auto-approved without HITL.
  - Large expenses ($250) are blocked and require Human-in-the-Loop verification.

Day 5 Capstone: Demonstrates SDD principle — code satisfies behavior specs, not vice versa.
"""

import sys
import io
import os
from unittest.mock import patch

# Ensure scripts/ dir is on the path so we can import expense_agent
sys.path.insert(0, os.path.dirname(__file__))
from expense_agent import process_expense


def parse_feature_file(filepath: str) -> list[dict]:
    """Minimal Gherkin parser: extracts scenario names and steps."""
    scenarios = []
    current_scenario = None

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("Scenario:"):
                if current_scenario:
                    scenarios.append(current_scenario)
                current_scenario = {
                    "name": line.split(":", 1)[1].strip(),
                    "steps": []
                }
            elif current_scenario and any(
                line.startswith(kw) for kw in ("Given", "When", "Then", "And")
            ):
                current_scenario["steps"].append(line)

    if current_scenario:
        scenarios.append(current_scenario)

    return scenarios


def run_tests(feature_path: str) -> bool:
    """Run Gherkin scenarios against the expense_agent implementation."""
    print("[*] Running SDD Gherkin validation tests...")
    scenarios = parse_feature_file(feature_path)

    if not scenarios:
        print("[-] No scenarios found in feature file!")
        return False

    all_passed = True

    # -------------------------------------------------------------------------
    # Scenario 1: Small expense claims are automatically approved
    # -------------------------------------------------------------------------
    scenario = scenarios[0]
    print(f"\n>> Scenario: {scenario['name']}")
    try:
        result = process_expense("Client Lunch", 45.0)
        assert result["status"] == "Approved", (
            f"Expected 'Approved' but got '{result['status']}'"
        )
        assert result["hitl"] is False, (
            "Expected hitl=False for small expense, got hitl=True"
        )
        print("   [+] PASSED: Auto-approved with hitl=False")
    except AssertionError as e:
        print(f"   [FAIL] {e}")
        all_passed = False

    # -------------------------------------------------------------------------
    # Scenario 2: Large expense claims block for HITL verification
    # -------------------------------------------------------------------------
    scenario = scenarios[1]
    print(f"\n>> Scenario: {scenario['name']}")
    try:
        # Mock user input to simulate human approving the HITL gate
        with patch("builtins.input", return_value="y"):
            result = process_expense("External Monitor", 250.0)

        assert result["status"] == "Approved", (
            f"Expected 'Approved' (mocked human said 'y') but got '{result['status']}'"
        )
        assert result["hitl"] is True, (
            "Expected hitl=True for large expense, got hitl=False"
        )
        print("   [+] PASSED: HITL gate triggered with hitl=True")
    except AssertionError as e:
        print(f"   [FAIL] {e}")
        all_passed = False

    print()
    if all_passed:
        print("[+] ALL GHERKIN SCENARIOS PASSED — implementation satisfies the spec.")
    else:
        print("[-] SOME SCENARIOS FAILED — please review expense_agent.py.")

    return all_passed


if __name__ == "__main__":
    feature_path = os.path.join(os.path.dirname(__file__), "expense_agent.feature")

    if not os.path.exists(feature_path):
        print(f"[-] Feature file not found: {feature_path}")
        sys.exit(1)

    success = run_tests(feature_path)
    sys.exit(0 if success else 1)
