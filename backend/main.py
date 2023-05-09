"""Entrypoint of backend API exposing the FastAPI `app` to be served by an application server such as uvicorn."""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .api import challenge, static_files, comment, login, user, post, upload, notifs
from .script.schedule import scheduler

__authors__ = ["Kris Jordan, Chalisa Phoomsakha"]
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
app.include_router(notifs.api)
app.mount("/", static_files.StaticFileMiddleware(directory="./static"))

# start the scheduler
scheduler.start()

# add a shutdown event handler to stop the scheduler when the application shuts down
@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()