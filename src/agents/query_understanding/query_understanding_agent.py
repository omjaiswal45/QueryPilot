from infrastructures.llm.llm_client import LlmClient
from configurations.logger import AppLogger
logger = AppLogger.get_logger(__name__)

PROMPT_PATH = __file__.replace("query_understanding_agent.py", "prompt.txt")


def run(state: dict) -> dict:
    with open(PROMPT_PATH, "r") as f:
        system_prompt = f.read()

    clarified = LlmClient.complete(
        prompt=state["raw_question"],
        system=system_prompt,
    )
    return {"clarified_question": clarified}
