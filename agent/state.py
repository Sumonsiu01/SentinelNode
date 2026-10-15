from dataclasses import dataclass, field

@dataclass
class IncidentState:
    incident_id: str
    event: dict
    detection: dict
    actions: list[str] = field(default_factory=list)
    status: str = "detected"
