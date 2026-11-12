import json

from contacts import Contact

c = Contact("张三", "13800001111", "zs@example.com", ["同事"])
d = c.to_dict()
print(json.dumps(d, ensure_ascii=False, sort_keys=True))

back = Contact.from_dict("张三", d)
print("存进去再读回来一样吗:", back == c)

old = Contact.from_dict("李四", "13900002222")
print("v1 旧格式:", old)