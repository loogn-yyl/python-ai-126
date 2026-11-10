# no.3-1
def countdown(start):
    n = start
    while n > 0:
        yield n
        n -= 1

for i in countdown(3):
    print(i)

cd = countdown(2)
print(list(cd))
print("第二次同一对象:", list(cd))
print("新建一个:", list(countdown(2)))

# no.3-2
def numbers(n):
    for i in range(n):
        print("  算出一个", i)
        yield i

print("开始循环")
for x in numbers(3):
    print("拿到", x)
print("结束")