# no.3-1
def deco(func):
    def wrapper():
        return func()

    return wrapper

@deco
def add(a, b):
    return a + b

# print(add(1, 2))

# no.3-2
import functools

def deco_plain(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

def deco_wraps(func):
    @functools.wraps(func)    # 写装饰器一定要加
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

@deco_plain
def a(x):
    """a 的文档字符串"""
    return x

@deco_wraps
def b(x):
    """b 的文档字符串"""
    return x

print("没有 wraps:", a.__name__, repr(a.__doc__))
print("有 wraps:", b.__name__, repr(b.__doc__))