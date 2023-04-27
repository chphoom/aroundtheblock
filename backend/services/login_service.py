from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import User, Token
from ..entities import UserEntity
from ..env import getenv
from datetime import datetime, timedelta
from typing import Optional
import jwt

SECRET_KEY = getenv('JWT_SECRET')
ALGORITHM = 'HS256'

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
        # email could be the display name i'm just too lazy to change the variabel names
        if "@" in email:
            user = self._session.get(UserEntity, email)
        else:
            user = self._session.query(UserEntity).filter_by(displayName=email).one()
        if not user:
            raise ValueError(f"No user found with that email and password combination.")
        if not password == user.password:
            raise ValueError(f"Passwords do not match")
        return user

    # Create the JWT access token
    def create_access_token(self, email: str, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = {"sub": email}
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(hours=24)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def decode(self, token: Token) -> dict:
        return jwt.decode(token, SECRET_KEY, ALGORITHM)