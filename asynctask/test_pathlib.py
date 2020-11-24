import asyncio


async def a(x):
    while x > 0:
        print('a:', x)
        await asyncio.sleep(0.5)
        x -= 1


async def b(x):
    while x > 0:
        print('b:', x)
        await asyncio.sleep(1.8)
        x -= 1


async def c(x):
    while x > 0:
        print('c:', x)
        await asyncio.sleep(1.5)
        x -= 1


loop = asyncio.get_event_loop()
tasks = [a(2), b(2), c(2)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
