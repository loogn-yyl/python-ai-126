# no.4
from typing import Optional

def find(name: str, data: dict[str, str]) -> Optional[str]:
    return data.get(name)

data = {"张三": "13800001111"}
print(find("张三", data))
print(find("李四", data))
print(find.__annotations__)
print("传 int 也不报错:", find(123, data))