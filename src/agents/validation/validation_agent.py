"""Checks generated SQL BEFORE execution — no LLM call, no prompt, delegates entirely
to guardrails/sql_validator.py.

TODO:
def run(state: AgentState) -> dict:
    # call core.sql_validator.validate_sql(); on failure, return
    # {"validation_passed": False} so the graph can route back to text_to_sql
    ...
"""
