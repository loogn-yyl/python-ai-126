# p8_timeout.py 加超时：给一个睡 2 秒的任务套 asyncio.wait_for(..., timeout=0.5)，抓住 TimeoutError 并打印
import asyncio

async def slow():
    await asyncio.sleep(2)
    return "终于好了"

async def fast():
    await asyncio.sleep(0.01)
    return "很快"

async def main():
    try:
        r = await asyncio.wait_for(slow(), timeout=0.5)
        print("0.5 秒内顺利完成, 拿到:", r)
    except TimeoutError:
        print("超时了, 0.5 秒内没完成")

    try:
        r = await asyncio.wait_for(fast(), timeout=0.5)
        print("0.5 秒内顺利完成, 拿到:", r)
    except TimeoutError:
        print("超时了, 0.5 秒内没完成")

asyncio.run(main())