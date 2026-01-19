“Built an autonomous AI analyst with pluggable LLM backend (cloud + local)”

This project is an autonomous AI system that Monitors sales data CSV file , Analyzes historical sales , Forecasts future sales , Generates human-readable reports automatically. It uses a multi-agent architecture:

Planner Agent → decides tasks

Reporter Agent → generates professional-style report

Analyst Agent → computes stats & forecasts

FOR INSTALLATION:

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python src/train_model.py

python src/main.py
