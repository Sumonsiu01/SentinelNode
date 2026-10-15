def drain_traffic(action_context: dict) -> dict:
    """Simulation only: does not modify Nginx or production traffic."""
    return {"action": "drain_traffic_simulated", "success": True, "mode": "simulation"}
