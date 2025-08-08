# FastAPI Real-Time Chat API

## Features
- Async REST endpoints for chat
- JWT user authentication
- MongoDB chat history
- WebSocket live chat
- Dockerized setup

## Getting Started

1. **Clone the repo and enter the folder**
2. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```
3. **API available at** `http://localhost:8000`
4. **Swagger docs at** `http://localhost:8000/docs`
<!-- 5. **WebSocket endpoint at** `ws://localhost:8000/ws/chat` -->

## Folder Structure
```
app/
├── main.py
├── models.py
├── db.py
├── auth.py
├── websocket.py
├── routers/
│   ├── users.py
│   └── chat.py
└── utils.py
requirements.txt
Dockerfile
docker-compose.yml
README.md
```

## Usage
- Register and login to get a JWT token.
- Use the token for `/send` and `/messages` endpoints.
- Connect to `/ws/chat` for real-time chat.

