from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import db_session
from datetime import datetime, timedelta
from typing import Optional
from ..models import User, Token
from ..entities import UserEntity
from ..config import SECRET_KEY, ALGORITHM
import jwt

class LoginService:
    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def get(self, email: str) -> User | None:
        # 
        user = self._session.get(UserEntity, email)
        if user:
            return user.to_model()
        else:
            raise ValueError(f"No user found with PID: {email}")
        
    # Authenticate the user
    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        user = self._session.get(UserEntity, email)
        if not user:
            raise ValueError(f"No uer found with that email and password combination.")
        if not password == user.password:
            raise ValueError(f"Passwords do not match")
        return user

    # Create the JWT access token
    def create_access_token(self, email: str, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = {"sub": email}
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(hours=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def decode(self, token: Token) -> dict:
        return jwt.decode(token, SECRET_KEY, ALGORITHM)