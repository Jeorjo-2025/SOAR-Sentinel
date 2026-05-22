# SOAR Sentinel: Automated Threat Intelligence & Incident Response Dashboard

End-to-end SOAR project combining:

- Python backend for synthetic security logs, threat intel enrichment, UEBA, and playbooks
- JSON export of incidents
- React + Vite dashboard deployed on Netlify
- Netlify Forms contact box so recruiters can send questions directly

## Run backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

copy config\settings_example.yaml config\settings.yaml

python run_pipeline.py
```
