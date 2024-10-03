import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from assem.db.database import get_db
from assem.models import Type, Category
from assem.schemas import AddType, ResponseType

typesApi = APIRouter(prefix='/api/v2/types', tags=['Виды бизнеса'])

@typesApi.post('/create', response_model=ResponseType)
async def add_type(type: AddType, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == type.category).first()
    if not category:
        raise HTTPException(status_code=400, detail="Категория не найдено")

    new_type = Type(
        name=type.name,
        category_id=category.id,
        type=type.type
    )
    db.add(new_type)
    db.commit()
    db.refresh(new_type)
    answere = {"status": 1, "version": 1, "data": [new_type]}
    return answere
