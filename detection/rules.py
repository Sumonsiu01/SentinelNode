from config import settings

def detect_anomaly(event: dict) -> dict:
    reasons = []
    if event["request_rate"] >= settings.REQUEST_RATE_THRESHOLD:
        reasons.append("high_request_rate")
    if event["cpu_percent"] >= settings.CPU_PERCENT_THRESHOLD:
        reasons.append("high_cpu")
    if event["memory_percent"] >= settings.MEMORY_PERCENT_THRESHOLD:
        reasons.append("high_memory")
    return {
        "is_anomaly": bool(reasons),
        "reasons": reasons,
        "severity": "high" if len(reasons) >= 2 else ("medium" if reasons else "low"),
    }
