# p7_to_from_dict.py 转字典往返：给 Contact 加 to_dict() / from_dict()，转成 JSON 字符串再读回来，验证电话和邮箱都没变
import json

class Contact:
    def __init__(self, name, phone, email=""):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"phone": self.phone, "email": self.email}
    
    @classmethod
    def from_dict(cls, name, d):
        if isinstance(d, str):
            return cls(name, d)
        return cls(name, d.get("phone", ""), d.get("email", ""))

a = Contact("张三", "13800001111", "zs@example.com")
text = json.dumps(a.to_dict(), ensure_ascii=False)
print(text)

back = Contact.from_dict("张三", json.loads(text))
print(back.name, back.phone, back.email)
print("属性一致吗:", back.phone == a.phone and back.email == a.email)