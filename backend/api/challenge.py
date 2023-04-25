"""This module provides a RESTful API for interacting with the challenge application.

Endpoints:
- GET /challenges - Retrieve all Challenges
- GET /wechallenges- Retrieve all weChallenges
- GET /mechallenges- Retrieve all meChallenges
- GET /current - Retrieve current active weChallenge
- GET /challenges/{id} - Retrieve a Challenge by it's id
- POST /generate - Create a new challenge
- DELETE delete/challenges/{id} - Delete a comment by it's id

Usage:
import challenge
"""

from fastapi import APIRouter, HTTPException, Depends
from ..services import ChallengeService
from ..models import Challenge

api = APIRouter()

@api.get("/api/challenges", tags=['Challenge'])
def get_challenges(challenge_service: ChallengeService = Depends()) -> list[Challenge]:
    """API endpoint for retrieving all challenges in the database

    Parameters:
    - challenge_service (ChallengeService): dependency injection for the ChallengeService class

    Returns:
    - list[Challenge]: a list of Challenge objects representing all Challenges stored in the database

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint
    - Returns a list of Challenge objects representing all Challenges stored in the database
    """
    return challenge_service.all()

@api.get("/api/wechallenges", tags=['Challenge'])
def get_wechallenges(challenge_service: ChallengeService = Depends()) -> list[Challenge]:
    """API endpoint for retrieving all weChallenges in the database

    Parameters:
    - challenge_service (ChallengeService): dependency injection for the ChallengeService class

    Returns:
    - list[Challenge]: a list of Challenge objects representing all weChallenges stored in the database

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint
    - Returns a list of Challenge objects representing all weChallenges stored in the database
    """
    return challenge_service.allwe()

@api.get("/api/mechallenges", tags=['Challenge'])
def get_mechallenges(challenge_service: ChallengeService = Depends()) -> list[Challenge]:
    """API endpoint for retrieving all meChallenges in the database

    Parameters:
    - challenge_service (ChallengeService): dependency injection for the ChallengeService class

    Returns:
    - list[Challenge]: a list of Challenge objects representing all meChallenges stored in the database

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint
    - Returns a list of Challenge objects representing all meChallenges stored in the database
    """
    return challenge_service.allme()

@api.get("/api/current", tags=['Challenge'])
def get_current_wechallenge(challenge_service: ChallengeService = Depends()) -> Challenge:
    """API endpoint for retrieving all challenges in the database

    Parameters:
    - challenge_service (ChallengeService): dependency injection for the ChallengeService class

    Returns:
    - Challenge: a Challenge object representing the currently active global Challenge

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint
    - Returns a Challenge object representing the currently active global Challenge
    """
    return challenge_service.currwe()

@api.post("/api/generate", tags=['Challenge'])
def new_challenge(challenge: Challenge, options: list[bool], challenge_service: ChallengeService = Depends()) -> Challenge:
    """API endpoint for generating a new Challenge and inserting it into the database

    Parameters:
    - challenge: A Challenge object
    - options: A list of boolean values to determine which attributes of the Challenge should be generated
    - challenge_service (ChallengeService): dependency injection for the ChallengeService class

    Returns:
    - Challenge: a Challenge object representing the currently active global Challenge

    HTTP Methods:
    - POST

    Usage:
    - Send a POST request to the endpoint
    - Returns a Challenge object representing the currently active global Challenge
    """
    try:
        return challenge_service.create(challenge, options)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
        
@api.get("/api/challenges/{id}", responses={404: {"model": None}}, tags=['Challenge'])
def get_challenge(id: int, challenge_service: ChallengeService = Depends()) -> Challenge:
    """API endpoint for retrieving a challenge

    Parameters:
    - id: an int of the primary key number of the challenge
    - challenge_service (ChallengeService): dependency injection for the ChallengeService class

    Returns:
    - Challenge: a Challenge object

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint
    - Returns a Challenge object
    """
    try: 
        return challenge_service.get(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@api.delete("/api/delete/challenges/{id}", tags=['Challenge'])
def delete_challenge(id: int, challenge_service = Depends(ChallengeService)) -> Challenge:
    """API endpoint for deleting a challenge object in the database

    Parameters:
    - id: an int of the primary key number of the challenge
    - challenge_service (ChallengeService): dependency injection for the ChallengeService class

    Returns:
    - Challenge: a Challenge object representing the deleted Challengee

    HTTP Methods:
    - DELETE

    Usage:
    - Send a DELETE request to the endpoint
    - Returns a Challenge object representing the deleted Challengee
    """
    try:
        return challenge_service.delete(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))