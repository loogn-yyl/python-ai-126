# 01 contacts_v1

一句话：115 行命令行通讯录，数据存 JSON，支持增删改查。

## 怎么跑
python contacts.py

## 用了什么
json / os / unicodedata

## 功能

- 添加联系人（自动查重）
- 删除联系人
- 按关键字模糊查找
- 显示全部联系人
- 数据存本地 contacts.json，关掉再开还在

## 遇到的问题
- 中文表格对不齐：len() 数的是字符数，一个汉字和字母 e 都算 1，但屏幕上汉字占两格；改用 unicodedata.east_asian_width 判断宽度再补空格
- 存盘后中文变成 \u5f20\u4e09：json.dump 默认 ensure_ascii=True，要显式关掉
- 数据文件被手改坏，json.load 抛 JSONDecodeError，程序直接起不来；捕获它并按空通讯录启动

## 已知不足
- 电话只判了非空，没校验格式（11 位数字的校验留给 v3）
- 拿姓名当主键，改名等于新建一条，没有唯一 id