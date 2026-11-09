# p4_frozen.py 不可变：frozen=True 的 Point，改属性看抛什么异常，并验证它能进 set
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p)
print(hash(p) is not None)
try:
    p.x = 10
except Exception as e:
    print(type(e).__name__ + ":", e)