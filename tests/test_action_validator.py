import json
import unittest
from pathlib import Path
from response.action_validator import validate_action

ROOT = Path(__file__).resolve().parents[1]
POLICY = json.loads((ROOT / "config" / "security_policy.json").read_text(encoding="utf-8"))

class ActionValidatorTests(unittest.TestCase):
    def test_simulated_action_allowed(self):
        self.assertTrue(validate_action("drain_traffic_simulated", POLICY)[0])

    def test_unknown_action_rejected(self):
        self.assertFalse(validate_action("delete_everything", POLICY)[0])

if __name__ == "__main__":
    unittest.main()
