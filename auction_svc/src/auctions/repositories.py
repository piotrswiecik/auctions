from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from auctions import models


class ItemRepository:

    def __init__(self, session: AsyncSession):
        self._session = session
        self._model_cls = models.Item

    async def get_all(self):
        qry = select(self._model_cls)
        result = await self._session.execute(qry)
        return result.scalars().all()