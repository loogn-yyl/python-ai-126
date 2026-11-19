# no.1
import time

def cooking(name, sec):
    """IO 密集型, 大部分时间在等"""
    time.sleep(sec)
    return f"{name} 好了"

def chopping(n):
    """CPU 密集型, 大部分时间在算"""
    total = 0
    for i in range(n):
        total += i * i
    return total

t0 = time.perf_counter()
for name, sec in [("水", 0.1), ("饭", 0.1), ("汤", 0.1)]:
    cooking(name, sec)
io_time = time.perf_counter() - t0
print(f"串行烧三样: {io_time:.1f} 秒(CPU 全程在等)")

total = chopping(500_000)
print("算 50 万次平方和:", total)
print("这段时间 CPU 没有一刻空闲")