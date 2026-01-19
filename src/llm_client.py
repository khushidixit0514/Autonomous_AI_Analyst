# src/llm_client.py

"""
Local MOCK LLM client
Purpose:
- Decide trend correctly (Increasing / Decreasing / Stable)
- Generate a simple analyst-style report
"""

from typing import List

def call_llm(forecasted: List[float]) -> str:
    """
    Simulates an AI (LLM) generating a sales report.

    Parameters:
        forecasted (List[float]): predicted sales values

    Returns:
        str: formatted analysis report
    """

    # -----------------------------
    # SAFETY CHECK: make sure we have enough data
    # -----------------------------
    if not forecasted or len(forecasted) < 2:
        trend = "Stable sales"  # not enough info to detect trend
    else:
        start_value = float(forecasted[0])  # first forecasted day
        end_value = float(forecasted[-1])   # last forecasted day

        # Decide the trend
        if end_value > start_value:
            trend = "Increasing sales"
        elif end_value < start_value:
            trend = "Decreasing sales"
        else:
            trend = "Stable sales"

    # -----------------------------
    # CREATE A SIMPLE REPORT
    # -----------------------------
    report = (
        "[MOCK GPT RESPONSE]\n"
        "Analysis:\n"
        f"- Trend: {trend}\n"
        "- Risks: Supply shortage next week\n"
        "- Recommendation 1: Adjust inventory based on trend\n"
        "- Recommendation 2: Launch promotional campaign if demand increases\n"
    )

    # Return the generated report as text
    return report
