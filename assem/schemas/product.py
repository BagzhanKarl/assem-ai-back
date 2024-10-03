# schemas/product.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ProductImageCreate(BaseModel):
    url: str  # URL изображения

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    images: List[ProductImageCreate]  # Список изображений

class ProductShow(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    images: List[ProductImageCreate]  # Список изображений
class ProductImageResponse(BaseModel):
    id: int
    product_id: int
    url: str
    created_at: datetime
    updated_at: datetime

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    views: int
    clicks: int
    impressions: int
    created_at: datetime
    updated_at: datetime
    images: List[ProductImageResponse] = []  # Список фотографий продукта

    class Config:
        from_attributes = True  # Используйте SQLAlchemy объекты
