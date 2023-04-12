from fastapi import APIRouter, HTTPException, Depends
from ..services import ChallengeService
from ..models import Challenge


api = APIRouter()

# ----------CHALLENGE API ROUTES----------------
#api route retrieves ALL challenges
@api.get("/api/challenges")
def get_challenges(challenge_service: ChallengeService = Depends()) -> list[Challenge]:
    return challenge_service.all()

#api route retrieves all wechallenges
@api.get("/api/wechallenges")
def get_wechallenges(challenge_service: ChallengeService = Depends()) -> list[Challenge]:
    return challenge_service.allwe()

#api route retrieves all mechallenges
@api.get("/api/mechallenges")
def get_mechallenges(challenge_service: ChallengeService = Depends()) -> list[Challenge]:
    return challenge_service.allme()

#api route retrieves all mechallenges
@api.get("/api/current")
def get_current_wechallenge(challenge_service: ChallengeService = Depends()) -> Challenge:
    return challenge_service.currwe()

#api route registers a new challenge
@api.post("/api/challenges")
def new_challenge(challenge: Challenge, challenge_service: ChallengeService = Depends()) -> Challenge:
        try:
            return challenge_service.create(challenge)
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
