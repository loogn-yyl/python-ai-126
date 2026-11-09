# D011 笔记

## @dataclass
- 只写字段声明：name: str，__init__ / __repr__ / __eq__ 全自动
- 有默认值的字段必须排在没默认值的后面
- 自己写的方法照常写，不会被覆盖
- 加字段只改一行声明

## field()
- 可变默认值（list/dict/set）必须用 field(default_factory=list)
- 写成 tags: list = [] 会在【定义类的时候】就 ValueError，连 import 都失败
- 其他参数：default=、repr=False

## 常用开关
- @dataclass(order=True)   自动生成 __lt__ 等，可以 sorted()、可以 >
- @dataclass(frozen=True)  不可变；改属性抛 FrozenInstanceError；能 hash、能进 set

## Enum
- class Status(Enum): ACTIVE = "active"
- Status.ACTIVE 打印带类名；.name 是 'ACTIVE'，.value 是 'active'
- Status("active") 按值反查，值不存在抛 ValueError
- Status.ACTIVE == "active" 是 False ！要对比就 .value
- 适合：订单状态、星期、日志级别；不适合：姓名、城市名这类无限取值

## 类型注解
- def f(x: str) -> Optional[int]:   只是注解，运行时不检查！
- list[Contact] / dict[str, int]    容器要写里面的类型
- Optional[X] 或 X | None           可能返回 None 时必须标
- 用处：IDE 补全、Pylance 查错、一个月后自己看得懂
- 校验外部数据要靠 try/except 或 Pydantic，不能靠注解

## Pydantic（预览）
- 第三方库：uv run --with pydantic demo.py
- class Contact(BaseModel): 字段注解 + 自动校验 + 自动类型转换
- 脏数据抛 ValidationError，能说清是哪个字段、错在哪
- 一句话：dataclass 信任数据，Pydantic 不信任

## 踩过的坑
- @dataclass(order=True) 表示按字段声明顺序逐个比较, 第一个不相等的字段决定结果, 并且可以不指明关键字来传参
- 对比 @dataclass(order=True, kw_only=True) 排序只看字段顺序, 但必须指明关键字来传参, 且关键字顺序可以变
- title: str = field(compare=False) 可以让这一字段退出比较, 包括排序、 == 和 hash 计算, 且不依赖 order