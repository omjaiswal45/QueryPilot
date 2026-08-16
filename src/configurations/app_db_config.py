from configurations.logger import AppLogger
logger = AppLogger.get_logger(__name__)


class AppDbConfig:
    def __init__(self, env):
        try:
            self.url = env.str("APP_DB_URL")
            logger.info("AppDB config loaded successfully")
        except Exception as e :
            logger.info(f"Error Loading App DB Configs: {e}")

