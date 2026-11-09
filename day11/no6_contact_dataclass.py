# no.6
from dataclasses import dataclass, field, asdict

@dataclass
class Contact:
    name: str
    phone: str
    email: str = ""
    tags: list = field(default_factory=list)

    def line(self):
        parts = [self.name, self.phone]
        if self.email:
            parts.append(self.email)
        return "  ".join(parts)

    def to_dict(self):
        d = asdict(self)    # 一键转成字典
        d.pop("name")       # name 在 JSON 里是 key, 不重复存
        return d

a = Contact("张三", "13800001111", "zs@example.com")
b = Contact("张三", "13800001111", "zs@example.com")
print(a)
print("内容相等:", a == b)
print(a.line())
print(a.to_dict())

c = Contact("李四", "13900002222", tags=["同事"])
c.tags.append("常联系")
d = Contact("王五", "13700003333")
print(c.tags, d.tags)