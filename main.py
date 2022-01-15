from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi import Request
from datetime import datetime
from typing import List
# from assign import *

class Lecture(BaseModel):
    name: str
    day: str
    start_time: str
    end_time: str

class Lectures(BaseModel):
    lectures: List[Lecture]

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.post("/test/{test_id}")
async def test(test_id: int, request: Request):
    print("success")
    return await request.json()

@app.post("/lectures")
async def read_lectures(lectures: Request):
    print("success")
    lectures_list = await lectures.json()
    print(lectures_list)
    # results = assign(lectures_list)
    return lectures_list

def algorithm(lectures):
    #put algorithm here
    return None

app.mount("/", StaticFiles(directory="frontend", html=True), name="static")

# POST -> send stuff to backend
# PUT
# GET -> Get a basic html from backend
# DELETE