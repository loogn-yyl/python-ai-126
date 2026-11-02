# no.1
sq = []
for x in range(5):
    sq.append(x * x)

sq2 = [x * x for x in range(5)]

print(sq)
print(sq2)

# no.2
print([x for x in range(1, 11) if x % 2 == 0])

print(["偶" if x % 2 == 0 else "奇" for x in range(1, 6)])

# no.3
sq_list = [x * x for x in range(5)]   # 方括号 -> 立即算出
sq_gen = (x * x for x in range(5))    # 圆括号 -> 用时算出

print(sq_list)
print(sq_gen)
print(list(sq_gen))