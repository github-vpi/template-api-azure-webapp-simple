from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import json
from fastapi import Header, Query, status, APIRouter, HTTPException, FastAPI, UploadFile, File, Request, Form
from pydantic import BaseModel
import json as json
from .predict_handlers import normalize_API
from typing import List
from fastapi import UploadFile, HTTPException

from domain import print_message

app = FastAPI()


@app.get('/hello')
async def hello():
    return {"message": "Hello World"}


@app.get('/message')
async def print_message(name: str = Query(None, alias="name")):
    message = print_message(name)
    content = f"""<html>
                    <head>
                        <title>Deploy simple API to Azure Webapp</title>
                    </head>
                    <body>
                        <h1>Deploy simple API to Azure Webapp</h1>
                        <p>Message: {message}</p>
                    </body>
                  </html>"""
    return HTMLResponse(content=content, status_code=200)
