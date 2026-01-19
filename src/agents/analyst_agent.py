# src/agents/analyst_agent.py

# This agent handles the "Analyst" role in the autonomous system.
# It computes statistics from the sales data and generates a forecast for future days.

from src.analyzer import analyze_data  # function to compute mean, max, min, std, etc.
from src.forecaster import forecast    # function to forecast next 7 days

def perform_analysis(df, model, window_size):
    """
    Analyst Agent: computes statistics and forecasts.
    
    Parameters:
        df: pandas DataFrame with sales data
        model: trained forecasting model
        window_size: number of past days to use for prediction
    
    Returns:
        stats: dictionary with statistics of sales
        forecasted: list of predicted sales for next days
    """
    # Compute stats like mean, max, min, std, etc.
    stats = analyze_data(df)

    # Forecast sales for the next few days using the model
    forecasted = forecast(df, model, window_size)

    # Return both stats and forecast
    return stats, forecasted
