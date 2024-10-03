# schemas/userSchemas.py
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserCreate(BaseModel):
    phone: str = '77761174378'
    first_name: str = 'Бағжан'
    last_name: str = 'Карл'
    password: str = '123456789'

class UserLogin(BaseModel):
    phone: str
    password: str
class UserData(BaseModel):
    id: int
    phone: str
    first_name: str
    last_name: str
    hashed_password: str
    role_id: Optional[int] = None
    business_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
class ResponseUserCreate(BaseModel):
    status: bool
    api: str
    data: List[UserData]