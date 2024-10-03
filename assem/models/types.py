# models/types.py
import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from assem.db.database import Base

class Type(Base):
    __tablename__ = "system_type"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(191), index=True)
    category_id = Column(Integer, ForeignKey('system_category.id'), nullable=False)
    type = Column(String(60), nullable=False, default='service')

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updatet_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Указание двусторонней связи с Category и Business
    category = relationship('Category', back_populates="types")  # изменил 'type' на 'types'
    business = relationship('Business', back_populates='type')

class Category(Base):
    __tablename__ = "system_category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(60), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updatet_at = Column(DateTime, default=datetime.datetime.utcnow)

    types = relationship('Type', back_populates='category')  # изменил 'type' на 'types'
