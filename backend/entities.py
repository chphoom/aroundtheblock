"""Definitions of SQLAlchemy table-backed object mappings called entities."""


from sqlalchemy import String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from typing import Self
from models import User, Post
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
    private: Mapped[bool] = mapped_column(Boolean)
    bio: Mapped[str] = mapped_column(String(64))
    pronouns: Mapped[str] = mapped_column(String(64))
    img: Mapped[str] = mapped_column(String(64))
    # userPosts: Mapped[list["PostEntity"]] = relationship(back_populates="postedBy")
    # savedPosts: Mapped[list["PostEntity"]] = relationship(back_populates="savedBy")

    @classmethod
    def from_model(cls, model: User) -> Self:
        return cls(email=model.email, displayName=model.displayName, password=model.password, created=model.created, private=model.private, bio=model.bio, pronouns=model.pronouns, img=model.img) #userPosts=model.userPosts)

    def to_model(self) -> User:
        return User(email=self.email, displayName=self.displayName, password=self.password, created=self.created, private=self.private, bio=self.bio, pronouns=self.pronouns, img=self.img)#, userPosts=self.userPosts)

#TODO maps post object from pydantic to post entity in database
# class PostEntity(Base):
#     __tablename__ = "posts"

#     img: Mapped[str] = mapped_column(String(64), primary_key=True)
#     desc: Mapped[str] = mapped_column(String(64))
#     private: Mapped[bool] = mapped_column(Boolean)
#     created: Mapped[datetime] = mapped_column(DateTime)
#     user_id = mapped_column(ForeignKey("users.email"))
#     postedBy: Mapped[UserEntity] = relationship(back_populates="userPosts")
#     savedBy: Mapped[UserEntity] = relationship(back_populates="savedPosts")

#     @classmethod
#     def from_model(cls, model: Post) -> Self:
#         return cls(img=model.img, desc=model.desc, private=model.private, created=model.created)

#     def to_model(self) -> Post:
#         return User(img=self.img, desc=self.desc, private=self.private, created=self.created)

#TODO maps comments object from pydantic to comments entity in database
#TODO maps challenges object fromo pydantic to challenges entity in database
