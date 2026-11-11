# no.4
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

@repeat(3)
def hello(name):
    print("hi", name)

hello("张三")
print(hello.__name__)