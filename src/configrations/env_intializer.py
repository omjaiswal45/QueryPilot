"""Decides which .env file to load, based on the ENV variable — must run BEFORE config_registry
reads anything.

TODO:
- Read ENV (default "dev") from the process environment.
- Load the matching src/resources/.env.{ENV} file with python-dotenv.
"""
