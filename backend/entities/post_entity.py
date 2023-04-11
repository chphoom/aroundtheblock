from sqlalchemy import String, DateTime, Boolean, ARRAY, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.mutable import MutableList
from typing import Self
from .entity_base import EntityBase
from ..models import Post
from datetime import datetime

# maps post object from pydantic to post entity in database
class PostEntity(EntityBase):
    __tablename__ = "posts"

    id = mapped_column(Integer, primary_key=True)
    img: Mapped[str] = mapped_column(String(64))
    desc: Mapped[str] = mapped_column(String(64))
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
            id=model.id, 
            img=model.img, 
            desc=model.desc, 
            private=model.private, 
            created=model.created, 
            user_id=model.postedBy, 
            comments=model.comments, 
            challenge_id=model.challenge, 
            tags=model.tags
            )

    def to_model(self) -> Post:
        #TODO: update logic to output name of the challenge
        return Post(
            id=self.id, 
            img=self.img, 
            desc=self.desc, 
            private=self.private, 
            created=self.created, 
            postedBy=self.user_id, 
            comments=self.comments, 
            challenge=self.challenge_id, 
            tags=self.tags)
