
from fastapi import FastAPI, HTMLResponse, Query
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
