from fastapi import FastAPI, HTTPException
from db import db
from models import User
from uuid import UUID

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

# in curly braces are called path variables
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist."
    )