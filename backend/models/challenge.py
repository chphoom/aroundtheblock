from pydantic import BaseModel
from datetime import datetime

#: Challenges
class Challenge(BaseModel):
    id: int | None
    posts: list['Post'] = []
    noun: str = ""
    verb: str = ""
    adj: str = ""
    emotion: str = ""
    style: str = ""
    colors: list[str] = []
    class Config:
        orm_mode = True

class weChallenge(Challenge):
    start: datetime | None
    end: datetime | None
 
class meChallenge(Challenge):
    createdBy: int | None

# copied fro professor's databse code at the end of User Model.. Assuming theres some importance here
# Python... :sob:... necessary due to circularity (TODO: refactor to remove circularity)
from .post import Post
Challenge.update_forward_refs()