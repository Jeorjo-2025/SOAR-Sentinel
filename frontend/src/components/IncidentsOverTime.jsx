import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

export default function IncidentsOverTime({ incidents }) {
  const byHour = {};
  incidents.forEach((d) => {
    const key = d.timestamp.toISOString().slice(0, 13) + ":00";
    byHour[key] = (byHour[key] || 0) + 1;
  });
  const data = Object.entries(byHour).map(([time, count]) => ({ time, count }));

  return (
    <div className="card">
      <h2>Incidents Over Time</h2>
      <ResponsiveContainer width="100%" height={250}>
        <LineChart data={data}>
          <XAxis dataKey="time" hide />
          <YAxis />
          <Tooltip />
          <Line
            type="monotone"
            dataKey="count"
            stroke="#4f46e5"
            strokeWidth={2}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
