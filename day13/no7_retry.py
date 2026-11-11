# no.7
import functools
import time

def retry(times=3):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, times + 1):
                time.sleep(0.1 * i)
                try:
                    return func(*args, **kwargs)
                except ValueError as e:
                    print(f"  第 {i} 次失败: {e}")

            print("  全部失败, 放弃")
            return None
        return wrapper
    return deco

@retry(3)
def parse(text):
    return int(text)

print(parse("42"))
print(parse("abc"))