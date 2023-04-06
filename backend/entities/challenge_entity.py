from sqlalchemy import String, Integer, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.mutable import MutableList
from typing import Self
from .entity_base import EntityBase
from .c2p_entity import c2p
from ..models.models import Challenge
# from datetime import datetime

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

    @classmethod
    def from_model(cls, model: Challenge) -> Self:
        return cls(
            posts=model.posts,
            noun=model.noun, 
            verb=model.verb, 
            adj=model.adj, 
            emotion=model.emotion, 
            style=model.style, 
            colors=model.colors
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
            colors=self.colors
            )

# class weChallengeEntity(ChallengeEntity):
#     start: Mapped[datetime] = mapped_column(DateTime)
#     end: Mapped[datetime] = mapped_column(DateTime)

# class meChallengeEntity(ChallengeEntity):
#     createdBy: Mapped[UserEntity] = relationship()
