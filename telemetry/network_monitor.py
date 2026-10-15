from telemetry.event_normalizer import normalise_event

def parse_network_sample(sample: dict) -> dict:
    """Parse a supplied network summary; no live Netlink monitoring is enabled."""
    event = {"source": "network", **sample}
    return normalise_event(event)
