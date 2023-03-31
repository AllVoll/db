from pydantic import BaseModel

class ApiKey(BaseModel):
    name: str
    binance_key: str
    binance_secret: str
