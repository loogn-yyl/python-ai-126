# D012 笔记

## for 背后
- it = iter(nums) → next(it) 一个个取 → 取不到抛 StopIteration → for 接住并结束
- 迭代器用「抛异常」表示结束，不是返回哨兵值

## 可迭代 vs 迭代器
- 可迭代：有 __iter__（list / str / dict / range / 生成器函数）
- 迭代器：有 __iter__ + __next__（iter(list)、生成器对象、文件对象）
- 可迭代可以反复遍历；迭代器一次性，走完就空
- 坑：sum、list、any、all 静默给出错误结果, max、min 直接抛 ValueError

## 手写迭代器
- __iter__ 返回 self
- __next__ 返回下一个值，没有了 raise StopIteration

## yield
- 函数里有 yield 就是生成器函数；调用只造对象，不执行
- 每次 next() 跑到下一个 yield 停住，下次从那里继续
- 好处：省内存、能表示无限序列、能边算边用
- 限制：只能往前，不能下标、不能 len、不能回头

## 惰性求值
- for line in f  → 一次只装一行（文件对象本身就是迭代器）
- f.readlines()  → 全部装进内存，5.4MB 文件峰值 18.5MB
- 大文件一律用 for line in f

## 生成器表达式
- [x for x in ...]  → list，全部算出来
- (x for x in ...)  → generator，算一个给一个
- sum/max/min/any/all 直接用圆括号，零成本优化

## itertools
| 函数 | 意义 |
| --- | --- |
| count(start, step) / islice(it, n) | 无限序列 + 截断(必须配 islice) |
| chain(a, b) | 拼接多个序列 |
| cycle(it) | 无限循环 |
| groupby(it) | 相邻分组！要全局分组先 sorted |
| accumulate(it) | 前缀和 |
| product(a, b) / combinations(it, a) | 笛卡尔积 / 组合 |

## C 对比
- 返回 NULL 当哨兵   → raise StopIteration
- 手动 malloc 整个数组  → yield 一个算一个
- 回调函数逐行处理  → for line in f

## 踩过的坑
- print([(k, len(list(g))) for k, g in itertools.groupby("AAABBBCCA")])
- groupby(it) 相邻相同的一组, 必须先排序才能全局分组
- groupby 产出一个 (键, 组迭代器), 后者是惰性的、一次性的, 只能当场用完