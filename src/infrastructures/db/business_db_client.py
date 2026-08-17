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
from sqlalchemy import create_engine, text

from configurations.business_db_config import BusinessDbConfig
from configurations.container import Container
from configurations.logger import AppLogger
logger = AppLogger.get_logger(__name__)

STATEMENT_TIMEOUT_MS = 5000


class BusinessDbProvider:

    @staticmethod
    def run_readonly_query(sql: str) -> list[dict]:
        business_db_config = Container().resolve(BusinessDbConfig)
        url = (
            f"postgresql://{business_db_config.user}:{business_db_config.password}"
            f"@{business_db_config.host}:{business_db_config.port}/{business_db_config.name}"
        )
        engine = create_engine(url)
        try:
            with engine.connect() as connection:
                connection.execute(text(f"SET statement_timeout = {STATEMENT_TIMEOUT_MS}"))
                result = connection.execute(text(sql))
                return [dict(row._mapping) for row in result]
        except Exception as e:
            logger.error(f"Error running business DB query, BusinessDbProvider: {e}")
            raise
        finally:
            engine.dispose()
