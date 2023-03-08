from fastapi import FastAPI, HTTPException, Depends
from user_service import UserService, User
from user import User
from checkin import CheckinRequest, Checkin
import storage
import os
#from static_files import StaticFileMiddleware


app = FastAPI()


@app.get("/api/registrations")
def get_registrations() -> list[User]:
    return storage.get_registrations()


@app.post("/api/registrations")
def new_registration(user: User) -> User:
    try:
        return storage.create_registration(user)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

@app.get("/api/checkins")
def get_checkIns() -> list[Checkin]:
    return storage.get_checkins()


@app.post("/api/checkins")
def new_checkIn(checkInRequest: CheckinRequest) -> Checkin:
    try:
        return storage.create_checkin(checkInRequest.pid)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

@app.delete("/api/delete/{userPID}")
def delete_user(userPID: int) -> User:
    try:
        return storage.delete_user(storage.get_user_by_pid(userPID))
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
        
app.mount("/", StaticFileMiddleware("../static", "index.html"))
@app.post("/api/reset")
def reset() -> str:
    """Development-only route for resetting storage module and adding fake user and checkin."""
    if "MODE" in os.environ and os.environ["MODE"] == "production":
        raise HTTPException(status_code=404, detail="Not Found")
    else:
        storage.reset()
        storage.create_registration(User(pid=710453084, first_name="Kris", last_name="Jordan"))
        storage.create_checkin(710453084)
        storage.create_registration(User(pid=730439634, first_name="Chalisa", last_name="Phoomsakha"))
        storage.create_checkin(730439634)
        return "OK"
 
@app.get("/api/users")
def get_users(user_service: UserService = Depends()) -> list[User]:
    return user_service.all()


@app.post("/api/users")
def new_user(user: User, user_service: UserService = Depends()) -> User:
    try:
        return user_service.create(user)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
    # raise NotImplemented()


@app.get("/api/users/{pid}", responses={404: {"model": None}})
def get_user(pid: int, user_service: UserService = Depends()) -> User:
    try: 
        return user_service.get(pid)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    # raise NotImplemented()


@app.delete("/api/users/{pid}")
def delete_user(pid: int, user_service = Depends(UserService)):
    try:
        return user_service.delete(pid)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    # raise NotImplemented()
