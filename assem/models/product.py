# models/product.py
import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from assem.db.database import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)  # Количество на складе

    views = Column(Integer, nullable=False, default=0)  # Количество просмотров
    clicks = Column(Integer, nullable=False, default=0)  # Количество кликов
    impressions = Column(Integer, nullable=False, default=0)  # Количество показов

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    business_id = Column(Integer, ForeignKey('business.id'), nullable=False)  # Внешний ключ на бизнес

    business = relationship('Business', back_populates='products')
    images = relationship('ProductImage', back_populates='product')  # Связь с фотографиями
