[x] 1.__eq__ 里 return False 和 return NotImplemented 有什么区别？
      return False 表示已比较过了, 结论是不相等
      return NotImplemented 表示比较双方类型不对
[x] 2.为什么 @dataclass 的 tags: list = [] 会在定义类的那一刻就报错？
      类属性在定义时只创建一次, 所以人共享 tags, 一个人执行完 tags.append, 所有人 tags 都变, 因此干脆报错 ValueError。 
      最好用 tags: list = field(default_factory=list)
[x] 3.生成器为什么只能遍历一次？list(gen) 之后再 for 为什么是空的？
      yield 只是暂停、保存当前位置 + 局部变量, 向前走, 只能前进、不能回滚, 因此再 for 只能为空
      重复用就存下来: data = list(gen), 代价是内存
[x] 4.@deco 之后，函数名指向的还是原来那个函数吗？
      不是, @deco 等价于 f = deco(f), f -> deco 里面返回的 wrapper
[x] 5.类属性里放一个列表，所有实例共享同一份，应该怎么改？
      __init__ 里面 self.tags = [], 表示每个实例一份新的
      dataclass 里面 tags: list = field(default_factory=list)
[x] 6.is 和 == 分别该在什么时候用？
      一般都用 == 
      is 用于 None/True/False/NotImplemented 