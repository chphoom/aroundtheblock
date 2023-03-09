"""Definitions of SQLAlchemy table-backed object mappings called entities."""


from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from typing import Self
from models import User
from datetime import datetime


class Base(DeclarativeBase):
    pass

#maps user object fromo pydantic to user entity in ddatabase
class UserEntity(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(64), primary_key=True)
    displayName: Mapped[str] = mapped_column(String(64))
    password: Mapped[str] = mapped_column(String(64))
    created: Mapped[datetime] = mapped_column(DateTime)

    @classmethod
    def from_model(cls, model: User) -> Self:
        return cls(email=model.email, displayName=model.displayName, password=model.password, created=model.created)

    def to_model(self) -> User:
        return User(email=self.email, displayName=self.displayName, password=self.password, created=self.created)

