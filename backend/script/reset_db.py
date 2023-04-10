from sqlalchemy.orm import Session
from ..database import engine
from .. import entities
from .. import models

# Reset Tables
entities.EntityBase.metadata.drop_all(engine)
entities.EntityBase.metadata.create_all(engine)

# Enter Mock Data
with Session(engine) as session:
    # : Add a UserEntity to the database session and commit it.
    from datetime import datetime, timedelta
    user_entity: entities.UserEntity = entities.UserEntity.from_model(
        models.User(
            email="keaw@email.unc.com", 
            displayName="keaw",
            password="4ho00o76i1", 
            created=datetime.now(), 
            private=True, 
            bio="", 
            pronouns="they/them", 
            img="", 
            userPosts=[], 
            connectedAccounts=["instagram.com/khaamkeaw", "pinterest.com/twofacedsatyr"], 
            savedPosts=[], 
            savedChallenges=[]))
    challenge_entity: entities.ChallengeEntity = entities.ChallengeEntity.from_model(
        models.weChallenge(
            id=0,
            posts=[],
            noun="bunny",
            verb="jump",
            adj="cute",
            emotion="sad",
            style="realism",
            colors=[],
            start=datetime.now(),
            end=datetime.now() + timedelta(days=7)))
    session.add(user_entity)
    session.add(challenge_entity)
    session.commit()