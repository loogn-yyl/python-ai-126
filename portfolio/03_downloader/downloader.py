# p7_download_progress.py 给下载器加进度：每完成一个打印 已完成 3/5，注意这个计数也要考虑线程安全
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

URLS = [f"file{i}.zip" for i in range(1, 6)]

def download(item):
    i, url = item
    time.sleep(0.02 * i)
    return f"{url} 下载完成"

total = len(URLS)
with ThreadPoolExecutor(max_workers=3) as pool:
    futures = {pool.submit(download, it): it[1] for it in enumerate(URLS, 1)}
    for n, f in enumerate(as_completed(futures), 1):
        print(f"已完成 {n}/{total} {f.result()}")