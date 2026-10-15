def health_check(simulated_status: str = "healthy") -> bool:
    """Placeholder health check for the prototype; not an HTTP probe."""
    return simulated_status == "healthy"
