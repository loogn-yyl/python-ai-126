# p3_deco.py 最简单的装饰器：调用前后各打印一行，先用 f = deco(f) 的手写形式，再用 @ 语法
def deco(func):
    def wrapper():
        print("  调用前, ", func.__name__)
        func()
        print("  调用后, ", func.__name__)

    return wrapper

def hello():
    print("  你好")

f = deco(hello)
f()

@deco
def hi():
    print("  你好")

hi()