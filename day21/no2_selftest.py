# 第 1 题 · 默认参数
def f(x, box=[]):
    box.append(x)
    return box

print(f(1), f(2))

# 第 2 题 · 切片
s = "Python"
print(s[::-1], s[1:4], s[-2:])

# 第 3 题 · == 与 is
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b)
print(c is a, c is b)

# 第 4 题 · 闭包与延迟绑定
fs = [lambda: i for i in range(3)]
print([f() for f in fs])

fs2 = [lambda i=i: i for i in range(3)]
print([f() for f in fs2])

# 第 5 题 · 生成器只能走一次
g = (x * x for x in range(3))
print(list(g))
print(list(g))

# 第 6 题 · try/finally 与 return
def f():
    try:
        return "try 里的值"
    finally:
        print("finally 先跑")

print(f())

# 第 7 题 · 类属性
class A:
    n = 0
    def __init__(self):
        A.n += 1

A()
A()
print(A.n)

# 第 8 题 · dataclass 的可变默认值
from dataclasses import dataclass, field

@dataclass
class Item:
    tags: list = field(default_factory=list)

a, b = Item(), Item()
a.tags.append("x")
print(a.tags, b.tags)

# 第 9 题 · match / search / fullmatch
import re

print(re.match(r"\d+", "abc123"))
print(re.search(r"\d+", "abc123").group())
print(re.fullmatch(r"\d+", "123").group())

# 第 10 题 · 协程只是「声明」
import asyncio

async def hello():
    return "hi"

c = hello()
print(type(c).__name__)
print(asyncio.run(c))