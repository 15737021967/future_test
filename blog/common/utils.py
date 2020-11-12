import asyncio
import redis

from blog import env

from asyncio import Future
from typing import List


class RedisClient:
    """
    封装 redis client
    """

    def __init__(self):
        self.prefix = "blog_"
        self.client = redis.Redis(
            host=env.REDIS_HOST,
            port=env.REDIS_PORT,
            db=env.REDIS_DB,
            password=env.REDIS_PASSWORD,
            decode_responses=True
        )

    def set(self, name, value):
        name = self.generate_key(name)
        return self.client.set(name, value)

    def setex(self, name, time, value):
        name = self.generate_key(name)
        self.client.setex(name, time, value)

    def get(self, name):
        name = self.generate_key(name)
        return self.client.get(name)

    def delete(self, name):
        name = self.generate_key(name)
        return self.client.delete(name)

    def generate_key(self, name):
        return self.prefix + name


redis_client = RedisClient()


def init_async_task(tasks: List[Future]):

    if not tasks:
        return []
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    return [task.result() for task in tasks]




