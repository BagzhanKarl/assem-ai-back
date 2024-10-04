from pydantic import BaseModel
from typing import List

class WebhookTextBody(BaseModel):
    body: str

class WebhookMessageCreate(BaseModel):
    id: str
    from_me: bool
    type: str
    chat_id: str
    timestamp: int
    source: str
    text: WebhookTextBody
    from_user: str
    from_name: str

    class Config:
        from_attributes = True

class WebhookCreate(BaseModel):
    messages: List[WebhookMessageCreate]
    channel_id: str

class AddSystem(BaseModel):
    content: str
    key: str = 'assemteam'