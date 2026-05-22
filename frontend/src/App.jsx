import { useEffect, useState } from "react";
import MetricsBar from "./components/MetricsBar";
import IncidentsOverTime from "./components/IncidentsOverTime";
import RiskDistribution from "./components/RiskDistribution";
import TopIps from "./components/TopIps";
import AlertsTable from "./components/AlertsTable";
import IncidentDetails from "./components/IncidentDetails";
import ContactForm from "./components/ContactForm";

function App() {
  const [incidents, setIncidents] = useState([]);
  const [filtered, setFiltered] = useState([]);
  const [selected, setSelected] = useState(null);

  useEffect(() => {
    fetch("/final_incidents.json")
      .then((res) => res.json())
      .then((data) => {
        const parsed = data.map((d, idx) => ({
          ...d,
          _id: idx,
          timestamp: new Date(d.timestamp),
        }));
        setIncidents(parsed);
        setFiltered(parsed);
        if (parsed.length) setSelected(parsed[0]);
      });
  }, []);

  return (
    <div className="app">
      <header className="app-header">
        <h1>SOAR Sentinel: Threat Intelligence & Incident Response</h1>
        <p>Automated SOAR pipeline with UEBA, playbooks.</p>
      </header>

      <MetricsBar incidents={filtered} />

      <div className="grid grid-2">
        <IncidentsOverTime incidents={filtered} />
        <RiskDistribution incidents={filtered} />
      </div>

      <div className="grid grid-2">
        <TopIps incidents={filtered} />
        <IncidentDetails incident={selected} />
      </div>

      <div className="grid grid-2">
        <AlertsTable
          incidents={filtered}
          onSelect={setSelected}
          selectedId={selected?._id}
        />
        <ContactForm />
      </div>
    </div>
  );
}

export default App;
