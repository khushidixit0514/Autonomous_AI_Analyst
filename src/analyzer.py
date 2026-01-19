def analyze_data(df):
    # Take only the "sales" column from the dataframe
    # .values converts it into a NumPy array
    sales = df["sales"].values

    # Return a dictionary that contains useful statistics
    return {
        # Average sales value
        "mean": float(sales.mean()),

        # Highest sales value
        "max": float(sales.max()),

        # Lowest sales value
        "min": float(sales.min()),

        # Standard deviation (shows how much sales vary)
        "std": float(sales.std()),

        # Convert NumPy array to a normal Python list
        # 🔥 VERY IMPORTANT:
        # This is needed because NumPy arrays cannot be
        # directly converted to JSON (for APIs / saving results)
        "sales": sales.tolist()
    }
