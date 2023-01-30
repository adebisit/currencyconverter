from pydantic import BaseSettings

class Settings(BaseSettings):
    ATLAS_URI: str
    DB_NAME: str
    API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()