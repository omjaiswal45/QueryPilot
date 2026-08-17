"""Proves UserRepository can actually create and fetch a real row in querypilot_app.

Run from the project root with `src` on the Python path:
    set PYTHONPATH=src
    python scripts\\smoke_test_user_repository.py
"""
from configurations.env_intializer import env
from configurations.config_registry import ConfigRegisterer
from repository.user_repository import UserRepository

ConfigRegisterer.register_configs(env)

existing = UserRepository.get_by_email("priya@example.com")
if existing is None:
    user = UserRepository.create_user(email="priya@example.com", name="Priya Sharma")
    print(f"Created user: id={user.id}, email={user.email}, is_active={user.is_active}")
else:
    print(f"Found existing user: id={existing.id}, email={existing.email}")
