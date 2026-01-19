# This file defines a function to forecast the next 7 days of sales
# using a trained model and the last few days of actual sales.

import numpy as np

def forecast(df, model, window_size):
    """
    Forecast next N days using trained model.
    df: pandas DataFrame with 'sales' column
    model: trained LinearRegression
    window_size: number of days to look back
    """
    # Take the 'sales' column values as a NumPy array
    sales = df['sales'].values  # use actual data, NOT model
    X_pred = []

    # Get the last 'window_size' points to start forecasting
    last_window = sales[-window_size:]
    window = last_window.copy()  # copy so we don't modify original data

    # List to store forecasted sales
    forecasted = []

    # Simple iterative forecast for next 7 days
    for _ in range(7):  # forecast 7 days
        # Prepare input for the model (reshape to 2D array)
        X_input = np.array(window).reshape(1, -1)

        # Predict the next day's sales
        y_pred = model.predict(X_input)[0]

        # Add prediction to forecast list
        forecasted.append(y_pred)

        # Update the window: remove oldest value, add new prediction
        window = np.roll(window, -1)  # shift values left
        window[-1] = y_pred           # replace last value with predicted one

    # Return the 7-day forecast
    return forecasted
