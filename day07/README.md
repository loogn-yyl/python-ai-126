# 命令行通讯录 v1

Python 学习第 7 天的练习项目：用字典存储联系人，JSON 持久化，纯命令行交互。

## 功能

- 添加联系人（自动查重）
- 删除联系人
- 按关键字模糊查找
- 显示全部联系人
- 数据存本地 contacts.json，关掉再开还在

## 运行

```bash
python3 contacts_v1.py
```

## 学到的东西

- 字典作为「按名字取」的存储结构（O(1) 查找）
- while True + enumerate 实现菜单循环
- JSON 读写与 ensure_ascii
- 分层组织代码：数据层 / 功能层 / 界面层

## 下一步

v2 打算用 Contact 类重构，加上修改功能和输入校验。
