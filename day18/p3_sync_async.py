# p3_sync_async.py 顺序 vs 并发：三个任务分别睡 0.3 / 0.2 / 0.1，先用顺序 await，再用 gather，各打印耗时
import asyncio
import time

async def work(name, sec):
    await asyncio.sleep(sec)
    return name

async def main():
    t0 = time.perf_counter()
    a = await work("A", 0.3)
    b = await work("B", 0.2)
    c = await work("C", 0.1)
    print(f"顺序 await: {[a, b, c]} {time.perf_counter() - t0:.1f} 秒")

    t0 = time.perf_counter()
    got = await asyncio.gather(
        work("A", 0.3), work("B", 0.2), work("C", 0.1)
    )
    print(f"gather    : {got} {time.perf_counter() - t0:.1f} 秒")

asyncio.run(main())