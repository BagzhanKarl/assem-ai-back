# models/plans.py
import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey,Float
from sqlalchemy.orm import relationship
from assem.db.database import Base

class Subscription(Base):
    __tablename__ = 'subscription'
    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey('business.id'), nullable=False)
    day = Column(Float, nullable=False)
    start_day = Column(String(10), nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.datetime.utcnow())

    business = relationship('Business', back_populates='subscription')

