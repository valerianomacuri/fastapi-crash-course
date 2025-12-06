from pydantic import BaseSettings


class Settings(BaseSettings):
    uvicorn_port: int = 8000

    class Config:
        env_file = ".env"


settings = Settings()
