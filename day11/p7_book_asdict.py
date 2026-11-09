# p7_asdict.py 转字典往返：asdict → json.dumps → json.loads → Book(**d) 
import json
from dataclasses import dataclass, asdict

@dataclass
class Book:
    title: str
    price: float

b = Book("钢铁是怎样炼成的", 29.9)
text = json.dumps(asdict(b), ensure_ascii=False)
print(text)

back = Book(**json.loads(text))
print(back)
print("往返后相等", back == b)