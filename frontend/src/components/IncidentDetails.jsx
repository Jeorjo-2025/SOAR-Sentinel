export default function IncidentDetails({ incident }) {
  if (!incident) {
    return (
      <div className="card">
        <h2>Incident Details</h2>
        <p>Select an alert from the table.</p>
      </div>
    );
  }

  return (
    <div className="card">
      <h2>Incident Details</h2>
      <p>
        <strong>Time:</strong> {incident.timestamp.toISOString()}
      </p>
      <p>
        <strong>User:</strong> {incident.user}
      </p>
      <p>
        <strong>Source IP:</strong> {incident.src_ip}
      </p>
      <p>
        <strong>Destination IP:</strong> {incident.dest_ip}
      </p>
      <p>
        <strong>Event:</strong> {incident.event_type}
      </p>
      <p>
        <strong>Severity:</strong> {incident.severity}
      </p>
      <p>
        <strong>Risk Level:</strong> {incident.risk_level}
      </p>
      <p>
        <strong>Playbook:</strong> {incident.playbook}
      </p>
      <p>
        <strong>IP Score:</strong> {incident.ip_malicious_score}
      </p>
      <p>
        <strong>Hash Score:</strong> {incident.hash_malicious_score}
      </p>
    </div>
  );
}
