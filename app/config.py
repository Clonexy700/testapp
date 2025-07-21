from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = 'sqlite:///reviews.db'
    HF_MODEL: str = "blanchefort/rubert-base-cased-sentiment"
    class Config:
        env_file = '.env'


@lru_cache()
def get_settings() -> Settings:
    return Settings()


