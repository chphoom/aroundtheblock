from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self
from .entity_base import EntityBase
from .reply_entity import reply_table
from ..models import Comment
from datetime import datetime

# maps comments object from pydantic to comments entity in database
class CommentEntity(EntityBase):
    __tablename__ = "comments"

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey("users.email"))
    commenter: Mapped['UserEntity'] = relationship(post_update=True)
    post_id = mapped_column(ForeignKey("posts.id"))
    post: Mapped['PostEntity'] = relationship(back_populates="comments", post_update=True)
    replyTo_id = mapped_column(ForeignKey("comments.id"))
    replies: Mapped[list["CommentEntity"]] = relationship(secondary="reply", primaryjoin=id==reply_table.c.comment_id,
                            secondaryjoin=id==reply_table.c.reply_id, back_populates="replies", post_update=True)
    text: Mapped[str] = mapped_column(String(1024))
    created: Mapped[datetime] = mapped_column(DateTime)

    @classmethod
    def from_model(cls, model: Comment) -> Self:
        return cls(
            user_id=model.commenter, 
            post_id=model.post, 
            text=model.text, 
            created=model.created,
            replies=model.replies
            )
    
    def to_model(self) -> Comment:
        return Comment(
            id=self.id, 
            commenter=self.user_id, 
            post=self.post_id, 
            text=self.text, 
            created=self.created,
            replies=[reply.to_model() for reply in self.replies]
            )