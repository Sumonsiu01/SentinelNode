from detection.rules import detect_anomaly

class AnomalyDetector:
    def detect(self, event: dict) -> dict:
        return detect_anomaly(event)
