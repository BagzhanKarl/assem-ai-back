# router/branch.py
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Cookie
from sqlalchemy.orm import Session
from assem.db.database import get_db
from assem.models import Business
from assem.models.branch import Branch
from assem.schemas.branch import BranchCreate, BranchResponse, BranchResponseAll
from assem.security import decode_token

branch_router = APIRouter(prefix='/api/v2/branch', tags=['Филиалы'])


@branch_router.post('/', response_model=BranchResponse)
async def create_branch(branch: BranchCreate, access_token: str = Cookie(None), db: Session = Depends(get_db)):
    if access_token is None:
        raise HTTPException(status_code=401, detail="Not authorized")
    try:
        payload = decode_token(access_token)
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Получение ID бизнеса из токена
    business_id = payload.get('business')

    # Создание нового филиала
    new_branch = Branch(
        region=branch.region,
        city=branch.city,
        street=branch.street,
        home=branch.home,
        business_id=business_id
    )

    db.add(new_branch)
    db.commit()
    db.refresh(new_branch)

    return new_branch

@branch_router.get('/all', response_model=List[BranchResponseAll])
async def get_all_branches(access_token: str = Cookie(None), db: Session = Depends(get_db)):
    if access_token is None:
        raise HTTPException(status_code=401, detail="Not authorized")
    try:
        payload = decode_token(access_token)
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Получаем все филиалы
    branches = db.query(Branch).all()

    # Обогащаем данные о бизнесах
    for branch in branches:
        branch.business = db.query(Business).filter(Business.id == branch.business_id).first()

    return branches