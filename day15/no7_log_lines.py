# no.7
import re

LOG_LINES = """127.0.0.1 - - [13/Nov/2026:02:15:33 +0800] "GET /index.html HTTP/1.1" 200 512
10.0.0.5 - - [13/Nov/2026:02:15:35 +0800] "POST /api/login HTTP/1.1" 200 128
10.0.0.5 - - [13/Nov/2026:02:15:36 +0800] "GET /api/user HTTP/1.1" 401 64
192.168.1.9 - - [13/Nov/2026:02:16:01 +0800] "GET /static/app.js HTTP/1.1" 304 0
坏行这一行故意不符合格式
127.0.0.1 - - [13/Nov/2026:02:16:10 +0800] "GET /missing HTTP/1.1" 404 32""".split()

PATTERN = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - -'
    r'\[(?P<time>[^\]]+)\] '
    r'"(?P<method>[A-Z]+) (?P<path>\S+) HTTP/[\d.]+" '
    r'(?P<status>\d{3}) (?P<size>\d+)'
)

rows, bad = [], []
for line in LOG_LINES:
    m = PATTERN.match(line)
    if m:
        rows.append(m.groupdict())
    else:
        bad.append(line)

print("成功解析:", len(rows), "行")
print("解析失败:", len(bad), "行")
print()
for r in rows:
    print(f"{r['ip']:<15} {r['time'][:20]:<20} {r['method']:<4} {r['path']:<18} {r['status']} {r['size']}")