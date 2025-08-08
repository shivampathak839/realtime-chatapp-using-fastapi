from fastapi import FastAPI, WebSocket, Depends, WebSocketDisconnect
from app.routers import users, chat
from app.websocket import manager
from app.auth import get_current_user

app = FastAPI()

# Include routers
app.include_router(users.router)
app.include_router(chat.router)

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Broadcast to all connected clients
            await manager.broadcast(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)