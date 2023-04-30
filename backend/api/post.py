"""This module provides a RESTful API for interacting with the post application.

Endpoints:
- GET /posts - Retrieve all posts
- POST /posts - Generate a new post
- GET /posts/{id} - Retrieve a particular post
- DELETE /delete/posts/{id} - Delete a post
 - PUT /post/edit - Update a post
 - GET /meposts - Retrieve all posts associated with weChallenges
 - GET /weposts - Retrieve all posts associated with meChallenges

Usage:
import post
"""
from fastapi import APIRouter, HTTPException, Depends
from ..services import PostService
from ..models import Post

api = APIRouter()

@api.get("/api/posts", tags=['Post'])
def get_posts(post_service: PostService = Depends()) -> list[Post]:
    """API endpoint for retrieving all the posts in the database

    Parameters:
    - post_service (PostService): dependency injection for the PostService class

    Returns:
    - list[Post]: a list of Post objects representing all the posts in the database

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint
    - Returns a list of Post objects representing all the posts in the database
    """
    return post_service.all()

#api route creates a new Post
@api.post("/api/createpost", tags=['Post'])
def new_post(post: Post, post_service: PostService = Depends()) -> Post:
    """API endpoint for creating a new post

    Parameters:
    - post: a Post object representing the newly created Post
    - post_service (PostService): dependency injection for the PostService class

    Returns:
    - Post: a Post object representing the newly created Post

    HTTP Methods:
    - POST

    Usage:
    - Send a POST request to the endpoint
    - Returns a Post object representing the newly created Post
    """
    try:
        return post_service.create(post)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
        
@api.get("/api/posts/{id}", responses={404: {"model": None}}, tags=['Post'])
def get_post(id: int, post_service: PostService = Depends()) -> Post:
    """API endpoint for retrieving a post by id

    Parameters:
    - id: an int represnting the primary key of the Post
    - post_service (PostService): dependency injection for the PostService class

    Returns:
    - Post: a Post object representing the desired Post

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint
    - Returns a Post object representing the desired Post
    """
    try: 
        return post_service.get(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@api.delete("/api/delete/posts/{id}", tags=['Post'])
def delete_post(id: int, post_service = Depends(PostService)) -> Post:
    """API endpoint for deleting a post by id

    Parameters:
    - id: an int represnting the primary key of the Post
    - post_service (PostService): dependency injection for the PostService class

    Returns:
    - Post: a Post object representing the deleted Post

    HTTP Methods:
    - DELETE

    Usage:
    - Send a DELETE request to the endpoint
    - Returns a Post object representing the deleted Post
    """
    try:
        return post_service.delete(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@api.put("/api/post/edit/{id}", tags=['Post'])
def update_post(id: int,
                title: str | None = None,
                desc: str | None = None,
                private: bool | None = None,
                tags: list[str] | None = None,
                post_service: PostService = Depends()) -> Post:
    """API endpoint for updating a post

    Parameters:
    - id: an int representing the primary key of the post
    - desc: a string representing the new desc fo the post
    - tags: a list of strings representing the new tags for the post
    - post_service (PostService): dependency injection for the PostService class

    Returns:
    - Post: a Post object representing the updated Post

    HTTP Methods:
    -PUT

    Usage:
    - Send a PUT request to the endpoint
    - Returns a Post object representing the updated Post
    """
    try:
        return post_service.update(id, title, desc, private, tags)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

@api.get("/api/meposts", tags=['Post'])
def get_me_posts(post_service: PostService = Depends()) -> list[Post]:
    """API endpoint for retrieving all the posts associated with meChallenges

    Parameters:
    - post_service (PostService): dependency injection for the PostService class

    Returns:
    - list[Post]: a list of Post objects representing all the posts associated with meChallenges

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint
    - Returns a list of Post objects representing all the posts associated with meChallenges
    """
    try:
        return post_service.get_me_posts()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

#api route to get all wechallenge posts
@api.get("/api/weposts", tags=['Post'])
def get_we_posts(post_service: PostService = Depends()) -> list[Post]:
    """API endpoint for retrieving all the posts associated with weChallenges

    Parameters:
    - post_service (PostService): dependency injection for the PostService class

    Returns:
    - list[Post]: a list of Post objects representing all the posts associated with weChallenges

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint
    - Returns a list of Post objects representing all the posts associated with meChallenges
    """
    try:
        return post_service.get_we_posts()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@api.get("/api/searchposts/{search_string}", response_model=list[Post], tags=["Post"])
def search_post(search_string: str, post_serv: PostService = Depends()) -> list[Post]:
    """API endpoint for retrieving posts that has content, description, title that match with the search string.

    Parameters:
    - search_string: a string literal used as a search criteria
    - post_serv: dependency injection from the post service 

    Returns:
    - list[Post]: a list of Post objects that has content, title, description that match the search string

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint api/post/{search_string}
    - Return a list of Post objects that has content, title, description that match the search string
    """
    try:
        return post_serv.search(search_string)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

@api.get("/api/tagged/{search_string}", response_model=list[Post], tags=["Post"])
def tagged(search_string: str, post_serv: PostService = Depends()) -> list[Post]:
    """API endpoint for retrieving posts that has content, description, title that match with the search string.

    Parameters:
    - search_string: a string literal used as a search criteria
    - post_serv: dependency injection from the post service 

    Returns:
    - list[Post]: a list of Post objects that has content, title, description that match the search string

    HTTP Methods:
    - GET

    Usage:
    - Send a GET request to the endpoint api/post/{search_string}
    - Return a list of Post objects that has content, title, description that match the search string
    """
    try:
        return post_serv.tagged(search_string)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))