from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import db_session
from models import Challenge, meChallenge, weChallenge
from entities import ChallengeEntity


class ChallengeService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def all(self) -> list[Challenge]:
        query = select(ChallengeEntity)
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]

    def create(self, challenge: Challenge) -> Challenge:
        temp = self._session.get(ChallengeEntity, challenge.id)
        if temp:
            raise ValueError(f"Duplicate Challenge: {temp.id}")
        else:
            challenge_entity: ChallengeEntity = ChallengeEntity.from_model(challenge)
            self._session.add(challenge_entity)
            self._session.commit()
            return challenge_entity.to_model() 
            
    def get(self, id: int) -> Challenge | None:
        challenge = self._session.get(ChallengeEntity, id)
        if challenge:
            return challenge.to_model()
        else:
            raise ValueError(f"Challenge not found.")

    def delete(self, id: int) -> Challenge:
        # 
        challenge = self._session.get(ChallengeEntity, id)
        if challenge:
            self._session.delete(challenge)
            self._session.commit()
            return challenge
        else:
            raise ValueError(f"Challenge not Found")

    # def update(self, challenge: Challenge) -> Challenge:
    #     temp = self._session.get(ChallengeEntity, challenge.id)
    #     if temp:
    #         #update value
    #         temp.img = challenge.img
    #         temp.bio = challenge.bio
    #         temp.displayName = challenge.displayName
    #         temp.password = challenge.password
    #         temp.private = challenge.private
    #         temp.pronouns = challenge.pronouns
    #         temp.connectedAccounts = challenge.connectedAccounts
    #         self._session.commit()
    #         return temp.to_model()
    #     else:
    #         raise ValueError(f"No challenge found with ID: {challenge.id}")
