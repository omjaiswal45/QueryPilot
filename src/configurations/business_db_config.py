from configurations.logger import AppLogger
logger = AppLogger.get_logger(__name__)


class BusinessDbConfig:
    def __init__(self, env):
        self.host = env.str("BUSINESS_DB_HOST")
        self.port = env.int("BUSINESS_DB_PORT")
        self.name = env.str("BUSINESS_DB_NAME")
        self.user = env.str("BUSINESS_DB_USER")
        self.password = env.str("BUSINESS_DB_PASSWORD")
