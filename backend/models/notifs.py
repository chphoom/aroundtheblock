from pydantic import BaseModel
from datetime import datetime

class Notif(BaseModel):
    id: int | None = None
    toUser_id: str = ""
    fromUser_id: str | None = None
    comment_id: int | None = None
    last_read: datetime | None = None
    challenge_id: int | None = None
    read: bool = False
    class Config:
        orm_mode = True
    

Notif.update_forward_refs()