"""Proves the first real agent works end to end: a raw, ambiguous question in,
a clarified question out, via a real LLM call.

Run from the project root with `src` on the Python path:
    set PYTHONPATH=src
    python scripts\\smoke_test_query_understanding_agent.py
"""
from configurations.env_intializer import env
from configurations.config_registry import ConfigRegisterer
from agents.query_understanding.query_understanding_agent import run

ConfigRegisterer.register_configs(env)

state = {"raw_question": "what were our top products recently"}
result = run(state)
print(f"Raw question:       {state['raw_question']}")
print(f"Clarified question: {result['clarified_question']}")
