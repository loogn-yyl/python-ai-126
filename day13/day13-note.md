# D013 笔记

## 闭包
- 内层函数用到外层函数的变量，外层函数把这个内层函数返回出去
- 返回的是「函数 + 它记住的变量」
- 每次调用外层函数 → 一份新的状态，互不影响
- 改外层变量要写 nonlocal；不写会 UnboundLocalError（LEGB 规则）

## 装饰器本质
- @deco 等价于 f = deco(f)，没有任何魔法
- deco 收一个函数，返回一个新的函数（wrapper）
- @ 之后，名字指向的已经是 wrapper，不是原函数

## 两个必踩的坑
- wrapper 忘了 *args, **kwargs → TypeError: takes 0 positional arguments
- 忘了 @functools.wraps(func) → __name__ 变 wrapper、__doc__ 变 None、报错栈里认不出是谁

## 带参数的装饰器
- 三层：外层收装饰器参数，中层收 func，内层 wrapper 收调用参数
- 判断方法：@ 后面有括号就是三层

## 类装饰器
- 实现 __call__ 的类也能当装饰器
- 好处：状态存在 self 里，不用 nonlocal
- 名字保留用 functools.update_wrapper(self, func)

## 三个常用
- timer：time.perf_counter()（单调时钟，测时长用它，别用 time.time()）
- retry：只对「可能会自己好」的错重试；必须设上限；真实场景要加退避间隔
- log：把日志从业务函数里赶出去，业务函数完全不知道有日志

## 反直觉
- 生成器省内存，但不一定更快（有 yield 的开销）
- 选型看瓶颈：内存吃紧用生成器，求快就建列表

## 踩过的坑
- 内外层函数都可以传参
- def repeat(n) 可以不指定次数, 在 @repeat(2) 中指定
  也可以 def repaet(times=2) 指定次数, 那么 @repeat(2) 中只能是 2