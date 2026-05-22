import os
import pandas as pd
from datetime import datetime

TEMPLATE = """
<html>
<head><title>Incident Report - {incident_id}</title></head>
<body>
<h1>Incident Report - {incident_id}</h1>
<p><b>Generated:</b> {generated_at}</p>
<h2>Executive Summary</h2>
<p>Risk level: <b>{risk_level}</b></p>
<p>Event type: <b>{event_type}</b></p>
<p>User: <b>{user}</b> | Source IP: <b>{src_ip}</b> | Dest IP: <b>{dest_ip}</b></p>

<h2>Timeline</h2>
<p>Timestamp: {timestamp}</p>

<h2>Threat Intelligence</h2>
<ul>
  <li>IP malicious score: {ip_score}</li>
  <li>IP threat category: {ip_category}</li>
  <li>Hash malicious score: {hash_score}</li>
  <li>Hash threat category: {hash_category}</li>
</ul>

<h2>UEBA Analysis</h2>
<ul>
  <li>Anomaly score: {anomaly_score}</li>
  <li>Normalized anomaly: {normalized_anomaly}</li>
</ul>

<h2>Actions Taken</h2>
<ul>
  <li>Playbook: {playbook}</li>
  <li>Details: {action_details}</li>
</ul>

<h2>Recommendations</h2>
<p>Review user activity, validate IP reputation with external TI sources, and update detection rules if needed.</p>
</body>
</html>
"""

def generate_incident_report(event: pd.Series, output_dir: str) -> str:
    os.makedirs(output_dir, exist_ok=True)
    incident_id = f"INC-{event.name}"
    html = TEMPLATE.format(
        incident_id=incident_id,
        generated_at=datetime.utcnow().isoformat(),
        risk_level=event["risk_level"],
        event_type=event["event_type"],
        user=event["user"],
        src_ip=event["src_ip"],
        dest_ip=event["dest_ip"],
        timestamp=event["timestamp"],
        ip_score=event["ip_malicious_score"],
        ip_category=event["ip_threat_category"],
        hash_score=event["hash_malicious_score"],
        hash_category=event["hash_threat_category"],
        anomaly_score=round(event["anomaly_score"], 3),
        normalized_anomaly=round(event["normalized_anomaly"], 3),
        playbook=event.get("playbook", "none"),
        action_details=str({
            k: event[k]
            for k in event.index
            if k.startswith("blocked_") or k.endswith("_disabled") or k.endswith("_isolated")
        })
    )

    path = os.path.join(output_dir, f"{incident_id}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path
