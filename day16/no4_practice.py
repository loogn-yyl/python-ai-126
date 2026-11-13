# no.4
import re
from collections import Counter

LOG = """127.0.0.1 - - [13/Nov/2026:02:15:33 +0800] "GET /index.html HTTP/1.1" 200 512
10.0.0.5 - - [13/Nov/2026:02:15:35 +0800] "POST /api/login HTTP/1.1" 200 128
10.0.0.5 - - [13/Nov/2026:02:15:36 +0800] "GET /api/user HTTP/1.1" 401 64
192.168.1.9 - - [13/Nov/2026:02:16:01 +0800] "GET /static/app.js HTTP/1.1" 304 0
127.0.0.1 - - [13/Nov/2026:02:16:10 +0800] "GET /index.html HTTP/1.1" 200 980
10.0.0.5 - - [13/Nov/2026:03:01:02 +0800] "GET /api/order HTTP/1.1" 500 32
127.0.0.1 - - [13/Nov/2026:03:18:44 +0800] "GET /missing HTTP/1.1" 404 32"""

PATTERN = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - '
    r'\[(?P<time>[^\]]+)\] '
    r'"(?P<method>[A-Z]+) (?P<path>\S+) HTTP/[\d.]+" '
    r'(?P<status>\d{3}) (?P<size>\d+)'
)
HOUR = re.compile(r":(\d{2}):\d{2}:\d{2}")

rows = [m.groupdict() for m in PATTERN.finditer(LOG)]
print("解析:", len(rows), "行")
print()
print("Top IP:")
for ip, n in Counter(r["ip"] for r in rows).most_common(3):
    print(f"  {ip:<15} {n}")
print()
print("Top URL:")
for p, n in Counter(r["path"] for r in rows).most_common(3):
    print(f"  {p:<18} {n}")
print()
print("状态码:")
for s, n in sorted(Counter(r["status"] for r in rows).items()):
    print(f"  {s} {n}")

total = len(rows)
bytes_total = sum(int(r["size"]) for r in rows)
errors = [r for r in rows if r["status"].startswith(("4", "5"))]

print("=" * 42)
print(f"总请求 {total} 条 · 流量 {bytes_total} 字节")
print(f"错误请求 {len(errors)} 条 · 错误率 {len(errors) / total:.1%}")
print("=" * 42)
print()
print("按小时")
for h in sorted({HOUR.search(r["time"]).group(1) for r in rows}):
    n = sum(1 for r in rows if HOUR.search(r["time"]).group(1) == h)
    print(f"  {h} 点  {'#' * n} {n}")