# p2_top_three.py 找出响应最大的 3 个请求：按 size 降序，输出 (path, size)
import re
from collections import Counter

LOG = """127.0.0.1 - - [13/Nov/2026:02:15:33 +0800] "GET /index.html HTTP/1.1" 200 512
10.0.0.5 - - [13/Nov/2026:02:15:35 +0800] "POST /api/login HTTP/1.1" 200 128
10.0.0.5 - - [13/Nov/2026:02:15:36 +0800] "GET /api/user HTTP/1.1" 401 64
192.168.1.9 - - [13/Nov/2026:02:16:01 +0800] "GET /static/app.js HTTP/1.1" 304 0
127.0.0.1 - - [13/Nov/2026:02:16:10 +0800] "GET /index.html HTTP/1.1" 200 980"""

PATTERN = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - '
    r'\[(?P<time>[^\]]+)\] '
    r'"(?P<method>[A-Z]+) (?P<path>\S+) HTTP/[\d.]+" '
    r'(?P<status>\d{3}) (?P<size>\d+)'
)

rows = [m.groupdict() for m in PATTERN.finditer(LOG)]

for r in rows:
    r["size"] = int(r["size"])
top = sorted(rows, key=lambda r: -r["size"])[:3]
print("最大的 3 个:", [(r["path"], r["size"]) for r in top])