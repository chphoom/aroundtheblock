from sqlalchemy import String, Integer, ARRAY, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.mutable import MutableList
from typing import Self
from .entity_base import EntityBase
from .c2p_entity import c2p
from ..models import Challenge
from datetime import datetime

# maps challenges object from pydantic to challenges entity in database
class ChallengeEntity(EntityBase):
    __tablename__ = "challenges"

    id = mapped_column(Integer, primary_key=True)
    posts: Mapped[list["PostEntity"]] = relationship(secondary=c2p, back_populates="challenge")
    noun: Mapped[str] = mapped_column(String(64))
    verb: Mapped[str] = mapped_column(String(64))
    adj: Mapped[str] = mapped_column(String(64))
    emotion: Mapped[str] = mapped_column(String(64))
    style: Mapped[str] = mapped_column(String(64))
    colors: Mapped[list[str]] = mapped_column(MutableList.as_mutable(ARRAY(String(64))))
    createdBy = mapped_column(ForeignKey("users.email"), nullable=True)
    start: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    end: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    type: Mapped[str] = mapped_column(String(64))

    @classmethod
    def from_model(cls, model: Challenge) -> Self:
        return cls(
            posts=model.posts,
            noun=model.noun, 
            verb=model.verb, 
            adj=model.adj, 
            emotion=model.emotion, 
            style=model.style, 
            colors=model.colors,
            createdBy=model.createdBy,
            start=model.start,
            end=model.end,
            type=model.getType()
            )

    def to_model(self) -> Challenge:
        return Challenge(
            id=self.id, 
            posts=self.posts, 
            noun=self.noun, 
            verb=self.verb, 
            adj=self.adj, 
            emotion=self.emotion, 
            style=self.style,
            colors=self.colors,
            createdBy=self.createdBy,
            start=self.start,
            end=self.end
            )
