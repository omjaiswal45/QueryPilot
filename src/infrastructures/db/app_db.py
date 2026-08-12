"""Your own Postgres — engine + session, built ONCE at startup, long-lived pool.

TODO:
- engine = create_engine(settings.APP_DB_URL, pool_size=...)
- SessionLocal = sessionmaker(bind=engine)
- get_app_db_session(): FastAPI dependency, yields one session per request, closes after

This file must never accept a per-request connection string as a parameter — if it
starts needing one, that's a sign business-DB logic has leaked in here.
"""
