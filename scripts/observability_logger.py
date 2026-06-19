import json
import time
import uuid

def log_agent_trajectory(intent: str, tools_called: list, response: str, latency_ms: int):
    """
    Simulates structured logging and tracing for a production agent.
    In a real production environment, this would integrate with OpenTelemetry
    and Google Cloud Trace/Logging.
    """
    trace_id = str(uuid.uuid4())
    log_entry = {
        "timestamp": time.time(),
        "trace_id": trace_id,
        "intent": intent,
        "trajectory": {
            "spans": []
        },
        "response": response,
        "total_latency_ms": latency_ms
    }

    # Simulate generating spans for tool calls
    current_time = time.time()
    for i, tool in enumerate(tools_called):
        span = {
            "span_id": str(uuid.uuid4())[:8],
            "tool_name": tool['name'],
            "input": tool['input'],
            "output_status": "SUCCESS",
            "latency_ms": tool.get('latency_ms', 150)
        }
        log_entry["trajectory"]["spans"].append(span)
    
    # Write structured log to standard out (which Cloud Logging captures automatically)
    print(json.dumps(log_entry, indent=2))
    return trace_id

if __name__ == "__main__":
    print("Testing Production Observability Logger...")
    # Simulate a user request to an expense agent
    mock_tools = [
        {"name": "fetch_policy", "input": {"policy_id": "EXP-2026"}, "latency_ms": 120},
        {"name": "check_fraud", "input": {"amount": 250, "merchant": "TechStore"}, "latency_ms": 305}
    ]
    
    trace = log_agent_trajectory(
        intent="Approve a $250 expense for a new monitor from TechStore",
        tools_called=mock_tools,
        response="Expense requires manual HITL approval due to amount > $100.",
        latency_ms=425
    )
    
    print(f"Trace {trace} successfully logged to stdout.")
