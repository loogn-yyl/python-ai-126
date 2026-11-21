# no.7-2
import argparse
import csv
import io
import json
import logging
import sys
import re
from pathlib import Path
from collections import Counter

LINE = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})'
    r' - - '
    r'\[(?P<time>[^\]]+)\]'
    r' "(?P<method>[A-Z]+) (?P<path>\S+) HTTP/[\d.]+"'
    r' (?P<status>\d{3})'
    r' (?P<size>\d+)'
)

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
    return rows, bad

def top_n(counter, n):
    # 次数降序, 次数相同按名字升序 —— 少了第二关键字, 顺序就不固定
    return sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[:n]

def build(rows, bad, n):
    """把「事实」算成一个 dict, 与怎么打印无关"""
    codes = Counter(r["status"] for r in rows)
    total = len(rows)
    errors = sum(c for s, c in codes.items() if s >= 400)
    return {
        "total_lines": total + len(bad),
        "parsed": total,
        "bad_lines": bad,
        "top_ips": top_n(Counter(r["ip"] for r in rows), n),
        "top_paths": top_n(Counter(r["path"] for r in rows), n),
        "codes": dict(sorted(codes.items())),
        "errors": errors,
        "error_rate": errors / total if total else 0.0,
    }

def render_text(d, n):
    out = [f"文件共 {d['total_lines']} 行, 解析成功 {d['parsed']} 行, 坏行 {len(d['bad_lines'])} 行"]
    if d["bad_lines"]:
        out.append(f"坏行行号: {d['bad_lines']}")
    out.append("")
    out.append(f"Top {n} IP")
    for ip, c in d["top_ips"]:
        out.append(f"  {ip:<12}{c:>4}  {c / d['parsed']:>6.1%}")
    out.append(f"Top {n} URL")
    for p, c in d["top_paths"]:
        out.append(f"  {p:<18}{c:>4}")
    out.append("状态码")
    for s, c in d["codes"].items():
        out.append(f"  {s}  {c:>4}")
    out.append(f"错误率  {d['error_rate']:.1%}({d['errors']}/{d['parsed']})")
    return "\n".join(out)

def render_csv(d):
    buf = io.StringIO(newline="")
    w = csv.writer(buf)
    w.writerow(["section", "key", "count"])
    for ip, c in d["top_ips"]:
        w.writerow(["ip", ip, c])
    for p, c in d["top_paths"]:
        w.writerow(["path", p, c])
    for s, c in d["codes"].items():
        w.writerow(["status", s, c])
    return buf.getvalue().rstrip("\r\n")

def parse_args(argv=None):
    p = argparse.ArgumentParser(prog="logtool", description="分析 nginx 访问日志")
    p.add_argument("path", help="日志文件路径")
    p.add_argument("-n", "--top", type=int, default=3, help="Top N, 默认 3")
    p.add_argument("-q", "--quiet", action="store_true", help="不打进度日志")
    p.add_argument("--format", choices=["text", "csv", "json"], default="text")
    return p.parse_args(argv)    # 若 argv=None 走 sys.argv

def setup_log(quiet):
    logging.basicConfig(
        level=logging.WARNING if quiet else logging.INFO,
        format="%(levelname)-8s | %(message)s",
        stream=sys.stderr,    # 日志走 stderr, 结果走 stdout
    )
    return logging.getLogger("logtool")

def run(args):
    """真正的干活函数: 读文件 -> 解析 -> 算 dict -> 渲染成字符串。返回值就是退出码。"""
    log = logging.getLogger("logtool")
    p = Path(args.path)
    if not p.exists():
        print(f"错误: 找不到文件 {args.path}", file=sys.stderr)
        return 1
    rows, bad = load(p.read_text(encoding="utf-8"))
    if not rows:
        print(f"错误: {args.path} 里一行都没解析出来", file=sys.stderr)
        return 1
    log.info("解析成功 %d 行, 坏行 %d 行", len(rows), len(bad))

    d = build(rows, bad, args.top)
    if args.format == "json":
        text = json.dumps(d, ensure_ascii=False, indent=2)
    elif args.format == "csv":
        text = render_csv(d)
    else:
        text = render_text(d, args.top)

    print(text)   # 结果永远走 stdout
    return 0

def main(argv=None):
    args = parse_args(argv)
    log = setup_log(args.quiet)
    log.info("开始处理 %s", args.path)
    code = run(args)
    log.info("结束, 退出码 %d", code)
    return code

if __name__ == "__main__":
    sys.exit(main())