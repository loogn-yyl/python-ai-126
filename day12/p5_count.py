# p5_count.py 生成器表达式：求 1 到 100 万里所有 3 的倍数的平方和（不许建列表）

print(sum(x * x for x in range(1000001) if x % 3 == 0))