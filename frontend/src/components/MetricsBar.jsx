export default function MetricsBar({ incidents }) {
  const total = incidents.length;
  const highCritical = incidents.filter((d) =>
    ["high", "critical"].includes(d.risk_level),
  ).length;
  const users = new Set(incidents.map((d) => d.user)).size;
  const ips = new Set(incidents.map((d) => d.src_ip)).size;

  return (
    <div className="metrics-bar">
      <div className="metric-card metric-blue">
        <span>Total Incidents</span>
        <strong>{total}</strong>
      </div>
      <div className="metric-card metric-red">
        <span>High / Critical</span>
        <strong>{highCritical}</strong>
      </div>
      <div className="metric-card metric-purple">
        <span>Unique Users</span>
        <strong>{users}</strong>
      </div>
      <div className="metric-card metric-green">
        <span>Source IPs</span>
        <strong>{ips}</strong>
      </div>
    </div>
  );
}
