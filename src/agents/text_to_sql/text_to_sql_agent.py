"""Generates SQL using ONLY the retrieved schema, then applies the user's permission
scope. Uses prompt.txt in this folder.

TODO:
def run(state: AgentState) -> dict:
    # build prompt from prompt.txt + state.relevant_schema,
    # call llm_client, apply guardrails/permission_policy.py, return {"generated_sql": ...}
    ...
"""
