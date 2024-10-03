from pydantic import BaseModel

class Chat(BaseModel):
    role: str
    content: str

class ChatArray(BaseModel):
    messages: list[Chat]

class SystemSettings(BaseModel):
    content: str
    admin: str = "admin123"