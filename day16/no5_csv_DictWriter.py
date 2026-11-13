# no.5
import csv
import io
from collections import Counter

rows = [
    {"ip": "127.0.0.1", "path": "/index.html", "status": "200", "size": "512"},
    {"ip": "10.0.0.5", "path": "/api/login", "status": "200", "size": "128"},
    {"ip": "10.0.0.5", "path": "/api/user", "status": "401", "size": "64"},
]

buf = io.StringIO()
w = csv.DictWriter(buf, fieldnames=["ip", "count"])
w.writeheader()
for ip, n in sorted(Counter(r["ip"] for r in rows).items()):
    w.writerow({"ip": ip, "count": n})
print("\n".join(buf.getvalue().splitlines()))