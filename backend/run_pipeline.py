from soar.orchestrator import run_soar_pipeline

if __name__ == "__main__":
    df = run_soar_pipeline()
    print("SOAR pipeline complete.")
    print(df[["timestamp", "user", "event_type", "risk_level", "playbook"]].head())
