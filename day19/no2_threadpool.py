# no.2
import time
from concurrent.futures import ThreadPoolExecutor

URLS = [f"https://site{i}.com" for i in range(1, 6)]
DELAY = 0.1

def fetch(url):
    time.sleep(DELAY)    # 模拟网络等待
    return f"{url} 的标题"

t0 = time.perf_counter()
serial = [fetch(u) for u in URLS]
print(f"串行   : {time.perf_counter() - t0:.1f} 秒")

t0 = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as pool:
    parallel = list(pool.map(fetch, URLS))
print(f"线程池 : {time.perf_counter() - t0:.1f} 秒")

print("结果一致:", serial == parallel)
print("第一条  :", serial[0], parallel[0])