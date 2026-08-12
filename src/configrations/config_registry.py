"""Single source of truth for all environment-driven settings.

TODO:
- Define a pydantic-settings BaseSettings subclass covering:
  ENV, APP_DB_URL, BUSINESS_DB_HOST/PORT/USER/PASSWORD/ENGINE (read-only creds),
  ANTHROPIC_API_KEY, pgvector table name.
- Missing/misconfigured env vars should fail at startup (pydantic-settings does this
  for you) rather than surface as a mystery None three layers down at request time.
- Instantiate ONE shared `settings` object here for the rest of the app to import.
"""
