# This file defines a function to generate natural language insights
# from statistics and forecasted sales using an AI (LLM) client.

from src.llm_client import call_llm  # function that calls GPT or other LLM

def generate_insights(stats, forecast):
    # Prepare a prompt (instruction) for the AI
    # Includes stats, forecast, and clear tasks for the AI to do
    prompt = f"""
You are an autonomous AI data analyst.

STATISTICS:
- Mean sales: {stats['mean']}
- Max sales: {stats['max']}
- Min sales: {stats['min']}
- Std deviation: {stats['std']}
- Trend: {stats['trend']}

FORECAST (next days):
{forecast}

TASKS:
1. Interpret the trend and forecast
2. Identify risks or anomalies
3. Give 2 actionable business recommendations
4. Write in a professional report style
"""

    # Send the prompt to the LLM and return the AI-generated report
    return call_llm(prompt)
