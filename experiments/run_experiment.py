import json
import time
from pathlib import Path

from agent.reasoning_engine import choose_action
from config.settings import PROJECT_ROOT
from detection.anomaly_detector import AnomalyDetector
from monitoring.audit_logger import audit
from monitoring.metrics import calculate_metrics
from recovery.container_recovery import recover_service
from response.action_validator import validate_action
from simulator.generate_traffic import demo_events

POLICY_PATH = PROJECT_ROOT / "config" / "security_policy.json"

def main() -> None:
    policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    detector = AnomalyDetector()
    records = []

    for index, event in enumerate(demo_events(), start=1):
        start = time.perf_counter()
        detection = detector.detect(event)
        detection_latency = (time.perf_counter() - start) * 1000
        action = choose_action(detection)
        allowed, message = validate_action(action, policy)
        audit("detection", {"event": event, "detection": detection})
        action_result = {"success": False, "mode": "blocked"}
        remediation_latency = None

        if allowed and action != "observe":
            action_start = time.perf_counter()
            # All actions are simulated. No real host/container controls are called.
            action_result = {"success": True, "mode": "simulation", "action": action}
            recovery = recover_service(image_verified=True)
            action_result["recovery"] = recovery
            remediation_latency = (time.perf_counter() - action_start) * 1000
            audit("simulated_response", {"action": action, "result": action_result})

        records.append({
            "event_id": index,
            "detected": detection["is_anomaly"],
            "detection_latency_ms": round(detection_latency, 2),
            "remediation_latency_ms": round(remediation_latency, 2) if remediation_latency is not None else None,
            "legitimate_request_success": True,
            "action": action,
            "action_allowed": allowed,
            "policy_message": message,
        })
        print(f"Event {index}: anomaly={detection['is_anomaly']} reasons={detection['reasons']} action={action} ({message})")

    report = calculate_metrics(records)
    output = PROJECT_ROOT / "data" / "demo_metrics.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"records": records, "metrics": report}, indent=2), encoding="utf-8")
    print("\nDemo metrics:")
    print(json.dumps(report, indent=2))
    print(f"\nSaved report to: {output}")

if __name__ == "__main__":
    main()
