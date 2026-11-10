# no.6
import itertools

print(list(itertools.islice(itertools.count(10, 5), 4)))
# count(start, stop) 无限递增, 搭配 islice 截断
# islice(it, n) 只取前 n 个

print(list(itertools.chain([1, 2], "ab", (3,))))
# chain(a, b) 把多个序列拼接起来

print(list(itertools.islice(itertools.cycle("AB"), 6)))
# cycle(it) 无限循环

print([(k, len(list(g))) for k, g in itertools.groupby("AAABBBCCA")])
# groupby(it) 相邻相同的一组, 必须先排序才能全局分组

print(list(itertools.accumulate([1, 2, 3, 4])))
# accumulate(it) 计算前缀和

print(list(itertools.product([1, 2], "ab")))
# product(a, b) 笛卡尔积, 暴力枚举、参数组合

print(list(itertools.combinations([1, 2, 3], 2)))
# combinations(it, a) it 中每 a 个构成一个组合