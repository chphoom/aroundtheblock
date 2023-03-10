"""Definitions of SQLAlchemy table-backed object mappings called entities."""


from sqlalchemy import String, DateTime, Boolean, ForeignKey, ARRAY, Integer, Column, Table
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy.ext.mutable import MutableList
from typing import Self, List
from models import User, Post, Challenge, Comment, weChallenge, meChallenge
from datetime import datetime


class Base(DeclarativeBase):
    pass

#savedPost relationship
savedPost = Table(
    "savedPost association table",
    Base.metadata,
    Column("users", ForeignKey("users.email")),
    Column("posts", ForeignKey("posts.id"))
)

#savedChallenge relationship
savedChallenge = Table(
    "savedChallenge association table",
    Base.metadata,
    Column("users", ForeignKey("users.email")),
    Column("challenges", ForeignKey("challenges.id"))
)

#challenge -> posts relationship
c2p = Table (
    "c2p association table",
    Base.metadata,
    Column("challenges", ForeignKey("challenges.id")),
    Column("posts", ForeignKey("posts.id"))
)

#comment reply
comment_reply_assoc = Table("comment_reply_assoc", Base.metadata,
    Column('comment_id', Integer, ForeignKey('comments.id')),
    Column('reply_id', Integer, ForeignKey('comments.id'))
)

#maps user object fromo pydantic to user entity in database
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
    userPosts: Mapped[list["PostEntity"]] = relationship(back_populates="postedBy")
    savedPosts: Mapped[list["PostEntity"]] = relationship(secondary=savedPost)
    savedChallenges: Mapped[list["ChallengeEntity"]] = relationship(secondary=savedChallenge)
    connectedAccounts: Mapped[list[str]] = mapped_column(MutableList.as_mutable(ARRAY(String(64))))

    @classmethod
    def from_model(cls, model: User) -> Self:
        return cls(email=model.email, displayName=model.displayName, password=model.password, created=model.created, private=model.private, bio=model.bio, pronouns=model.pronouns, img=model.img, userPosts=model.userPosts, connectedAccounts=model.connectedAccounts, savedPosts=model.savedPosts,  savedChallenges=model.savedChallenges)

    def to_model(self) -> User:
        return User(email=self.email, displayName=self.displayName, password=self.password, created=self.created, private=self.private, bio=self.bio, pronouns=self.pronouns, img=self.img, userPosts=self.userPosts, connectedAccounts=self.connectedAccounts, savedPosts=self.savedPosts, savedChallenges=self.savedChallenges)

# maps challenges object fromo pydantic to challenges entity in database
class ChallengeEntity(Base):
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
        return cls(posts=model.posts, noun=model.noun, verb=model.verb, adj=model.adj, emotion=model.emotion, style=model.style, colors=model.colors)

    def to_model(self) -> Challenge:
        return Challenge(id=self.id, posts=self.posts, noun=self.noun, verb=self.verb, adj=self.adj, emotion=self.emotion, style=self.style, colors=self.colors)

# class weChallengeEntity(ChallengeEntity):
#     start: Mapped[datetime] = mapped_column(DateTime)
#     end: Mapped[datetime] = mapped_column(DateTime)

# class meChallengeEntity(ChallengeEntity):
#     createdBy: Mapped[UserEntity] = relationship()

# maps post object from pydantic to post entity in database
class PostEntity(Base):
    __tablename__ = "posts"

    id = mapped_column(Integer, primary_key=True)
    img: Mapped[str] = mapped_column(String(64))
    desc: Mapped[str] = mapped_column(String(64))
    private: Mapped[bool] = mapped_column(Boolean)
    created: Mapped[datetime] = mapped_column(DateTime)
    user_id = mapped_column(ForeignKey("users.email"))
    postedBy: Mapped[UserEntity] = relationship(back_populates="userPosts", post_update=True)
    comments: Mapped[list["CommentEntity"]] = relationship(back_populates="post")
    tags: Mapped[list[str]] = mapped_column(MutableList.as_mutable(ARRAY(String(64))))
    challenge_id = mapped_column(ForeignKey("challenges.id"))
    challenge: Mapped[ChallengeEntity] = relationship(back_populates="posts", post_update=True)

    @classmethod
    def from_model(cls, model: Post) -> Self:
        return cls(id=model.id, img=model.img, desc=model.desc, private=model.private, created=model.created, postedBy=model.postedBy, comments=model.comments, challenge=model.challenge, tags=model.tags)

    def to_model(self) -> Post:
        #TODO: update logic to output name of the challenge
        return Post(id=self.id, img=self.img, desc=self.desc, private=self.private, created=self.created, postedBy=self.user_id, comments=self.comments, challenge=self.challenge.noun, tags=self.tags)

# maps comments object from pydantic to comments entity in database
class CommentEntity(Base):
    __tablename__ = "comments"

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey("users.email"))
    commenter: Mapped[UserEntity] = relationship(post_update=True)
    post_id = mapped_column(ForeignKey("posts.id"))
    post: Mapped[PostEntity] = relationship(back_populates="comments", post_update=True)
    replyTo_id = mapped_column(ForeignKey("comments.id"))
    replies: Mapped[list["CommentEntity"]] = relationship(secondary="comment_reply_assoc", primaryjoin=id==comment_reply_assoc.c.comment_id,
                            secondaryjoin=id==comment_reply_assoc.c.reply_id, back_populates="replies", post_update=True)
    text: Mapped[str] = mapped_column(String(64))
    created: Mapped[datetime] = mapped_column(DateTime)

    @classmethod
    def from_model(cls, model: Comment) -> Self:
        return cls(commenter=model.commenter, post=model.post, text=model.text, created=model.created)
    
    def to_model(self) -> Comment:
        return Comment(id=self.id, commenter=self.user_id, post=self.post_id, text=self.text, created=self.created)
