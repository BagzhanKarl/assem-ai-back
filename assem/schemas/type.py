import datetime
from typing import Optional, List

from pydantic import BaseModel

class AddType(BaseModel):
    category: int = 1
    name: str = 'Барбершоп'
    type: str = 'service'

class BaseType(BaseModel):
    id: int
    name: str
    category_id: int
    type: str

class ResponseType(BaseModel):
    status: bool = True
    version: int = 1
    data: Optional[List[BaseType]]