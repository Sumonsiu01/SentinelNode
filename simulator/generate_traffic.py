from telemetry.event_normalizer import normalise_event

def demo_events() -> list[dict]:
    """Small synthetic dataset. It sends no network traffic."""
    samples = [
        {"source": "synthetic_benign", "request_rate": 35, "cpu_percent": 28, "memory_percent": 42},
        {"source": "synthetic_http_flood", "request_rate": 240, "cpu_percent": 72, "memory_percent": 65},
        {"source": "synthetic_resource_exhaustion", "request_rate": 65, "cpu_percent": 97, "memory_percent": 94},
    ]
    return [normalise_event(sample) for sample in samples]
