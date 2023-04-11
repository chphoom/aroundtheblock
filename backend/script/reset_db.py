from sqlalchemy import text
from sqlalchemy.orm import Session
from ..database import engine
from .. import entities
from .. import models

# Reset Tables
entities.EntityBase.metadata.drop_all(engine)
entities.EntityBase.metadata.create_all(engine)



# Add Users
with Session(engine) as session:
    from .devdata import users
    to_entity = entities.UserEntity.from_model
    session.add_all([to_entity(model) for model in users.models])
    # session.execute(text(f'ALTER SEQUENCE {entities.UserEntity.__table__}_id_seq RESTART WITH {len(users.models) + 1}'))
    session.commit()

# Add Post
with Session(engine) as session:
    from .devdata import posts
    to_entity = entities.PostEntity.from_model
    session.add_all([to_entity(model) for model in posts.models])
    session.execute(text(f'ALTER SEQUENCE {entities.PostEntity.__table__}_id_seq RESTART WITH {len(users.models) + 1}'))
    session.commit()


# Enter Mock User Data
with Session(engine) as session:
    from datetime import datetime, timedelta
    challenge_entity: entities.ChallengeEntity = entities.ChallengeEntity.from_model(
        models.Challenge(
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
    session.add(challenge_entity)
    session.commit()