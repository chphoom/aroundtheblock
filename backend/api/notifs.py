"""This module provides a RESTful API for interacting with the notifcation application.

Endpoints:
- GET /notifs - Retrieve all Notifs
- POST /notifs/new - Generate a new Notif
- DELETE /delete/notif/{id} - Delete a Notif
- GET /notifs/to/{email} - Retrieve all Notifs to a user
- GET /notifs/from/{email} - Retrieve all Notifs from a user
- GET /notifs/id/{id} - Retrieve a particular Notif by it's ID
- PUT /notifs/read - Read a notification
- PUT /notifs/unread - Mark a notification as unread

Usage:
import comment
"""
from fastapi import APIRouter, HTTPException, Depends
from ..services import NotifService
from ..models import Notif

api = APIRouter()

@api.get("/api/notifs", tags=['Notifications'])
def get_All(notif_service: NotifService = Depends()) -> list[Notif]:
    """API endpoint for retrieving all the notifications in the database

    Parameters:
    - notif_service (NotifService): dependency injection for the NotifService class

    Returns:
    - list[Notif]: a list of Notif objects representing all the Notifs in the database

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint
    - Returns a list of User objects representing all the Notifs in the database
    """
    return notif_service.all()

@api.post("/api/notif/new", tags=['Notifications'])
def new(notif: Notif, notif_service: NotifService = Depends()) -> Notif:
        """API endpoint for creaitng a new notification

        Parameters:
        - notif_service (NotifService): dependency injection for the NotifService class

        Returns:
        - Notif: a nottif object representing the newly created notification

        HTTP Methods:
        - POST

        Usage:
        - Send a POST request to the endpoint
        - Returns a Notif object representing the newly created notification
        """
        try:
            return notif_service.create(notif)
        except Exception as e:
            raise HTTPException(status_code=422, detail=str(e))

@api.delete("/api/delete/notif/{id}", tags=['Notifications'])
def delete(id: int, notif_service = Depends(NotifService)):
    """API endpoint for deleting a notification

    Parameters:
    - id: an int representing the prinmary key of of the Notif object
    - notif_service (CommentService): dependency injection for the CommentService class

    Returns:
    - Notif: a Notif object representing the newly deleted notification

    HTTP Methods:
    - DELETE

    Usage:
    - Send a DELETE request to the endpoint
    - Returns a notif object representing the newly deleted notification
    """
    try:
        return notif_service.delete(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@api.get("/api/notifs/to/{email}", tags=['Notifications'])
def get_by_to_User(email: str, notif_service: NotifService = Depends()) -> list[Notif]:
    """API endpoint for retrieving all the notifications in the database to a particular user

    Parameters:
    - email: a strign presenting the primary key of the user
    - notif_service (NotifService): dependency injection for the NotifService class

    Returns:
    - list[Notif]: a list of Notif objects representing all the Notifs in the database to a particular user

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint
    - Returns a list of User objects representing all the Notifs in the database to a particular user
    """
    return notif_service.get_by_toUser(email)

@api.get("/api/notifs/from/{email}", tags=['Notifications'])
def get_by_from_User(email: str, notif_service: NotifService = Depends()) -> list[Notif]:
    """API endpoint for retrieving all the notifications in the database from a particular user

    Parameters:
    - email: a strign presenting the primary key of the user
    - notif_service (NotifService): dependency injection for the NotifService class

    Returns:
    - list[Notif]: a list of Notif objects representing all the Notifs in the database from a particular user

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint
    - Returns a list of User objects representing all the Notifs in the database from a particular user
    """
    return notif_service.get_by_fromUser(email)

@api.get("/api/notif/id/{id}", responses={404: {"model": None}}, tags=['Notifications'])
def get_notif(id: int, notif_service: NotifService = Depends()) -> Notif:
    """API endpoint for retrieving a notification

    Parameters:
    - id: an int of the primary key number of the notification
    - notif_service (NotifService): dependency injection for the NotifService class

    Returns:
    - Notif: a Notif object

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint
    - Returns a Challenge object
    """
    try: 
        return notif_service.get(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@api.put("/api/notifs/read/{id}", tags=['Notifications'])
def read(id: int, notif_service: NotifService = Depends()) -> Notif:
    """API endpoint for updating a notification

    Parameters:
    - id: an int representing the prinmary key of of the Notif object
    - notif_service (NotifService): dependency injection for the NotifService class

    Returns:
    - Notif: a Notif object representing the newly updated Notif

    HTTP Methods:
    - PUT

    Usage:
    - Send a PUT request to the endpoint
    - Returns a Notif object representing the updated Notif
    """
    try:
        return notif_service.read(id)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
    
@api.put("/api/notifs/unread/{id}", tags=['Notifications'])
def unread(id: int, notif_service: NotifService = Depends()) -> Notif:
    """API endpoint for updating a notification

    Parameters:
    - id: an int representing the prinmary key of of the Notif object
    - notif_service (NotifService): dependency injection for the NotifService class

    Returns:
    - Notif: a Notif object representing the newly updated Notif

    HTTP Methods:
    - PUT

    Usage:
    - Send a PUT request to the endpoint
    - Returns a Notif object representing the updated Notif
    """
    try:
        return notif_service.unread(id)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))