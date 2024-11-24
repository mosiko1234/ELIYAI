from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    db_connection_string: str = "sqlite:///db.sqlite3"

    class Config:
        env_file = ".env"

settings = Settings()
