from redis import Redis

from parse_utils import ParsedResult


class HotStorage:
    QUEUE_NAME = "books"

    def __init__(self, redis: Redis):
        self.client = redis

    async def add_result(self, parsed_result: ParsedResult):
        self.client.rpush(self.QUEUE_NAME, parsed_result.title)

    async def get_results(self):
        return self.client.lrange(self.QUEUE_NAME, 0, -1)

    async def clear_results(self):
        self.client.delete(self.QUEUE_NAME)