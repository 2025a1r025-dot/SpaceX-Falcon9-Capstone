# SpaceX Falcon 9 Landing Prediction — Starter Project

This is a reproducible starter project to help you complete the IBM/Coursera-style SpaceX capstone.
It is not a personal GitHub repository until you upload it to your own GitHub account.

## Dataset and attribution
The project uses the public 56-row course dashboard dataset hosted in the repository below:
https://github.com/IslamSaqer/Applied-Data-Science-Capstone
Raw CSV:
https://raw.githubusercontent.com/IslamSaqer/Applied-Data-Science-Capstone/main/spacex_launch_dash.csv

The source repository reports: 56 records, 4 launch-site labels, 42.9% landing success,
KSC LC-39A highest site success proportion of 76.9%, mean payload mass 3,697 kg,
and SVM best held-out accuracy of 100% on a fixed 75/25 split.
These are source-reported summary figures, not a claim that this starter script independently reproduced them.
Because the sample is small, the reported model score should not be interpreted as production readiness.

## Setup
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
python analysis_pipeline.py
python spacex_dash_app.py
```

## Suggested GitHub upload
Create a new public repository in your own GitHub account, upload this folder, and paste your actual repository URL into your presentation.
Do not claim the source repository above as your own.

## Files
- `analysis_pipeline.py`: downloads the public CSV, runs summary analysis and compares four classifiers.
- `queries.sql`: SQL examples for the project.
- `spacex_dash_app.py`: simple interactive Plotly Dash dashboard.
- `requirements.txt`: dependencies.
