from sqlalchemy import Column, Integer, String
from .base import Base

class ApiKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    binance_key = Column(String, unique=True, index=True)
    binance_secret = Column(String, unique=True, index=True)
