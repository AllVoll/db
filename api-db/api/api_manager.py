from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Инициализируем объект шаблонизатора Jinja2Templates
templates = Jinja2Templates(directory="templates")


# Создаем функцию зависимости для получения сессии базы данных
def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        if db:
            db.close()


# Рендеринг страницы с формой для добавления нового ключа
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("api_manager.html", {"request": request})


# Добавление нового ключа в базу данных
@app.post("/api_keys/", response_model=schemas.ApiKey)
def create_api_key(api_key: schemas.ApiKeyCreate, db: Session = Depends(get_db)):
    return crud.create_api_key(db=db, api_key=api_key)
