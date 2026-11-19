# no.4-1
import asyncio
import time

async def work_blocking(name, sec):
    print(f"  开始 {name}")
    time.sleep(sec)    # 阻塞！整个事件循环停在这儿
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

# no.4-2
import asyncio
import time

def blocking_request(url):
    """假设这是 D017 里那个 requests.get, 同步阻塞"""
    time.sleep(0.1)
    return f"{url} 的标题"

async def fetch(url):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, blocking_request, url)

async def main():
    urls = [f"https://site{i}.com" for i in range(1, 6)]
    t0 = time.perf_counter()
    results = await asyncio.gather(*(fetch(u) for u in urls))
    print(f"耗时 {time.perf_counter() - t0:.1f} 秒")
    print("第一条:", results[0])

asyncio.run(main())

# no.4-3
import os

print(f"ThreadPoolExcutor 的默认上限:", min(32, os.cpu_count() + 4))