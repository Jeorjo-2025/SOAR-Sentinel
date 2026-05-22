import logging
import pandas as pd

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def playbook_malicious_ip(event: pd.Series) -> dict:
    action = {
        "playbook": "malicious_ip",
        "blocked_ip": event["src_ip"],
        "notified": True
    }
    logger.info(f"[PLAYBOOK] Blocking IP {event['src_ip']} and notifying SOC.")
    return action

def playbook_suspicious_user(event: pd.Series) -> dict:
    action = {
        "playbook": "suspicious_user",
        "user_disabled": event["user"],
        "password_reset_forced": True
    }
    logger.info(f"[PLAYBOOK] Disabling user {event['user']} and forcing password reset.")
    return action

def playbook_malware_hash(event: pd.Series) -> dict:
    action = {
        "playbook": "malware_hash",
        "file_quarantined": event["file_hash"],
        "host_isolated": event["dest_ip"]
    }
    logger.info(f"[PLAYBOOK] Quarantining file {event['file_hash']} and isolating host {event['dest_ip']}.")
    return action

def playbook_privilege_escalation(event: pd.Series) -> dict:
    action = {
        "playbook": "privilege_escalation",
        "process_killed": event["process_name"],
        "tier2_alerted": True
    }
    logger.info(f"[PLAYBOOK] Killing process {event['process_name']} and alerting Tier-2.")
    return action

def run_playbooks(enriched_df: pd.DataFrame) -> pd.DataFrame:
    actions = []
    for _, row in enriched_df.iterrows():
        if row["risk_level"] in ["high", "critical"]:
            if row["ip_malicious_score"] > 70:
                actions.append(playbook_malicious_ip(row))
            elif row["event_type"] in ["failed_login", "impossible_travel"]:
                actions.append(playbook_suspicious_user(row))
            elif row["event_type"] == "malware_detected":
                actions.append(playbook_malware_hash(row))
            elif row["event_type"] == "privilege_escalation":
                actions.append(playbook_privilege_escalation(row))
            else:
                actions.append({"playbook": "none", "note": "No matching playbook"})
        else:
            actions.append({"playbook": "none", "note": "Risk below threshold"})

    actions_df = pd.DataFrame(actions)
    result = pd.concat([enriched_df.reset_index(drop=True), actions_df], axis=1)
    return result
