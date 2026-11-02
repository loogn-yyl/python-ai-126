# p4_sum100.py 1~100 求和：分别用 for 累加和 sum(range()) 两种写法，结果要相同
total = 0
for x in range(1, 101):
    total += x

print(f"1~100 求和, 结果是{total}")

print(f"1~100 求和, 结果是{sum(range(1, 101))}")