from pydantic import BaseModel
from typing import Optional, List, Dict

class MessageSchema(BaseModel):
    role: str
    content: str

class ChoiceSchema(BaseModel):
    finish_reason: str
    index: int
    message: MessageSchema
    logprobs: Optional[Dict]  # Если это значение может быть null, указываем как Optional

class UsageSchema(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int
    completion_tokens_details: Optional[Dict[str, int]]  # JSON-структура

class ChatCompletionSchema(BaseModel):
    id: str
    object: str
    model: str
    created: int
    choices: List[ChoiceSchema]
    usage: UsageSchema

    class Config:
        from_attributes = True
