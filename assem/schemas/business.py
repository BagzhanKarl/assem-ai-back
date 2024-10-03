# schemas/business.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NewBusiness(BaseModel):
    name: str
    branch: int
    type: int
    balance: float
    role: int  # ID роли, которую хотим назначить пользователю

class BusinessResponse(BaseModel):
    id: int
    name: str
    branch: int
    type_id: int
    platformid: str
    balance: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone: str
    role_id: Optional[int]
    business_id: Optional[int]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class FullResponse(BaseModel):
    user: UserResponse
    business: BusinessResponse
