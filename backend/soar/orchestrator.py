import os
import pandas as pd
from .config_loader import load_config
from .log_generator import generate_synthetic_events
from .enrichment import enrich_events
from .ueba_model import fit_ueba_model, score_events
from .playbooks import run_playbooks
from .report_generator import generate_incident_report

def run_soar_pipeline(
    n_events: int = 1500,
    config_path: str = None,
    save_intermediate: bool = True
) -> pd.DataFrame:
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_dir = os.path.join(base_dir, "data")
    reports_dir = os.path.join(base_dir, "reports")
    frontend_public = os.path.join(base_dir, "..", "frontend", "public")

    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(reports_dir, exist_ok=True)
    os.makedirs(frontend_public, exist_ok=True)

    cfg = load_config(config_path)

    events = generate_synthetic_events(n_events=n_events)
    if save_intermediate:
        events.to_csv(os.path.join(data_dir, "synthetic_events.csv"), index=False)

    enriched = enrich_events(events)
    if save_intermediate:
        enriched.to_csv(os.path.join(data_dir, "enriched_events.csv"), index=False)

    model = fit_ueba_model(
        enriched,
        contamination=cfg["model"]["contamination"],
        random_state=cfg["model"]["random_state"]
    )

    scored = score_events(enriched, model)
    if save_intermediate:
        scored.to_csv(os.path.join(data_dir, "scored_events.csv"), index=False)

    final_df = run_playbooks(scored)
    if save_intermediate:
        final_df.to_csv(os.path.join(data_dir, "final_incidents.csv"), index=False)

    json_path = os.path.join(frontend_public, "final_incidents.json")
    final_df.to_json(json_path, orient="records", date_format="iso")

    high_risk = final_df[final_df["risk_level"].isin(["high", "critical"])]
    for _, row in high_risk.iterrows():
        generate_incident_report(row, reports_dir)

    return final_df
