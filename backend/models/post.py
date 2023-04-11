from pydantic import BaseModel
from datetime import datetime

#: Post object
class Post(BaseModel):
    id: int | None
    img: str = ""
    desc: str = ""
    private: bool
    created: datetime = datetime.now()
    challenge: int | None
    postedBy: str | None
    comments: list['Comment'] = []
    tags: list[str] = []
    class Config:
        orm_mode = True

# copied fro professor's databse code at the end of User Model.. Assuming theres some importance here
# Python... :sob:... necessary due to circularity (TODO: refactor to remove circularity)
# from .user import User
from .comment import Comment
Post.update_forward_refs()