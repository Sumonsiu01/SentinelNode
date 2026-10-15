from telemetry.event_normalizer import normalise_event

def parse_container_sample(sample: dict) -> dict:
    """Parse a supplied container-metrics snapshot; no host cgroups are read."""
    event = {"source": "container", **sample}
    return normalise_event(event)
