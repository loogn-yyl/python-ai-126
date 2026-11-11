# no.6
import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        used = (time.perf_counter() - start) * 1000
        print(f"  [{func.__name__}] 用时 {used:.2f} ms")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(i * i for i in range(n))

print("结果:", slow_sum(1000000))
print("函数名还是:", slow_sum.__name__)