# p8_book_json.py 存盘再读回（综合）：把两个 Book 存成 JSON 文件、读回来重建列表，验证整体相等、且 tags 是新的列表而不是同一个
import json
import os
from dataclasses import dataclass, field, asdict

FILE = "books.json"

@dataclass
class Book:
    title: str
    price: float
    tags: list = field(default_factory=list)

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

books = [Book("钢铁是怎样炼成的", 29.9, ["必读书目"]), Book("假如给我三天光明", 39.9)]

with open(FILE, "w", encoding="utf-8") as f:
    json.dump([b.to_dict() for b in books], f, ensure_ascii=False, indent=2)

with open(FILE, "r", encoding="utf-8") as f:
    back = [Book.from_dict(d) for d in json.load(f)]

print("读回来", len(back), "本")
print(back[0])
print("整体相等:", back == books)
print("tags 也相等:", back[0].tags == books[0].tags)
print("tags 不是同一个列表:", back[0].tags is not books[0].tags)
os.remove(FILE)