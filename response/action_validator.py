from agent.tools import ALLOWED_ACTIONS

def validate_action(action: str, policy: dict) -> tuple[bool, str]:
    if action not in ALLOWED_ACTIONS:
        return False, "Action is not allow-listed"
    if action not in policy.get("allowed_actions", []):
        return False, "Action is not permitted by security policy"
    if not policy.get("dry_run", True):
        return False, "This starter prototype blocks live actions"
    return True, "Approved for simulation only"
