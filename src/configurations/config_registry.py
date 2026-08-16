"""Single source of truth for all environment-driven settings.

TODO:
- Define a pydantic-settings BaseSettings subclass covering:
  ENV, APP_DB_URL, BUSINESS_DB_HOST/PORT/USER/PASSWORD/ENGINE (read-only creds),
  ANTHROPIC_API_KEY, pgvector table name.
- Missing/misconfigured env vars should fail at startup (pydantic-settings does this
  for you) rather than surface as a mystery None three layers down at request time.
- Instantiate ONE shared `settings` object here for the rest of the app to import.
"""
from configurations.container import Container
from configurations.llm_config import LlmConfig
from configurations.app_db_config import AppDbConfig
from configurations.business_db_config import BusinessDbConfig
from configurations.logger import AppLogger
logger = AppLogger.get_logger(__name__)

class ConfigRegisterer:

    @classmethod
    def register_configs(cls, env):
        try:
            logger.info("Initializing Configs")
            container = Container()

            llm_config = LlmConfig(env)
            container.register(LlmConfig, instance=llm_config)
            logger.info("LLM configuration registered successfully")

            app_db_config = AppDbConfig(env)
            container.register(AppDbConfig, instance=app_db_config)
            logger.info("APP Db configuration registered successfully")

            business_db_config = BusinessDbConfig(env)
            container.register(BusinessDbConfig, instance=business_db_config)
            logger.info("Business DB configuration registered successfully")

            
        except Exception as e:
            logger.info(f"Error initiaizing configs: {e}")
            raise