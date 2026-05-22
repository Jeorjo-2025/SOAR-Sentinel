import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

EVENT_TYPES = [
    "failed_login",
    "successful_login",
    "suspicious_powershell",
    "lateral_movement",
    "malware_detected",
    "privilege_escalation",
    "impossible_travel"
]

USERS = [f"user{i}" for i in range(1, 21)]
IPS = [f"10.0.0.{i}" for i in range(1, 51)]
PROCESSES = ["powershell.exe", "cmd.exe", "winword.exe", "chrome.exe", "svchost.exe"]

def generate_synthetic_events(n_events: int = 2000, start_days_ago: int = 7) -> pd.DataFrame:
    now = datetime.utcnow()
    start_time = now - timedelta(days=start_days_ago)

    timestamps = [
        start_time + timedelta(seconds=random.randint(0, start_days_ago * 24 * 3600))
        for _ in range(n_events)
    ]

    data = {
        "timestamp": timestamps,
        "user": np.random.choice(USERS, size=n_events),
        "src_ip": np.random.choice(IPS, size=n_events),
        "dest_ip": np.random.choice(IPS, size=n_events),
        "event_type": np.random.choice(
            EVENT_TYPES,
            size=n_events,
            p=[0.25, 0.4, 0.05, 0.05, 0.1, 0.05, 0.1]
        ),
        "process_name": np.random.choice(PROCESSES, size=n_events),
        "file_hash": [
            f"hash_{random.randint(1, 200)}" if random.random() < 0.2 else None
            for _ in range(n_events)
        ],
        "severity": np.random.choice(
            ["low", "medium", "high", "critical"],
            size=n_events,
            p=[0.5, 0.3, 0.15, 0.05]
        )
    }

    df = pd.DataFrame(data)
    df.sort_values("timestamp", inplace=True)
    return df
