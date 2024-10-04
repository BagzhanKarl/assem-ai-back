from sqlalchemy.orm import Session
import models, schemas

def create_webhook_message(db: Session, webhook_message: schemas.WebhookMessageCreate):
    db_message = models.WebhookMessage(
        message_id=webhook_message.id,
        from_me=str(webhook_message.from_me),
        type=webhook_message.type,
        chat_id=webhook_message.chat_id,
        timestamp=webhook_message.timestamp,
        source=webhook_message.source,
        text=webhook_message.text.body,  # Извлекаем текст из body
        from_user=webhook_message.from_user,
        from_name=webhook_message.from_name
    )

    messageArray = models.Messages(
        chat_id=webhook_message.chat_id,
        role='user',
        content=webhook_message.text.body,
        name='user',
    )
    db.add(messageArray)
    db.add(db_message)
    db.commit()
    db.refresh(messageArray)
    db.refresh(db_message)
    return messageArray.chat_id

def create_system_mesasges(db: Session, webhook_message: schemas.AddSystem):

    messageArray = models.Messages(
        chat_id='all',
        role='system',
        content=webhook_message.content,
        name='system',
    )
    db.add(messageArray)
    db.commit()
    db.refresh(messageArray)
    return messageArray

def create_message_array(chatid: str, db: Session):
    messages = []
    system_messages = db.query(models.Messages).filter(models.Messages.role == 'system').all()

    for message in system_messages:
        messages.append({
            "role": message.role,
            "content": message.content,
            "name": message.name
        })

    chat_message = db.query(models.Messages).filter(models.Messages.chat_id == chatid).all()
    for message in chat_message:
        messages.append({
            "role": message.role,
            "content": message.content,
            "name": message.name
        })

    messages.append({
        "role": "system",
        "content": f"ID чата: {chatid}",
        "name": "system",
    })
    return messages

def save_answere(chat_id: str, role: str, content: str, name: str, db: Session):
    message = models.Messages(
        chat_id=chat_id,
        role=role,
        content=content,
        name=name,
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message