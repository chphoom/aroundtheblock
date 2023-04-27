from fastapi import Depends
from sqlalchemy import select, func
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import Notif
from ..entities import CommentEntity, ChallengeEntity, UserEntity, NotifEntity
from sqlalchemy.sql.expression import and_
from datetime import datetime

class NotifService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def all(self) -> list[Notif]:
        query = select(NotifEntity)
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]
    
    def create(self, notif: Notif) -> Notif:
        toUser = self._session.get(UserEntity, notif.toUser_id)
        if toUser:
            comment = self._session.get(CommentEntity, notif.comment_id)
            challenge = self._session.get(ChallengeEntity, notif.challenge_id)
            if comment:
                fromUser = self._session.get(UserEntity, notif.fromUser_id)
                if fromUser:
                    new_entity: NotifEntity = NotifEntity.from_model(notif)
                    self._session.add(new_entity)
                    self._session.commit()
                    return new_entity.to_model()
                else:
                    raise ValueError(f"No user found with email: {notif.fromUser_id}")
            elif challenge:
                new_entity: NotifEntity = NotifEntity.from_model(notif)
                self._session.add(new_entity)
                self._session.commit()
                return new_entity.to_model()
            else:
                raise ValueError(f"No comment found with id: {notif.comment_id} and no challenge found with id: {notif.challenge_id}")
        else:
            raise ValueError(f"No user found with email: {notif.toUser_id}")
            
    def get(self, id: int) -> Notif | None:
        notif = self._session.get(NotifEntity, id)
        if notif:
            return notif.to_model()
        else:
            raise ValueError(f"Notification not found")

    def delete(self, id: int) -> Notif:
        notif = self._session.get(NotifEntity, id)
        if notif:
            self._session.delete(notif)
            self._session.commit()
            return notif
        else:
            raise ValueError(f"No notification found")
    
    def get_by_toUser(self, email: str) -> list[Notif]:
        statement = select(NotifEntity).where(NotifEntity.toUser_id == email).limit(25)
        entities = self._session.execute(statement).scalars()
        return [entity.to_model() for entity in entities]

    
    def get_by_fromUser(self, email: str) -> list[Notif]:
        statement = select(NotifEntity).where(NotifEntity.fromUser_id == email).limit(25)
        entities = self._session.execute(statement).scalars()
        return [entity.to_model() for entity in entities]

    def read(self, notification_id: int) -> Notif:
        notif = self._session.get(NotifEntity, notification_id)
        if notif:
            notif.last_read = datetime.now()
            notif.read = True
            self._session.commit()
            return notif.to_model()
        else:
            raise ValueError(f"No notification found")

    def unread(self, notification_id: int) -> Notif:
        notif = self._session.get(NotifEntity, notification_id)
        if notif:
            notif.last_read = datetime.now()
            notif.read = False
            self._session.commit()
            return notif.to_model()
        else:
            raise ValueError(f"No notification found")
