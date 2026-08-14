"""Wires up Python logging using configrations/logger.yaml.

TODO:
- Load logger.yaml with logging.config.dictConfig().
- Expose a get_logger(name: str) helper the rest of the app imports,
  instead of every module calling logging.getLogger() directly.
"""
import logging
import yaml
import os
from pathlib import Path
from logging.config import dictConfig

class AppLogger:
    _configured=False

    @classmethod
    def get_logger(cls, file_name):
        current_env = os.getenv('ENV').lower()
        if not cls._configured:
            yaml_path = Path(__file__).parent / "logging.yaml"
            with open(yaml_path, 'r') as file:
                config = yaml.load(file, Loader=yaml.SafeLoader)

                # Remove file logging in PROD
                if current_env == "prod":
                    config["handlers"].pop("timed_file", None)
                    if "timed_file" in config["root"]["handlers"]:
                        config["root"]["handlers"].remove("timed_file")
                    if "timed_file" in config["loggers"]["myapp"]["handlers"]:
                        config["loggers"]["myapp"]["handlers"].remove("timed_file")

                dictConfig(config)
            cls._configured=True
        return logging.getLogger(file_name)