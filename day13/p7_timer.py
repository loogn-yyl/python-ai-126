# p7_timer.py 计时器：给「列表推导」和「生成器求和」两个函数各加 @timer，比一比
import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        used = (time.perf_counter() - start) * 1000
        print(f"  [{func.__name__} 用时 {used:.2f} ms]")
        return result
    return wrapper

@timer
def build_list(n):
    return [x * x for x in range(n)]

@timer
def build_gen(n):
    return sum(x * x for x in range(n))

print(build_list(20000)[-1])
print(build_gen(20000))