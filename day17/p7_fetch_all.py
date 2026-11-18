# p7_fetch_all.py 并发前的准备：写 fetch_all(urls)，串行请求（用 time.sleep(0.1) 模拟网络延迟），打印总耗时
import time

def fetch(url):
    time.sleep(0.1)
    return f"{url} 的内容"

def fetch_all(urls):
    return [fetch(u) for u in urls]

urls = [f"https://site{i}.com" for i in range(1, 6)]

start = time.perf_counter()
results = fetch_all(urls)
elapsed = time.perf_counter() - start

print("抓到", len(results), "个页面")
print(f"总耗时 {elapsed:.2f} 秒")
print(f"平均每个 {elapsed / len(urls):.1f} 秒")