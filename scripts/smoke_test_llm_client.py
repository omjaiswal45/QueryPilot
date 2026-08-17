"""Proves LlmClient can actually call Groq and get a real response back.

Run from the project root with `src` on the Python path:
    set PYTHONPATH=src
    python scripts\\smoke_test_llm_client.py
"""
from configurations.env_intializer import env
from configurations.config_registry import ConfigRegisterer
from infrastructures.llm.llm_client import LlmClient

ConfigRegisterer.register_configs(env)

answer = LlmClient.complete(
    prompt="Reply with exactly one short sentence confirming you received this.",
    system="You are a test assistant.",
)
print(f"LLM responded: {answer}")
