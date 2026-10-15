ALLOWED_ACTIONS = {
    "observe",
    "drain_traffic_simulated",
    "isolate_container_simulated",
    "restart_container_simulated",
}

def available_actions() -> list[str]:
    return sorted(ALLOWED_ACTIONS)
