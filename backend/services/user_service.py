from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import User
from ..entities import UserEntity


class UserService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def all(self) -> list[User]:
        query = select(UserEntity)
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]

    def create(self, user: User) -> User:
        temp = self._session.get(UserEntity, user.email)
        if temp:
            raise ValueError(f"Duplicate PID: {temp.email}")
        else:
            user_entity: UserEntity = UserEntity.from_model(user)
            self._session.add(user_entity)
            self._session.commit()
            return user_entity.to_model() 
            

    def get(self, email: str) -> User | None:
        # 
        user = self._session.get(UserEntity, email)
        if user:
            return user.to_model()
        else:
            raise ValueError(f"No user found with PID: {email}")

    def delete(self, email: str) -> User:
        # 
        user = self._session.get(UserEntity, email)
        if user:
            self._session.delete(user)
            self._session.commit()
            return user
        else:
            raise ValueError(f"No user found with PID: {email}")

    def update(self, user: User) -> User:
        temp = self._session.get(UserEntity, user.email)
        if temp:
            #update value
            temp.img = user.img
            temp.bio = user.bio
            temp.displayName = user.displayName
            temp.password = user.password
            temp.private = user.private
            temp.pronouns = user.pronouns
            temp.connectedAccounts = user.connectedAccounts
            self._session.commit()
            return temp.to_model()
        else:
            raise ValueError(f"No user found with PID: {temp.email}")