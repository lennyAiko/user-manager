from fastapi import FastAPI
from db import db
from models import User

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "Lennox"} 

@app.get("/api/v1/users")
async def fetch_users():
    return db

# user(a variable to hold the entity): User(the entity received)
@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}