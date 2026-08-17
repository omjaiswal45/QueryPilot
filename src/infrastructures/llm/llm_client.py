"""Single wrapper around the Groq SDK — the only file that imports `groq` directly.

Every agent calls THIS, never the SDK directly — keeps provider-swapping and
mocking-in-tests confined to one file.
"""
from groq import Groq

from configurations.llm_config import LlmConfig
from configurations.container import Container
from configurations.logger import AppLogger
logger = AppLogger.get_logger(__name__)


class LlmClient:

    @staticmethod
    def complete(prompt: str, system: str | None = None) -> str:
        llm_config = Container().resolve(LlmConfig)
        client = Groq(api_key=llm_config.api_key)

        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        try:
            response = client.chat.completions.create(
                model=llm_config.model,
                messages=messages,
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error calling Groq API, LlmClient: {e}")
            raise
