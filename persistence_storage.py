from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from parse_utils import ParsedResult


class PersistenceStorage:
    async def add_book(self, session: AsyncSession, title: str) -> None:
        await session.execute(text(f'INSERT INTO books  (title) VALUES (:title)'), {"title": title})