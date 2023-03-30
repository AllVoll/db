from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, schemas

router = APIRouter()

# Обработчик для сохранения API-ключа
@router.post("/api/key")
def save_api_key(api_key: schemas.ApiKey, db: Session = Depends(get_db)):
    db_api_key = models.ApiKey(api_key=api_key.api_key)
    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)
    return {"message": "API key saved successfully"}

# Функция зависимости для получения экземпляра базы данных
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
