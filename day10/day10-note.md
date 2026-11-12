# D010 笔记

## 打印
- __str__  → print(obj) / str(obj) / f"{obj}"     
  给人看
- __repr__ → repr(obj) / 打印列表 / 调试器  
  给开发者看，最好能重建对象
- print([obj]) 走的是 __repr__，不是 __str__ → 两个都要写
- repr 里用 !r：f"Book({title!r})" → Book('书名')

## 比较
- 默认 == 和 is 一个意思，比的是「是不是同一个对象」  
  只在自定义类没写 __eq__ 时成立, 2 == 2.0 -> True, 2 is 2.0 -> False
- __eq__ 里先 isinstance 检查，比不了就 return NotImplemented（不是 False）
- 定义了 __eq__ 不定义 __hash__ → 类变成不可哈希，不能进 set、不能当 dict key
- __hash__ 要和 __eq__ 用同一个字段算

## 排序
- sorted(books) 需要 __lt__，否则 TypeError
- sorted(books, key=lambda b: b.x) 更常用，key 优先于 __lt__
- __eq__ 和 __lt__ 口径要一致，否则排序结果不稳定

## 让它像容器
- __len__      → len(obj)
- __getitem__  → obj[0] / obj[-1] / obj[0:2]（切片收到 slice 对象）
- __iter__     → for x in obj / in / 推导式 / list()
- 只写 __getitem__ 也能 for, 必须从 0 连续递增, 靠越界报错停   
  因此能写 __iter__ 就写

## 让它像函数
- __call__ → obj(x)
- 比函数强的地方：能带状态（self.n 就是配置）

## @property
- @property + @x.setter → 长得像属性，实际走方法
- 内部字段用 self._x，不能同名（会无限递归）
- __init__ 里赋值也会走 setter → 校验只写一处
- 只写 getter 就是只读，赋值报 AttributeError
- 调用时不加括号！d.total 不是 d.total()

## 三种装饰器
- @classmethod —— cls —— 第二个构造函数
- @staticmethod —— 无参数 —— 工具函数
- @property —— 不加括号 —— 当属性用

## 踩过的坑
- callable 判断类型上有没有 __call__