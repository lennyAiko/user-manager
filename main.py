from fastapi import FastAPI
from typing import List
from models import User, Gender, Role
from uuid import uuid4

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        first_name="Lennox", 
        last_name="Charles",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=uuid4(), 
        first_name="Hikmah", 
        last_name="Adunni",
        gender=Gender.female,
        roles=[Role.student]
    ),
]

@app.get("/")
async def root():
    return {"Hello": "Lennox"}

