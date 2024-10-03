# models/ai.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from assem.db.database import Base
import datetime

class AiSettings(Base):
    __tablename__ = 'ai_settings'

    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String(60), nullable=False)
    role = Column(String(60), nullable=False)
    content = Column(Text(25000), nullable=False)
