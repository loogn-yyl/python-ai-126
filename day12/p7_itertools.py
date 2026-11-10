# p7_itertools.py itertools 五个：count+islice、chain、groupby、accumulate、combinations 各跑一次

import itertools

print(list(itertools.islice(itertools.count(1, 5), 4)))
print(list(itertools.chain([1, 2, 3], "ab", (3,))))
print([(k, len(list(g))) for k, g in itertools.groupby("AAABBBCCCCDA")])
print(list(itertools.accumulate([1, 3, 5, 7, 9])))
print(list(itertools.combinations([1, 3, 5, 7, 9], 2)))