'''User accounts for all registered users in the application.'''

from sqlalchemy import String, DateTime, Boolean, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.mutable import MutableList
from typing import Self
from .entity_base import EntityBase
from .savedPost_entity import savedPost
from .savedChallenge_entity import savedChallenge
from ..models import User
from datetime import datetime

#maps user object fromo pydantic to user entity in database
class UserEntity(EntityBase):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(64), primary_key=True)
    displayName: Mapped[str] = mapped_column(String(64))
    password: Mapped[str] = mapped_column(String(64))
    created: Mapped[datetime] = mapped_column(DateTime)
    private: Mapped[bool] = mapped_column(Boolean)
    bio: Mapped[str] = mapped_column(String(256))
    pronouns: Mapped[str] = mapped_column(String(64))
    img: Mapped[str] = mapped_column(String(64))
    userPosts: Mapped[list["PostEntity"]] = relationship(back_populates="postedBy")
    savedPosts: Mapped[list["PostEntity"]] = relationship(secondary=savedPost)
    savedChallenges: Mapped[list["ChallengeEntity"]] = relationship(secondary=savedChallenge)
    connectedAccounts: Mapped[list[str]] = mapped_column(MutableList.as_mutable(ARRAY(String(64))))

    @classmethod
    def from_model(cls, model: User) -> Self:
        return cls(
            email=model.email, 
            displayName=model.displayName, 
            password=model.password, 
            created=model.created, 
            private=model.private, 
            bio=model.bio, 
            pronouns=model.pronouns, 
            img=model.img, 
            userPosts=model.userPosts, 
            connectedAccounts=model.connectedAccounts, 
            savedPosts=model.savedPosts,  
            savedChallenges=model.savedChallenges)

    def to_model(self) -> User:
        return User(
            email=self.email, 
            displayName=self.displayName, 
            password=self.password, 
            created=self.created, 
            private=self.private, 
            bio=self.bio, 
            pronouns=self.pronouns, 
            img=self.img, 
            userPosts=self.userPosts, 
            connectedAccounts=self.connectedAccounts, 
            savedPosts=self.savedPosts, 
            savedChallenges=self.savedChallenges)
