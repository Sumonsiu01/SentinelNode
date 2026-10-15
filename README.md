# SentinelNode
### Agentic AI-Based Self-Healing Framework for Cyber Defence in Containerised Microservices

SentinelNode is an MSc research prototype for experimenting with telemetry collection, anomaly detection, policy-validated response actions, recovery checks, and incident metrics.

> **Prototype note:** This starter version uses synthetic events and simulated response actions. It does not automatically isolate real containers or change live Nginx routes. Add and test real integrations separately in an authorised lab.

## Architecture
- `telemetry/`: normalises application, container, and network events.
- `detection/`: detects simple rate and resource anomalies.
- `agent/`: chooses a response from a fixed, allow-listed action set.
- `response/`: validates actions and simulates containment.
- `recovery/`: simulates image verification and health checks.
- `monitoring/`: writes audit events and calculates metrics.
- `simulator/`: creates safe synthetic events.
- `experiments/`: runs a repeatable demo experiment.
- `tests/`: unit tests.

## Quick start (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m experiments.run_experiment
python -m unittest discover -s tests -v
```

## Configuration
Review `config/settings.py` and `config/security_policy.json`. Keep secrets out of Git. `.env.example` is a template only.

## Research metrics
The demo reports detection status, detection latency, remediation latency, and request success rate. These are prototype measurements, not dissertation results. Run repeated, controlled trials before reporting results.

## Safety
Run attack simulations only in an isolated environment you own or are authorised to test. Keep actions in dry-run mode until access controls, rollback, audit logging, and health checks have been reviewed.
