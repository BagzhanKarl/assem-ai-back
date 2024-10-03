# schemas/branch.py
from pydantic import BaseModel
from datetime import datetime

class BranchCreate(BaseModel):
    region: str
    city: str
    street: str
    home: str

class BranchResponse(BaseModel):
    id: int
    region: str
    city: str
    street: str
    home: str
    business_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class BusinessDetails(BaseModel):
    id: int
    name: str

class BranchResponseAll(BaseModel):
    id: int
    region: str
    city: str
    street: str
    home: str
    business_id: int
    created_at: datetime
    updated_at: datetime
    business: BusinessDetails  # Добавляем детали бизнеса

    class Config:
        from_attributes = True  # Используйте orm_mode, чтобы использовать SQLAlchemy объекты
