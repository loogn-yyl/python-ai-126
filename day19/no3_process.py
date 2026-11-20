# no.3
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

def cpu_work(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

N = 4_000_000
# N = 40_000_000    # 测试更多任务
TASKS = [N, N]

if __name__ == "__main__":
    t0 = time.perf_counter()
    r1 = [cpu_work(n) for n in TASKS]
    print(f"单线程   : {time.perf_counter() - t0:.2f} 秒")

    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=2) as pool:
        r2 = list(pool.map(cpu_work, TASKS))
    print(f"线程池 2 : {time.perf_counter() - t0:.2f} 秒")

    t0 = time.perf_counter()
    with ProcessPoolExecutor(max_workers=2) as pool:
        r3 = list(pool.map(cpu_work, TASKS))
    print(f"进程池 2 : {time.perf_counter() - t0:.2f} 秒")

    print("结果一致:", r1 == r2 == r3)