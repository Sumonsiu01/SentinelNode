import unittest
from monitoring.metrics import calculate_metrics

class MetricsTests(unittest.TestCase):
    def test_detection_rate(self):
        result = calculate_metrics([
            {"detected": True, "detection_latency_ms": 2, "legitimate_request_success": True},
            {"detected": False, "detection_latency_ms": 1, "legitimate_request_success": True},
        ])
        self.assertEqual(result["detection_rate_percent"], 50.0)
        self.assertEqual(result["request_success_rate_percent"], 100.0)

if __name__ == "__main__":
    unittest.main()
