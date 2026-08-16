from configurations.logger import AppLogger
logger = AppLogger.get_logger(__name__)


class LlmConfig:
    def __init__(self, env):
        try:
            self.api_key = env.str("ANTHROPIC_API_KEY")
            self.model = env.str("ANTHROPIC_MODEL", default="claude-sonnet-5")
            logger.info("LLM config loaded successfully")
        except Exception as e:
            logger.info(f"Error Loading LLM Configs: {e}")
            raise
