# p1_make_counter.py 闭包计数器：make_counter() 返回一个函数，每次调用 +1；造两个计数器验证互不影响
def make_counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner

c1 = make_counter()
c2 = make_counter()
print(c1(), c1(), c1())
print(c2(), c2())
print(c1())