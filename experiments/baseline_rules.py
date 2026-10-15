def baseline_action(event: dict) -> str:
    """Simple threshold baseline for comparison with the agent decision layer."""
    if event.get("request_rate", 0) >= 120:
        return "traffic_alert"
    if event.get("cpu_percent", 0) >= 90 or event.get("memory_percent", 0) >= 90:
        return "resource_alert"
    return "observe"
