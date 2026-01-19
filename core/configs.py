
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar
from sqlalchemy.orm.decl_api import DeclarativeMeta
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
   DB_URL: str
   DBBaseModel: ClassVar[DeclarativeMeta] = declarative_base()
   MEDIA: ClassVar[Path] = Path("media")
   API_V1_STR: str = "/api/v1"

   class Config:
     env_file = BASE_DIR / ".env"
     env_file_encoding = "utf-8"
     case_sensitive = True

settings: Settings = Settings()
