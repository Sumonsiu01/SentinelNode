import unittest
from detection.anomaly_detector import AnomalyDetector
from telemetry.event_normalizer import normalise_event

class DetectionTests(unittest.TestCase):
    def setUp(self):
        self.detector = AnomalyDetector()

    def test_benign_event(self):
        event = normalise_event({"source": "test", "request_rate": 20, "cpu_percent": 25, "memory_percent": 30})
        self.assertFalse(self.detector.detect(event)["is_anomaly"])

    def test_high_rate_detected(self):
        event = normalise_event({"source": "test", "request_rate": 200, "cpu_percent": 25, "memory_percent": 30})
        self.assertIn("high_request_rate", self.detector.detect(event)["reasons"])

if __name__ == "__main__":
    unittest.main()
