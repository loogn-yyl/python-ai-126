# p7_semophore.py 限流：10 个任务但只允许同时跑 3 个，用 asyncio.Semaphore 实现，打印「当前并发数」
import asyncio

running = 0
peak = 0

async def work(i, sem):
    global running, peak
    async with sem:
        running += 1
        peak = max(peak, running)
        print(f"  任务 {i} 开始, 当前并发 {running}")
        await asyncio.sleep(0.1)
        running -= 1

async def main():
    sem = asyncio.Semaphore(3)
    await asyncio.gather(*(work(i, sem) for i in range(1, 11)))
    print("历史最高并发:", peak)

asyncio.run(main())