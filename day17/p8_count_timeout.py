# p8_count_timeout.py 加超时分类统计：给 fetch_all 加返回值，统计「成功 / 超时 / 其他失败」各几个
import time
from collections import Counter

def fetch(url):
    time.sleep(0.1)
    if "timeout" in url:
        return "timeout"
    if "bad" in url:
        return "error"
    return "ok"

def fetch_all(urls):
    stats = Counter()
    for u in urls:
        stats[fetch(u)] += 1
    return stats

urls =[
    "https://a.com", "https://timeout1.com", "https://b.com",
    "https://bad1.com", "https://timeout2.com"
]
s = fetch_all(urls)
print("成功:", s["ok"], "超时:", s["timeout"], "其他:", s["error"])
print("总数对得上:", sum(s.values()) == len(urls))