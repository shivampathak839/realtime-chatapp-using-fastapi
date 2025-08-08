from fastapi import APIRouter, Depends, HTTPException
from app.models import MessageCreate, MessageOut
from app.db import chat_collection
from app.auth import get_current_user
from datetime import datetime

router = APIRouter()

@router.post("/send")
async def send_message(msg: MessageCreate, user=Depends(get_current_user)):
    doc = {
        "username": user["username"],
        "message": msg.message,
        "timestamp": datetime.utcnow().isoformat()
    }
    await chat_collection.insert_one(doc)
    return {"msg": "Message sent"}

@router.get("/messages", response_model=list[MessageOut])
async def get_messages(user=Depends(get_current_user)):
    messages = await chat_collection.find().sort("timestamp", -1).to_list(50)
    messages.reverse()  # oldest first
    return messages