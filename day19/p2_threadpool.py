# p2_threadpool.py 改用线程池：把上题换成 ThreadPoolExecutor，数一下代码少了多少行
import time
from concurrent.futures import ThreadPoolExecutor

DELAY = 0.1

t0 = time.perf_counter()
with ThreadPoolExecutor(max_workers=3) as pool:
    list(pool.map(time.sleep, [DELAY] * 3))
print(f"线程池: {time.perf_counter() - t0:.1f} 秒")