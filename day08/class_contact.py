import json

class Contact:
    def __init__(self, name, phone, email=""):
        self.name = name
        self.phone = phone
        self.email = email

    def line(self):
        parts = [self.name, self.phone]
        if self.email:
            parts.append(self.email)
        return "  ".join(parts)

    def to_dict(self):
        return {"phone": self.phone, "email": self.email}

    @classmethod
    def from_dict(cls, name, d):
        if isinstance(d, str):
            return cls(name, d)
        return cls(name, d.get("phone", ""), d.get("email", ""))

c = Contact("张三", "13800001111", "zs@example.com")
print(c.line)
print(json.dumps(c.to_dict(), ensure_ascii=False))

raw = {"张三": "13800001111", "李四": {"phone": "13800002222", "email": ""}}
for name, d in raw.items():
    print(Contact.from_dict(name, d).line())