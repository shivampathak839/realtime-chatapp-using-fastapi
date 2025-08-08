from fastapi import APIRouter, HTTPException
from app.models import UserCreate, UserLogin
from app.auth import get_password_hash, verify_password, create_access_token
from app.db import users_collection
from datetime import timedelta

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate):
    if await users_collection.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_pw = get_password_hash(user.password)
    await users_collection.insert_one({"username": user.username, "password": hashed_pw})
    return {"msg": "Registered successfully"}

@router.post("/token")
async def login(user: UserLogin):
    db_user = await users_collection.find_one({"username": user.username})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.username}, timedelta(minutes=60))
    return {"access_token": token, "token_type": "bearer"}