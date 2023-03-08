import database
from entities import Base, UserEntity

# Reset Tables
Base.metadata.drop_all(database.engine)
Base.metadata.create_all(database.engine)

# Enter Mock Data
from sqlalchemy.orm import Session
session = Session(database.engine)

# : Add a UserEntity to the database session and commit it.
from models import User
user_entity: UserEntity = UserEntity.from_model(User(pid=730439634, first_name="Chalisa",last_name="Phoomsakha"))
session.add(user_entity)
session.commit()