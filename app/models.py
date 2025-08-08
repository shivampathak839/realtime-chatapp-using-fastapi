from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class MessageCreate(BaseModel):
    message: str

class MessageOut(BaseModel):
    username: str
    message: str
    timestamp: str