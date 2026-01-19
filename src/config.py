# This file stores all the configuration settings for the project,
# like file paths, model parameters, and feature flags, so they can be easily changed in one place.



DATA_PATH = "data/raw/sales.csv"           # Path to the raw sales CSV file
MODEL_PATH = "model/forecasting_model.pkl" # Path where the trained model is saved/loaded
REPORT_PATH = "reports/analysis_report.txt" # Path to save the generated report

WINDOW_SIZE = 7        # Number of past days used to predict the next day
FORECAST_DAYS = 7      # How many days into the future to forecast
USE_CLOUD_LLM = False  # Set True if you want to make real GPT API calls
