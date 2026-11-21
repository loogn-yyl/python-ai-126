# no..7-1
import contextlib
import io
import re
import sys
from pathlib import Path

LINE = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})'
    r' - - '
    r'\[(?P<time>[^\]]+)\]'
    r' "(?P<method>[A-Z]+) (?P<path>\S+) HTTP/[\d.]+"'
    r' (?P<status>\d{3})'
    r' (?P<size>\d+)'
)

GOOD = '10.0.0.7 - - [12/Nov/2026:09:01:11 +0800] "GET /api/user HTTP/1.1" 200 512\n'

def load(text):
    rows = []
    for line in text.splitlines():
        m = LINE.match(line)
        if m:
            rows.append(m.groupdict())
    return rows

def run(path):
    p = Path(path)
    if not p.exists():
        print(f"错误: 找不到文件 {path}", file=sys.stderr)
        return 1
    rows = load(p.read_text(encoding="utf-8"))
    if not rows:
        print(f"错误: {path} 里一行都没解析出来", file=sys.stderr)
        return 1
    print(f"成功: {path} 解析出 {len(rows)} 行")
    return 0

Path("ok.log").write_text(GOOD, encoding="utf-8")
Path("bad.log").write_text("全是坏行\n再来一行坏的\n", encoding="utf-8")

for name in ("ok.log", "bad.log", "missing.log"):
    err = io.StringIO()
    with contextlib.redirect_stderr(err):
        code = run(name)
    print(f"  {name:<12} 退出码 {code}   {err.getvalue().strip()}")