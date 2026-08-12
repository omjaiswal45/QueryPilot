"""Pydantic model for AgentState — the data shape passed between every node in the graph.

Every agent function has the same shape: (state: AgentState) -> dict (a partial update).
Keeping the shape in one place is what makes orchestrator/graph.py's wiring mechanical
instead of bespoke per agent.

TODO: define fields as you add agents, e.g.:
  raw_question: str
  clarified_question: str | None
  relevant_schema: list[str]
  refusal_reason: str | None  # set when schema_retrieval finds zero accessible
                               # tables (see orchestrator/graph.py's fast-fail edge);
                               # its presence is what tells the graph to skip straight
                               # to a refusal response instead of text_to_sql
  generated_sql: str | None
  validation_passed: bool
  query_result: list[dict] | None
  retry_count: int
  summary: str | None
"""
