# no.2-1
# from dataclasses import dataclass

# @dataclass
# class Bad:
    # tags: list = []
    # 给空列表当默认值, 会报错 ValueType

# no.2-2
from dataclasses import dataclass, field

@dataclass
class Good:
    tags: list = field(default_factory=list)

a = Good()
a.tags.append("同学")
b = Good()
print(a.tags, b.tags, a.tags is b.tags)