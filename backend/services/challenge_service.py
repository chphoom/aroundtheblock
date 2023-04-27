from fastapi import Depends
from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import Challenge
from ..entities import ChallengeEntity
from .generator import generate
from datetime import datetime, timedelta


class ChallengeService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def all(self) -> list[Challenge]:
        query = select(ChallengeEntity)
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]

    def allwe(self) -> list[Challenge]:
        query = select(ChallengeEntity).where(ChallengeEntity.type == 'we')
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]

    def allme(self) -> list[Challenge]:
        query = select(ChallengeEntity).where(ChallengeEntity.type == 'me')
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]
    
    def currwe(self) -> Challenge:
        query = select(ChallengeEntity).where(ChallengeEntity.start <= datetime.now())
        entities = self._session.scalars(query).all()
        for e in entities:
            if e.end >= datetime.now():
                return e.to_model()

    def create(self, challenge: Challenge, options: list) -> Challenge:
        temp = self._session.get(ChallengeEntity, challenge.id)
        if temp:
            raise ValueError(f"Duplicate Challenge: {temp.id}")
        else:
            temp = generate(options[0], options[1], options[2], options[3], options[4], options[5])
            challenge.noun = temp.noun
            challenge.verb = temp.verb
            challenge.adj = temp.adj
            challenge.emotion = temp.emotion
            challenge.style = temp.style
            challenge.colors = temp.colors
            challenge_entity: ChallengeEntity = ChallengeEntity.from_model(challenge)
            self._session.add(challenge_entity)
            self._session.commit()
            return challenge_entity.to_model()

    def current(self) -> Challenge:
        return self._session.query(ChallengeEntity).order_by(ChallengeEntity.end.desc()).first()

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

    def search(self, query: str) -> list[Challenge] | None:      
        statement = select(ChallengeEntity)
        criteria = or_(
            ChallengeEntity.noun.ilike(f'%{query}%'),
            ChallengeEntity.verb.ilike(f'%{query}%'),
            ChallengeEntity.emotion.ilike(f'%{query}%'),
            ChallengeEntity.style.ilike(f'%{query}%'),
            func.array_to_string(ChallengeEntity.colors, ',').ilike(f'%{query}%')
        )
        statement = statement.where(criteria).limit(25)
        entities = self._session.execute(statement).scalars()
        return [entity.to_model() for entity in entities]
