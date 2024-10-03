# router/role.py
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from assem.db.database import get_db
from assem.models.roles import Role
from assem.schemas.role import RoleCreate, RoleRead

role_router = APIRouter(prefix="/api/v2/roles", tags=["Roles"])

# Добавление новой роли
@role_router.post("/create", response_model=RoleRead, status_code=status.HTTP_201_CREATED)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    db_role = Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

# Получение всех ролей
@role_router.get("/all", response_model=list[RoleRead])
def read_roles(db: Session = Depends(get_db)):
    return db.query(Role).all()
