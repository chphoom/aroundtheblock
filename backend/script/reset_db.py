from sqlalchemy.orm import Session
from ..database import engine
from .. import entities

# Reset Tables
entities.EntityBase.metadata.drop_all(engine)
entities.EntityBase.metadata.create_all(engine)

# Enter Mock Data
with Session(engine) as session:
    # : Add a UserEntity to the database session and commit it.
    from datetime import datetime
    user_entity: entities.UserEntity = entities.UserEntity.from_model(entities.User(email="keaw@email.unc.com", displayName="keaw",password="4ho00o76i1", created=datetime.now(), private=True, bio="", pronouns="they/them", img="", userPosts=[], connectedAccounts=[], savedPosts=[], savedChallenges=[]))
    session.add(user_entity)
    session.commit()