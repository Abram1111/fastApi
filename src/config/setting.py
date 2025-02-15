from typing import Any , Dict ,Optional
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, field_validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    APP_NAME: str  = "FastAPI"
    DOMAIN: str
    DEBUG_MODE: bool = True
    BACKEND_PORT: int = 5000

    @field_validator("BACKEND_PORT")
    @classmethod
    def setPortDefault(cls, v:str):
        if v :
            return v
        return 8000
    

settings = Settings()