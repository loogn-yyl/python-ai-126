# no.1
def area(r):
    return 3.14159 * r * r

print(area(2))
print(f"{area(2):.2f}")

# no.2
def say_hi(name):
    print(f"你好, {name}")
# Python 里所有函数都有返回值，没写就是 None

result = say_hi("张三")
print("返回值是:", result)

# no.3
def bad_area(r):
    print(3.14159 * r * r)

def good_area(r):
    return 3.14159 * r * r

# bad_area(2) * 2

# no.4
# 最后一行是「关键字参数」：按名字传，顺序随便。C 没有这个能力。
# 规则：带默认值的参数必须放在不带默认值的后面。def f(a=1, b) 会直接 SyntaxError。
def greet(name, greeting="你好"):
    return f"{greeting}, {name}"

print(greet("张三"))
print(greet("张三", "早上好"))
print(greet(greeting="晚上好", name="李四"))

# no.5
def bad(item, box=[]):
    box.append(item)
    return box
# 默认值只在函数「定义」时创建一次，不是每次调用都新建

print(bad(1))
print(bad(2))
print(bad(3))

# no.6
def good(item, box=None):
    if box is None:
        box = []
    box.append(item)
    return box

print(good(1))
print(good(2))

# no.7
def total(*args):
    return sum(args)
# 一个星号 → 多余的位置参数，装成元组

print(total(1, 2, 3))
print(total(1, 2, 3, 4, 5))

# no.8
def profile(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
# 两个星号 → 多余的关键字参数，装成字典

profile(name="张三", age=18)

# no.9
nums = [3, 1, 4, 1, 5]

print(nums)
print(*nums)

# no.10
def minmax(nums):
    return min(nums), max(nums)
# 返回元组

lo, hi = minmax([3, 1, 4, 1, 5])
print(lo, hi)

print(minmax([3, 1, 4]))

# no.11
x = "全局"

def outer():
    x = "外层"
    def inner():
        x = "内层"
        print(x)
    inner()
    print(x)

outer()
print(x)

# no.12
count = 0

def add():
    global count
    # 函数内改全局变量, 要声明 global
    count += 1

add()
add()
print(count)

# no.13
def add(count):
    return count + 1

count = 0
count = add(count)
count = add(count)
print(count)

# no.14
double = lambda x: x * 2
print(double(5))
# lambda 只适合一行能写完的表达式

# 完全等价于
def double2(x):
    return x * 2

print(double2(5))

# no.15
nums = [3, 1, 4, 1, 5]
print(sorted(nums, key=lambda x: -x))
# 降序

students = [("张三", 88), ("李四", 95), ("王五", 76)]
print(sorted(students, key=lambda s: s[1]))

print(list(map(lambda x: x * 2, nums)))
print([x * 2 for x in nums])
print(list(filter(lambda x: x > 2, nums)))
print([x for x in nums if x > 2])