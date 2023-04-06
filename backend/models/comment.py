from pydantic import BaseModel
from datetime import datetime

#: Comments
class Comment(BaseModel):
    id: int | None
    commenter: int
    post: int
    replies: list['Comment'] = []
    text: str = ""
    created: datetime = datetime.now()
    class Config:
        orm_mode = True

# copied from professor's databse code at the end of User Model.. Assuming theres some importance here
# Python... :sob:... necessary due to circularity (TODO: refactor to remove circularity)
# from .user import User
# from .post import Post
Comment.update_forward_refs()