from ..services.generator import generateWe
from sqlalchemy import func, select
from sqlalchemy.orm import Session, subqueryload
from ..database import engine
from ..models import Challenge
from ..entities import ChallengeEntity, UserEntity
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

# print("Starting the APScheduler task...")

session = Session(engine)

# INTERVAL = 60 * 5 # five minutes for demo

def new():
    c: Challenge = generateWe()
    c.start = datetime.now()
    c.end = c.start + timedelta(days=7) #normal weekly
    # c.end = c.start + timedelta(seconds=INTERVAL) # demo
    c_entity: ChallengeEntity = ChallengeEntity.from_model(c)
    session.add(c_entity)
    session.commit()

def clean():
    # Define a subquery that selects only the ChallengeEntity objects that satisfy the required conditions
    subq = (
        session.query(ChallengeEntity)
        .filter(
            ChallengeEntity.type == 'me',
            func.array_length(ChallengeEntity.posts, 1) == 0
        )
        .subquery()
    )

    # Use the subquery as the filter for the any method
    query = (
        session.query(UserEntity)
        .options(subqueryload(UserEntity.savedChallenges).subquery(subq))
        .filter(UserEntity.savedChallenges.any())
    )
    
    entities = query.all()
    print([entity.to_model() for entity in entities])

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(new, 'interval', days=7, next_run_time=datetime.now()) # normal weekly challenges
scheduler.add_job(clean, 'interval', seconds=60, next_run_time=datetime.now()) 
# scheduler.add_job(new, 'interval', seconds=INTERVAL, next_run_time=datetime.now()) # demo five min challenges