from sqlalchemy import Boolean, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self
from .entity_base import EntityBase
from ..models import Notif
from datetime import datetime

class NotifEntity(EntityBase):
    __tablename__ = "notifications"

    id = mapped_column(Integer, primary_key=True)
    toUser_id = mapped_column(ForeignKey("users.email"))
    fromUser_id = mapped_column(ForeignKey("users.email"), nullable=True)
    comment_id = mapped_column(ForeignKey("comments.id"), nullable=True)
    last_read: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    challenge_id = mapped_column(ForeignKey("challenges.id"), nullable=True)
    read: Mapped[bool] = mapped_column(Boolean, nullable=True)

    @classmethod
    def from_model(cls, model: Notif) -> Self:
        return cls(
            toUser_id=model.toUser_id,
            fromUser_id=model.fromUser_id,
            comment_id=model.comment_id,
            last_read=model.last_read,
            challenge_id=model.challenge_id,
            read=model.read
            )

    def to_model(self) -> Notif:
        return Notif(
            id=self.id,
            toUser_id=self.toUser_id,
            fromUser_id=self.fromUser_id,
            comment_id=self.comment_id,
            last_read=self.last_read,
            challenge_id=self.challenge_id,
            read=self.read)