# schemas/webhooks.py
from pydantic import BaseModel, Field
from typing import List, Optional

class MessageBody(BaseModel):
    id: str
    from_me: bool
    type: str
    chat_id: str
    timestamp: int
    source: str
    text: dict
    from_: str = Field(..., alias='from')
    from_name: str

class WebhookRequest(BaseModel):
    messages: List[MessageBody]
    channel_id: str
