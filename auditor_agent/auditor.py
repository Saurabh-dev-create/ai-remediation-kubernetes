import json
import os
from datetime import datetime


INCIDENT_FILE = "auditor_agent/data/incidents.json"


def log_incident(
    pod_name,
    reason,
    root_cause,
    action,
    status
):

    incident = {
        "timestamp": datetime.utcnow().isoformat(),
        "pod": pod_name,
        "reason": reason,
        "root_cause": root_cause,
        "action": action,
        "status": status
    }

    # Load existing incidents
    if os.path.exists(INCIDENT_FILE):

        with open(INCIDENT_FILE, "r", encoding="utf-8") as f:

            try:
                incidents = json.load(f)

            except json.JSONDecodeError:
                incidents = []

    else:
        incidents = []

    # Add new incident
    incidents.append(incident)

    # Save back
    with open(INCIDENT_FILE, "w", encoding="utf-8") as f:
        json.dump(
            incidents,
            f,
            indent=4
        )

    print("📝 Incident logged successfully.")