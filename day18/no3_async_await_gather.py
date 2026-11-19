# no.3-1
import asyncio
import time

async def work(name, sec):
    await asyncio.sleep(sec)
    return name

async def seq():
    t0 = time.perf_counter()
    out = []
    out.append(await work("A", 0.3))
    out.append(await work("B", 0.2))
    out.append(await work("C", 0.1))
    print("顺序 await:", out, f"{time.perf_counter() - t0:.1f} 秒")

asyncio.run(seq())

# no.3-2
import asyncio
import time

async def work(name, sec):
    print(f"  开始 {name}")
    await asyncio.sleep(sec)
    print(f"  结束 {name}")
    return name

async def main():
    t0 = time.perf_counter()
    results = await asyncio.gather(
        work("A", 0.3), work("B", 0.2), work("C", 0.1)
    )
    print("结果:", results)
    print(f"耗时 {time.perf_counter() - t0:.1f} 秒")

asyncio.run(main())