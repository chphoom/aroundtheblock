from pydantic import BaseModel
from datetime import datetime, timedelta

#: Challenges
class Challenge(BaseModel):
    id: int | None
    posts: list = []
    noun: str = ""
    verb: str = ""
    adj: str = ""
    emotion: str = ""
    style: str = ""
    colors: list[str] = []
# class weChallenge(Challenge):
    start: datetime | None #= datetime.now()
    end: datetime | None #= start + timedelta(days=7)
# class meChallenge(Challenge):
    createdBy: str | None
    class Config:
        orm_mode = True

    def getType(self) -> str:
        if self.start != None and self.end != None:
            return "we"
        elif self.createdBy != None:
            return "me"
        else:
            return "generic"

# copied fro professor's databse code at the end of User Model.. Assuming theres some importance here
# Python... :sob:... necessary due to circularity (TODO: refactor to remove circularity)
from .post import Post
Challenge.update_forward_refs()