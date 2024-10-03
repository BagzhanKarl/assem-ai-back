# schemas/role.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Схема для создания роли
class RoleCreate(BaseModel):
    name: str

# Схема для отображения данных о роли
class RoleRead(BaseModel):
    id: int
    name: str
    created_at: datetime
    updatet_at: datetime

    class Config:
        from_attributes = True
