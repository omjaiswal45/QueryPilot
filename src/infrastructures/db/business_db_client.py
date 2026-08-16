"""Read-only connector to your company's 500-table operational database.

Deliberately NOT built like app_db_client.py:
- A fresh engine is opened per query and disposed immediately after — never pooled
  long-term, unlike AppDbProvider's one-engine-for-the-app's-life pattern.
- Executes under BUSINESS_DB_USER (querypilot_reader) — a role that only has SELECT
  granted at the database level. That grant is the real enforcement; the statement
  below is defense in depth, not the only thing standing between a bad query and
  your data.
- Sets a short statement_timeout so a bad or expensive generated query can't hang.
"""



