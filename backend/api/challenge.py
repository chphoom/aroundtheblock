from fastapi import APIRouter, HTTPException, Depends
from ..services import ChallengeService
from ..models import Challenge
from apscheduler.schedulers.blocking import BlockingScheduler
import asyncio
import httpx


api = APIRouter()

# ----------CHALLENGE API ROUTES----------------
# @api.post("/api/test")
# def test(challenge: Challenge, test: list, challenge_service: ChallengeService = Depends()) -> Challenge:
#     print(test)
#     try:
#         return challenge_service.create(challenge, test)
#     except Exception as e:
#         raise HTTPException(status_code=422, detail=str(e))

#api route retrieves ALL challenges
@api.get("/api/challenges")
def get_challenges(challenge_service: ChallengeService = Depends()) -> list[Challenge]:
    return challenge_service.all()

#api route retrieves all weChallenges
@api.get("/api/wechallenges")
def get_wechallenges(challenge_service: ChallengeService = Depends()) -> list[Challenge]:
    return challenge_service.allwe()

#api route retrieves all meChallenges
@api.get("/api/mechallenges")
def get_mechallenges(challenge_service: ChallengeService = Depends()) -> list[Challenge]:
    return challenge_service.allme()

#api route retrieves current weChallenge
@api.get("/api/current")
def get_current_wechallenge(challenge_service: ChallengeService = Depends()) -> Challenge:
    return challenge_service.currwe()

#api route registers a new challenge
@api.post("/api/generate")
def new_challenge(challenge: Challenge, options: list[bool], challenge_service: ChallengeService = Depends()) -> Challenge:
    try:
        return challenge_service.create(challenge, options)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
        
#api route retrieves challenge given id
#TODO: implement a way to find challenge and get the correct id
@api.get("/api/challenges/{id}", responses={404: {"model": None}})
def get_challenge(id: int, challenge_service: ChallengeService = Depends()) -> Challenge:
    try: 
        return challenge_service.get(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
#api route deletes challenge FROM THE DATABASE
@api.delete("/api/delete/challenges/{id}")
def delete_challenge(id: int, challenge_service = Depends(ChallengeService)) -> Challenge:
    try:
        return challenge_service.delete(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

async def create_new_wechallenge():
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:1560/api/generate", 
            json={ 
            "challenge": {
                "id": 0,
                "posts": [],
                "noun": "",
                "verb": "",
                "adj": "",
                "emotion": "",
                "style": "",
                "colors": [],
                "start": "2023-04-18T00:27:58.223Z",
                "end": "2023-04-18T00:27:58.223Z",
                "createdBy": "string"
            }, "options": [True, True, True, False, False, False]})
        response.raise_for_status()

scheduler = BlockingScheduler()
scheduler.add_job(create_new_wechallenge, 'interval', seconds=30)
scheduler.start()