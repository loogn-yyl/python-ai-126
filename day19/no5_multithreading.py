# no.5
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

URLS = [f"https://site{i}.com/file{i}.zip" for i in range(1, 6)]

def download(item):
    i, url = item
    time.sleep(0.05 * i)
    if "site3" in url:
        raise ConnectionError("连不上 site3")
    return f"{url} -> {100 * i} 字节"

def batch(urls, workers=3):
    ok, fail = [], []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(download, it): it[1] for it in enumerate(urls, 1)}
        for f in as_completed(futures):
            url = futures[f]
            try:
                ok.append(f.result())
                print(f"完成 {url}")
            except Exception as e:
                fail.append(url)
                print(f"失败 {url} ({type(e).__name__})")
    return ok, fail

ok, fail = batch(URLS)
print()
print(f"成功 {len(ok)} 个, 失败 {len(fail)} 个")
print("失败清单:", fail)