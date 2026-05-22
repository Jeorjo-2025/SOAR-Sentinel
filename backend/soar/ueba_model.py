import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

CATEGORICAL = ["user", "event_type", "process_name", "severity"]
NUMERICAL = ["ip_malicious_score", "hash_malicious_score"]

def build_ueba_pipeline(contamination: float = 0.05, random_state: int = 42) -> Pipeline:
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL),
            ("num", "passthrough", NUMERICAL),
        ]
    )

    clf = IsolationForest(
        n_estimators=200,
        contamination=contamination,
        random_state=random_state
    )

    pipe = Pipeline(steps=[
        ("preprocess", preprocessor),
        ("clf", clf)
    ])

    return pipe

def fit_ueba_model(df: pd.DataFrame, contamination: float = 0.05, random_state: int = 42) -> Pipeline:
    pipe = build_ueba_pipeline(contamination, random_state)
    X = df[CATEGORICAL + NUMERICAL]
    pipe.fit(X)
    return pipe

def score_events(df: pd.DataFrame, model: Pipeline) -> pd.DataFrame:
    X = df[CATEGORICAL + NUMERICAL]
    scores = model.decision_function(X)
    preds = model.predict(X)  # -1 anomaly, 1 normal

    df = df.copy()
    df["anomaly_score"] = -scores
    df["is_anomaly"] = (preds == -1).astype(int)

    def risk_level(score):
        if score < 0.2:
            return "low"
        elif score < 0.5:
            return "medium"
        elif score < 0.8:
            return "high"
        else:
            return "critical"

    max_score = df["anomaly_score"].max() or 1
    df["normalized_anomaly"] = df["anomaly_score"] / max_score
    df["risk_level"] = df["normalized_anomaly"].apply(risk_level)
    return df
