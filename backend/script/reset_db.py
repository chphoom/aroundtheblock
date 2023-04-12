from sqlalchemy import text
from sqlalchemy.orm import Session
from ..database import engine
from .. import entities
from .. import models
import random

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
        user = session.get(entities.UserEntity, model.user_id)
        # model.user_id = user
        challenge = session.get(entities.ChallengeEntity, model.challenge)
        # model.challenge = challenge
        e = to_entity(model)
        user.userPosts.append(e)
        challenge.posts.append(e)
        session.add(e)
        # print(f"e: {e.id} user_id: {e.user_id.displayName}")
        session.add(user)
        session.add(challenge)
        # print(f"challenge: {challenge.id}\n")
        # for i in challenge.posts:
        #     print(f"\t{challenge.posts}")
    # session.execute(text(f'ALTER SEQUENCE {entities.PostEntity.__table__}_id_seq RESTART WITH {len(posts.models) + 1}'))
    session.commit()

# Add Comment
with Session(engine) as session:
    from .devdata import comments
    to_entity = entities.CommentEntity.from_model
    for model in comments.models:
        user = session.get(entities.UserEntity, model.commenter)
        # model.user_id = user
        post = session.get(entities.PostEntity, model.post)
        # model.post = post
        e = to_entity(model)
        post.comments.append(e)
        # print(post.comments)
        session.add(e)
        session.add(user)
        session.add(post)
    # session.execute(text(f'ALTER SEQUENCE {entities.PostEntity.__table__}_id_seq RESTART WITH {len(posts.models) + 1}'))
    session.commit()

# Add Reply
with Session(engine) as session:
    from .devdata import replies
    to_entity = entities.CommentEntity.from_model
    for model in replies.models:
        comment = session.get(entities.CommentEntity,1)
        if comment != None:
            reply = to_entity(model)
            reply.replyTo_id = comment.id
            comment.replies.append(reply)
            session.add(reply)
    # session.execute(text(f'ALTER SEQUENCE {entities.PostEntity.__table__}_id_seq RESTART WITH {len(posts.models) + 1}'))
    session.commit()

# # Enter Mock User Data
# with Session(engine) as session:
#     from datetime import datetime, timedelta
#     session.commit()