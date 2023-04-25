"""This module provides a RESTful API for interacting with the user application.

Endpoints:
- GET /registrations - Retrieve all registered users
- POST /registrations - Generate a user
- GET /users/{email} - Retrieve a particular user
- PUT /users/{email}] - Update a user's info
- DELETE /delete/users/{email} - Delete a user

Usage:
import user
"""
from fastapi import APIRouter, HTTPException, Depends
from ..services import UserService, ChallengeService
from ..models import User, Challenge

api = APIRouter()

@api.get("/api/registrations", tags=['User'])
def get_registrations(user_service: UserService = Depends()) -> list[User]:
    """API endpoint for retrieving all the users in the database

    Parameters:
    - user_service (UserService): dependency injection for the UserService class

    Returns:
    - list[User]: a list of User objects representing all the Users in the database

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint
    - Returns a list of User objects representing all the Users in the database
    """
    return user_service.all()

@api.post("/api/registrations", tags=['User'])
def new_registration(user: User, user_service: UserService = Depends()) -> User:
    """API endpoint for creating a new User

    Parameters:
    - user: a User object representing the newly created User
    - user_service (UserService): dependency injection for the UserService class

    Returns:
    - User: a User object representing the newly created User

    HTTP Methods:
    - POST

    Usage:
    - Send a POST request to the endpoint
    - Returns a User object representing the newly created User
    """
    try:
        return user_service.create(user)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

@api.get("/api/users/{email}", responses={404: {"model": None}}, tags=['User'])
def get_user(email: str, user_service: UserService = Depends()) -> User:
    """API endpoint for retrieving a User by email

    Parameters:
    - email: a string represnting the primary key of the User
    - user_service (UserService): dependency injection for the UserService class

    Returns:
    - User: a User object representing the desired User

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint
    - Returns a User object representing the desired User
    """
    try: 
        return user_service.get(email)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@api.put("/api/users/{email}", tags=['User'])
def update_user(email: str,
                pronouns: str | None,
                displayName: str | None, 
                private: bool | None, 
                pfp: str | None, 
                bio: str | None, 
                connectedAccounts: list[str] | None, 
                user_service: UserService = Depends()) -> User:
    """API endpoint for updating a post

    Parameters:
    - email: a string representing the primary key of the User
    - pronouns: an optional string representing the new pronouns of the User
    - displayName: an optional string representing the new displya name of the User
    - private: an optional boolean representing the new privacy setting of the User
    - pfp: an optional string representing the new filename of the User's pfp
    - bio: an optional string representing the new bio of the User
    - connectedAccounts: an optional list of strings representing the new connected accounts of the User
    - user_service (UserService): dependency injection for the UserService class

    Returns:
    - User: a User object representing the updated User

    HTTP Methods:
    -PUT

    Usage:
    - Send a PUT request to the endpoint
    - Returns a User object representing the updated User
    """
    try:
        return user_service.update(email, pronouns, displayName, private, pfp, bio, connectedAccounts)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

#api route deletes registered user
@api.delete("/api/delete/users/{email}", tags=['User'])
def delete_user(email: str, user_service = Depends(UserService)) -> User:
    """API endpoint for deleting a User by it's email

    Parameters:
    - email: an string represnting the primary key of the User
    - user_service (UserService): dependency injection for the UserService class

    Returns:
    - User: a User object representing the deleted User

    HTTP Methods:
    - DELETE

    Usage:
    - Send a DELETE request to the endpoint
    - Returns a User object representing the deleted User
    """
    try:
        return user_service.delete(email)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@api.get("/api/searchusers/{search_string}", response_model=list[User], tags=["User"])
def search(search_string: str, user_serv: UserService = Depends()) -> list[User]:
    """API endpoint for retrieving users that have email, display name, bio, or connected accounts that match with the search string.

    Parameters:
    - search_string: a string literal used as a search criteria
    - user_serv: dependency injection from the post service 

    Returns:
    - list[User]: a list of User objects that have email, display name, bio, or connected accounts that match with the search string.

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint api/searchusers/{search_string}
    - Return a list of User objects that have email, display name, bio, or connected accounts that match with the search string.

    """
    try:
        return user_serv.search(search_string)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
