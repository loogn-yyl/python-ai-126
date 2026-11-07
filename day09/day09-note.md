# D009 笔记

## 继承
- class 子类(父类):           子类自动拥有父类所有方法
- 子类写 __init__ 时，第一行必须 super().__init__(...)
- 不写 super 不会报错，只是父类的属性全都不存在 → 以后在别处 AttributeError
- 方法重写：子类再写一遍同名方法，子类的优先

## 多态
- s.describe() 调用哪个版本，看 s 实际是谁，不看变量声明成什么
- 加新子类不用改调用方 —— 这是继承最大的价值
- 反例：if isinstance(...) 一长串，每加一种都要改

## 抽象基类
- from abc import ABC, abstractmethod
- class Shape(ABC):  @abstractmethod def area(self): ...
- 子类没实现就造不出对象 → TypeError，把错误提前到最早的时刻
- 有通用实现的父类方法不要标 abstractmethod

## MRO
- D.__mro__ 就是查找顺序，从左到右，最后一定是 object
- class D(B, C) → 先 B 后 C，B 的方法优先
- 菱形继承里 A 只出现一次

## 继承还是组合
- is-a（圆是一种图形）→ 继承
- has-a（通讯录有一个字典）→ 组合
- 继承 dict/list 会把它们的全部方法暴露出去，绕过你自己的校验
- 想复用代码用组合，想替换实现用继承

## C 对比
- struct 嵌套模拟继承              vs  class Circle(Shape)
- enum + switch 分发              vs  直接 s.area()
- 改了 switch 要重测所有分支        vs  加子类不动调用方

## 踩过的坑
- :.2f 是 f-string 的语法, 用的时候必须在 f"{}" 里, 如 print(f"{c.area():.2f})
- 类似的表示有 print(format(c.area(), ".2f")) 和 print("{:.2f}".format(c.area()))
- 注意 round(12.5, 2) 返回只是 12.5, 后面不补 0; round(12.51, 2) 才返回 12.51