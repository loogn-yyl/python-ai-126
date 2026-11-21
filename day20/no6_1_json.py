# no.6-1
import json

# 假设解析已完成, rows 里每条记录长这样
rows = [
    {"ip": "10.0.0.7", "path": "/api/user", "status": 200},
    {"ip": "10.0.0.7", "path": "/api/user", "status": 200},
    {"ip": "10.0.0.9", "path": "/api/login", "status": 401},
]
codes = {}
for r in rows:
    key = str(r["status"])
    codes[key] = codes.get(key, 0) + 1

data = {"total": len(rows), "codes": codes, "备注": "含中文"}
print(json.dumps(data, ensure_ascii=False, indent=2))
print()
print(json.dumps(data, ensure_ascii=True))