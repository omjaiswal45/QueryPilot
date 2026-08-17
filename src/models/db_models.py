"""SQLAlchemy ORM models — App DB tables ONLY. Never used to model the business DB
(it isn't yours to model — the agent introspects it at runtime instead).

TODO: define ChatHistory, QueryAuditLog, SchemaEmbeddingMeta.
Only files in repository/ should import from this module.
"""
from datetime import datetime, timezone

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, UniqueConstraint

Base = declarative_base()


def _utcnow():
    return datetime.now(timezone.utc)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=_utcnow)
    updated_at = Column(DateTime, default=_utcnow, onupdate=_utcnow)


class UserCredential(Base):
    """One row per way a user can log in — a user may have a 'password' row,
    a 'google' row, or both."""
    __tablename__ = "user_credentials"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    provider = Column(String, nullable=False)  # "password" or "google"
    hashed_password = Column(String, nullable=True)
    google_id = Column(String, unique=True, nullable=True)
    created_at = Column(DateTime, default=_utcnow)

    __table_args__ = (
        UniqueConstraint("user_id", "provider", name="uq_user_credentials_user_provider"),
    )


class PermissionRule(Base):
    """A user can have zero, one, or multiple rules — e.g. access to more than
    one region."""
    __tablename__ = "permission_rules"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    region = Column(String, nullable=True)
    created_at = Column(DateTime, default=_utcnow)
