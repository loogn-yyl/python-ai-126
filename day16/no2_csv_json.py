# no.2
import csv
import io
import json

CSV_TEXT = """ip,path,status,size
127.0.0.1,/index.html,200,512
10.0.0.5,/api/login,200,128
10.0.0.5,/api/user,401,64"""

rows = list(csv.DictReader(io.StringIO(CSV_TEXT)))
print("读 csv:", len(rows), "行")
print("第一行:", rows[0])
print()
for r in rows:
    r["status"] = int(r["status"])
    r["size"] = int(r["size"])
print("转 int:", rows[0])
print("总流量:", sum(r["size"] for r in rows))
print()
as_json = json.dumps(rows, ensure_ascii=False)
print(as_json)
print("再读回来一样吗:", json.loads(as_json) == rows)