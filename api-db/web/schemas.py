# schemas.py
from typing import List, Optional
from pydantic import BaseModel

class ApiKeyBase(BaseModel):
    name: str
    binance_key: str
    binance_secret: str

class ApiKeyCreate(ApiKeyBase):
    id: Optional[int] = None

class ApiKey(ApiKeyBase):
    id: int

    class Config:
        orm_mode = True
