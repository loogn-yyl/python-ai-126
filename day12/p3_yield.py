# p3_yield.py yield 版：用 yield 重写上一题，数一下少了几行
def countdown(start):
    n = start
    while n > 0:
        yield n
        n -= 1

print(list(countdown(5)))