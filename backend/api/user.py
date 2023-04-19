from fastapi import APIRouter, HTTPException, Depends
from ..services import UserService, ChallengeService
from ..models import User, Challenge

api = APIRouter()


# ----------USER API ROUTES----------------
#api route retrieves ALL registered users
@api.get("/api/registrations")
def get_registrations(user_service: UserService = Depends()) -> list[User]:
    return user_service.all()

#api route registers a new user
@api.post("/api/registrations")
def new_registration(user: User, user_service: UserService = Depends()) -> User:
        try:
            return user_service.create(user)
        except Exception as e:
            raise HTTPException(status_code=422, detail=str(e))

#api route retrieves user given email
@api.get("/api/users/{email}", responses={404: {"model": None}})
def get_user(email: str, user_service: UserService = Depends()) -> User:
    try: 
        return user_service.get(email)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

#api route to update user info
@api.put("/api/users/{email}")
def update_user(email: str,
                pronouns: str | None,
                displayName: str | None, 
                private: bool | None, 
                pfp: str | None, 
                bio: str | None, 
                connectedAccounts: list[str] | None, 
                user_service: UserService = Depends()) -> User:
    try:
        return user_service.update(email)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

#api route deletes registered user
@api.delete("/api/delete/users/{email}")
def delete_user(email: str, user_service = Depends(UserService)) -> User:
    try:
        return user_service.delete(email)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
