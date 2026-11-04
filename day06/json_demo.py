# no.1
import json

data = {"name": "张三", "scores": [88, 95]}

with open("stu.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# no.2
import json

with open("stu.json", "r", encoding="utf-8") as f:
    back = json.load(f)

print(back)
print(type(back))

# no.3
import json

s = json.dumps({"a": 1}, ensure_ascii=False)
print(s)
print(json.loads(s))