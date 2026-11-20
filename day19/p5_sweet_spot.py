# p5_sweet_spot.py 测出线程池的甜点：5 个任务，分别用 max_workers = 1 / 2 / 5 / 10，各跑一次记耗时，解释为什么 10 不比 5 快
import time
from concurrent.futures import ThreadPoolExecutor

DELAY = 0.1
TASKS = [DELAY] * 5

for w in [1, 2, 5, 10]:
    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=w) as pool:
        list(pool.map(time.sleep, TASKS))
    print(f"max_workers={w:<2} : {time.perf_counter() - t0:.1f} 秒")