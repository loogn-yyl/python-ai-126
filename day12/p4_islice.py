# p4_islice.py 无限序列：斐波那契生成器，用 islice 取前 10 个、再取第 20 个
import itertools

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print(list(itertools.islice(fib(), 10)))
gen = fib()
print([next(gen) for _ in range(5)])
print("第 20 个:", next(itertools.islice(fib(), 19, 20)))