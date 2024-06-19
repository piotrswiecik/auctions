from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "auctions"
    db_user: str = "development"
    db_password: str = "development"
    init_db: bool = True


settings = Settings()
