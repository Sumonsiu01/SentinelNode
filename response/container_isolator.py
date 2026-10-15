def isolate_container(action_context: dict) -> dict:
    """Simulation only: does not change firewall rules or container state."""
    return {"action": "isolate_container_simulated", "success": True, "mode": "simulation"}
