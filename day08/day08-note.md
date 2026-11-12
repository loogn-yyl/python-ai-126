# D008 笔记

## class 三件套
- class 名字:           定义模板，此时还没有对象
- def __init__(self,...):  造对象时自动执行，用来存属性
- def 方法(self):        实例方法，调用时 self 自动是那个对象

## self
- 不是关键字，是约定（第一个参数名）
- 少写 self → TypeError: takes 1 positional argument but 2 were given
- a.hello()  等价于  Contact.hello(a)

## 两种属性
- 实例属性：self.x = ...   → 每个对象各一份（绝大多数用它）
- 类属性：  count = 0      → 所有对象共用，改的时候必须写类名
- 读：先找实例，再找类；写：写在你指定的那层

## 三个坑
- 可变类属性 tags = []  → 所有实例共用一个列表
- 构造函数的可变默认参数 def __init__(self, tags=[])  → 同上
  → 都改用 None + if None 判断
- a = b 不是复制；a == b 默认比的还是「是不是同一个」

## 三种方法
- 普通方法：     第一个参数 self  →  obj.m()
- @classmethod 第一个参数 cls   →  第二个构造入口（from_text / from_dict）
- @staticmethod 没有自动参数    →  和类相关但不用数据的工具函数

## 对象 ↔ JSON
- json.dump 不认自定义对象 → 必须自己 to_dict()
- 读回来用 @classmethod from_dict(cls, name, d)
- 文件格式和内存表示是两件事，靠两个函数连接

## C 对比
- struct 定义形状，函数在外面 —— class 把数据和动作装一起
- struct Contact *p        —— self 就是那个 p
- printf("%p", p) 打地址    —— print(obj) 打 <类名 object at 0x...>

## 踩过的坑
- 注意 def __init__ 参数有没有默认值, 没有需要之后赋 ""
- 需要使用 self 的函数, 一律写在 def __init__(self) 之后
- 要造对象、要读类属性的函数, 需要写在 @classmethod 之后
- 不需要 self 也不需要 cls, 但属于这个类的规则或工具, 需要写在 @staticmethod 之后