from pydantic import BaseModel
from datetime import datetime

#User object
class User(BaseModel):
    email: str 
    displayName: str
    password: str
    created: datetime
    private: bool
    bio: str
    pronouns: str
    img: str
    class Config:
        orm_mode = True