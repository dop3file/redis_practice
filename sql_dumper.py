import asyncio

import redis

from database import async_session_maker
from hot_storage import HotStorage
from persistence_storage import PersistenceStorage


persistence_storage = PersistenceStorage()
hot_storage = HotStorage(
    redis.Redis(
        host="localhost",
        port=6379
    )
)


async def main():
    while True:
        async with async_session_maker() as session:
            for parse_result in await hot_storage.get_results():
                await persistence_storage.add_book(session, parse_result.decode("utf-8"))
            await session.commit()
            await hot_storage.clear_results()
        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())