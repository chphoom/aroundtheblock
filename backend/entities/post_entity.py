from sqlalchemy import String, DateTime, Boolean, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.mutable import MutableList
from typing import Self
from .entity_base import EntityBase
from ..models import Post
from datetime import datetime

# maps post object from pydantic to post entity in database
class PostEntity(EntityBase):
    __tablename__ = "posts"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    img: Mapped[str] = mapped_column(String(512))
    title: Mapped[str] = mapped_column(String(64))
    desc: Mapped[str] = mapped_column(String(2048))
    private: Mapped[bool] = mapped_column(Boolean)
    created: Mapped[datetime] = mapped_column(DateTime)
    user_id = mapped_column(ForeignKey("users.email"), onupdate="cascade")
    postedBy: Mapped['UserEntity'] = relationship(back_populates="userPosts", post_update=True)
    comments: Mapped[list["CommentEntity"]] = relationship(back_populates="post")
    tags: Mapped[list[str]] = mapped_column(MutableList.as_mutable(ARRAY(String(64))))
    challenge_id = mapped_column(ForeignKey("challenges.id"), onupdate="cascade")
    challenge: Mapped['ChallengeEntity'] = relationship(back_populates="posts", post_update=True)

    @classmethod
    def from_model(cls, model: Post) -> Self:
        return cls(
            img=model.img, 
            title=model.title,
            desc=model.desc, 
            private=model.private, 
            created=model.created, 
            user_id=model.user_id, 
            comments=model.comments, 
            challenge_id=model.challenge, 
            tags=model.tags
            )

    def to_model(self) -> Post:
        return Post(
            id=self.id, 
            img=self.img,
            title=self.title,
            desc=self.desc, 
            private=self.private, 
            created=self.created, 
            user_id=self.user_id, 
            comments=self.comments, 
            challenge=self.challenge_id, 
            tags=self.tags)
