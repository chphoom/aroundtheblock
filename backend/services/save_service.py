from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import User
from ..entities import ChallengeEntity, UserEntity, PostEntity

class SaveService: 

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def saveChallenge(self, email: str, challenge_id: int) -> User:
        user = self._session.get(UserEntity, email)
        if user:
            challenge = self._session.get(ChallengeEntity, challenge_id)
            if challenge:
                user.savedChallenges.append(challenge)
                # self._session.add(user)
                self._session.commit()
                return user.to_model()
            else:
                raise ValueError(f"No challenge found with id: {challenge_id}")
        else:
            raise ValueError(f"No user found with email: {email}")

    def savePost(self, email: str, post_id: int) -> User:
        user = self._session.get(UserEntity, email)
        if user:
            post = self._session.get(PostEntity, post_id)
            if post:
                user.savedPosts.append(post)
                # self._session.add(user)
                self._session.commit()
                return user.to_model()
            else:
                raise ValueError(f"No post found with id: {post_id}")
        else:
            raise ValueError(f"No user found with email: {email}")

