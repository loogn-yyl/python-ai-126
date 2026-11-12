# D014 笔记 · 第 2 周复盘与通讯录 v3

## 第 2 周六天一句话
- D008 类：数据 + 操作放在一起；忘写 self 会报 takes 1 positional argument
- D009 继承：父类定契约，子类换实现；组合优于继承
- D010 魔法方法：__str__ 给人看，__repr__ 给调试看；改 __eq__ 要连 __hash__
- D011 dataclass：自动生成 __init__/__repr__/__eq__；可变默认值用 default_factory
- D012 生成器：一次一个，省内存；只能走一遍
- D013 装饰器：@deco 就是 f = deco(f)；必写 *args/**kwargs + functools.wraps

## 项目分层
- models.py：数据长什么样 + 校验 + 进出字典        （不许 open）
- store.py ：能做什么（增删查、存盘读盘）
- decorators.py：跟业务无关的横切逻辑（日志）
- __init__.py：__all__ 白名单，对外只开一扇门
- 判断标准：能不能单独测

## 虚拟环境启动及测试
- 第一步: 建(只做一次)
  cd 进入项目根目录 + python3 -m vent .venv -> 无任何输出即成功
  (Ls .venv -> # bin include lib pyvenv.cfg)
- 第二步: 开(每个新终端都要执行一次)
  cd 进入项目根目录 + source .venv/bin/active -> 提示符前多了一段 (.venv)
  (Which python -> 路径中包含.venv)
- 第三步: 装(每个环境一次)
  python -m pip install -U pip
  Python -m pip install pytest pytest-cov
- 第四步: 跑
  cd 进入本次任务目录
  python -m pytest -q (--cov=contacts --cov-report=term-missing)

## 数据模型
- dataclass 四行顶手写三个方法
- 校验写 __post_init__，不覆盖 __init__（覆盖了等于放弃 dataclass）
- 快速失败：创建时就报错，别带着坏数据跑
- 判空要 name.strip()，纯空格字符串挡不住
- to_dict 用 asdict()；from_dict 要兼容旧格式（向后兼容）

## 装饰器加在哪一层
- 日志记录的是「操作」，不是「数据」→ 加在 store 层，不加 models 层
- 加在 save() 上会失控（批量导入时一次操作记很多行）
- 一行的粒度 = 用户做的一件事
- 附加动作（日志/监控）绝不能被它们影响主流程：包 try/except

## pytest
- 文件名 test_*.py，函数名 test_*，不写 main
- assert 条件，不成立就抛异常；assert 后面写一句人话
- 读报错：> 是出错行，E assert 11 == 10 是实际 vs 期望，
  E + where 11 = len(...) 是中间值怎么来的
- pytest.raises(ValueError)：断言这里必须炸；没炸就 FAILED: DID NOT RAISE
- fixture：抽公共准备；每个测试各执行一次
- tmp_path：每个测试一个空目录，用完自动清 —— 读写文件必须用
- monkeypatch：临时改属性，测试结束自动还原
- 验证结果，别验证过程（别 mock save 再断言它被调用）

## 覆盖率
- Stmts 语句数 / Miss 没跑到 / Cover 比例 / Missing 哪几行 ★
- 真正该看的是 Missing —— 那是「没被测过的代码清单」
- 87% → 90%（补坏 json 分支）→ 100%（补 line、旧格式、__iter__）
- 100% 不等于没 bug：只说明被执行过，不说明断言过结果
- 没有 assert 的测试能刷满覆盖率，但保护力是零

## 踩过的坑
- 多参数输入注意补空缺参数的位置