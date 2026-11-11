# p4_args.py 保留参数：装饰一个带默认参数的函数，验证 *args/**kwargs 能把位置参数和关键字参数都转过去
import functools

def deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("调用", func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return wrapper

@deco
def add(a, b=0):
    return a + b

print(add(1, 2))
print(add(1, b=5))
print(add(1))
print(add.__name__)