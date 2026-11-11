# p5_wraps.py wraps 对比：同一个装饰器写两版，打印 __name__ 和 __doc__ 看差别
import functools

def plain(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def kept(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@plain
def a(x):
    """a 的文档字符串"""
    return x

@kept
def b(x):
    """b 的文档字符串"""
    return x

print("没有 wraps:", a.__name__, repr(a.__doc__))
print("有 wraps:", b.__name__, repr(b.__doc__))