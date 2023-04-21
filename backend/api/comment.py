"""This module provides a RESTful API for interacting with the comment application.

Endpoints:
- GET /comments - Retrieve all Comments
- POST /comment- Generate a new Comment
- DELETE /delete/comment/{id} - Delete a Comment
- PUT /comment/edit - Update a Comment
- POST /reply - Retrieve a Challenge by it's id

Usage:
import comment
"""
from fastapi import APIRouter, HTTPException, Depends
from ..services import CommentService
from ..models import Comment

api = APIRouter()


@api.get("/api/comments")
def get_comments(comment_service: CommentService = Depends(), tags=['Comment']) -> list[Comment]:
    """API endpoint for retrieving all comments in the database

    Parameters:
    - comment_service (CommentService): dependency injection for the CommentService class

    Returns:
    - list[Comment]: a list of Comment objects representing all Comments stored in the database

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint
    - Returns a list of Comment objects representing all Comments stored in the database
    """
    return comment_service.all()

#api route creates a new comment
@api.post("/api/comment", tags=['Comment'])
def new_comment(comment: Comment, comment_service: CommentService = Depends()) -> Comment:
        """API endpoint for creaitng a new comment

        Parameters:
        - comment_service (CommentService): dependency injection for the CommentService class

        Returns:
        - Comment: a Comment object representing the newly created Comment

        HTTP Methods:
        - POST

        Usage:
        - Send a POST request to the endpoint
        - Returns a Comment object representing the newly created Comment
        """
        try:
            return comment_service.create(comment)
        except Exception as e:
            raise HTTPException(status_code=422, detail=str(e))
        
#api route deletes comment
@api.delete("/api/delete/comment/{id}", tags=['Comment'])
def delete_comment(id: int, comment_service = Depends(CommentService)):
    """API endpoint for deleting a comment

    Parameters:
    - id: an int representing the prinmary key of of the Comment object
    - comment_service (CommentService): dependency injection for the CommentService class

    Returns:
    - Comment: a Comment object representing the newly deleted Comment

    HTTP Methods:
    - DELETE

    Usage:
    - Send a DELETE request to the endpoint
    - Returns a Comment object representing the newly deleted Comment
    """
    try:
        return comment_service.delete(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
#api route to update a comment's text
@api.put("/api/comment/edit", tags=['Comment'])
def update_comment(comment_id: int, newText: str, comment_service: CommentService = Depends()) -> Comment:
    """API endpoint for updating a comment

    Parameters:
    - id: an int representing the prinmary key of of the Comment object
    - newText: a string representing the new content of the Comment
    - comment_service (CommentService): dependency injection for the CommentService class

    Returns:
    - Comment: a Comment object representing the newly updated Comment

    HTTP Methods:
    - PUT

    Usage:
    - Send a PUT request to the endpoint
    - Returns a Comment object representing the updated deleted Comment
    """
    try:
        return comment_service.update(comment_id, newText)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
    
#api route to reply to a comment
@api.post("/api/reply", tags=['Comment'])
def create_reply(comment_id: int, reply: Comment, comment_service: CommentService = Depends()) -> Comment:
    """API endpoint for replying to a comment

    Parameters:
    - id: an int representing the prinmary key of the "parent" Comment object
    - reply: a Comment object represnting the new Comment to be created
    - comment_service (CommentService): dependency injection for the CommentService class

    Returns:
    - Comment: a Comment object representing the newly created Comment

    HTTP Methods:
    - POST

    Usage:
    - Send a POST request to the endpoint
    - Returns a Comment object representing the newly created Comment
    """
    try: 
        return comment_service.reply(comment_id=comment_id,reply=reply)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
