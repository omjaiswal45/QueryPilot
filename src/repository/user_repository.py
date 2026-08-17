"""App DB access for users — the only file (besides other repository/ files) allowed to
import User from models/db_models.py.
"""
from sqlalchemy import select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from configurations.container import Container
from configurations.logger import AppLogger
from models.db_models import User
logger = AppLogger.get_logger(__name__)


class UserRepository:

    @staticmethod
    def get_by_email(email: str) -> User | None:
        engine = Container().resolve(Engine)
        try:
            with Session(engine) as session:
                statement = select(User).where(User.email == email)
                return session.scalars(statement).first()
        except Exception as e:
            logger.error(f"Error fetching user by email, UserRepository: {e}")
            raise

    @staticmethod
    def create_user(email: str, name: str) -> User:
        engine = Container().resolve(Engine)
        try:
            with Session(engine) as session:
                user = User(email=email, name=name)
                session.add(user)
                session.commit()
                session.refresh(user)
                return user
        except Exception as e:
            logger.error(f"Error creating user, UserRepository: {e}")
            raise
