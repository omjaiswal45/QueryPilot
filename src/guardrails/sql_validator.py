"""Pure logic, no DB/LLM — validates generated SQL before it's allowed to run.
This is the easiest file in the whole app to unit test — start here (see tests/core/).

TODO:
def validate_sql(sql: str, allowed_tables: list[str]) -> None:
    # - parse with sqlglot
    # - raise SQLSafetyError if it contains DROP/DELETE/UPDATE/ALTER
    # - raise SQLSafetyError if it references a table outside `allowed_tables`
    #   (a hallucination signal — the LLM inventing a table name)
    ...
"""
