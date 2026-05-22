import random
import pandas as pd
from typing import Dict

THREAT_CATEGORIES = ["botnet", "phishing", "ransomware", "bruteforce", "unknown"]

def simulate_ip_reputation(ip: str) -> Dict:
    score = random.randint(0, 100)
    return {
        "ip": ip,
        "malicious_score": score,
        "threat_category": random.choice(THREAT_CATEGORIES) if score > 40 else "benign",
        "confidence": random.randint(50, 100) if score > 40 else random.randint(0, 50)
    }

def simulate_hash_reputation(file_hash: str) -> Dict:
    if file_hash is None:
        return {
            "file_hash": None,
            "malicious_score": 0,
            "threat_category": "none",
            "confidence": 0
        }
    score = random.randint(0, 100)
    return {
        "file_hash": file_hash,
        "malicious_score": score,
        "threat_category": random.choice(THREAT_CATEGORIES) if score > 40 else "benign",
        "confidence": random.randint(50, 100) if score > 40 else random.randint(0, 50)
    }

def enrich_events(df: pd.DataFrame) -> pd.DataFrame:
    ip_enrichment = df["src_ip"].apply(simulate_ip_reputation).apply(pd.Series)
    hash_enrichment = df["file_hash"].apply(simulate_hash_reputation).apply(pd.Series)

    ip_enrichment = ip_enrichment.add_prefix("ip_")
    hash_enrichment = hash_enrichment.add_prefix("hash_")

    enriched = pd.concat([df.reset_index(drop=True), ip_enrichment, hash_enrichment], axis=1)
    return enriched
