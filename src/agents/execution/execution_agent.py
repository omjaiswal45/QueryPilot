"""Runs the validated SQL against the real business DB — no LLM call, no prompt.
The only agent that touches infrastructures/db/business_db_client.py.

TODO:
def run(state: AgentState) -> dict:
    # guard on state.validation_passed, call business_db_connector.run_readonly_query()
    ...
"""
