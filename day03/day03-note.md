# D003 笔记

## 核心概念
- 列表 = 可变有序；元组 = 不可变；字典 = key→value；集合 = 去重无序
- b = a 是引用不是拷贝！要复制用 a[:] 或 copy()
- 切片是浅拷贝，嵌套列表会穿透，彻底独立要 deepcopy
- sort() 原地改返回 None；sorted() 返回新列表

## 方法速查
- append / extend / insert / remove / pop / del / clear
- remove(x) 按值删，del lst[i] 按下标删
- dict.get(k, 默认值) 不会崩，d[k] 会抛 KeyError
- 遍历字典用 d.items() 同时拿 key 和 value

## 语法
- [x * x for x in range(1,6)]           列表推导式
- [x for x in nums if x % 2 == 0]       带条件
- name, age = ("张三", 18)              元组解包
- a, b = b, a                           交换不用临时变量
- (5,) 才是单元素元组，(5) 是 int

## 集合
- 空集合是 set()，{} 是空字典
- & 交集 | 并集 - 差集 ^ 对称差
- 去重会乱序，要保序自己写循环

## 性能
- x in list 是 O(n)，x in set/dict 是 O(1)

## 踩过的坑
- 第 2 题 —— if x not in seen 是「去重保序」的标准解法
- 第 5 题 —— max(scores, key=scores.get) 这个写法值得背下来：max 默认比 key，加了 key= 参数就改成「按 value 比，但返回 key」。
- 第 8 题 —— lambda x: x[1] 的意思是「拿每个元组的第 2 个元素（分数）来比较」。这是排序题的标准套路。

## C 对比
- 列表变量类似指针，赋值复制的是指针
- Python 数组自动扩容，不用管长度
- 不需要临时变量的 swap