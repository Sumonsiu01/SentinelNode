from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = PROJECT_ROOT / "logs"
DATA_DIR = PROJECT_ROOT / "data"
AUDIT_LOG = LOG_DIR / "audit.jsonl"

# Keep True for this starter project. Real system changes are not implemented.
DRY_RUN = True

# Example thresholds for synthetic demo events; calibrate with measured data.
REQUEST_RATE_THRESHOLD = 120
CPU_PERCENT_THRESHOLD = 90.0
MEMORY_PERCENT_THRESHOLD = 90.0
