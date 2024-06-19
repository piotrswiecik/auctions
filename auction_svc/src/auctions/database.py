from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from auctions.config import settings


class Base(AsyncAttrs, DeclarativeBase):
    pass


def get_db_conn_string(is_async: bool = True) -> str:
    driver = "postgresql+asyncpg" if is_async else "postgresql+psycopg"

    return "".join(
        [
            f"{driver}://",
            f"{settings.db_user}:{settings.db_password}@",
            f"{settings.db_host}:{settings.db_port}/",
            f"{settings.db_name}",
        ]
    )


async_engine = create_async_engine(get_db_conn_string(), echo=True)


async def get_db():
    async with AsyncSession(async_engine) as session:
        async with session.begin():
            yield session


# models section to be moved


class Sample(Base):
    __tablename__ = "sample"
    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[str] = mapped_column()
