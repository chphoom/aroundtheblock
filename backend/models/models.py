from pydantic import BaseModel
from datetime import datetime
from typing import List

#User object
class User(BaseModel):
    email: str 
    displayName: str
    password: str
    created: datetime
    private: bool
    bio: str | None
    pronouns: str | None
    img: str | None
    userPosts: List | None
    savedChallenges: List | None
    savedPosts: List | None
    connectedAccounts: List[str] | None
    class Config:
        orm_mode = True

#: Challenges
class Challenge(BaseModel):
    id: int | None
    posts: List
    noun: str | None
    verb: str | None
    adj: str | None
    emotion: str | None
    style: str | None
    colors: List[str] | None
    class Config:
        orm_mode = True

class weChallenge(Challenge):
    start: datetime
    end: datetime

class meChallenge(Challenge):
    createdBy: User

#: Post object
class Post(BaseModel):
    id: int | None
    img: str
    desc: str
    private: bool
    created: datetime
    challenge: Challenge | str | None
    postedBy: User | str | None
    comments: List
    tags: List[str]
    class Config:
        orm_mode = True

#: Comments
class Comment(BaseModel):
    id: int | None
    commenter: User | str
    post: Post | int
    replies: List | None
    text: str
    created: datetime
    class Config:
        orm_mode = True

# Define the JWT token schema
class Token(BaseModel):
    access_token: str
    token_type: str