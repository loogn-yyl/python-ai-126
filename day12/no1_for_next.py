# no.1-1
nums = [10, 20, 30]
it = iter(nums)
print(type(it).__name__)
print(next(it))
print(next(it))
print(next(it))
try:
    next(it)
except StopIteration:
    print("StopIteration: 没有了")

# no.1-2
# for 循环 ==
it = iter(nums)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    print(x)

# no.1-3
nums = [1, 2, 3]
print("列表有 __iter__ 吗:", hasattr(nums, "__iter__"))
print("列表有 __next__ 吗:", hasattr(nums, "__next__"))

it = iter(nums)
print("迭代器有 __next__ 吗:", hasattr(it, "__next__"))
print("iter(迭代器) 还是自己吗:", iter(it) is it)

for x in it:
    print("消耗:", x)
print("再遍历一遍:", list(it))