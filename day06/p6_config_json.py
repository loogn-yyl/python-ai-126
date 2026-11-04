# p6_config_json.py JSON 存取：把一个含列表的字典存成 config.json，再读回来验证类型没变

import json

config = {"name": "我的项目", "tags": ["python", "ai"], "version": 1}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

with open("config.json", "r", encoding="utf-8") as f:
    back = json.load(f)

print(back)
print("tags 还是列表吗:", isinstance(back["tags"], list))
print("version 还是数字吗:", isinstance(back["version"], int))