import database
from typing import List
from entities import Base, UserEntity

# Reset Tables
Base.metadata.drop_all(database.engine)
Base.metadata.create_all(database.engine)

# Enter Mock Data
from sqlalchemy.orm import Session
session = Session(database.engine)

# : Add a UserEntity to the database session and commit it.
from models import User, Post
from datetime import datetime
user_entity: UserEntity = UserEntity.from_model(User(email="keaw@email.unc.com", displayName="keaw",password="4ho00o76i1", created=datetime.now(), private=True, bio="", pronouns="they/them", img="", userPosts=[], connectedAccounts=[], savedPosts=[], savedChallenges=[]))
session.add(user_entity)
session.commit()