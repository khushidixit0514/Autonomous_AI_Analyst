# This file runs the main autonomous AI loop that continuously watches data changes,
# retrains the model if needed, analyzes results using agents, and generates updated reports automatically.

# src/autonomous_loop.py
import os
import time
import joblib
from src.data_loader import load_data
from src.train_model import train
from src.agents.planner_agent import plan_tasks
from src.agents.analyst_agent import perform_analysis
from src.agents.reporter_agent import generate_report
from src.config import DATA_PATH, WINDOW_SIZE, REPORT_PATH, MODEL_PATH

CHECK_INTERVAL = 10       # seconds between loop iterations

def run_autonomous_analysis(df, model, window_size, continuous=True, report_path=REPORT_PATH):
    """
    Phase 4 Autonomous AI Analyst Loop
    - Multi-Agent Planner → Analyst → Reporter
    - Automatic CSV hot-reload and model retraining
    - Continuous monitoring & report update
    """
    last_csv_mod_time = os.path.getmtime(DATA_PATH)

    while True:
        # --- Check if CSV changed ---
        current_mod_time = os.path.getmtime(DATA_PATH)
        if current_mod_time != last_csv_mod_time:
            print("[Autonomous Loop] CSV changed. Retraining model...")
            train()  # retrain model on updated CSV
            model = joblib.load(MODEL_PATH)  # reload trained model
            df = load_data()                  # reload updated CSV
            last_csv_mod_time = current_mod_time

        # --- Planner: define tasks ---
        tasks = plan_tasks()
        print(f"[Planner] Tasks: {tasks}")

        # --- Analyst: compute stats & forecast ---
        stats, forecasted = perform_analysis(df, model, window_size)
        print(f"[Analyst] Stats computed, forecast generated.")

        # --- Reporter: generate report ---
        report = generate_report(stats, forecasted)
        with open(report_path, "w") as f:
            f.write(report)
        print(f"[Reporter] Report generated. Saved to {report_path}")
        print("✅ Cycle complete.\n")

        if not continuous:
            break

        time.sleep(CHECK_INTERVAL)
