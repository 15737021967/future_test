import asyncio
import dataclasses
import datetime
import decimal
import json

import redis

from ezreal import config

from asyncio import Future
from typing import List
from ezreal.common.logging import logger


class RedisClient:
    """
    封装 redis client
    """

    def __init__(self):
        self.prefix = "feature_"
        self.client = redis.Redis(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            db=config.REDIS_DB,
            password=config.REDIS_PASSWORD,
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


date_format = '%Y-%m-%d'
time_format = '%H:%M'
time_ms_format = '%H:%M:%S'
datetime_format = ' '.join([date_format, time_format])
datetime_ms_format = ' '.join([date_format, time_ms_format])
datetime_hour_format = ' '.join([date_format, '%H:00'])


class WebSDKJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o == o.to_integral_value():
                return int(o)
            return float(o)
        elif dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        elif isinstance(o, datetime.datetime):
            return o.strftime(datetime_format)
        elif isinstance(o, datetime.date):
            return o.strftime(date_format)
        elif isinstance(o, datetime.time):
            return o.strftime(time_format)
        elif isinstance(o, bytes):
            return o.decode('utf-8')
        return super().default(o)


class DecimalEncoder(WebSDKJSONEncoder):
    def default(self, o):
        try:
            return super().default(o)
        except TypeError:
            logger.error("json encoder error", stack_info=True)
            return ""


response_encoder = DecimalEncoder(indent=None, separators=(',', ':'))




