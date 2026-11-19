# no.5
import asyncio
import time

def sync_fetch(url):
    time.sleep(0.1)
    return url

async def async_fetch(url):
    await asyncio.sleep(0.1)
    return url

urls = [f"https://site{i}.com" for i in range(1, 6)]

t0 = time.perf_counter()
sync_results = [sync_fetch(u) for u in urls]
sync_time = time.perf_counter() - t0

async def main():
    t0 = time.perf_counter()
    results = await asyncio.gather(*(async_fetch(u) for u in urls))
    return results, time.perf_counter() - t0

async_results, async_time = asyncio.run(main())

print(f"同步 {len(urls)} 个: {sync_time:.1f} 秒")
print(f"异步 {len(urls)} 个: {async_time:.1f} 秒")
print("结果一致:", sync_results == async_results)
print(f"异步 {len(urls)} 个: {async_time:.5f} 秒")
print("异步耗时 ≈ 单次延迟, 不随数量增长")