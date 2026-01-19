

# This agent handles the "Reporter" role in the autonomous system.
# It generates a human-readable report based on the sales data.

from src.llm_client import call_llm  # function to simulate AI-generated report

def generate_report(stats, forecasted):
    """
    Generate a report using the actual sales data from CSV.

    Parameters:
        stats: dictionary containing statistics and sales list
        forecasted: list of predicted sales (ignored here intentionally)

    Returns:
        report (str): formatted analyst-style report
    """

    # Get the original sales values from the stats dictionary
    sales_values = stats["sales"]

    # Call the LLM client to generate a report
    # We intentionally ignore forecasted values here to avoid incorrect trend analysis
    report = call_llm(sales_values)

    # Return the generated report as text
    return report
