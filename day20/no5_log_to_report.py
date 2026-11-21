# no.5
import re
import sys
from collections import Counter

LINE = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})'
    r' - - '
    r'\[(?P<time>[^\]]+)\]'
    r' "(?P<method>[A-Z]+) (?P<path>\S+) HTTP/[\d.]+"'
    r' (?P<status>\d{3})'
    r' (?P<size>\d+)'
)

RAW = """10.0.0.7 - - [12/Nov/2026:09:01:11 +0800] "GET /api/user HTTP/1.1" 200 512
10.0.0.7 - - [12/Nov/2026:09:01:12 +0800] "GET /api/user HTTP/1.1" 200 512
10.0.0.9 - - [12/Nov/2026:09:02:03 +0800] "POST /api/login HTTP/1.1" 401 231
10.0.0.7 - - [12/Nov/2026:09:02:44 +0800] "GET /static/app.js HTTP/1.1" 200 88213
10.0.0.9 - - [12/Nov/2026:09:03:10 +0800] "GET /api/user HTTP/1.1" 500 0
这行是坏的, 没有方括号和引号
10.0.0.11 - - [12/Nov/2026:09:04:00 +0800] "GET /api/order HTTP/1.1" 200 1024
10.0.0.11 - - [12/Nov/2026:09:05:30 +0800] "GET /api/detail HTTP/1.1" 404 87"""

def parse_line(line):
    m = LINE.match(line)
    if not m:
        return None
    d = m.groupdict()
    d["status"] = int(d["status"])
    d["size"] = int(d["size"])
    return d

def load(text):
    rows, bad = [], []
    for i, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        rec = parse_line(line)
        rows.append(rec) if rec else bad.append(i)
    if not rows:
        print(f"[load] 收到 {len(text)} 字符 / {len(text.splitlines())} 行, "
              f"解析成功 0 条, 坏行 {len(bad)} 条", file=sys.stderr)
    return rows, bad

def top_n(counter, n):
    # 次数降序, 次数相同按名字升序 —— 少了第二关键字, 顺序就不固定
    return sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[:n]

def report(rows, bad, n=3):
    ips = Counter(r["ip"] for r in rows)
    paths = Counter(r["path"] for r in rows)
    codes = Counter(r["status"] for r in rows)
    errors = sum(c for s, c in codes.items() if s >= 400)
    out = [f"文件共 {len(rows) + len(bad)} 行, 解析成功 {len(rows)} 行, 坏行 {len(bad)} 行"]
    if bad:
        out.append(f"坏行行号: {bad}")
    out.append("")
    out.append(f"Top {n} IP")
    for ip, c in top_n(ips, n):
        out.append(f"  {ip:<12}{c:>4}  {c / len(rows):>6.1%}")
    out.append(f"Top {n} URL")
    for p, c in top_n(paths, n):
        out.append(f"  {p:<18}{c:>4}")
    out.append("状态码")
    for s, c in sorted(codes.items()):
        out.append(f"  {s}  {c:>4}")   
    if len(rows) == 0:
        out.append("没有可统计的数据, 错误率按 0.0% 记")
    else:
        out.append(f"错误率 {errors / len(rows):.1%}({errors}/{len(rows)})")
    return "\n".join(out)

rows, bad = load(RAW)
print(report(rows, bad))