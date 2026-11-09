# p2_book_field.py 可变默认值：加 tags 字段，用 field(default_factory=list)，验证两个实例的列表互不影响
from dataclasses import dataclass, field

@dataclass
class Book:
    title: str
    tags: list = field(default_factory=list)

a = Book("钢铁是怎样炼成的")
a.tags.append("必读书目")
b = Book("假如给我三天光明")
print(a)
print(b)
print(a.tags, b.tags, a.tags is b.tags)