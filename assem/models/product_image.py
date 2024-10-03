# models/product_image.py
import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from assem.db.database import Base


class ProductImage(Base):
    __tablename__ = 'product_image'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)  # Внешний ключ на продукт
    url = Column(String(255), nullable=False)  # Ссылка на фотографию

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    product = relationship('Product', back_populates='images')  # Связь с продуктом
