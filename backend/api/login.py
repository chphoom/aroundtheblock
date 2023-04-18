import jwt
from fastapi import APIRouter, HTTPException, Depends, Response, Header
from fastapi.security import OAuth2PasswordRequestForm
from ..models import User, Token
from ..services import LoginService
from datetime import timedelta, datetime
from typing import Optional

api = APIRouter()

#-----------JWT TOKENS (for login) ---------

#Define function to get user from token
@api.get("/api/login")
def get_token_info(authorization: str = Header(None), login_service: LoginService = Depends()) -> User:
    if authorization is None:
        raise HTTPException(status_code=401, detail='Authorization header missing')
    try:
        token = authorization.split(' ')[1]
        decoded_token = login_service.decode(token=token)
        # Extract user data from the decoded token here
        user_email = decoded_token['sub']
        user = login_service.get(user_email)
    except:
        raise HTTPException(status_code=401, detail='Invalid authorization token')
    return user

# Define the login route
@api.post("/api/login")
async def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends(), login_service: LoginService = Depends()) -> Token:
    user = login_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    _access_token = login_service.create_access_token(expires_delta=timedelta(hours=15), email=user.email)
    response.set_cookie(key="access_token", value=_access_token, httponly=True, max_age=3600, expires=3600, path="/")

    return {"access_token": _access_token, "token_type": "bearer"}