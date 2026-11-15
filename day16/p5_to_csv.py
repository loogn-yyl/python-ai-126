# p5_to_csv.py 结果写成 csv：用 io.StringIO 写，打印出来看格式对不对
import csv
import io
from collections import Counter

rows = [
    {"ip": "127.0.0.1"}, {"ip": "10.0.0.5"},
    {"ip": "10.0.0.5"}, {"ip": "192.168.1.9"}
]

buf = io.StringIO()
w = csv.DictWriter(buf, fieldnames=["ip", "count"])
w.writeheader()
for ip, n in sorted(Counter(r["ip"] for r in rows).items()):
    w.writerow({"ip": ip, "count": n})
print("\n".join(buf.getvalue().splitlines()))