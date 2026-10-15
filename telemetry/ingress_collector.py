from telemetry.event_normalizer import normalise_event

def parse_ingress_sample(sample: dict) -> dict:
    """Parse a pre-collected access-log summary; no live log socket is opened."""
    event = {"source": "ingress", **sample}
    return normalise_event(event)
