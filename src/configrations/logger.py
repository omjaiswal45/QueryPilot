"""Wires up Python logging using configrations/logger.yaml.

TODO:
- Load logger.yaml with logging.config.dictConfig().
- Expose a get_logger(name: str) helper the rest of the app imports,
  instead of every module calling logging.getLogger() directly.
"""
