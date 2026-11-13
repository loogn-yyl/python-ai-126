# no.6
import re

LOG = '127.0.0.1 - - [13/Nov/2026:02:15:33 +0800] "GET /index.html HTTP/1.1" 200 512'

PATTERN = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})'
    r' - - '
    r'\[(?P<time>[^\]]+)\]'
    r' "(?P<method>[A-Z]+) (?P<path>\S+) HTTP/[\d.]+"'
    r' (?P<status>\d{3})'
    r' (?P<size>\d+)'
)

m = PATTERN.match(LOG)
print(m.groupdict())
print()
print("IP      :", m.group("ip"))
print("时间    :", m.group("time"))
print("方法    :", m.group("method"))
print("路径    :", m.group("path"))
print("状态码  :", m.group("status"))
print("大小    :", m.group("size"))