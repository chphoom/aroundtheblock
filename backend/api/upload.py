"""This module provides a RESTful API for uploading files into the application

Endpoints:
- POST /uploadfile/ - Saves file into file system

Usage:
import post
"""

from fastapi import APIRouter, HTTPException, File, UploadFile
import os
import imghdr

api = APIRouter()

@api.post("/api/uploadfile/", tags=['Upload'])
async def create_upload_file(file: UploadFile = File()):
    """API endpoint for uploading a file

    Parameters:
    - file: a file

    Returns:
    - dict: representing the json compatible success message

    HTTP Methods:
    -POST

    Usage:
    - Send a POST request to the endpoint
    - Returns a json compatible success message
    """
    contents = await file.read()
    file_type = imghdr.what(file.filename, contents)
    if not file_type:
        raise HTTPException(status_code=400, detail='Invalid image file')
    filename = file.filename.replace(" ", "") # Remove any whitespace from the filename
    filename = file.filename.split('.')[0] + '.' + file_type
    with open(os.path.join(os.path.dirname(__file__), '..', 'images', filename), 'wb') as f:
        f.write(contents)
    return {'message': 'File uploaded successfully!'}