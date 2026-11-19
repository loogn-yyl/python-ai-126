# p4_timesleep_asyncsleep.py 把 time.sleep 换成 asyncio.sleep：拿第 5 节第一个坑的代码，只改这一处，看耗时从 0.6 变成多少
import asyncio
import time

async def work_blocking(name, sec):
    print(f"  开始 {name}")
    await asyncio.sleep(sec)     # 原来是 time.sleep(sec)
    print(f"  结束 {name}")

async def main():
    t0 = time.perf_counter()
    await asyncio.gather(
        work_blocking("A", 0.3),
        work_blocking("B", 0.2),
        work_blocking("C", 0.1)
    )
    print(f"耗时 {time.perf_counter() - t0:.1f} 秒")

asyncio.run(main())