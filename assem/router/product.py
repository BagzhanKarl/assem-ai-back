# routes/product.py
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Cookie, Response,Query
from sqlalchemy.orm import Session
from assem.db.database import get_db
from assem.models import Business
from assem.models.product import Product
from assem.models.product_image import ProductImage
from assem.schemas.product import ProductResponse, ProductImageResponse, ProductCreate, ProductShow
from assem.security import decode_token

product_router = APIRouter(prefix='/api/v2/products', tags=['Продукты'])


@product_router.post('/add', response_model=ProductResponse)
async def create_product(product_create: ProductCreate, access_token: str = Cookie(None),db: Session = Depends(get_db)):
    if access_token is None:
        raise HTTPException(status_code=401, detail="Not authorized")
    try:
        payload = decode_token(access_token)
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

    new_product = Product(
        name=product_create.name,
        description=product_create.description,
        price=product_create.price,
        stock=product_create.stock,
        business_id=payload.get('business')  # Получаем ID бизнеса из токена
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    # Обработка добавления фотографий
    for image in product_create.images:
        new_image = ProductImage(
            product_id=new_product.id,
            url=image.url
        )
        db.add(new_image)

    db.commit()
    db.refresh(new_product)

    return new_product

# router/product.py
@product_router.get('/all', response_model=List[ProductShow])
async def get_products(
    platform: str,
    search: str = Query(None),  # Новый параметр для поиска
    skip: int = Query(0, ge=0),
    limit: int = Query(15, le=100),
    db: Session = Depends(get_db)
):
    # Найти бизнесы по platform
    businesses = db.query(Business).filter(Business.platformid == platform).all()
    if not businesses:
        raise HTTPException(status_code=404, detail="Бизнесы не найдены по указанной платформе")

    # Получить список ID бизнесов
    business_ids = [business.id for business in businesses]

    # Формируем базовый запрос для поиска продуктов
    query = db.query(Product).filter(Product.business_id.in_(business_ids))

    # Если параметр поиска не пустой, добавляем фильтрацию по названию
    if search:
        query = query.filter(Product.name.ilike(f'%{search}%'))  # Ищем по названию с учетом регистра

    # Получаем продукты с пагинацией
    products = query.offset(skip).limit(limit).all()

    return products
