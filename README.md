“Built an autonomous AI analyst with pluggable LLM backend (cloud + local)”


pip install python-dotenv
src/
 ├── agents/                  # Phase 3 agents folder
 │    ├── planner_agent.py
 │    ├── analyst_agent.py
 │    └── reporter_agent.py
 ├── analyzer.py              # Existing — computes stats from data
 ├── data_loader.py           # Existing — loads CSVs, etc.
 ├── forecaster.py            # Existing — forecasting model
 ├── autonomous_loop.py       # Existing — orchestrates single-agent loop
 ├── llm_agent.py             # Existing — GPT / mock reasoning
 ├── llm_client.py            # Existing — real or mock LLM calls
 ├── train_model.py           # Existing — model training script
 ├── main.py                  # Existing — main entry point
 └── config.py                # Existing — constants (paths, window size, etc.)
