export default function AlertsTable({ incidents, onSelect, selectedId }) {
  return (
    <div className="card">
      <h2>Live Alerts</h2>
      <div className="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Time</th>
              <th>User</th>
              <th>Src IP</th>
              <th>Event</th>
              <th>Severity</th>
              <th>Risk</th>
            </tr>
          </thead>
          <tbody>
            {incidents
              .slice()
              .sort((a, b) => b.timestamp - a.timestamp)
              .slice(0, 100)
              .map((d) => (
                <tr
                  key={d._id}
                  className={d._id === selectedId ? "row-selected" : ""}
                  onClick={() => onSelect(d)}
                >
                  <td>{d.timestamp.toISOString()}</td>
                  <td>{d.user}</td>
                  <td>{d.src_ip}</td>
                  <td>{d.event_type}</td>
                  <td>{d.severity}</td>
                  <td>{d.risk_level}</td>
                </tr>
              ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
