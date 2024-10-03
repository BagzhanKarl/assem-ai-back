from fastapi import APIRouter, Depends, HTTPException, Response, Cookie
from sqlalchemy.orm import Session
from assem.db.database import engine, get_db, Base
from assem.models import User
from assem.schemas import UserCreate, UserLogin, ResponseUserCreate
from assem.security import hash_password, generate_token, verify_password, decode_token

User.metadata.create_all(bind=engine)

user_router = APIRouter(prefix='/api/v2/users', tags=['Пользователи'])




@user_router.post('/registration')
async def registration(newuser: UserCreate, response: Response, db: Session = Depends(get_db)):
    check = db.query(User).filter(User.phone == newuser.phone).first()

    if check:
        raise HTTPException(status_code=404, detail="Пользователь с таким логином уже зарегистрирован")

    user = User(
        first_name=newuser.first_name,
        last_name=newuser.last_name,
        phone=newuser.phone,
        hashed_password=hash_password(newuser.password),
        role_id=None,
        business_id=None,
        is_active=True,
        is_verify=False,
        is_superuser=False

    )
    db.add(user)
    db.commit()
    db.refresh(user)
    token = generate_token(user.id, user.business_id, user.role_id)
    response.set_cookie(key="access_token", value=token, httponly=True, max_age=3600, secure=True, domain="*.assemcrm.kz", samesite=None)

    return user

@user_router.post('/logout')
async def logout(response: Response):
    response.delete_cookie(key="access_token")  # Удаляем токен из cookies
    return {"status": True, "message": "Successfully logged out"}

@user_router.post("/login")
async def login_user(user: UserLogin, response: Response, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.phone == user.phone).first()
    if existing_user == None:
        raise HTTPException(status_code=400, detail="Неправильный номер телефона или пароль")

    passChek = verify_password(user.password, existing_user.hashed_password)

    if(passChek == False):
        raise HTTPException(status_code=400, detail="Неправильный номер телефона или пароль")

    token = generate_token(existing_user.id, existing_user.business_id, existing_user.role_id)
    response.set_cookie(key="access_token", value=token, httponly=True, max_age=3600)
    return {'phone': user.phone}