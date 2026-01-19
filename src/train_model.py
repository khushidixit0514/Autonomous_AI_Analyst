# src/train_model.py

# This file handles training the forecasting model.
# It reads the sales data, prepares it into sequences for supervised learning,
# trains a Linear Regression model, and saves the trained model to disk.

import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
from src.data_loader import load_data
from src.config import WINDOW_SIZE, MODEL_PATH

def create_sequences(data, window):
    """
    Convert a 1D array of sales into sequences for training.
    Each X is 'window' past days, each y is the next day.
    """
    X, y = [], []
    for i in range(len(data) - window):
        X.append(data[i:i + window])  # past 'window' days
        y.append(data[i + window])    # target: next day
    return np.array(X), np.array(y)

def train():
    df = load_data()  # Load the CSV data

    # --- Handle missing values ---
    if df['sales'].isnull().any():
        print("[Train] Found NaNs in CSV. Filling with 0.")
        df['sales'] = df['sales'].fillna(0)  # or df.dropna() if preferred

    # Get sales values as NumPy array
    sales = df["sales"].values

    # Create sequences for training
    X, y = create_sequences(sales, WINDOW_SIZE)

    # Check again for NaNs in sequences and fix them
    if np.isnan(X).any() or np.isnan(y).any():
        print("[Train] Warning: NaNs found in sequences. Replacing with 0.")
        X = np.nan_to_num(X)
        y = np.nan_to_num(y)

    # Initialize and train Linear Regression model
    model = LinearRegression()
    model.fit(X, y)

    # Save the trained model to disk
    joblib.dump(model, MODEL_PATH)
    print("✅ Model trained and saved")

if __name__ == "__main__":
    train()  # Train the model if this script is executed directly
