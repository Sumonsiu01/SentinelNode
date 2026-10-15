from recovery.health_checker import health_check

def recover_service(image_verified: bool = True) -> dict:
    if not image_verified:
        return {"success": False, "reason": "image_verification_failed"}
    healthy = health_check("healthy")
    return {"success": healthy, "reason": "healthy" if healthy else "health_check_failed"}
