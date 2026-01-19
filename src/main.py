# src/main.py

# This is the entry point of the Autonomous AI Analyst project.
# It loads the data, loads the trained model, and starts the continuous
# autonomous loop where the AI observes, analyzes, and generates reports.

import joblib
from src.data_loader import load_data
from src.config import MODEL_PATH, WINDOW_SIZE, REPORT_PATH
from src.autonomous_loop import run_autonomous_analysis

def main():
    print("Loading data...")
    df = load_data()  # Load and prepare the sales data

    print("Loading model...")
    model = joblib.load(MODEL_PATH)  # Load the trained forecasting model

    print("Running Phase 4 Autonomous AI Analyst...")
    # Start the continuous autonomous analysis loop
    # This loop will monitor CSV changes, retrain the model if needed,
    # run the planner/analyst/reporter agents, and save updated reports.
    run_autonomous_analysis(
        df,
        model,
        WINDOW_SIZE,
        continuous=True,
        report_path=REPORT_PATH
    )

if __name__ == "__main__":
    main()  # Run the main function when this script is executed
