"""Restricts which tables the Schema-Retrieval Agent is allowed to surface to the LLM,
based on the user's permission rule — applied BEFORE text-to-SQL generation, not after.

Why this exists alongside permission_policy.py: permission_policy.py scopes ROWS in
already-generated SQL (e.g. region = 'West'). This guardrail scopes TABLES earlier,
before the LLM ever sees them — e.g. a non-HR user's prompt should never even mention
the `payroll` table exists. Defense in depth: a sensitive table can't leak into the
LLM's context, regardless of how well text_to_sql_agent behaves afterward.

TODO:
def filter_allowed_tables(retrieved_tables: list[str], permission_rule) -> list[str]:
    ...
"""
