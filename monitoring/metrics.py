def calculate_metrics(records: list[dict]) -> dict:
    if not records:
        return {
            "events": 0, "detected": 0, "detection_rate_percent": 0.0,
            "mean_detection_latency_ms": 0.0, "mean_remediation_latency_ms": 0.0,
            "request_success_rate_percent": 0.0,
        }
    detected = [r for r in records if r.get("detected")]
    detection_latencies = [r["detection_latency_ms"] for r in detected if "detection_latency_ms" in r]
    remediation_latencies = [r["remediation_latency_ms"] for r in records if r.get("remediation_latency_ms") is not None]
    success = sum(bool(r.get("legitimate_request_success", True)) for r in records)
    mean = lambda values: round(sum(values) / len(values), 2) if values else 0.0
    return {
        "events": len(records),
        "detected": len(detected),
        "detection_rate_percent": round(100 * len(detected) / len(records), 2),
        "mean_detection_latency_ms": mean(detection_latencies),
        "mean_remediation_latency_ms": mean(remediation_latencies),
        "request_success_rate_percent": round(100 * success / len(records), 2),
    }
