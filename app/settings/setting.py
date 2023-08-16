import os

class Settings:
    PROJECT_NAME: str = "pythonBackEnd"
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    DATABASE_URL: str = os.environ.get("DATABASE_URL")

settings = Settings()
