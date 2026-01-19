# This file defines a function to load the sales CSV,
# convert the date column to proper datetime format,
# and sort the data by date for analysis.

import pandas as pd
from src.config import DATA_PATH  # import the path to the CSV from config

def load_data():
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(DATA_PATH)

    # Convert the 'date' column to datetime objects so we can sort and analyze correctly
    df['date'] = pd.to_datetime(df['date'])

    # Sort the DataFrame by date in ascending order
    df = df.sort_values('date')

    # Return the cleaned and sorted DataFrame
    return df
