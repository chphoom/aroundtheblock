from fastapi import Depends
from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import User
from ..entities import UserEntity
from sqlalchemy.orm.exc import NoResultFound


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
        
    def getbyName(self, name: str) -> User | None:
        try:
            user_entity = self._session.query(UserEntity).filter_by(displayName=name).one()
            return user_entity.to_model()
        except NoResultFound:
            raise ValueError(f"No user found with display name: {name}")

    def delete(self, email: str) -> User:
        # 
        user = self._session.get(UserEntity, email)
        if user:
            self._session.delete(user)
            self._session.commit()
            return user
        else:
            raise ValueError(f"No user found with PID: {email}")

    def update(self, email: str, 
                    pronouns: str | None = None,
                    displayName: str | None = None, 
                    private: bool | None = None, 
                    pfp: str | None = None, 
                    bio: str | None = None, 
                    connectedAccounts: list[str] | None = None,) -> User:
            temp = self._session.get(UserEntity, email)
            if temp:
                if pronouns != None:
                    temp.pronouns = pronouns
                if displayName != None:
                    temp.displayName = displayName
                if private != None:
                    temp.private = private
                if pfp != None:
                    temp.pfp = pfp
                if bio != None:
                    temp.bio = bio
                if connectedAccounts != None:
                    temp.connectedAccounts = connectedAccounts
                self._session.commit()
                return temp.to_model()
            else:
                raise ValueError(f"No user found with email: {temp.email}")
            
    def search(self, query: str) -> list[User] | None:      
        statement = select(UserEntity)
        criteria = or_(
            UserEntity.email.ilike(f'%{query}%'),
            UserEntity.displayName.ilike(f'%{query}%'),
            UserEntity.bio.ilike(f'%{query}%'),
            func.array_to_string(UserEntity.connectedAccounts, ',').ilike(f'%{query}%')
        )
        statement = statement.where(criteria).limit(25)
        entities = self._session.execute(statement).scalars()
        return [entity.to_model() for entity in entities]