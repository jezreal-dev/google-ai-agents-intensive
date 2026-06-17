import sys
import json

def process_expense(description, amount):
    print(f"[*] Processing expense: '{description}' for ${amount:.2f}...")
    
    # Check if human approval is required (Threshold is $100)
    if amount > 100.0:
        print(f"[!] WARNING: Expense exceeds $100.00. Human approval required.")
        approval = input("Approve this expense? (y/n): ").strip().lower()
        if approval == 'y':
            return {"status": "Approved", "amount": amount, "description": description, "hitl": True}
        else:
            return {"status": "Rejected", "amount": amount, "description": description, "hitl": True}
    else:
        # Auto-approve small expenses
        print("[*] Expense under limit. Auto-approving...")
        return {"status": "Approved", "amount": amount, "description": description, "hitl": False}

if __name__ == "__main__":
    # Test data representing typical transactions
    test_expenses = [
        {"description": "Team lunch", "amount": 45.50},
        {"description": "Cloud server subscription", "amount": 250.00},
        {"description": "Office chair", "amount": 120.00}
    ]
    
    results = []
    print("=== Starting Expense Agent Evaluation ===")
    for expense in test_expenses:
        res = process_expense(expense["description"], expense["amount"])
        results.append(res)
        print(f"[+] Result: {res['status']} (HITL: {res['hitl']})\n")
        
    # Write output to results file (Default to File Output)
    output_file = "expense_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"[#] Test complete. Results saved to: {output_file}")
