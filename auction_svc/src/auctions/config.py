import os

from pydantic_settings import BaseSettings


# TODO(ps): handle validation/type errors
class Settings(BaseSettings):
    db_host: str = os.environ.get("DB_HOST", "postgres")
    db_port: int = int(os.environ.get("DB_PORT", 5432))
    db_name: str = os.environ.get("DB_NAME", "auctions")
    db_user: str = os.environ.get("DB_USER", "development")
    db_password: str = os.environ.get("DB_PASSWORD", "development")
    init_db: bool = bool(os.environ.get("INIT_DB", False))

    class Config:
        case_sensitive = True
        env_file = ".env.development"


settings = Settings()
