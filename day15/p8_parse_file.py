# p8_parse_file.py 带行号的报错：写一个 parse_file(lines)，遇到解析不了的行时打印行号和前 30 个字符，最后返回「成功行数 / 失败行数」
import re

PATTERN = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - -'
    r'\[(?P<time>[^\]]+)\] '
    r'"(?P<method>[A-Z]+) (?P<path>\S+) HTTP/[\d.]+" '
    r'(?P<status>\d{3}) (?P<size>\d+)'
)

def parse_file(lines):
    ok, fail = [], 0
    for no, line in enumerate(lines, start=1):
        m = PATTERN.match(line)
        if m:
            ok.append(m.groupdict())
        else:
            fail += 1
            print(f"  第 {no} 行解析失败: {line[:30]}")
    return len(ok), fail

lines = [
    '127.0.0.1 - - [13/Nov/2026:02:15:33 +0800] "GET /a HTTP/1.1" 200 10',
    '这一行是坏的',
    '10.0.0.5 - - [13/Nov/2026:02:15:35 +0800] "GET /b HTTP/1.1" 404 0'
]
ok, fail = parse_file(lines)
print(f"成功 {ok} 行, 失败 {fail} 行")