from pydantic import BaseModel

class User(BaseModel):
    pid: int 
    first_name: str
    last_name: str
    class Config:
        orm_mode = True