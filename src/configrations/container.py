"""Dependency wiring for FastAPI's Depends() — plain factory functions, not a heavyweight
DI framework. FastAPI's own Depends() IS your DI container; this file just centralizes
the factories so routes don't construct their own instances.

TODO:
- get_app_db_session() -> yields a SQLAlchemy session (infrastructures/db/app_db.py)
- get_llm_client() -> returns the shared LLM client (infrastructures/llm/llm_client.py)
- get_business_db_connector() -> returns infrastructures/db/business_db_connector.py
- get_query_service() -> builds QueryService with its repository/connector deps injected
"""
from pymongo import MongoClient

from configurations.container import Container
from configurations.google_auth_config import GoogleAuthConfig
from configurations.mongo_config import MongoConfig
from infrastructure.mongo_client import MongoClientProvider
from configurations.llm_config import LlmConfig
from configurations.logger import AppLogger
logger = AppLogger.get_logger(__name__)

class ConfigRegisterer:

    @classmethod
    def register_configs(cls, env):
        try:
            logger.info("Initializing Configs")
            container = Container()

            google_auth_cfg = GoogleAuthConfig(env)
            container.register(GoogleAuthConfig, instance=google_auth_cfg)

            mongo_config = MongoConfig(env)
            container.register(MongoConfig, instance=mongo_config)
            logger.info("Mongo configuration registered successfully")

            mongo_client: MongoClient = MongoClientProvider.create_mongo_client()
            container.register(MongoClient, instance=mongo_client)
            logger.info("Mongo client registered successfully")

            llm_config = LlmConfig(env)
            container.register(LlmConfig, instance=llm_config)
            logger.info("LLM configuration registered successfully")


        except Exception as e:
            logger.info(f"Error initiaizing configs: {e}")
            raise