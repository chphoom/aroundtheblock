from fastapi import APIRouter, HTTPException, Depends
from ..services import ChallengeService
from ..models import Challenge
import requests
import random
from urllib.request import urlopen
import nltk

api = APIRouter()

API_URL = "https://grizzly-fifth-citrine.glitch.me/api"

# test api route... for testing.
@api.get("/api/test")
def test() -> str:
    return noun()

@api.get("/api/noun") # routes are for resting purposes
def noun() -> str:
    params = {"generator": "common-noun", "list": "noun"}
    return requests.get(API_URL, params=params).text

@api.get("/api/verb")
def verb() -> str:
    params = {"generator": "verb", "list": "verb"}
    return requests.get(API_URL, params=params).text

@api.get("/api/adj")
def adj() -> str:
    params = {"generator": "adjective", "list": "adjective"}
    return requests.get(API_URL, params=params).text

@api.get("/api/style")
def style() -> str:
    params = {"generator": "artism", "list": "output"}
    return requests.get(API_URL, params=params).text

@api.get("/api/emotion")
def emotion() -> str:
    params = {"generator": "emotion", "list": "emotion"}
    return requests.get(API_URL, params=params).text

@api.get("/api/emotion")
def emotion() -> str:
    params = {"generator": "emotion", "list": "emotion"}
    return requests.get(API_URL, params=params).text

@api.get("/api/colors")
def colors(number: int | None) -> list:
    if number == None:
        return []
    else:
        params = {"generator": "hex-code-gen", "list": "output"}
        result = []
        for i in range(number):
            result.append(requests.get(API_URL, params=params).text)
        return result

# ----------CHALLENGE API ROUTES----------------
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
@api.post("/api/challenges")
def new_challenge(challenge: Challenge, challenge_service: ChallengeService = Depends()) -> Challenge:
        try:
            _id=3
            _posts=[]
            _noun=noun()
            _verb=verb()
            _adj=adj()
            _emotion=emotion()
            _style=style()
            _colors=colors(3)
            return challenge_service.create(Challenge(id=_id, posts=_posts, noun=_noun, verb=_verb, adj=_adj, emotion=_emotion,
            style=_style, colors=_colors))
        except Exception as e:
            raise HTTPException(status_code=422, detail=str(e))

# def new_challenge(challenge: Challenge = Challenge(id=None, posts=[], noun=noun(), verb=verb(),adj=adj(), emotion=emotion(), style=style(),colors=colors(3)), challenge_service: ChallengeService = Depends()) -> Challenge:
        # try:
        #     return challenge_service.create(challenge)
        # except Exception as e:
        #     raise HTTPException(status_code=422, detail=str(e))
        
     
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
