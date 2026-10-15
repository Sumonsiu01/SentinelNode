from agent.tools import ALLOWED_ACTIONS

def choose_action(detection: dict) -> str:
    """Deterministic, explainable baseline for the future ReAct agent integration."""
    if not detection.get("is_anomaly"):
        return "observe"
    reasons = set(detection.get("reasons", []))
    if "high_request_rate" in reasons:
        action = "drain_traffic_simulated"
    elif "high_cpu" in reasons or "high_memory" in reasons:
        action = "isolate_container_simulated"
    else:
        action = "observe"
    if action not in ALLOWED_ACTIONS:
        return "observe"
    return action
