def resource_test_summary() -> dict:
    """Returns synthetic test metadata; does not consume CPU or memory."""
    return {"test": "synthetic_resource_exhaustion", "safe": True, "real_resources_consumed": False}
