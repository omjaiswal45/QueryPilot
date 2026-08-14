"""Dependency wiring for FastAPI's Depends() — plain factory functions, not a heavyweight
DI framework. FastAPI's own Depends() IS your DI container; this file just centralizes
the factories so routes don't construct their own instances.

TODO:
- get_app_db_session() -> yields a SQLAlchemy session (infrastructures/db/app_db.py)
- get_llm_client() -> returns the shared LLM client (infrastructures/llm/llm_client.py)
- get_business_db_connector() -> returns infrastructures/db/business_db_connector.py
- get_query_service() -> builds QueryService with its repository/connector deps injected
"""
import punq


class Container:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._container = punq.Container()
        return cls._instance

    def register(self, cls, *, instance=None):
        """
        Register a class or an instance
        """
        if instance is not None:
            self._container.register(cls, instance=instance)
        else:
            self._container.register(cls)

    def resolve(self, cls):
        """
        Resolve a class with dependencies injected
        """
        return self._container.resolve(cls)

