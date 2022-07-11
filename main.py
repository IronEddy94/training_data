from datetime import datetime


from fastapi import FastAPI
from pydantic import BaseModel

data = []


class Exercise(BaseModel):
    id: int
    exercise: str
    time: int
    date: datetime


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
