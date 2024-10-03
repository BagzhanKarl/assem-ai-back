# models/branch.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from assem.db.database import Base
import datetime

class Branch(Base):
    __tablename__ = 'branch'

    id = Column(Integer, primary_key=True, index=True)
    region = Column(String(60), nullable=False)
    city = Column(String(60), nullable=False)
    street = Column(String(60), nullable=False)
    home = Column(String(60), nullable=False)

    business_id = Column(Integer, ForeignKey('business.id'), nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)  # Добавлено
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)  # Добавлено

    business = relationship('Business', back_populates='branches')
