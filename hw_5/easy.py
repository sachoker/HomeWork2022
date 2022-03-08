# -*- coding: utf-8 -*-
import asyncio

import aiofiles
import aiohttp


async def save_pict(pict, n):
    async with aiofiles.open(fr'C:\Users\Sanya\PycharmProjects\HomeWork\hw_5\artifacts\easy\pict{n}.jpeg',
                             mode='bw+') as file:
        print('file opened')
        await file.write(pict)


async def get_pict(session):
    site = 'https://picsum.photos/300'
    async with session.get(site) as pict:
        print('Pict downloaded')
        res = await pict.read()
        return res


async def download_picts(n):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(n):
            task = asyncio.create_task(get_pict(session))
            tasks.append(task)
        a = asyncio.gather(*tasks)
        await a
        return a


async def save_picts(n: int, picts: list):
    tasks = []
    for i, p in enumerate(picts):
        tasks.append(asyncio.create_task(save_pict(p, i)))
    a = asyncio.gather(*tasks)
    await a


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    n = int(input())
    try:
        # loop.create_task(download_picts(n))
        # loop.run_forever()
        task = loop.create_task(download_picts(n))
        res = loop.run_until_complete(task)
        res = res.result()
        task = loop.create_task(save_picts(n, res))
        loop.run_until_complete(task)
    except KeyboardInterrupt as e:
        print('Keyboard stoped')
    finally:
        loop.close()
