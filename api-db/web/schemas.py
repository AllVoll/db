from datetime import datetime
from typing import List

from pydantic import BaseModel


class ApiKeyBase(BaseModel):
    name: str
    binance_key: str
    binance_secret: str


class ApiKeyCreate(ApiKeyBase):
    pass


class ApiKey(ApiKeyBase):
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    api_keys: List[ApiKey] = []

    class Config:
        orm_mode = True
