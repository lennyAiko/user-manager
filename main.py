from fastapi import FastAPI, HTTPException
from db import db
from models import User, UserUpdateRequest
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

# getting the id and then sending a body/payload
@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )