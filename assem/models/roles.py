# models/roles.py
import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from assem.db.database import Base

class Role(Base):
    __tablename__ = "system_role"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(191), index=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updatet_at = Column(DateTime, default=datetime.datetime.utcnow)

    permission = relationship('Permission', back_populates="role")
    user = relationship('User', back_populates='role')
class Permission(Base):
    __tablename__ = "system_permission"
    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer, ForeignKey("system_role.id"), nullable=False)
    function = Column(String(191), nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updatet_at = Column(DateTime, default=datetime.datetime.utcnow)

    role = relationship('Role', back_populates='permission')
