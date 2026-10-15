from datetime import datetime, timezone

def normalise_event(event: dict) -> dict:
    """Validate and standardise a synthetic telemetry event."""
    required = {"source", "request_rate", "cpu_percent", "memory_percent"}
    missing = required - event.keys()
    if missing:
        raise ValueError(f"Missing telemetry fields: {', '.join(sorted(missing))}")
    result = dict(event)
    result["timestamp"] = result.get("timestamp") or datetime.now(timezone.utc).isoformat()
    result["request_rate"] = max(0, int(result["request_rate"]))
    result["cpu_percent"] = float(result["cpu_percent"])
    result["memory_percent"] = float(result["memory_percent"])
    return result
