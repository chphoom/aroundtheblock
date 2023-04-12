from fastapi import APIRouter, HTTPException, Depends
from ..services import PostService
from ..models import Post

api = APIRouter()


# ----------POST API ROUTES----------------
#api route retrieves ALL challenges
#returns user_id as the email (primary key) of the user
#  and challenge as the noun of the challenge (logic to generate a challenge name is to be implemented)
@api.get("/api/posts")
def get_posts(post_service: PostService = Depends()) -> list[Post]:
    return post_service.all()

#api route creates a new Post
@api.post("/api/posts")
def new_post(post: Post, post_service: PostService = Depends()) -> Post:
        try:
            return post_service.create(post)
        except Exception as e:
            raise HTTPException(status_code=422, detail=str(e))
        
#api route retrieves post given id
#TODO: implement a way to find post and get the correct id
@api.get("/api/posts/{id}", responses={404: {"model": None}})
def get_post(id: int, post_service: PostService = Depends()) -> Post:
    try: 
        return post_service.get(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
#api route deletes post FROM THE DATABASE
@api.delete("/api/delete/posts/{id}")
def delete_post(id: int, post_service = Depends(PostService)) -> Post:
    try:
        return post_service.delete(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
#api route to update post desc, tags, and comments
@api.post("/api/post/edit")
def update_post(post: Post, post_service: PostService = Depends()) -> Post:
    try:
        return post_service.update(post)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
