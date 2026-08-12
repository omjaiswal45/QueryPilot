"""Finds which of the 500 tables are relevant to the question — pure vector search,
no LLM call, no prompt needed.

Calls infrastructures/vectorstore/pgvector_store.py directly. No tools.py here for
now — add one only if this agent grows a second distinct capability (e.g. retrieving
similar past question -> SQL examples), not just to look like the other agents.

TODO:
def run(state: AgentState) -> dict:
    # 1. call pgvector_store.search_relevant_tables()
    # 2. call guardrails/schema_access_guardrail.py's filter_allowed_tables() with the
    #    user's permission rule, BEFORE returning — so a table the user can't see
    #    never reaches the text_to_sql_agent's prompt at all
    # return {"relevant_schema": [...]}
    #
    # NOTE: if filter_allowed_tables() removes every retrieved table, leave
    # relevant_schema as an empty list rather than raising — orchestrator/graph.py's
    # conditional edge reads that empty list as the "no access at all" signal and
    # short-circuits to a refusal, without ever calling text_to_sql_agent.
    ...
"""
