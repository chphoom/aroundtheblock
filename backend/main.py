from fastapi import FastAPI, HTTPException, Depends
from user_service import UserService, User
from challenge_service import ChallengeService, Challenge
import os
# from static_files import StaticFileMiddleware


app = FastAPI()

# ----------USER API ROUTES----------------
#api route retrieves ALL registered users
@app.get("/api/registrations")
def get_registrations(user_service: UserService = Depends()) -> list[User]:
    return user_service.all()

#api route registers a new user
@app.post("/api/registrations")
def new_registration(user: User, user_service: UserService = Depends()) -> User:
        try:
            return user_service.create(user)
        except Exception as e:
            raise HTTPException(status_code=422, detail=str(e))

#api route retrieves user given email
@app.get("/api/users/{email}", responses={404: {"model": None}})
def get_user(email: str, user_service: UserService = Depends()) -> User:
    try: 
        return user_service.get(email)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

#api route to update user info
@app.post("/api/users")
def update_user(user: User, user_service: UserService = Depends()) -> User:
    try:
        return user_service.update(user)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

#api route deletes registered user
@app.delete("/api/delete/users/{email}")
def delete_user(email: str, user_service = Depends(UserService)) -> User:
    try:
        return user_service.delete(email)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# ----------CHALLENGE API ROUTES----------------
#api route retrieves ALL challenges
@app.get("/api/challenges")
def get_challenges(challenge_service: ChallengeService = Depends()) -> list[Challenge]:
    return challenge_service.all()

#api route registers a new challenge
@app.post("/api/challenges")
def new_challenge(challenge: Challenge, challenge_service: ChallengeService = Depends()) -> Challenge:
        try:
            return challenge_service.create(challenge)
        except Exception as e:
            raise HTTPException(status_code=422, detail=str(e))
        
#api route retrieves challenge given id
#TODO: implement a way to find challenge and get the correct id
@app.get("/api/challenges/{id}", responses={404: {"model": None}})
def get_user(id: int, challenge_service: ChallengeService = Depends()) -> Challenge:
    try: 
        return challenge_service.get(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
#api route deletes challenge FROM THE DATABASE
@app.delete("/api/delete/challenges/{id}")
def delete_user(id: int, challenge_service = Depends(ChallengeService)) -> Challenge:
    try:
        return challenge_service.delete(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


# app.mount("/", StaticFileMiddleware("../static", "index.html"))

