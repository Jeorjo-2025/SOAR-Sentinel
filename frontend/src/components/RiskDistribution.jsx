import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

export default function RiskDistribution({ incidents }) {
  const counts = {};
  incidents.forEach((d) => {
    counts[d.risk_level] = (counts[d.risk_level] || 0) + 1;
  });
  const data = Object.entries(counts).map(([risk, count]) => ({ risk, count }));

  return (
    <div className="card">
      <h2>Risk Distribution</h2>
      <ResponsiveContainer width="100%" height={250}>
        <BarChart data={data}>
          <XAxis dataKey="risk" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="count" fill="#f97316" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
