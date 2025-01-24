import os
from pydantic_settings import BaseSettings
import logging
from dotenv import load_dotenv

class Settings(BaseSettings):
    DB_USER: str = os.environ.get('DB_USER')
    DB_HOST: str = os.environ.get('DB_HOST_AMVERA') if int(os.environ.get('AMVERA', 0)) == 1 else os.environ.get('DB_HOST')
    DB_NAME: str = os.environ.get('DB_NAME')
    DB_PORT: int = os.environ.get('DB_PORT')
    DB_PASSWORD: str = os.environ.get('DB_PASSWORD')
    
    def get_db_url(self):
        try:
            return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        except Exception as e:
            logging.error('ERROR WHILE URL FROM TO DB', e)
            raise

load_dotenv()
settings = Settings()
