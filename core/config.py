from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent

DB_PATH = BASE_DIR / 'db.sqlite3'

class DbSettings(BaseModel):
    url: str = f'sqlite+aiosqlite:///{DB_PATH}'
    echo: bool = False

class Settings(BaseSettings):
    db: DbSettings = DbSettings()


settings = Settings()