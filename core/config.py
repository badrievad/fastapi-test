from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    DB_URL: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    DB_ECHO: bool = True
    API_V1_PREFIX: str = "/api/v1"


settings = Settings()
