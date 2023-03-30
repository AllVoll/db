from fastapi import FastAPI, Request, Form, Depends, HTTPException
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

app.mount("/static", StaticFiles(directory="/app/web/static"), name="static")

templates = Jinja2Templates(directory="/app/web/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request, db: Session = Depends(database.get_db)):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/tradingview_widget")
async def tradingview_widget(request: Request, db: Session = Depends(database.get_db)):
    return templates.TemplateResponse("tradingview_widget.html", {"request": request})


@app.get("/settings")
async def tradingview_widget(request: Request, db: Session = Depends(database.get_db)):
    return templates.TemplateResponse("settings.html", {"request": request})


@app.get("/api_manager")
async def api_manager(request: Request, db: Session = Depends(database.get_db)):
    return templates.TemplateResponse("api_manager.html", {"request": request})

@app.get("/api_keys")
async def api_manager(request: Request, db: Session = Depends(database.get_db)):
    return templates.TemplateResponse("api_keys.html", {"request": request})






