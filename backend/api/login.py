import jwt
from fastapi import APIRouter, HTTPException, Depends, Response, Header
from fastapi.security import OAuth2PasswordRequestForm
from ..env import getenv
from ..models import User
from ..services import UserService
from datetime import timedelta, datetime
from typing import Optional

# Define the JWT token schema
from pydantic import BaseModel
class Token(BaseModel):
    access_token: str
    token_type: str


_JWT_SECRET = getenv('JWT_SECRET')
_JST_ALGORITHM = 'HS256'


api = APIRouter()

#-----------JWT TOKENS (for login) ---------

#Define function to get user from token
@api.get("/api/login")
def get_token_info(authorization: str = Header(None), user_service: UserService = Depends()) -> User:
    if authorization is None:
        raise HTTPException(status_code=401, detail='Authorization header missing')
    try:
        token = authorization.split(' ')[1]
        decoded_token = decode(token=token)
        # Extract user data from the decoded token here
        user_email = decoded_token['sub']
        user = user_service.get(user_email)
    except:
        raise HTTPException(status_code=401, detail='Invalid authorization token')
    return user

def decode(token: Token) -> dict:
    return jwt.decode(token, _JWT_SECRET, _JST_ALGORITHM)

# Define the login route
@api.post("/api/login")
async def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    _access_token = create_access_token(expires_delta=timedelta(hours=15), email=user.email)
    response.set_cookie(key="access_token", value=_access_token, httponly=True, max_age=3600, expires=3600, path="/")

    return {"access_token": _access_token, "token_type": "bearer"}

# Authenticate the user
def authenticate_user(email: str, password: str, user_service: UserService = Depends()) -> Optional[User]:
    user = user_service.get(email)
    if not user:
        raise ValueError(f"No user found with that email and password combination.")
    if not password == user.password:
        raise ValueError(f"Passwords do not match")
    return user

# Create the JWT access token
def create_access_token(email: str, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = {"sub": email}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, _JWT_SECRET, algorithm=_JST_ALGORITHM)
    return encoded_jwt