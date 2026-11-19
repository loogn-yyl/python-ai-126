# p6_return_exceptions.py 异常处理：gather 里有一个会抛异常，用return_exceptions=True 看看结果列表里是什么
import asyncio

async def ok(name):
    await asyncio.sleep(0.05)
    return name

async def boom():
    await asyncio.sleep(0.05)
    raise ValueError("坏了")

async def main():
    got = await asyncio.gather(ok("a"), boom(), ok("c"), return_exceptions=True)
    print("结果列表:", [type(x).__name__ if isinstance(x, Exception) else x for x in got])
    print("异常本身:", got[1])

    try:
        await asyncio.gather(ok("a"), boom())
    except ValueError as e:
        print("不设标志时:", type(e).__name__, e)

asyncio.run(main())