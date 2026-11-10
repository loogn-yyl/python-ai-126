# no.5
nums = range(5)

lst = [x * x for x in nums]
gen = (x * x for x in nums)

print(type(lst).__name__, lst)
print(type(gen).__name__)
print(list(gen))
print("第二次 list:", list(gen))
print("一百万个平方的和:", sum(x * x for x in range(1000000)))