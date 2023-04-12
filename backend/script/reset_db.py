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

# Add Challenges
with Session(engine) as session:
    from .devdata import challenges
    to_entity = entities.ChallengeEntity.from_model
    session.add_all([to_entity(model) for model in challenges.models])
    # session.execute(text(f'ALTER SEQUENCE {entities.ChallengeEntity.__table__}_id_seq RESTART WITH {len(challenges.models) + 1}'))
    session.commit()

# Add Post
with Session(engine) as session:
    from .devdata import posts
    to_entity = entities.PostEntity.from_model
    for model in posts.models:
        user = session.get(entities.UserEntity, model.postedBy)
        # model.postedBy = user
        challenge = session.get(entities.ChallengeEntity, model.challenge)
        # model.challenge = challenge
        e = to_entity(model)
        user.userPosts.append(e)
        challenge.posts.append(e)
        session.add(e)
        session.add(user)
        session.add(challenge)
    # session.execute(text(f'ALTER SEQUENCE {entities.PostEntity.__table__}_id_seq RESTART WITH {len(posts.models) + 1}'))
    session.commit()


# # Enter Mock User Data
# with Session(engine) as session:
#     from datetime import datetime, timedelta
#     session.commit()