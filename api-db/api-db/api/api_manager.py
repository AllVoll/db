from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .. import database, schemas


router = APIRouter()

templates = Jinja2Templates(directory="/app/web/templates")


@router.get("/api_manager", response_class=HTMLResponse)
async def read_api_manager(request: Request, db: Session = Depends(database.get_db)):
    api_keys = db.query(schemas.ApiKey).all()
    return templates.TemplateResponse("api_manager.html", {"request": request, "api_keys": api_keys})
