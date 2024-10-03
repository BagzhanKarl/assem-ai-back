# models/business.py
import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from assem.db.database import Base

class Business(Base):
    __tablename__ = 'business'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(60), nullable=False)
    branch = Column(Integer, nullable=False, default=1)
    type_id = Column(Integer, ForeignKey('system_type.id'), nullable=False)
    platformid = Column(String(60), nullable=False)
    logo_link = Column(String(255), nullable=True)
    kaspi_pay = Column(String(255), nullable=True)

    balance = Column(Numeric(10, 2), nullable=False, default=0)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Добавил back_populates для двусторонней связи
    type = relationship('Type', back_populates='business')
    user = relationship('User', back_populates='business')
    branches = relationship('Branch', back_populates='business')  # back_populates пропущен в вашей модели Branch
    subscription = relationship('Subscription', back_populates='business')
    products = relationship('Product', back_populates='business')