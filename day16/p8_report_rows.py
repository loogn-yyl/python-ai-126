# p8_report_rows.py 写 report(rows) 函数：返回一个字典（total / bytes / error_rate / top_ip），要能直接 json.dumps
import json
from collections import Counter

rows = [
    {"ip": "127.0.0.1", "status": "200", "size": "512"},
    {"ip": "10.0.0.5", "status": "200", "size": "128"},
    {"ip": "10.0.0.5", "status": "401", "size": "64"},
    {"ip": "192.168.1.9", "status": "304", "size": "0"},
]

def report(rows):
    total = len(rows)
    errors = sum(1 for r in rows if r["status"][0] in "45")
    return {
        "total": total,
        "bytes": sum(int(r["size"]) for r in rows),
        "error_rate": round(errors / total, 3) if total else 0,
        "top_ip": Counter(r["ip"] for r in rows).most_common(3),
    }

r = report(rows)
print(json.dumps(r, ensure_ascii=False, indent=2))
print()
print("空列表也能跑:", report([]))