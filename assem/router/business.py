from fastapi import APIRouter, Depends, HTTPException, Cookie, Response
from sqlalchemy.orm import Session

from assem.db.database import get_db
from assem.models import Type, Business, User
from assem.schemas import NewBusiness, BusinessResponse, FullResponse  # Предположим, что вы создали схему BusinessResponse
from assem.security import generate_id, decode_token, generate_token

businessAPI = APIRouter(prefix='/api/v2/business', tags=['Бизнес'])


@businessAPI.post('/create', response_model=FullResponse)
async def new_business(new: NewBusiness, response: Response, access_token: str = Cookie(None), db: Session = Depends(get_db)):
    if access_token is None:
        raise HTTPException(status_code=401, detail="Not authorized")
    try:
        payload = decode_token(access_token)  # Используйте access_token
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Проверка существования типа бизнеса
    type = db.query(Type).filter(Type.id == new.type).first()
    if not type:
        raise HTTPException(status_code=404, detail='Вид бизнеса не найдено')

    # Создание нового бизнеса
    nbus = Business(
        name=new.name,
        branch=new.branch,
        type_id=new.type,
        platformid=generate_id(),
        balance=new.balance
    )
    db.add(nbus)
    db.commit()
    db.refresh(nbus)

    # Обновление данных пользователя
    user = db.query(User).filter(User.id == payload.get('user')).first()
    user.role_id = new.role
    user.business_id = nbus.id
    db.add(user)
    db.commit()
    db.refresh(user)

    # Обновление JWT токена
    response.delete_cookie(key="access_token")
    newtoken = generate_token(user.id, user.business_id, user.role_id)
    response.set_cookie(key="access_token", value=newtoken, httponly=True, max_age=3600, secure=True, domain="*.assemcrm.kz", samesite=None)

    return FullResponse(user=user, business=nbus)


@businessAPI.get('/my')
async def get_user_business(access_token: str = Cookie(None), db: Session = Depends(get_db)):
    if access_token is None:
        raise HTTPException(status_code=401, detail="Not authorized")
    try:
        payload = decode_token(access_token)  # Используйте access_token
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

    business = db.query(Business).filter(Business.id == payload.get('business')).first()

    return business