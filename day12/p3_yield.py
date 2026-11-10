# p3_yield.py yield 版：用 yield 重写上一题，数一下少了几行
def countdown(start):
    n = start
    while n > 0:
        yield n
        n -= 1

print(list(countdown(5)))
# 类共 12 行(含 2 空行) -> 函数体 5行, 少了 7 行