# p6_repeat_2.py 带参数的装饰器：@repeat(2) 让函数执行两次，返回最后一次的结果
import functools

def repeat(n):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return deco

@repeat(2)
def shout(text):
    print("  " + text * 2)
    return text

print(shout("嘿"))