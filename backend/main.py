"""Entrypoint of backend API exposing the FastAPI `app` to be served by an application server such as uvicorn."""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .api import challenge, static_files, comment, login, user, post, upload

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

description = """
Welcome to Around the Block
"""

app = FastAPI(
    title="Around the Block API",
    version="0.0.1",
    description=description,
)

app.include_router(user.api)
app.include_router(login.api)
app.include_router(post.api)
app.include_router(upload.api)
app.include_router(comment.api)
app.include_router(challenge.api)
app.mount("/images", StaticFiles(directory="backend/images"), name="images")
app.mount("/", static_files.StaticFileMiddleware(directory="./static"))

