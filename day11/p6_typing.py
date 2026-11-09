# p6_typing.py 类型注解：写 group_by_prefix(contacts: list[Contact]) -> dict[str, list[str]]，打印 __annotations__ 看看注解被存成了什么
from dataclasses import dataclass
from typing import Optional

@dataclass
class Contact:
    name: str
    phone: str

def group_by_prefix(contacts: list[Contact]) -> dict[str, list[str]]:
    res: dict[str, list[str]] = {}
    for c in contacts:
        res.setdefault(c.phone[:3], []).append(c.name)
    return res

def find(contacts: list[Contact], name: str) -> Optional[Contact]:
    for c in contacts:
        if c.name == name:
            return c
    return None

data = [Contact("张三", "13800001111"), Contact("李四", "13900002222"), Contact("王五", "13800003333")]
print(group_by_prefix(data))
print(find(data, "李四"))
print(find(data, "赵六"))
print(group_by_prefix.__annotations__)