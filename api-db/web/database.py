from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import asyncpg
from .models import ApiKey
from .models import Base

SQLALCHEMY_DATABASE_URL = "postgresql://av:password@192.168.224.1:5432/av"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def get_pg_conn():
    conn = await asyncpg.connect(SQLALCHEMY_DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

