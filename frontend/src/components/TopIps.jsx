import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

export default function TopIps({ incidents }) {
  const scores = {};
  incidents.forEach((d) => {
    scores[d.src_ip] = Math.max(scores[d.src_ip] || 0, d.ip_malicious_score);
  });
  const data = Object.entries(scores)
    .map(([ip, score]) => ({ ip, score }))
    .sort((a, b) => b.score - a.score)
    .slice(0, 10);

  return (
    <div className="card">
      <h2>Top Malicious IPs</h2>
      <ResponsiveContainer width="100%" height={250}>
        <BarChart data={data}>
          <XAxis dataKey="ip" hide />
          <YAxis />
          <Tooltip />
          <Bar dataKey="score" fill="#ef4444" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
