"""Your own Postgres — engine built ONCE, long-lived pool.
shape: a static factory that resolves its own config from the container and returns the
one reusable client/engine object other code holds onto.
"""
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from configurations.app_db_config import AppDbConfig
from configurations.container import Container
from configurations.logger import AppLogger
logger = AppLogger.get_logger(__name__)


class AppDbProvider:

    @staticmethod
    def create_app_db_engine() -> Engine:
        try:
            app_db_config = Container().resolve(AppDbConfig)
            engine = create_engine(app_db_config.url)
            return engine
        except Exception as e:
            logger.error(f"Error creating app db engine, AppDbProvider: {e}")
            raise
