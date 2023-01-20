from fastapi import FastAPI
from db import db

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "Lennox"} 

@app.get("/api/v1/users")
async def fetch_users():
    return db