"""Decides which .env file to load, based on the ENV variable — must run BEFORE config_registry
reads anything.

TODO:
- Read ENV (default "dev") from the process environment.
- Load the matching src/resources/.env.{ENV} file with python-dotenv.
"""
import pathlib
import os
from dotenv import load_dotenv
from environs import Env

from configurations.logger import AppLogger

logger = AppLogger.get_logger(__name__)

env = Env()

# ENV=Local, Dev, Prod, etc.
running_env = os.getenv("ENV", "Local").lower()

resources_path = pathlib.Path(__file__).parent.parent / "resources"

# Default .env
default_env_path = resources_path / ".env.default"

# Environment-specific .env
env_file_path = resources_path / f".env.{running_env}"

# Load default .env first
if default_env_path.is_file():
    try:
        load_dotenv(default_env_path)
        env.read_env(default_env_path)
        logger.info(f"Loaded default environment variables from {default_env_path}")
    except Exception as e:
        logger.error(f"Failed to load default .env file: {e}")
        raise
else:
    logger.warning(f"Default .env file not found at: {default_env_path}")


if env_file_path.is_file():
    try:
        load_dotenv(env_file_path, override=True)
        env.read_env(env_file_path, override=True)
        logger.info(f"Loaded environment variables from {env_file_path}")
    except Exception as e:
        logger.error(f"Failed to load environment variables from {env_file_path}: {e}")
        raise
else:
    logger.warning(f"No environment-specific .env file found at: {env_file_path}")
    raise FileNotFoundError(
        f"Environment variables file not found: {env_file_path}"
    )