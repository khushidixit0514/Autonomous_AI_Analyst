# src/agents/planner_agent.py

# This agent handles the "Planner" role in the autonomous system.
# It decides what tasks need to be done by the Analyst Agent.

def plan_tasks():
    """
    Planner agent decides what tasks to perform.

    Returns:
        tasks (list of str): list of tasks for the Analyst Agent
    """
    # Define a simple set of tasks for the Analyst to perform
    tasks = [
        "Analyze sales statistics",   # Compute mean, max, min, std, etc.
        "Forecast next 7 days",       # Predict future sales
        "Check for anomalies"         # Identify unusual patterns or risks
    ]
    return tasks
