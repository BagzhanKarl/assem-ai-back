import httpx
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import whatsapp
from database import SessionLocal, engine
import models, crud, schemas, open

# Создание таблиц в БД, если их нет
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_meet_on_top_manager(chat_id: str, name: str, desc: str, date: str, time: str, db: Session = Depends(get_db)):
    meet = models.Calendar(
        chat_id=chat_id,
        name=name,
        date=date,
        time=time,
        user_data=desc
    )
    db.add(meet)
    db.commit()
    db.refresh(meet)

    return meet
@app.post("/webhook/")
async def create_webhook_message(webhook: schemas.WebhookCreate, db: Session = Depends(get_db)):
    last_chat = None
    for message in webhook.messages:
        chat = crud.create_webhook_message(db=db, webhook_message=message)
        last_chat = chat  # Сохраняем последнее созданное сообщение

    if last_chat:
        async with httpx.AsyncClient() as client:
            response = await client.post(f'http://127.0.0.1:8000/ai/generate/{last_chat}', timeout=10)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", "Error generating response"))

    return {"detail": "Messages saved and processed successfully"}


@app.post('/settings/systemmessages')
def create_system_message(AddSystem: schemas.AddSystem, db: Session = Depends(get_db)):
    crud.create_system_mesasges(db=db, webhook_message=AddSystem)
    return {"status": "success"}

@app.get('/settings/systemmessages')
def get_all_system(db: Session = Depends(get_db)):
    system = db.query(models.Messages).filter(models.Messages.role == 'system').all()
    return {"status": "success", "data": system}

@app.put('/settings/systemmessages/{message_id}')
def update_system_message(message_id: int, update_data: schemas.AddSystem, db: Session = Depends(get_db)):
    # Ищем сообщение по ID
    system_message = db.query(models.Messages).filter(models.Messages.id == message_id, models.Messages.role == 'system').first()

    if not system_message:
        raise HTTPException(status_code=404, detail="System message not found")

    # Обновляем поля
    system_message.content = update_data.content
    system_message.key = update_data.key

    db.commit()
    db.refresh(system_message)

    return {"status": "success", "data": system_message}

@app.delete('/settings/systemmessages/{message_id}')
def delete_system_message(message_id: int, db: Session = Depends(get_db)):
    # Ищем сообщение по ID
    system_message = db.query(models.Messages).filter(models.Messages.id == message_id, models.Messages.role == 'system').first()

    if not system_message:
        raise HTTPException(status_code=404, detail="System message not found")

    # Удаляем сообщение
    db.delete(system_message)
    db.commit()

    return {"status": "success", "message": "System message deleted"}

@app.post('/message/array')
def generate_message_array(chat_id: str, db: Session = Depends(get_db)):
    array = crud.create_message_array(chat_id, db)
    return array

@app.post('/ai/generate/{chat_id}')
async def generate_answere(chat_id: str, db: Session = Depends(get_db)):
    array = crud.create_message_array(chat_id, db)
    ans = open.generate_ai('', array)
    crud.save_answere(chat_id, 'assistant', ans, 'assistant', db)
    whatsapp.sent_text_message(ans, chat_id, 'THjJOt2vo26nYYj4IbqKXVqInFv1wx55')
    return ans