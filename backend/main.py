from fastapi import FastAPI, HTTPException, Depends
from user_service import UserService, User
import os
# from static_files import StaticFileMiddleware


app = FastAPI()

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
@app.delete("/api/delete/{email}")
def delete_user(email: str, user_service = Depends(UserService)) -> User:
    try:
        return user_service.delete(email)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


# app.mount("/", StaticFileMiddleware("../static", "index.html"))

