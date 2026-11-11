# no.5
import functools

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"  第 {self.count} 次调用 {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    return f"你好 {name}"

print(greet("张三"))
print(greet("李四"))
print("调用次数:", greet.count)
print(greet.__name__)