# 04 logtool

一句话：解析 nginx 访问日志，输出 Top IP / Top URL / 状态码 / 错误率。

## 怎么跑
python logtool.py sample_access.log -n 5 --format json

## 用了什么
re / collections.Counter / argparse / logging / pathlib

## 遇到的问题
- 中文日志按 utf-8 读会抛 UnicodeDecodeError，改成先 read_bytes 再试三种编码
- Top N 顺序不稳定，加了 (-次数, 名称) 双排序键

## 已知不足
- 只支持 combined 格式，main 格式没做
- 单文件 200 行，超过就该拆包了