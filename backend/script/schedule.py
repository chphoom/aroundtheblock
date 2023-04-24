from ..services.generator import generateWe
from sqlalchemy.orm import Session
from ..database import engine
from ..models import Challenge
from ..entities import ChallengeEntity
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

# print("Starting the APScheduler task...")

session = Session(engine)

INTERVAL = 60 # five minutes for demo

def new():
    c: Challenge = generateWe()
    c.start = datetime.now()
    # c.end = c.start + timedelta(days=7) #normal weekly
    c.end = c.start + timedelta(seconds=INTERVAL) # demo
    c_entity: ChallengeEntity = ChallengeEntity.from_model(c)
    session.add(c_entity)
    session.commit()

scheduler = BackgroundScheduler(daemon=True)
# scheduler.add_job(new, 'interval', days=7, next_run_time=datetime.now()) # normal weekly challenges
scheduler.add_job(new, 'interval', seconds=INTERVAL, next_run_time=datetime.now()) # demo five min challenges