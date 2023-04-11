from pydantic import BaseModel
from datetime import datetime

#User object
class User(BaseModel):
    email: str 
    displayName: str
    password: str
    created: datetime
    private: bool
    bio: str = ""
    pronouns: str = ""
    pfp: str = ""
    userPosts: list['Post'] = []
    savedChallenges: list['Challenge'] = []
    savedPosts: list['Post'] = []
    connectedAccounts: list[str] = []
    class Config:
        orm_mode = True

# Python... :sob:... necessary due to circularity (TODO: refactor to remove circularity)
from .challenge import Challenge
from .post import Post
User.update_forward_refs()