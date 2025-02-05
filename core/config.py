from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db.sqlite3"


class Database(BaseSettings):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = True


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: Database = Database()


settings = Settings()
