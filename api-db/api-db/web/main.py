from fastapi import FastAPI, Request, Form, Depends, HTTPException, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import asyncpg
from sqlalchemy.orm import Session
from . import schemas
from db import database

app = FastAPI()

api_router = APIRouter()

app.mount("/static", StaticFiles(directory="/app/web/static"), name="static")

templates = Jinja2Templates(directory="/app/web/templates")

app.include_router(api_router, prefix="/api")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request, db: Session = Depends(database.get_db)):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/tradingview_widget")
async def tradingview_widget(request: Request, db: Session = Depends(database.get_db)):
    return templates.TemplateResponse("tradingview_widget.html", {"request": request})

@app.get("/settings")
async def settings(request: Request, db: Session = Depends(database.get_db)):
    return templates.TemplateResponse("settings.html", {"request": request})

@app.get("/api_manager")
async def api_manager(request: Request, db: Session = Depends(database.get_db)):
    return templates.TemplateResponse("api_manager.html", {"request": request})

@app.get("/api_keys")
async def api_manager(request: Request, db: Session = Depends(database.get_db)):
    return templates.TemplateResponse("api_keys.html", {"request": request})

@app.post("/api/api_manager")
async def add_api_key(request: Request, name: str = Form(...), binance_key: str = Form(...), binance_secret: str = Form(...), db: Session = Depends(database.get_db)):
    api_key = schemas.ApiKey(name=name, binance_key=binance_key, binance_secret=binance_secret)
    db.add(api_key)
    db.commit()
    return templates.TemplateResponse("api_manager.html", {"request": request})