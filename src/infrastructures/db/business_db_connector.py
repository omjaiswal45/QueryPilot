"""Read-only connector to your company's 500-table operational database.

Deliberately NOT built like app_db.py:
- A fresh connection is opened per query and closed immediately after — never pooled
  long-term.
- Executes under a database ROLE that only has SELECT granted — defense in depth,
  independent of the app-level check in guardrails/sql_validator.py.
- Enforces a short statement_timeout so a bad or expensive generated query can't hang
  the process.

TODO:
def run_readonly_query(sql: str) -> list[dict]:
    # 1. open a fresh connection using settings.BUSINESS_DB_* (read-only credentials)
    # 2. SET statement_timeout
    # 3. execute sql
    # 4. fetch rows, close connection
    ...
"""
