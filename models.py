from sqlalchemy import Column, Integer, String, BigInteger, JSON
from database import Base

class WebhookMessage(Base):
    __tablename__ = "webhook_messages"

    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(String(255))
    from_me = Column(String(10))
    type = Column(String(50))
    chat_id = Column(String(255))
    timestamp = Column(BigInteger)
    source = Column(String(255))
    text = Column(String(255))  # Здесь теперь храним текст из body
    from_user = Column(String(255))
    from_name = Column(String(255))

class Messages(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(String(255))
    role = Column(String(255))
    content = Column(String(500))
    name = Column(String(255))
