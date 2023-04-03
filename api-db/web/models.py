from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .base import Base



#Base = declarative_base()

#metadata = Base.metadata

class ApiKey(Base):
    __tablename__ = "api_keys"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    binance_key = Column(String)
    binance_secret = Column(String)

    def __repr__(self):
        return f"<ApiKey(id={self.id}, name='{self.name}')>"
    
#Table('api_keys', metadata, extend_existing=True)

