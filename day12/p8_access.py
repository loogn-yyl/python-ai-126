# p8_access.py 日志统计（综合）：造一个 1000 行的日志文件，逐行统计行数、字段数、最长行，再统计每个 IP 的请求数，全程不用 readlines()
import os
import tracemalloc

FIFE = "access.log"

with open(FIFE, "w", encoding="utf-8") as f:
    for i in range(1000):
        f.write(f"10.0.0.{i % 10} GET /page/{i % 7} 200\n")

tracemalloc.start()
lines = words = longest = 0
with open(FIFE, encoding="utf-8") as f:
    for line in f:
        lines += 1
        words += len(line.split())
        longest = max(longest, len(line.rstrip("\n")))
cur, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("行数:", lines)
print("字段数:", words)
print("最长行:", longest,"字符")
print("峰值内存小于 1MB:", peak < 1024 * 1024)

ip_counts = {}
with open(FIFE, encoding="utf-8") as f:
    for line in f:
        ip = line.split()[0]
        ip_counts[ip] = ip_counts.get(ip, 0) + 1
print("IP 数:", len(ip_counts))
print("每个 IP 的请求数都相同:", len(set(ip_counts.values())) == 1)
print("前 3 个 IP:", sorted(ip_counts)[:3])

os.remove(FIFE)