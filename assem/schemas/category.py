# schemas/business.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class CategoryCreate(BaseModel):
    name: str = 'Красота'
    admin: str

class CategoryIndi(BaseModel):
    id: int = 1
    name: str = 'Красота'

class CategoryResponse(BaseModel):
    status: bool = True
    version: int = 1
    data: Optional[List[CategoryIndi]]