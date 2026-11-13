# p7_collections.py 统计状态码：拿第 6 节那份日志，数出每个状态码各出现几次，按次数排序输出
import re
from collections import Counter

LOG = """127.0.0.1 - - [13/Nov/2026:02:15:33 +0800] "GET /index.html HTTP/1.1" 200 512
10.0.0.5 - - [13/Nov/2026:02:15:35 +0800] "POST /api/login HTTP/1.1" 200 128
10.0.0.5 - - [13/Nov/2026:02:15:36 +0800] "GET /api/user HTTP/1.1" 401 64
192.168.1.9 - - [13/Nov/2026:02:16:01 +0800] "GET /static/app.js HTTP/1.1" 304 0
坏行这一行故意不符合格式
127.0.0.1 - - [13/Nov/2026:02:16:10 +0800] "GET /missing HTTP/1.1" 404 32"""

codes = re.findall(r'"\s(\d{3})\s', LOG)
print("抓到的状态码:", codes)
print("统计:", sorted(Counter(codes).most_common()))