"""Wires the agents into a LangGraph StateGraph — defines order and the validation-retry loop.

TODO:
- Build a StateGraph[AgentState] (models/state.py)
- Add each agent (agents/<name>/<name>_agent.py) as a node, in order:
  query_understanding -> schema_retrieval -> text_to_sql -> validation

- Conditional edge from schema_retrieval (fast-fail for "no access at all"):
    relevant_schema is EMPTY after guardrails/schema_access_guardrail.py has filtered
    it -> short-circuit straight to a refusal response ("you don't have access to the
    data needed to answer that"), skip text_to_sql entirely — no point generating SQL
    against zero allowed tables.
    relevant_schema is NON-empty -> continue to text_to_sql as normal.
    (This only catches "no access at all". Partial/row-level access, e.g. Priya can
    see `orders` but only her own region's rows, can't be known yet at this point —
    that's what permission_policy.py handles below, once real SQL exists.)

- Conditional edge from validation:
    validation_passed=True  -> execution -> insight -> END
    validation_passed=False -> back to text_to_sql, bounded by state.retry_count
    (cap at ~2 retries, then end honestly with an "I couldn't answer this confidently" state)
"""
