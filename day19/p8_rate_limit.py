# p8_rate_limit.py 限流版下载器：max_workers=2 处理 6 个任务，打印每个任务的开始和结束，从输出里数出同时在跑几个
import time
from concurrent.futures import ThreadPoolExecutor

DELAY = 0.1
TASKS = list(range(1, 7))

def download(t):
    print(f"{t} 下载开始")
    time.sleep(DELAY)
    print(f"{t} 下载结束")

with ThreadPoolExecutor(max_workers=2) as pool:
    list(pool.map(download, TASKS))