import os
import yaml

def load_config(path: str = None) -> dict:
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "..", "config", "settings.yaml")
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Config file not found at {path}. Copy settings_example.yaml to settings.yaml."
        )
    with open(path, "r") as f:
        return yaml.safe_load(f)
