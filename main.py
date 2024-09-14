import asyncio
import logging
import time

import redis
from bs4 import BeautifulSoup

import aiohttp

from hot_storage import HotStorage
from parse_utils import TITLE_SELECTOR, ParsedResult


logging.basicConfig(level=logging.DEBUG)


async def parse(url: str) -> ParsedResult:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), "lxml")
            parsed_result = ParsedResult(
                title=soup.select_one(TITLE_SELECTOR).get_text()
            )
            logging.debug(parsed_result)
            return parsed_result


async def main():
    hot_storage = HotStorage(
        redis.Redis(
            host="localhost",
            port=6379,
            db=0,
        )
    )
    while True:
        urls = [
            "https://www.litres.ru/audiobook/erofey-trofimov/sotnya-kazachiy-krest-seriya-4-71056168/",
            "https://www.litres.ru/audiobook/vladimir-poselyagin/okopnik-71015158/",
            "https://www.litres.ru/audiobook/vladimir-poselyagin/zhnec-3-snayper-70729657/"
        ]
        tasks = [parse(url) for url in urls]
        for finished_task in asyncio.as_completed(tasks):
            await hot_storage.add_result(await finished_task)


if __name__ == "__main__":
    asyncio.run(main())