import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from assem.db.database import get_db
from assem.models import Category
from assem.schemas import CategoryCreate
from assem.schemas.category import CategoryResponse

categoryAPI = APIRouter(prefix='/api/v2/category', tags=['Категории бизнеса'])

@categoryAPI.post('/create')
async def new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    n_category = Category(
        name=category.name
    )
    db.add(n_category)
    db.commit()
    db.refresh(n_category)
    print(category.admin)
    return n_category

@categoryAPI.get('/all', response_model=CategoryResponse)
async def get_all_list(db: Session = Depends(get_db)):
    data = db.query(Category).all()
    answere = {"status": True, "version": 1, "data": data}
    return answere