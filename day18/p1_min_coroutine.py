# p1_min_coroutine.py 最小协程：写一个 async def ping() 返回 "pong"，用 asyncio.run 拿到结果
import asyncio

async def ping():
    return "pong"

print("拿到结果:", asyncio.run(ping()))