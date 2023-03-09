from pydantic import BaseModel
from datetime import datetime

#User object
class User(BaseModel):
    email: str 
    displayName: str
    password: str
    created: datetime
    class Config:
        orm_mode = True