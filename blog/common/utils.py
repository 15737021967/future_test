import asyncio

from asyncio import Future
from typing import List


def init_async_task(tasks: List[Future]):

    if not tasks:
        return []
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    return [task.result() for task in tasks]




