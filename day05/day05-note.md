# D005 笔记

## 函数基础
- def name(param): 缩进，没有 {} 和类型声明
- 没有 return 的函数返回 None（不是「不返回」）
- print 是给人看，return 是给程序用
- 函数内部尽量只 return 不 print，输出交给调用方

## 参数
- 默认参数必须放在后面
- **默认参数不能写 [] {} set()** —— 只会创建一次，所有调用共用
  正确写法：默认 None，函数里 if x is None: x = []
- *args 收成元组，**kwargs 收成字典
- 反向用：max(*nums) 把列表拆成参数

## 作用域 LEGB
- Local → Enclosing → Global → Built-in，就近找
- 改全局变量要 global，但更好的做法是当参数传、用返回值带出

## lambda
- 一行表达式，不能有多语句
- 主要用途：sorted(key=...)、map、filter 的参数
- 但 map/filter 用推导式更清楚

## 模块
- import math / from math import sqrt / import numpy as np
- 不要写 from xxx import *
- import 会执行那个文件一次（所以要有 __main__ 保护）
- __name__：直接运行 = "__main__"，被 import = 文件名
- 包 = 带 __init__.py 的文件夹，点号就是路径

## C 对比
- #include 贴内容，import 执行模块并拿名字
- void 函数 vs 返回 None
- 返回多个值：C 要传指针，Python 返回元组

## 踩过的坑
- 降序可以写成 sorted(nums, key=lambda x: -x)
  也可以写成 sorted(students, key=lambda s: s[1], reverse=True)