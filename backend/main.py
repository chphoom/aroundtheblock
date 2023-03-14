from fastapi import FastAPI, HTTPException, Depends, File, UploadFile, Response, Header
from fastapi.security import OAuth2PasswordRequestForm
from user_service import UserService, User
from challenge_service import ChallengeService, Challenge
from post_service import PostService, Post
from comment_service import CommentService, Comment
from login_service import LoginService, Token
from datetime import timedelta
import os
import imghdr

# from static_files import StaticFileMiddleware

app = FastAPI()

#-----------JWT TOKENS (for login) ---------

#Define function to get user from token
@app.get("/api/login")
def get_token_info(authorization: str = Header(None), login_service: LoginService = Depends()) -> User:
    if authorization is None:
        raise HTTPException(status_code=401, detail='Authorization header missing')
    try:
        token = authorization.split(' ')[1]
        decoded_token = login_service.decode(token=token)
        # Extract user data from the decoded token here
        user_email = decoded_token['sub']
        user = login_service.get(user_email)
    except:
        raise HTTPException(status_code=401, detail='Invalid authorization token')
    return user

# Define the login route
@app.post("/api/login")
async def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends(), login_service: LoginService = Depends()) -> Token:
    user = login_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    _access_token = login_service.create_access_token(expires_delta=timedelta(hours=15), email=user.email)
    response.set_cookie(key="access_token", value=_access_token, httponly=True, max_age=3600, expires=3600, path="/")

    return {"access_token": _access_token, "token_type": "bearer"}

#-----------SAVING MEDIAUPLOADS------------
@app.post("/api/uploadfile/")
async def create_upload_file(file: UploadFile = File()): 
    contents = await file.read()
    file_type = imghdr.what(file.filename, contents)
    if not file_type:
        raise HTTPException(status_code=400, detail='Invalid image file')
    filename = file.filename.replace(" ", "") # Remove any whitespace from the filename
    filename = file.filename.split('.')[0] + '.' + file_type
    with open(os.path.join('./images', filename), 'wb') as f:
        f.write(contents)
    return {'message': 'File uploaded successfully!'}


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
#TODO: Change update function use PUT instead of POST
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
def get_challenge(id: int, challenge_service: ChallengeService = Depends()) -> Challenge:
    try: 
        return challenge_service.get(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
#api route deletes challenge FROM THE DATABASE
@app.delete("/api/delete/challenges/{id}")
def delete_challenge(id: int, challenge_service = Depends(ChallengeService)) -> Challenge:
    try:
        return challenge_service.delete(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# ----------POST API ROUTES----------------
#api route retrieves ALL challenges
#returns postedBy as the email (primary key) of the user
#  and challenge as the noun of the challenge (logic to generate a challenge name is to be implemented)
@app.get("/api/posts")
def get_posts(post_service: PostService = Depends()) -> list[Post]:
    return post_service.all()

#api route creates a new Post
@app.post("/api/posts")
def new_post(post: Post, post_service: PostService = Depends()) -> Post:
        try:
            return post_service.create(post)
        except Exception as e:
            raise HTTPException(status_code=422, detail=str(e))
        
#api route retrieves post given id
#TODO: implement a way to find post and get the correct id
@app.get("/api/posts/{id}", responses={404: {"model": None}})
def get_post(id: int, post_service: PostService = Depends()) -> Post:
    try: 
        return post_service.get(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
#api route deletes post FROM THE DATABASE
@app.delete("/api/delete/posts/{id}")
def delete_post(id: int, post_service = Depends(PostService)) -> Post:
    try:
        return post_service.delete(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
#api route to update post desc, tags, and comments
@app.post("/api/post/edit")
def update_post(post: Post, post_service: PostService = Depends()) -> Post:
    try:
        return post_service.update(post)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

# ----------COMMENT API ROUTES----------------
#api route retrieces ALL comments
@app.get("/api/comments")
def get_comments(comment_service: CommentService = Depends()) -> list[Comment]:
    return comment_service.all()

#api route creates a new comment
@app.post("/api/comment")
def new_comment(comment: Comment, comment_service: CommentService = Depends()) -> Comment:
        try:
            return comment_service.create(comment)
        except Exception as e:
            raise HTTPException(status_code=422, detail=str(e))
        
#api route deletes comment
@app.delete("/api/delete/comment/{id}")
def delete_comment(id: int, comment_service = Depends(CommentService)):
    try:
        return comment_service.delete(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
#api route to update a comment's text
@app.post("/api/comment/edit")
def update_comment(comment_id: int, newText: str, comment_service: CommentService = Depends()) -> Comment:
    try:
        return comment_service.update(comment_id, newText)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
    
#api route to reply to a comment
@app.post("/api/reply")
def create_reply(comment_id: int, reply: Comment, comment_service: CommentService = Depends()) -> Comment:
    try: 
        return comment_service.reply(comment_id=comment_id,reply=reply)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
# app.mount("/", StaticFileMiddleware("../static", "index.html"))

