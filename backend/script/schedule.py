from ..services.generator import generate
from sqlalchemy.orm import Session
from ..database import engine
from ..models import Challenge
from ..entities import ChallengeEntity
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

# print("Starting the APScheduler task...")

session = Session(engine)

INTERVAL = 60

def new():
    # print("Entered schedule function")
    c: Challenge = generate(True, True, True, False, False, False)
    c.start = datetime.now()
    c.end = c.start + timedelta(seconds=INTERVAL)
    c_entity: ChallengeEntity = ChallengeEntity.from_model(c)
    session.add(c_entity)
    session.commit()
    # print("Session committed")

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(new, 'interval', seconds=INTERVAL) # Run the task every 5 seconds