# 02 contacts_v3

一句话：拆成 4 个模块 117 行，另配 129 行测试、20 个用例全绿。

## 怎么跑
cd portfolio/02_contacts_v3
python -m pytest -q
# 想看覆盖率: pip install pytest-cov 之后
python -m pytest -q --cov=contacts --cov-report=term-missing  

## 用了什么
json / functools / dataclasses.dataclass / dataclasses.field / dataclasses.asdict / pytest

## 遇到的问题
- 测试文件最初叫 contacts.py，和包目录 contacts/ 重名，pytest 报 import file mismatch，一个用例都收集不到；而且它不匹配 test_*.py，pytest -q 直接 no tests ran。改名 test_contacts.py 才跑起来
- 测试会真往 contacts.json 和日志里写，跑一遍污染本地数据；用 tmp_path + monkeypatch 把两个路径都指到临时目录
- 日志写失败不能让业务失败：decorators 里捕获 OSError 并吞掉，否则目录没权限时连「加联系人」都做不了

## 已知不足
- 仍然拿姓名当主键，没有唯一 id
- 只有 JSON 后端，换 SQLite 要动 store 一层