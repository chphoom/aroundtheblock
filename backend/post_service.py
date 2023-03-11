from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import db_session
from models import Post
from entities import PostEntity, ChallengeEntity, UserEntity
from user_service import UserService

class PostService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def all(self) -> list[Post]:
        query = select(PostEntity)
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]
            
    def get(self, id: int) -> Post | None:
        # 
        post = self._session.get(PostEntity, id)
        if post:
            return post.to_model()
        else:
            raise ValueError(f"Post not found")

    def delete(self, id: int) -> Post:
        # 
        post = self._session.get(PostEntity, id)
        if post:
            self._session.delete(post)
            self._session.commit()
            return post
        else:
            raise ValueError(f"No post found")

    # def update(self, user: User) -> User:
    #     temp = self._session.get(UserEntity, user.email)
    #     if temp:
    #         #update value
    #         temp.img = user.img
    #         temp.bio = user.bio
    #         temp.displayName = user.displayName
    #         temp.password = user.password
    #         temp.private = user.private
    #         temp.pronouns = user.pronouns
    #         temp.connectedAccounts = user.connectedAccounts
    #         self._session.commit()
    #         return temp.to_model()
    #     else:
    #         raise ValueError(f"No user found with PID: {temp.email}")
